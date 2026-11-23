"""Cajas continuas de líneas, centros y cruces para GL20 #10, en seis hojas."""
import hashlib
import json
import os
import sys
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
from types import SimpleNamespace

for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[k] = "1"

import numpy as np
from iv import I

CERT = Path(__file__).resolve().parents[1]
MODELO = CERT / "modelo_bivariado" / "modelo_GL20_10_m256.npz"
COEF = CERT / "base" / "resultados" / "candidato_coeficientes.json"
FUNC = CERT / "resolvente" / "funcional_validado.json"
sys.path.insert(0, str(CERT / "resolvente"))
from linea import Tabla, dn, up

FAMILIA = (0, 1, 2, 2, 3, 3)
COLOR = (-1, -1, 0, 1, 0, 1)
DOMINIO = ((0, 1), (0, 1), (-1, 1), (-1, 1), (0, 2), (0, 2))
PARES = tuple(combinations(range(4), 2))
G6 = "a15d61a91bcc0ac711eccd09eb0c3486b5d1b510951dc3ad47cd773e5ed3abc5"
GL = "3189b0aa0076fc7853f78192af07fdc091b1a26d20efcf59e10fb5f0ac83592a"
NPZ = "73a9978dd15c6bdd8062e712d423d78fb34e0ad9de6f2d99c558c15d38ea94f0"


def verificar_huella(archivo, huella):
    actual = hashlib.sha256(archivo.read_bytes()).hexdigest()
    assert actual == huella, (archivo, actual)


def inversa_positiva(i):
    assert np.all(i.lo > 0)
    return I(dn(1 / i.hi), up(1 / i.lo))


def unir_cotas(i, l, h):
    return I(np.maximum(i.lo, l), np.minimum(i.hi, h))


def modelo_agregado(n):
    """Recinto de todas las combinaciones finas, incluidas parejas distintas del mismo panel."""
    verificar_huella(MODELO, NPZ)
    m = 256
    L, N, g = 10*n, 10*m, m//n
    with np.load(MODELO, allow_pickle=False) as src:
        assert int(src["m"]) == m and int(src["potencia_dos"]) == -20
        hojas = np.repeat(np.arange(6), [m*(b-a) for a,b in DOMINIO])
        ticks = np.concatenate([np.arange(2*m*a, 2*m*b, 2) for a,b in DOMINIO])
        assert np.array_equal(src["hoja"], hojas) and np.array_equal(src["y0_ticks"], ticks)
        izq, der = src["L_min"], src["L_max"]
        dl = np.min(src["diagonal_min"].reshape(L, g), axis=1)
        dh = np.max(src["diagonal_max"].reshape(L, g), axis=1)
    z = np.arange(N)[None, :]
    lo, hi = np.empty((L,L)), np.empty((L,L))
    for i in range(L):
        y = np.arange(i*g,(i+1)*g)[:,None]
        a, b = np.minimum(y,z), np.maximum(y,z)
        ids = a*N - (a*(a+1))//2 + b
        lo[i] = np.min(izq[ids].reshape(g,L,g), axis=(0,2)) * 2.**-20
        hi[i] = np.max(der[ids].reshape(g,L,g), axis=(0,2)) * 2.**-20
    assert np.array_equal(lo,lo.T) and np.array_equal(hi,hi.T)
    return I(lo,hi), I(dl*2.**-20,dh*2.**-20)


def interseccion(f,g,y,z):
    """Cruce de dos bordes de franja en unidades 1/(2n); los bordes tienen tick par."""
    if (f,g)==(0,1):
        return y,z
    if (f,g)==(0,2):
        return y,y-z
    if (f,g)==(0,3):
        return y,z-y
    if (f,g)==(1,2):
        return y+z,y
    if (f,g)==(1,3):
        return z-y,y
    assert (f,g)==(2,3) and (y+z)%2==0
    return (y+z)//2,(z-y)//2


