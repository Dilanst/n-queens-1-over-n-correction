"""Encierro continuo de las torres en el semitablero. Un único caso por proceso."""
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
from fractions import Fraction as Q

HERE = Path(__file__).resolve().parent
PERFIL = HERE.parent / "perfil"
sys.path.insert(0, str(PERFIL))
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[key] = "1"
import numpy as np
from paneles import bernstein, split_bern, potencias

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def down(x):
    return np.nextafter(x, -np.inf)

def up(x):
    return np.nextafter(x, np.inf)

class I:
    """Intervalos de extremos binarios con difusión de NumPy."""
    def __init__(self, l, h=None):
        self.l = np.asarray(l, dtype=float)
        self.h = self.l if h is None else np.asarray(h, dtype=float)
    def __getitem__(self, k):
        return I(self.l[k], self.h[k])
    def __add__(a, b):
        b = asiv(b)
        return I(down(a.l + b.l), up(a.h + b.h))
    __radd__ = __add__
    def __neg__(a):
        return I(-a.h, -a.l)
    def __sub__(a, b):
        return a + -asiv(b)
    def __rsub__(a, b):
        return asiv(b) + -a
    def __mul__(a,b):
        b = asiv(b)
        ab = (a.l*b.l, a.l*b.h, a.h*b.l, a.h*b.h)
        return I(down(np.minimum(np.minimum(ab[0],ab[1]),np.minimum(ab[2],ab[3]))),
                 up(np.maximum(np.maximum(ab[0],ab[1]),np.maximum(ab[2],ab[3]))))
    __rmul__ = __mul__
    def reciprocal(a):
        assert np.all(a.l>0)
        return I(down(1/a.h), up(1/a.l))
    def avg(a, axis=None):
        l,h = a.l,a.h
        if axis is None:
            l,h = l.ravel(),h.ravel()
        else:
            l,h = np.moveaxis(l,axis,-1),np.moveaxis(h,axis,-1)
        while l.shape[-1]>1:
            assert l.shape[-1]%2 == 0
            l,h = down((l[...,::2]+l[...,1::2])*.5),up((h[...,::2]+h[...,1::2])*.5)
        return I(l[...,0],h[...,0])
    def cap(a):
        return np.maximum(abs(a.l),abs(a.h))
    def diag(a):
        return I(a.l.diagonal(),a.h.diagonal())
    def widen(a, error):
        return I(down(a.l-error), up(a.h+error))

def asiv(q):
    return q if isinstance(q,I) else I(q)

def rat(q):
    return I(down(float(q)),up(float(q)))

def conv(a, b):
    """Cauchy de productos de núcleos, mediante centros y radios diádicos exactos."""
    n = a.l.shape[-1]
    assert n <= 1024
    def integers(v):
        # Una sola potencia de dos para centros y radios. La holgura de los
        # productos permite sumarlos en cualquier orden exactamente en binary64.
        peak = float(np.max(v.cap()))
        exponent = 20 - math.frexp(max(peak, 2.0**-100))[1]
        factor = 2.0**exponent
        cm = np.rint((v.l*.5 + v.h*.5)*factor)
        # Los extremos escalados son exactos. nextafter envuelve cualquier
        # redondeo de su resta al entero central antes de tomar el techo.
        rad = np.ceil(up(np.maximum(cm-v.l*factor,v.h*factor-cm)))
        assert np.max(abs(cm)+rad) <= 2.0**21
        return cm,rad,exponent
    ac,ar,ea = integers(a)
    bc,br,eb = integers(b)
    center = ac @ bc
    radius = abs(ac) @ br + ar @ (abs(bc)+br)
    # Centro absoluto más radio <= n*2^42 <= 2^52.
    factor = 2.0**(-ea-eb)/n
    return I((center-radius)*factor,(center+radius)*factor)

