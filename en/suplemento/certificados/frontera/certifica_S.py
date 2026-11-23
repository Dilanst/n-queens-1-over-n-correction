"""Cubatura dirigida del término S con el perfil G6. Uso: python -B certifica_S.py 48."""
import hashlib
import json
import os
import sys
import time
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
for env in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[env] = '1'
import numpy as np
from geometria import tetrahedra
from gauss import rule

def down(x): return np.nextafter(x,-np.inf)
def up(x): return np.nextafter(x,np.inf)

def ends(q):
    f = float(q)
    real = F.from_float(f)
    return (f if real <= q else down(f), f if real >= q else up(f))

def outward(q, upper=False, digits=13):
    n = (q.numerator*10**digits)//q.denominator
    if upper and F(n,10**digits) < q: n+=1
    return f'{n//10**digits}.{n%10**digits:0{digits}d}'

def input_data(g6):
    files = [g6/'resultados'/name for name in ('candidato_coeficientes.json','res_nk_4096.json')]
    digests = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    manifest = (g6/'SHA256SUMS').read_text(encoding='utf8')
    for p in files:
        assert any(digests[p.name] == line.split()[0] and line.split()[-1].endswith('/'+p.name)
                   for line in manifest.splitlines())
    coefficients = json.loads(files[0].read_bytes())
    nk = json.loads(files[1].read_bytes(),parse_float=F)
    es, eu = F('8.75e-10'), F('4.38e-11')
    assert nk['eps_S_sup'] < es and nk['eps_u_sup'] < eu
    return ({key:[F.from_float(float(s)) for s in coefficients[key]] for key in ('cS','cu0','cu1')},
            es,eu,digests)

class Profile:
    def __init__(self,cc,nb):
        self.nb = nb
        x = np.arange(nb+1,dtype=np.float64)*(2/nb)-1
        assert nb & (nb-1) == 0
        tmlo = tmhi = np.ones_like(x)
        tlo = thi = x
        lo = np.full_like(x,float(cc[0]))
        hi = lo.copy()
        for i,coef in enumerate(cc[1:],1):
            c = float(coef)
            lo = down(lo + down(c * (tlo if c >= 0 else thi)))
            hi = up(hi + up(c * (thi if c >= 0 else tlo)))
            if i+1 == len(cc):
                break
            lo_x = down(2*x*np.where(x>=0,tlo,thi))
            hi_x = up(2*x*np.where(x>=0,thi,tlo))
            nlo = np.maximum(-1,down(lo_x-tmhi))
            nhi = np.minimum(1,up(hi_x-tmlo))
            tmlo,tmhi,tlo,thi = tlo,thi,nlo,nhi
        self.lo,self.hi = lo,hi
        self.sl = down(lo[1:]-hi[:-1])
        self.su = up(hi[1:]-lo[:-1])
        self.lip = ends(2*sum(k*k*abs(c) for k,c in enumerate(cc)))[1]
        d2 = 4*sum(F(k**4-k*k,3)*abs(c) for k,c in enumerate(cc))
        self.rem = ends(d2/(8*nb*nb))[1]
        self.minimum = down(np.min(lo) - self.rem)
        assert self.minimum > 0

    def at(self,yl,yh):
        nb = self.nb
        z = np.maximum(0.,yl)*nb
        k = np.minimum(z.astype(np.int64),nb-1)
        t = z-k
        l = down(self.lo[k] + down(self.sl[k]*t))
        h = up(self.hi[k] + up(self.su[k]*t))
        error = up(self.rem + up(self.lip * up(np.minimum(1.,yh)-np.maximum(0.,yl))))
        return down(l-error), up(h+error)

def positive_product(a,b):
    al,au = a
    bl,bu = b
    return np.maximum(0.,down(al*bl)), up(au*bu)

def positive_add(a,b):
    return np.maximum(0.,down(a[0]+b[0])), up(a[1]+b[1])

def complement(a):
    return np.maximum(0.,down(1-a[1])),np.minimum(1.,up(1-a[0]))

def project(lam,verts):
    out = (0.,0.)
    for l,v in zip(lam,verts):
        if v:
            out = positive_add(out,positive_product(l,ends(v)))
    return np.maximum(0.,out[0]),np.minimum(1.,out[1])

