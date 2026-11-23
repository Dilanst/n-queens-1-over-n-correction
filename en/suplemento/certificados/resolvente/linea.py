"""Control variacional en L²(rho) de la línea R(3/8), con cajas continuas."""
import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import time

for env in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[env] = "1"
import numpy as np
from funcional import encierra_gamma


def dn(x):
    return np.nextafter(x, -np.inf)


def up(x):
    return np.nextafter(x, np.inf)


def rango_num(x):
    v = float(x)
    return dn(v), up(v)


def suma(x, eje):
    # Error de cualquier árbol binario de a lo sumo n-1 adiciones.
    n = x.shape[eje]
    v = np.sum(x, axis=eje)
    e = up(n*n*2.0**-49 * np.max(np.abs(x), axis=eje) + n*1e-310)
    return dn(v-e), up(v+e)


def cheb(c,t):
    b1 = b2 = F(0)
    for a in reversed(c[1:]):
        b0 = a + 2*t*b1-b2
        b2, b1 = b1, b0
    return c[0]+t*b1-b2


class Tabla:
    """Rangos en celdas elementales. En la costura cada lado usa su polinomio."""
    def __init__(self, m, paneles, es_s, eps):
        escala = 2*m
        tramos, puntos = [], []
        for i in range(escala):
            medio = i >= m
            c = paneles[0] if es_s or not medio else paneles[1]
            def val(j):
                y = F(j,escala)
                t = 4*(1-y)-1 if es_s and medio else 4*y-(3 if medio else 1)
                return cheb(c,t)
            z0, z1 = val(i), val(i+1)
            # max |T_j''| = j²(j²-1)/3; el cambio de coordenada aporta 16.
            m2 = 16*sum(abs(a)*F(j*j*(j*j-1),3) for j,a in enumerate(c))
            e = m2/(8*escala**2) + eps
            tramos.append((rango_num(min(z0,z1)-e)[0], rango_num(max(z0,z1)+e)[1]))
            puntos.append((rango_num(z0-eps)[0], rango_num(z0+eps)[1]))
        puntos.append((rango_num(z1-eps)[0], rango_num(z1+eps)[1]))
        # Los dos valores laterales en la unión pueden diferir en el candidato.
        if not es_s:
            left = cheb(paneles[0],F(1))
            puntos[m] = (min(puntos[m][0],rango_num(left-eps)[0]),
                         max(puntos[m][1],rango_num(left+eps)[1]))
        self.seg, self.pt = np.asarray(tramos), np.asarray(puntos)

    def bounds(self, a,b):
        assert np.all((a>=0)&(b>=a)&(b<len(self.pt))) and np.max(b-a)<=8
        lo, hi = self.pt[a,0], self.pt[a,1]
        for j in range(int(np.max(b-a))):
            k = np.minimum(a+j,len(self.seg)-1)
            lo = np.where(a+j < b,np.minimum(lo,self.seg[k,0]),lo)
            hi = np.where(a+j < b,np.maximum(hi,self.seg[k,1]),hi)
        return np.minimum(lo,self.pt[b,0]), np.maximum(hi,self.pt[b,1])


def abs_box(a,b):
    return np.maximum(0,np.maximum(a,-b)), np.maximum(np.abs(a),np.abs(b))