def proyecciones(n,f,g,franja,otra):
    """Vértices de la intersección de las dos franjas cerradas con el cuadrado."""
    q = 2*n
    rect = ((0,q),(0,q),(-q,q),(0,2*q))
    limites = list(rect)
    limites[f], limites[g] = franja, otra
    extremos = tuple(interseccion(f,g,y,z) for y,z in product(franja,otra))
    seguro = all(0<=r<=q and 0<=c<=q for r,c in extremos)
    if seguro:
        vertices = [(r,c,r-c,r+c) for r,c in extremos]
    else:
        vertices = []
        for h,k in PARES:
            for y,z in product(limites[h],limites[k]):
                r,c = interseccion(h,k,y,z)
                v = (r,c,r-c,r+c)
                if all(a<=w<=b for w,(a,b) in zip(v,limites)):
                    vertices.append(v)
    if not vertices:
        return False, None
    return seguro, tuple((min(t),max(t)) for t in zip(*vertices))


def construir_perfil(n):
    verificar_huella(COEF,G6)
    verificar_huella(FUNC,GL)
    d = json.loads(COEF.read_bytes())
    cc = [[Fraction.from_float(float(v)) for v in d[k]] for k in ("cS","cu0","cu1")]
    st = Tabla(256,[cc[0]],True,Fraction("8.75e-10"))
    ut = Tabla(256,cc[1:],False,Fraction("4.38e-11"))
    cert = json.loads(FUNC.read_bytes())
    umin = dn(float(Fraction(cert["constantes_corregidas"]["u_min"])))
    nmax = up(float(Fraction(cert["constantes_corregidas"]["nu_sup"])))
    a,b = map(Fraction,cert["nodos"]["GLb_n10"]["x_GL"])
    x = I(dn(float(a)),up(float(b)))
    @lru_cache(None)
    def tabla(u,ini,fin):
        t = ut if u else st
        ini,fin = (ini*(256//n), fin*(256//n))
        assert 0<=ini<=fin<=512
        lo = min(t.pt[ini,0],t.pt[fin,0])
        hi = max(t.pt[ini,1],t.pt[fin,1])
        if ini<fin:
            lo = min(lo,np.min(t.seg[ini:fin,0]))
            hi = max(hi,np.max(t.seg[ini:fin,1]))
        return I(max(umin,lo),min(1.,hi)) if u else I(lo,hi)
    @lru_cache(None)
    def oblicua(franja,centro):
        a,b = franja[0]-centro,franja[1]-centro
        u = tabla(True,max(0,a,-b),max(abs(a),abs(b)))
        # U es creciente en u y x. Evalúa ambos extremos con el mismo u.
        U = I(dn(u.lo+dn(x.lo*dn(1-u.lo))),up(u.hi+up(x.hi*up(1-u.hi))))
        return u, U
    @lru_cache(None)
    def casilla(pr):
        r,c,d,a = pr
        ud,Ud = oblicua(d,0)
        ua,Ua = oblicua(a,2*n)
        nu = unir_cotas(tabla(False,*r)*tabla(False,*c)*ud*ua,0.,nmax)
        W = nu*inversa_positiva(Ud*Ua)
        return nu,W,Ud,Ua
    return x, oblicua, casilla


def preparar(n=8):
    assert isinstance(n,int) and 0<n<=256 and 256%n==0
    L=10*n
    g=SimpleNamespace(n=n,L=L)
    g.L0,g.diagonal=modelo_agregado(n)
    x,oblicua,casilla=construir_perfil(n)
    g.x=x
    counts=[(b-a)*n for a,b in DOMINIO]
    offsets=np.cumsum([0]+counts).tolist()
    g.hoja=np.repeat(np.arange(6),counts)
    g.familia=np.array(FAMILIA)[g.hoja]
    g.color=np.array(COLOR)[g.hoja]
    g.y0=np.concatenate([np.arange(2*n*a,2*n*b,2) for a,b in DOMINIO])
    def ids(h,rango):
        base=2*n*DOMINIO[h][0]
        a,b=(v-base for v in rango)
        assert 0<=a<=b<=2*counts[h]
        k=min(a//2,counts[h]-1)
        l=max(k,(b-1)//2)
        return list(range(offsets[h]+k,offsets[h]+l+1))
    omlo=np.full(L,1/n)
    omhi=omlo.copy()
    nblo=omlo.copy()
    nbhi=omlo.copy()
    for i in range(2*n,L):
        u,U=oblicua((g.y0[i],g.y0[i]+2), (2*n if g.familia[i]==3 else 0))
        om=U*inversa_positiva(x)*(1/(2*n))
        # Pushforward of ν in this coloured sheet, density (1-u)/2.
        nb=unir_cotas((I(1.)-u)*(1/(2*n)),0.,1.)
        omlo[i],omhi[i],nblo[i],nbhi[i]=om.lo,om.hi,nb.lo,nb.hi
    g.om,g.nbar=I(omlo,omhi),I(nblo,nbhi)
    # Each centre is a rectangle in (r,c) at one definite colour.
    centros=[]
    jcentros=[]
    pesos=[]
    for e,r,c in product((0,1),range(n),range(n)):
        cr=(2*r,2*r+2)
        cc=(2*c,2*c+2)
        pr=(cr,cc,(cr[0]-cc[1],cr[1]-cc[0]),(cr[0]+cc[0],cr[1]+cc[1]))
        centros.append((e,r,c))
        jl=[ids(h,fr) for h,fr in zip((0,1,2+e,4+e),pr)]
        jcentros.append([s+[s[-1]]*(2-len(s)) for s in jl])
        pesos.append(casilla(pr)[0]*(1/(2*n*n)))
    g.centros_id=np.array(centros)
    g.J=np.asarray(jcentros,dtype=np.intp)
    g.peso=I(np.array([w.lo for w in pesos]),np.array([w.hi for w in pesos]))
    # Compute each unordered pair once. Fill symmetric slots for oriented paths.
    g.posible=np.zeros((L,L),bool)
    g.seguro=np.zeros((L,L),bool)
    listas=[{} for f in range(4)]
    kl,kh,vl,vh=(np.zeros((L,L)) for _ in range(4))
    for i,j in combinations(range(L),2):
        f,h=map(int,(g.familia[i],g.familia[j]))
        if f==h or (f==2 and h==3 and g.color[i]!=g.color[j]):
            continue
        ij=(int(g.y0[i]),int(g.y0[j]))
        seguro,pr=proyecciones(n,f,h,(ij[0],ij[0]+2),(ij[1],ij[1]+2))
        if pr is None:
            continue
        g.posible[i,j]=g.posible[j,i]=True
        g.seguro[i,j]=g.seguro[j,i]=seguro
        colores=(0,1) if h==1 else (int(g.color[j]),)
        for k in range(4):
            if k in (f,h):
                paneles=[i if k==f else j]
            elif k<2:
                paneles=ids(k,pr[k])
            else:
                paneles=[p for e in colores for p in ids(2*(k-1)+e,pr[k])]
            listas[k][(i,j)]=paneles
        nu,W,Ud,Ua=casilla(pr)
        # p=K/W after exact cancellation of ν, on the conditioned intersection.
        p = (x if 2 in (f,h) else Ud)*(x if 3 in (f,h) else Ua)
        p = unir_cotas(p,0.,1.)
        K = nu
        for k,U in ((2,Ud),(3,Ua)):
            if k in (f,h):
                K=K*(x*inversa_positiva(U))
        # W² p(1-p), with the global bound p(1-p)≤1/4.
        V=W.sq()*unir_cotas(p*(I(1.)-p),0.,0.25)
        kl[i,j]=kl[j,i]=max(0.,K.lo) if seguro else 0.
        kh[i,j]=kh[j,i]=K.hi
        vl[i,j]=vl[j,i]=max(0.,V.lo) if seguro else 0.
        vh[i,j]=vh[j,i]=V.hi
    g.cruces=[]
    for catalogo in listas:
        b=max(map(len,catalogo.values()))
        cat=np.zeros((L,L,b),dtype=np.intp)
        for (i,j),indices in catalogo.items():
            cat[i,j]=cat[j,i]=indices+[indices[-1]]*(b-len(indices))
        g.cruces.append(cat)
    g.K,g.V=I(kl,kh),I(vl,vh)
    v=np.array((1.,-1.,0.,0.))[g.familia]
    g.Pi=I(0.5*np.outer(v,v))
    g.G=g.L0-g.K
    g.GPi=g.G+g.Pi
    return g
