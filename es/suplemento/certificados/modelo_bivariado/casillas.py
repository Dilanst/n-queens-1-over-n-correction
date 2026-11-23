"""Integra I y Omega con el modelo de las seis hojas en casillas del continuo."""
from fractions import Fraction as F
import json
import numpy as np
from linea import Tabla, abs_box, dn, up, suma


def momentos(m,candidato,a,b,l0,l1,diag0,diag1):
    data=json.loads(candidato.read_bytes())
    cs,cu,cv=[[F.from_float(float(x)) for x in data[k]] for k in ("cS","cu0","cu1")]
    st=Tabla(m,[cs],True,F("8.75e-10"))
    ut=Tabla(m,[cu,cv],False,F("4.38e-11"))
    i,j=np.ogrid[:m,:m]
    z=np.arange(m)
    sl,sh=st.bounds(2*z,2*z+2)
    dl,dh=ut.bounds(*abs_box(2*(i-j-1),2*(i-j+1)))
    al,ah=ut.bounds(*abs_box(2*(i+j-m),2*(i+j+2-m)))
    xlo,xhi=dn(float(a)),up(float(b))
    def U(lo,hi):
        lo=np.maximum(lo,.17399999999999998)
        hi=np.minimum(hi,1.)
        return dn(lo+dn(xlo*dn(1-lo))),up(hi+up(xhi*up(1-hi)))
    ud,Ud=U(dl,dh)
    ua,Ua=U(al,ah)
    nlo=dn(dn(sl[i]*sl[j])*dn(dl*al))
    nhi=np.minimum(1.405000000000001,up(up(sh[i]*sh[j])*up(dh*ah)))
    wlo=dn(nlo/up(Ud*Ua))
    whi=up(nhi/dn(ud*ua))
    blo,bhi=dn(nlo*wlo),up(nhi*whi)
    def integral(lo,hi):
        rl=suma(lo,1)[0]
        rh=suma(hi,1)[1]
        return dn(suma(rl,0)[0]/(m*m)),up(suma(rh,0)[1]/(m*m))
    def por_beta(lo,hi):
        return integral(dn(np.minimum(blo*lo,bhi*lo)),up(np.maximum(blo*hi,bhi*hi)))
    Imin=Imax=Omin=Omax=0.
    for e in (0,1):
        dbase=(2+2*e)*m + m + i-j-1
        abase=(6+2*e)*m + i+j
        indices=([i],[m+j],[dbase,dbase+1],[abase,abase+1])
        so0,so1,sd0,sd1=0.,0.,0.,0.
        for k,indices_k in enumerate(indices):
            dlo=diag0[indices_k[0]]
            dhi=diag1[indices_k[0]]
            for p in indices_k[1:]:
                dlo=np.minimum(dlo,diag0[p])
                dhi=np.maximum(dhi,diag1[p])
            sd0,sd1=dn(sd0+dlo),up(sd1+dhi)
            for indices_h in indices[k+1:]:
                lo=np.inf
                hi=-np.inf
                for p in indices_k:
                    for q in indices_h:
                        lo=np.minimum(lo,l0[p,q])
                        hi=np.maximum(hi,l1[p,q])
                so0,so1=dn(so0+lo),up(so1+hi)
        ol,oh=por_beta(so0,so1)
        il,ih=por_beta(np.maximum(0.,dn(sd0+2*so0)),up(sd1+2*so1))
        Omin,Omax=dn(Omin+ol*.5),up(Omax+oh*.5)
        Imin,Imax=dn(Imin+il*.5),up(Imax+ih*.5)
    T0,T1=integral(dn(blo*wlo),up(bhi*whi))
    return {"I":[float(Imin),float(Imax)],"Omega":[float(Omin),float(Omax)],
            "f5c":[float(dn(-3*Omax)),float(up(-3*Omin))],
            "f4":[float(dn(Omin-up(9*T1))),float(up(Omax-dn(9*T0)))],
            "T1_cajas":[float(T0),float(T1)]}