def sum_dir(x,rounding):
    x = x.ravel()
    while len(x)>1:
        if len(x)%2:
            x = np.append(x,0.)
        x = rounding(x[::2] + x[1::2])
    return x[0]

def cube(rule_):
    x = (np.array([ends(s[0])[0] for s in rule_]),np.array([ends(s[1])[1] for s in rule_]))
    w = (np.array([ends(s[2])[0] for s in rule_]),np.array([ends(s[3])[1] for s in rule_]))
    a,b,c = [tuple(t.reshape(shape) for t in x) for shape in ((-1,1,1),(1,-1,1),(1,1,-1))]
    wa,wb,wc = [tuple(t.reshape(shape) for t in w) for shape in ((-1,1,1),(1,-1,1),(1,1,-1))]
    ab = positive_product(a,b)
    lam = [complement(a), positive_product(a,complement(b)),
           positive_product(ab,complement(c)), positive_product(ab,c)]
    weight = positive_product(positive_product(positive_product(wa,wb),wc),positive_product(ab,a))
    return lam, weight

def ellipse_error(cc,n,es,eu):
    rho = F(3,2)
    bounds = {key:sum(abs(c)*(rho**k+rho**(-k))/2 for k,c in enumerate(coef))
              for key,coef in cc.items()}
    arg = (2+rho+1/rho)/4
    M = (bounds['cS']+es)**8 * (max(bounds['cu0'],bounds['cu1'])+eu)**6 * arg**3
    return 72*M*rho**(-2*n)/(1-1/rho)

def main():
    start = time.process_time()
    n = int(sys.argv[1]) if len(sys.argv)>1 else 48
    nb = int(sys.argv[2]) if len(sys.argv)>2 else 2**18
    assert n in (24,32,48,64,96) and nb in (2**16,2**17,2**18,2**19,2**20)
    default = BASE.parent / 'base'
    g6 = Path(sys.argv[3]) if len(sys.argv)>3 else default
    cc,es,eu,hashes = input_data(g6)
    tables = {k:Profile(c,nb) for k,c in cc.items()}
    chambers,tets = tetrahedra()
    lam, weight = cube(rule(n))
    vals = []
    for tet,vol,forms in tets:
        tot = weight
        for key,vertices,power in forms:
            pl,pu = tables[key].at(*project(lam,vertices))
            eps_hi = ends(es if key == 'cS' else eu)[1]
            profile = down(pl-eps_hi), up(pu+eps_hi)
            assert np.min(profile[0]) > 0
            if power==2:
                profile = positive_product(profile,profile)
            tot = positive_product(tot,profile)
        scaled = [24*vol*F.from_float(float(sum_dir(arr,fn))) for arr,fn in zip(tot,(down,up))]
        vals.append(scaled)
        assert time.process_time()-start < 295, 'CPU agotada'
    errors = ellipse_error(cc,n,es,eu)
    ql,qu = (sum(pair[i] for pair in vals) for i in range(2))
    low,high = ql-errors,qu+errors
    amin = F.from_float(float(tables['cS'].minimum))
    umin = min(F.from_float(float(tables[k].minimum)) for k in ('cu0','cu1'))
    result = dict(orden=n,subintervalos_por_panel=nb,piezas=chambers,tetraedros=len(tets),
                  suma_determinantes='1/4',regla_envolventes=[outward(ql),outward(qu,True)],
                  error_cubatura=outward(errors,True),minimos_candidato=[outward(amin),outward(umin)],
                  eps_fila=str(es),eps_vacancia=str(eu),S=[outward(low),outward(high,True)],
                  segundos_cpu=round(time.process_time()-start,3),hilos=1,sha256_entradas=hashes,
                  python=sys.version.split()[0],numpy=np.__version__,
                  sha256_codigo={s:hashlib.sha256((BASE/s).read_bytes()).hexdigest()
                                 for s in ('geometria.py','gauss.py','certifica_S.py')})
    data = json.dumps(result,indent=2)+'\n'
    if len(sys.argv)>4:
        with open(sys.argv[4],'x',encoding='utf8') as dest:
            dest.write(data)
    print(data,end='')

if __name__=='__main__':
    main()
