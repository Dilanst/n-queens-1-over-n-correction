"""Polinomios interpolados y residuo del perfil en una malla racional auxiliar.

Los únicos flotantes intervienen en la búsqueda del candidato, nunca en la
evaluación del residuo. Los dos ejes se refieren al continuo de G6.
"""
import argparse
from decimal import Decimal
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, lcm
from pathlib import Path
import hashlib
import json
import os
import platform
import sys
import time

for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[key]='1'

from suelo import bound, digest

Q=10**45


def guardar(path,obj):
    with path.open('x',encoding='utf8') as f:
        json.dump(obj,f,indent=1,ensure_ascii=False)


def estandar(datos, opts, t0, w0):
    datos.update(python=sys.version, plataforma=platform.platform(),cpu_s=time.process_time()-t0,
                 pared_s=time.perf_counter()-w0, guion_sha256=digest(Path(__file__)),
                 auxiliar_sha256=digest(Path(__file__).with_name('suelo.py')),
                 hilos=1, paneles_en_unidad=opts.M, grado=opts.d)
    return datos


def diferencias(vals):
    row=list(vals)
    while row:
        yield row[0]
        row=[b-a for a,b in zip(row,row[1:])]


def potencias(vals):
    """d! p(w) con p(0)=v0,...,p(d)=vd, en la base 1,w,...,w^d."""
    d=len(vals)-1
    out=[0]*(d+1)
    base=[1]
    for k,delta in enumerate(diferencias(vals)):
        escala=delta*(factorial(d)//factorial(k))
        for i,c in enumerate(base):
            out[i]+=c*escala
        sig=[0]+base
        for i,c in enumerate(base):
            sig[i]-=k*c
        base=sig
    return out


@lru_cache(None)
def regla(m):
    """Newton-Cotes cerrada, integral media en el intervalo. Pesos enteros."""
    result=[]
    for i in range(m+1):
        coef=potencias([int(j==i) for j in range(m+1)])
        result.append(sum(F(v*m**k, factorial(m)*(k+1)) for k,v in enumerate(coef)))
    den=lcm(*(x.denominator for x in result))
    return [int(x*den) for x in result], den


def cortes(typ,x,H,M):
    """Intervalos en unidades de 1/H tras plegar por el punto medio."""
    step=H//M
    if typ=='S':
        a,b=0,H//2
        shifts=[(0,step),(x,step),(-x,step)]
    else:
        a,b=x,(H+x)//2
        assert 2*b==H+x
        shifts=[(0,step),(x,step),((H+x)//2,step//2)]
    edges={a,b}
    for origin,period in shifts:
        start=a+1+(origin-a-1)%period
        edges.update(range(start,b,period))
    return sorted(edges)


def argumentos(typ,x,t,H):
    if typ=='S':
        return (('S',t),('u',abs(x-t)),('u',abs(x+t-H)))
    return (('S',t),('S',t-x),('u',abs(2*t-x-H)))


class Perfil:
    def __init__(self,vals,M,d,H):
        assert H%(M*d)==0
        self.H,self.M,self.d=H,M,d
        L=H//(M*d)
        self.den=Q*factorial(d)*L**d
        self.pol={}
        for typ in ('S','u'):
            for p in range((M//2) if typ=='S' else M):
                c=potencias(vals[typ][p*d:p*d+d+1])
                self.pol[typ,p]=[v*L**(d-i) for i,v in enumerate(c)]
        self.cached={}

    def valor(self,typ,x):
        H,M=self.H,self.M
        w=min(x,H-x) if typ=='S' else x
        key=(typ,w)
        if key in self.cached:
            return self.cached[key]
        width=H//M
        p=min(w//width,(M//2 if typ=='S' else M)-1)
        local=w-p*width
        answer=0
        for c in reversed(self.pol[typ,p]):
            answer=answer*local+c
        self.cached[key]=answer
        return answer


class Residuo:
    def __init__(self,vals,M,d,N):
        self.M,self.d,self.N=M,d,N
        self.m=3*d
        self.H=4*M*N*self.m
        self.f=Perfil(vals,M,d,self.H)
        self.weights,wd=regla(self.m)
        self.intden=self.H*wd*self.f.den**3
        self.den=self.intden*self.f.den

    def valor(self,typ,x):
        H,M,m=self.H,self.M,self.m
        val=self.f.valor
        pieces=cortes(typ,x,H,M)
        integ=0
        for a,b in zip(pieces,pieces[1:]):
            assert (b-a)%m==0
            ts=range(a,b+1,(b-a)//m)
            if typ=='S':
                v=sum(w*val('S',t)*val('u',abs(x-t))*val('u',abs(x+t-H)) for t,w in zip(ts,self.weights))
            else:
                v=sum(w*val('S',t)*val('S',t-x)*val('u',abs(2*t-x-H)) for t,w in zip(ts,self.weights))
            integ+=2*(b-a)*v
        if typ=='u':
            integ+=self.intden
        return val(typ,x)*integ-self.den


def viejo(typ,x,data):
    if typ=='S':
        t=4*min(x,1-x)-1
        c=data['cS']
    elif x<=F(1,2):
        t=4*x-1
        c=data['cu0']
    else:
        t=4*x-3
        c=data['cu1']
    a,b=0,0
    for z in reversed(c[1:]):
        a,b=z+2*t*a-b,a
    return c[0]+t*a-b


def origen(base):
    path=base/'resultados'/'candidato_coeficientes.json'
    content=json.loads(path.read_text('utf8'))
    return {k:[F.from_float(float(v)) for v in content[k]] for k in ('cS','cu0','cu1')},path


def nudos(M,d):
    return [(typ,j) for typ,size in [('S',M//2),('u',M)] for j in range(size*d+1)]


def jacobiano(vals,M,d):
    """Matriz aproximada. Sólo genera propuestas; una verificación exacta posterior decide."""
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    grid=nudos(M,d)
    n=len(grid)
    H=4*M*d
    nodes,weights=leggauss(2*d)
    A=np.zeros((n,n))
    indices=np.arange(d+1)
    bases=np.array([(-1)**(d-i)/(factorial(i)*factorial(d-i)) for i in indices.tolist()])
    y=np.array([float(F(vals[t][j],Q)) for t,j in grid])
    def leer(typ,x):
        x=np.minimum(x,1-x) if typ=='S' else x
        p=np.minimum(np.floor(M*x).astype(int),(M//2 if typ=='S' else M)-1)
        loc=(M*x-p)*d
        offsets=np.zeros_like(p) if typ=='S' else np.full_like(p, M//2*d+1)
        idx=p[:,None]*d+indices+offsets[:,None]
        dif=loc[:,None]-indices
        co=np.empty_like(dif)
        for k in indices:
            co[:,k]=bases[k]*dif[:,:k].prod(axis=1)*dif[:,k+1:].prod(axis=1)
        return (co*y[idx]).sum(axis=1),co,idx
    for row,(typ,j) in enumerate(grid):
        x=j/(M*d)
        pts=np.asarray(cortes(typ,j*4,H,M))/H
        q=((pts[1:,None]+pts[:-1,None])+(pts[1:,None]-pts[:-1,None])*nodes)/2
        w=((pts[1:,None]-pts[:-1,None])*weights).ravel()
        q=q.ravel()
        terms=[leer(k,v) for k,v in argumentos(typ,x,q,1)]
        vals3=[a[0] for a in terms]
        A[row,row]=float(typ=='u')+(w*vals3[0]*vals3[1]*vals3[2]).sum()
        for k,(v,co,idx) in enumerate(terms):
            mult=w*y[row]*vals3[(k+1)%3]*vals3[(k+2)%3]
            A[row]+=np.bincount(idx.ravel(),weights=(mult[:,None]*co).ravel(),minlength=n)
    return A


def generar(o):
    import numpy as np
    t0,w0=time.process_time(),time.perf_counter()
    M,d=o.M,o.d
    ref,src=origen(o.base)
    grid=nudos(M,d)
    vals={typ:[] for typ in ('S','u')}
    for typ,j in grid:
        vals[typ].append(round(viejo(typ,F(j,M*d),ref)*Q))
    A=jacobiano(vals,M,d)
    hist=[]
    for step in range(5):
        res=Residuo(vals,M,d,d)
        vs=[F(res.valor(typ,res.H*j//(M*d)),res.den) for typ,j in grid]
        hist.append(bound(max(map(abs,vs)),True))
        if max(map(abs,vs))<F(1,10**37):
            break
        correction=np.linalg.solve(A,np.array([float(v) for v in vs]))
        for dy,(typ,j) in zip(correction,grid):
            vals[typ][j]-=round(Q*F.from_float(float(dy)))
    ans=estandar(dict(escala=str(Q),valores={k:[str(n) for n in vv] for k,vv in vals.items()},
                      max_residuos_en_nudos=hist,sha256_G6=digest(src),numpy=np.__version__),o,t0,w0)
    guardar(o.salida,ans)
    print('residuos de colocación',hist,'CPU',ans['cpu_s'],flush=True)


def bernstein(vals):
    """Coeficientes de Bernstein de p en [0,1] desde p(i/n), exactos."""
    n=len(vals)-1
    c=potencias(vals)
    powers=[F(a*n**k,factorial(n)) for k,a in enumerate(c)]
    return [sum(powers[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]


def split_bern(b):
    left,right=[],[]
    while b:
        left.append(b[0])
        right.append(b[-1])
        b=[(a+c)/2 for a,c in zip(b,b[1:])]
    return left,right[::-1]


def rango_b(b,nivel):
    if nivel==0:
        return min(b),max(b)
    l,r=split_bern(b)
    a,z=rango_b(l,nivel-1)
    x,y=rango_b(r,nivel-1)
    return min(a,x),max(z,y)


def certificado(o):
    t0,w0=time.process_time(),time.perf_counter()
    M,d=o.M,o.d
    raw=json.loads(o.candidato.read_text('utf8'))
    assert raw['paneles_en_unidad']==M and raw['grado']==d and int(raw['escala'])==Q
    vals={k:list(map(int,v)) for k,v in raw['valores'].items()}
    ref,src=origen(o.base)
    assert raw['sha256_G6']==digest(src)
    assert len(vals['S'])==M//2*d+1 and len(vals['u'])==M*d+1
    N=4*d+1
    res=Residuo(vals,M,d,N)
    reg=[]
    dist={}
    for typ,panels in [('S',M//2),('u',M)]:
        max_delta=F(0)
        for p in range(panels):
            # En el panel actual el candidato Antiguo y el Nuevo son polinomios.
            n=max(d,47)
            H=M*n*d
            f=Perfil(vals,M,d,H)
            delta=[]
            for j in range(n+1):
                num=(p*n+j)*d
                x=F(num,H)
                # Elegir el límite lateral del panel alto en x=1/2, incluso en el extremo.
                vr=viejo(typ,x,ref)
                if typ=='u' and p==M//2 and j==0:
                    vr=sum((-1)**i*c for i,c in enumerate(ref['cu1']))
                delta.append(F(f.valor(typ,num),f.den)-vr)
            lo,hi=rango_b(bernstein(delta),3)
            max_delta=max(max_delta,abs(lo),abs(hi))
        dist[typ]=max_delta
        # En ambas ecuaciones el orden de todos los cortes es constante en cada 1/(2M).
        for p in range(2*panels):
            x0=res.H*p//(2*M)
            dx=res.H//(2*M*N)
            rv=[res.valor(typ,x0+j*dx) for j in range(N+1)]
            lo,hi=rango_b(bernstein(rv),2)
            reg.append(dict(tipo=typ,indice=p,abs_R_sup=bound(max(abs(lo),abs(hi))/res.den,True)))
    # Constantes originales se reemplazan por mayorantes enteros que cubren el redondeo.
    old=o.base/'resultados'/'res_nk_4096.json'
    nk=json.loads(old.read_text('utf8'),parse_float=Decimal)
    assert nk['beta']<57 and nk['L']<5700 and nk['radio_unicidad_w']>=Decimal('1e-6')
    # La norma binaria original usa gamma=float(0.05) >= 1/20.
    gw=F.from_float(float(nk['gam']))
    assert F(1,20)<=gw<F(51,1000)
    dst=max(dist['S'],dist['u']/gw)
    # Para el residuo: en el nuevo perfil ambos factores son positivos, todo el dominio.
    marge={}
    for typ in ['S','u']:
        bounds=[]
        for p in range(M//2 if typ=='S' else M):
            a,b=rango_b(bernstein([F(Y,Q) for Y in vals[typ][p*d:p*d+d+1]]),2)
            bounds.append((a,b))
        marge[typ]=(min(a for a,b in bounds),max(b for a,b in bounds))
        assert marge[typ][0]>0
    rs,ru=(max(F(v['abs_R_sup']) for v in reg if v['tipo']==typ) for typ in ['S','u'])
    assert rs<1
    rho=max(rs*marge['S'][1]/(1-rs),ru/gw)
    # Inversa en el centro nuevo y contracción de Newton congelado en la nueva bola.
    beta,L=F(57),F(5700)
    assert beta*L*dst<1
    bnew=beta/(1-beta*L*dst)
    eta=bnew*rho
    rad=eta*(1+F(1,1000))
    assert dst+rad<=F(1,10**6)
    assert bnew*L*rad<1 and eta+bnew*L*rad**2/2<=rad
    result=estandar(dict(candidato_sha256=digest(o.candidato),G6_sha256=digest(src),NK_sha256=digest(old),
              sup_dist_G6={k:bound(v,True) for k,v in dist.items()},distancia_ponderada=bound(dst,True),
              rango_perfil={k:[bound(a,False),bound(b,True)] for k,(a,b) in marge.items()},
              beta_nueva=bound(bnew,True),rho_ponderada=bound(rho,True),epsilon_S=bound(rad,True),
              epsilon_u=bound(rad*gw,True),regimenes=reg),o,t0,w0)
    guardar(o.salida,result)
    print('radios',result['epsilon_S'],result['epsilon_u'],'CPU',result['cpu_s'],flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('accion',choices=['generar','verificar'])
    p.add_argument('base',type=Path)
    p.add_argument('M',type=int)
    p.add_argument('d',type=int)
    p.add_argument('salida',type=Path)
    p.add_argument('--candidato',type=Path)
    o=p.parse_args()
    assert o.M>=2 and o.M%2==0 and o.d>=2
    (generar if o.accion=='generar' else certificado)(o)