def run(m, cand, x0, a, b, m_ensayo=None, solo_ensayo=False, solo_operador=False):
    t0 = time.process_time()
    assert m > 0 and m%8 == 0 and m & (m-1) == 0
    q = 2*m
    raw = cand.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == "a15d61a91bcc0ac711eccd09eb0c3486b5d1b510951dc3ad47cd773e5ed3abc5"
    coef = json.loads(raw)
    S, U0, U1 = [[F.from_float(float(v)) for v in coef[k]] for k in ("cS","cu0","cu1")]
    ps = Tabla(m,[S],True,F("8.75e-10"))
    pu = Tabla(m,[U0,U1],False,F("4.38e-11"))
    familias = (0,1,2,2,3,3)
    # Todos los extremos espaciales se representan como enteros en unidad 1/(2m).
    ys = [np.arange(lo,hi,2,dtype=int)
          for lo,hi in ((0,q),(0,q),(-q,q),(-q,q),(0,2*q),(0,2*q))]
    inc = np.cumsum([0]+[len(y) for y in ys])
    slices = [slice(k,j) for k,j in zip(inc[:-1],inc[1:])]
    L = inc[-1]
    xl, xh = rango_num(a)[0], rango_num(b)[1]
    def alpha(ul,uh):
        # alpha(x,u) creciente en x y decreciente en u. U = x+(1-x)u.
        return (dn(xl/up(xl+up(up(1-xl)*uh))),
                up(xh/dn(xh+dn(dn(1-xh)*ul))))
    def en_linea(f,y,e):
        if f<=1:
            return np.ones_like(y,dtype=float), np.ones_like(y,dtype=float)
        lo, hi = abs_box(y-(q if f==3 else 0),y+e-(q if f==3 else 0))
        ul,uh = pu.bounds(lo,hi)
        return alpha(ul,uh)
    alfas = [en_linea(f,y,2) for f,y in zip(familias,ys)]
    wl = np.concatenate([dn((1/m if f<2 else .5/m)/hi) for f,(_,hi) in zip(familias,alfas)])
    wh = np.concatenate([up((1/m if f<2 else .5/m)/lo) for f,(lo,_) in zip(familias,alfas)])
    def bloque(s,t,y,z,dy,dz):
        # s<t, familias diferentes, hojas compatibles. Producto completo de paneles.
        f,g = familias[s], familias[t]
        y,Y,z,Z = y[:,None],(y+dy)[:,None],z[None,:],(z+dz)[None,:]
        if (f,g)==(0,1):
            r,R,c,C = y,Y,z,Z
        elif (f,g)==(0,2):
            r,R,c,C = y,Y,y-Z,Y-z
        elif (f,g)==(0,3):
            r,R,c,C = y,Y,z-Y,Z-y
        elif (f,g)==(1,2):
            r,R,c,C = z+y,Z+Y,y,Y
        elif (f,g)==(1,3):
            r,R,c,C = z-Y,Z-y,y,Y
        else:
            r,R,c,C = (y+z)//2,(Y+Z)//2,(z-Y)//2,(Z-y)//2
        # Un borde aislado en la variable integrada tiene medida nula.
        fuera = (R<0)|(r>q)|(C<0)|(c>q)
        dentro = (r>=0)&(R<=q)&(c>=0)&(C<=q)
        r,R,c,C = (np.clip(k,0,q) for k in (r,R,c,C))
        d,D = (z,Z) if g==2 else (r-C,R-c)
        if f==2:
            d,D = y,Y
        e,E = (z-q,Z-q) if g==3 else (r+c-q,R+C-q)
        rl,rh = ps.bounds(r,R)
        cl,ch = ps.bounds(c,C)
        dl,dh = pu.bounds(*abs_box(d,D))
        el,eh = pu.bounds(*abs_box(e,E))
        lo = dn(dn(rl*cl)*dn(dl*el))
        hi = up(up(rh*ch)*up(dh*eh))
        lo = np.where(dentro, np.maximum(lo,0.), 0.)
        hi = np.where(fuera,0.,np.minimum(hi,1.405000000000001))
        for line,coord,top in ((f,y,Y),(g,z,Z)):
            if line>=2:
                fl,fh = en_linea(line,coord,top-coord)
                lo,hi = dn(lo*fl),up(hi*fh)
        return np.maximum(0.,lo),hi

    bl, bh = np.zeros(L), np.zeros(L)
    densa = m_ensayo is None or m==m_ensayo
    if densa:
        kl = np.zeros((L,L))
        kh = np.zeros_like(kl)
    for s, (f,y,si) in enumerate(zip(familias,ys,slices)):
        for t in range(s+1,len(ys)):
            if not densa or f==familias[t] or (f==2 and familias[t]==3 and (t-s)%2):
                continue
            sj = slices[t]
            lo,hi = bloque(s,t,y,ys[t],2,2)
            kl[si,sj],kh[si,sj] = lo,hi
            kl[sj,si],kh[sj,si] = lo.T,hi.T
        if s > 0:
            lo,hi = bloque(0,s,np.array([3*q//8]),y,0,2)
            bl[si],bh[si] = lo[0],hi[0]
    v = np.concatenate([np.full(len(y),1 if f==0 else (-1 if f==1 else 0)) for f,y in zip(familias,ys)])
    if solo_operador:
        assert densa
        return kl,kh,wl,wh,v,ys
    def matriz_peso(kmin,kmax,proj,wmin,wmax):
        tl,tu = dn(kmin+proj),up(kmax+proj)
        return dn(np.minimum(tl*wmin,tl*wmax)),up(np.maximum(tu*wmin,tu*wmax))

    def accion(ml,mh,psi):
        pl = dn(np.minimum(ml*psi,mh*psi))
        ph = up(np.maximum(ml*psi,mh*psi))
        return suma(pl,1)[0],suma(ph,1)[1]

    if densa:
        proj = .5*np.outer(v,v)
        ml,mh = matriz_peso(kl,kh,proj,wl,wh)
        # Esta resolución sólo elige el ensayo y puede redondear libremente.
        psi = np.linalg.solve(np.eye(L)+(ml+mh)*.5,(bl+bh)*.5)
        if solo_ensayo:
            return psi
        op_l,op_h = accion(ml,mh,psi)
    else:
        assert m >= m_ensayo and m%m_ensayo==0
        psi = np.repeat(run(m_ensayo,cand,x0,a,b,solo_ensayo=True),m//m_ensayo)
        op_l,op_h = np.zeros(L),np.zeros(L)
        for s,f in enumerate(familias):
            for i in range(0,len(ys[s]),32):
                y = ys[s][i:i+32]
                si = slice(inc[s]+i,inc[s]+i+len(y))
                for t,g in enumerate(familias):
                    sj=slices[t]
                    if f==g or (min(f,g)==2 and max(f,g)==3 and (s-t)%2):
                        lo=hi=0.
                    elif s<t:
                        lo,hi=bloque(s,t,y,ys[t],2,2)
                    else:
                        lo,hi=bloque(t,s,ys[t],y,2,2)
                        lo,hi=lo.T,hi.T
                    ml,mh=matriz_peso(lo,hi,.5*np.outer(v[si],v[sj]),wl[sj],wh[sj])
                    el,eh=accion(ml,mh,psi[sj])
                    op_l[si]=dn(op_l[si]+el)
                    op_h[si]=up(op_h[si]+eh)
    rlo = dn(dn(bl-psi)-op_h)
    rhi = up(up(bh-psi)-op_l)
    abs_r = np.maximum(np.abs(rlo),np.abs(rhi))
    n2 = suma(up(wh*up(abs_r*abs_r)),0)[1]
    pcl, pch = dn(bl+rlo), up(bh+rhi)
    yl = dn(np.minimum(psi*pcl,psi*pch))
    yh = up(np.maximum(psi*pcl,psi*pch))
    evl = suma(dn(np.minimum(yl*wl,yl*wh)),0)[0]
    evh = suma(up(np.maximum(yh*wl,yh*wh)),0)[1]
    gamma = rango_num(encierra_gamma(b,F(".174"),F(".164")))[0]
    err = up(n2/gamma)
    Llo,Lhi = dn(evl-1.5),up(up(evh+err)-1.5)
    assert np.isfinite([Llo,Lhi,n2]).all() and 0<gamma and Llo<=Lhi
    return {"m":m, "m_ensayo":m_ensayo or m, "paneles":int(L), "x0_piloto":x0.hex(), "linea":"R(3/8)",
            "perfil_sha256":hashlib.sha256(raw).hexdigest(), "n2_sup":n2,
            "residuo_cuadratico_sobre_gamma_sup":err,
            "Q_variacional":[evl,evh], "L0_diag":[Llo,Lhi],
            "gamma_min":gamma, "cpu_s":time.process_time()-t0}


if __name__ == "__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("m",type=int)
    ap.add_argument("candidato",type=Path)
    ap.add_argument("cert_funcional",type=Path)
    ap.add_argument("salida",type=Path)
    ap.add_argument("--m-ensayo",type=int)
    args=ap.parse_args()
    cert=json.loads(args.cert_funcional.read_text(encoding="utf8"))["nodos"]["GLb_n10"]
    a,b=map(F,cert["x_GL"])
    res=run(args.m,args.candidato,float.fromhex(cert["x_almacenado"]),a,b,args.m_ensayo)
    res["cert_funcional_sha256"]=hashlib.sha256(args.cert_funcional.read_bytes()).hexdigest()
    assert res["cpu_s"]<300
    with args.salida.open("x",encoding="utf8") as out:
        json.dump(res,out,indent=2)
        out.write("\n")
    print(json.dumps(res))