def perfil(n):
    cand = PERFIL/"candidato_M16d14.json"
    cert = PERFIL/"log_M16d14.json"
    data,log = (json.loads(p.read_bytes()) for p in (cand,cert))
    assert sha(cand)==log["candidato_sha256"]=="25d0bae0401917dc8c165890557ac9c05fd13754e89b2df720b54f06ceb36816"
    assert sha(PERFIL/"certificado_M16d14.json")==log["residuo_certificado_sha256"]
    assert Q(log["epsilon_S"])<Q("2.1e-15") and Q(log["epsilon_u"])<Q("4.3e-16")
    tables={}
    W=I(0)
    for kind in ("S","u"):
        eps = Q("2.1e-15" if kind=="S" else "4.3e-16")
        l,h=[],[]
        values=[Q(int(x),int(data["escala"])) for x in data["valores"][kind]]
        for p in range((len(values)-1)//14):
            nodes=values[14*p:14*p+15]
            base=bernstein(nodes)
            pieces=[base]
            for _ in range((2*n//16).bit_length()-1):
                pieces=[z for b in pieces for z in split_bern(b)]
            l.extend(down(float(min(z)-eps)) for z in pieces)
            h.extend(up(float(max(z)+eps)) for z in pieces)
            if kind!="u":
                continue
            # Simpson en coordenada local por panel. Las derivadas hasta 4 se
            # encierran por diferencias de coeficientes de Bernstein.
            a=min(base)
            der=base
            D=[]
            for i in range(4):
                der=[(len(der)-1)*(v-u) for u,v in zip(der,der[1:])]
                D.append(max(abs(k) for k in der))
            d1,d2,d3,d4=D
            major=24*d1**4/a**5+36*d1*d1*d2/a**4+(6*d2*d2+8*d1*d3)/a**3+d4/a**2+d4
            m=64
            rem=major/(180*m**4)+eps*(1+1/(a-eps)**2)
            c=potencias(nodes)
            enclosure=I(0)
            for j in range(m+1):
                arg=Q(14*j,m)
                v=Q(0)
                for co in reversed(c):
                    v=v*arg+co
                v/=math.factorial(14)
                wt=1 if j in (0,m) else (4 if j%2 else 2)
                enclosure+=rat(wt*(1/v+v-2)/(3*m))
            W+=enclosure.widen(rat(rem).h)*.125
        tables[kind]=I(l,h)
    return tables["S"],tables["u"],W,{p.name:sha(p) for p in (cand,cert,PERFIL/"certificado_M16d14.json",PERFIL/"paneles.py",Path(__file__))}

def span(tab,lo,hi):
    # Los índices son celdas de la malla 2n en [0,1]. La imagen de una
    # caja por distancia o suma cubre a lo sumo dos de estas celdas.
    assert np.all(hi-lo<=1) and np.min(lo)>=0 and np.max(hi)<len(tab.l)
    return I(np.minimum(tab.l[lo],tab.l[hi]),np.maximum(tab.h[lo],tab.h[hi]))

class Dual:
    def __init__(self,v,d=0):
        self.v,self.d=asiv(v),asiv(d)
    def __add__(a,b):
        b=dual(b)
        return Dual(a.v+b.v,a.d+b.d)
    __radd__=__add__
    def __neg__(a):
        return Dual(-a.v,-a.d)
    def __sub__(a,b):
        return a+-dual(b)
    def __mul__(a,b):
        b=dual(b)
        return Dual(a.v*b.v,a.d*b.v+a.v*b.d)
    __rmul__=__mul__
    def col(a):
        return Dual(a.v[:,None],a.d[:,None])
    def row(a):
        return Dual(a.v[None,:],a.d[None,:])
    def avg(a):
        return Dual(a.v.avg(),a.d.avg())

def dual(a):
    return a if isinstance(a,Dual) else Dual(a)

def F(z,T,U,j,w):
    j0=(j*w).avg()
    weights=w.col()*w.row()
    avg2=lambda k:(k*weights).avg()
    return (j0*j0*.5+avg2(T*T)-1.5*j0-1.5*(j*j*w).avg()
            +avg2(j.col()*(z+U-T)*j.row())-dual(rat(Q(2,3)))*avg2(T*T*T)
            +2*avg2(z*U*U)+dual(rat(Q(2,3)))*avg2(U*U*U))

def expand(n,N,start):
    s,u,W,hashes=perfil(n)
    i,j=np.ogrid[:n,:n]
    q=np.abs(i-j)
    d=span(u,np.maximum(q-1,0),q)
    a=span(u,2*n-i-j-2,2*n-i-j-1)
    p=s[:,None]*s[None,:]*d*a
    z=p-1
    gamma=d.reciprocal()+a.reciprocal()-2
    eta=2*W-(p*gamma).avg(1)
    rho=Q.from_float(float(np.max(I(z.cap()).avg(1).h)))
    b=Q.from_float(float(np.max(z.cap())))
    assert rho<1
    # v=-B eta+B² eta-... ; h_delta=v, h_x=eta+v-W
    term=eta
    v=I(np.zeros(n))
    for k in range(1,N+1):
        term=-conv(z,term)
        v+=term
    v=v.widen(rat(Q.from_float(float(np.max(eta.cap())))*rho**(N+1)/(1-rho)).h)
    h=eta+v-W
    zd=p*(v[:,None]+v[None,:])
    zx=p*(h[:,None]+h[None,:]+gamma)
    zero=I(np.zeros(n))
    with_density=(eta[:,None]+eta[None,:])*.5
    Cd=zd+z*with_density
    # Núcleos conjugados C=sqrt(w_i w_j)(p-1). La medida fija es Lebesgue.
    Cpow=z
    derivatives=[Cd,zx]
    Dpow=list(derivatives)
    zero_mat=I(np.zeros((n,n)))
    T=[zero_mat]*3
    U=[zero_mat]*3
    J=[zero]*3
    for k in range(2,N+1):
        assert time.process_time()-start < 260
        old=Cpow
        Cpow=conv(z,old)
        Dpow=[conv(D,old)+conv(z,dk) for D,dk in zip(derivatives,Dpow)]
        for ix,val in enumerate([Cpow]+Dpow):
            if k%2:
                U[ix]+=val
            else:
                T[ix]+=val
                if k>=4:
                    J[ix]+=val.diag()
    # Incluye todas las potencias >N, aun las de la otra paridad.
    tails=[b*rho**N/(1-rho)]
    tails.extend(Q.from_float(float(np.max(D.cap()))) *
                 rho**N*(N+1-N*rho)/(1-rho)**2 for D in derivatives)
    for ix,err in enumerate(tails):
        for arr in (T,U,J):
            arr[ix]=arr[ix].widen(rat(err).h)
    def compute(ix,measure,dz,conj):
        tt=Dual(T[0],T[ix]-T[0]*conj)
        uu=Dual(U[0],U[ix]-U[0]*conj)
        jj=Dual(J[0],J[ix]-J[0]*measure)
        ww=Dual(I(np.ones(n)),measure)
        return F(Dual(z,dz),tt,uu,jj,ww)
    fd=compute(1,eta,zd,with_density)
    fx=compute(2,zero,zx,0)
    pt=(rat(Q(1,6))-2*fd.v)*W-fd.d
    def output(iv):
        # Decimal fijo exterior a cada extremo binario.
        scale=10**15
        def endpoint(x,lower):
            val=Q.from_float(float(x))*scale
            t=math.floor(val) if lower else math.ceil(val)
            return ('-' if t<0 else '')+f'{abs(t)//scale}.{abs(t)%scale:015d}'
        return [endpoint(iv.l,True),endpoint(iv.h,False)]
    return dict(celdas_medio=n,orden=N,contraccion=output(rat(rho)),W=output(W),
                F0=output(fd.v),Fprima0=output(fx.d),delta_F=output(fd.d),P_T=output(pt),
                colas=[float(rat(e).h) for e in tails],sha256=hashes)

if __name__=="__main__":
    t=time.process_time()
    clock=time.perf_counter()
    n,N=int(sys.argv[1]),int(sys.argv[2])
    dest=Path(sys.argv[3])
    assert 16<=n<=1024 and n&(n-1)==0 and 6<=N<=24
    results=expand(n,N,t)
    results.update(cpu_s=time.process_time()-t,pared_s=time.perf_counter()-clock,
                   hilos=1,python=sys.version,numpy=np.__version__)
    assert results["cpu_s"]<300
    with dest.open("x",encoding="utf8") as f:
        json.dump(results,f,indent=2,ensure_ascii=False)
    print(json.dumps({k:results[k] for k in ("F0","Fprima0","delta_F","P_T","W","cpu_s")}))
