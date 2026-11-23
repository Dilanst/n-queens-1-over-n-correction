"""Certificado continuo por paneles para todos los pares de líneas de un nodo real."""
import argparse
import hashlib
import json
import os
from fractions import Fraction as F
from pathlib import Path
import sys
import time

for env in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[env] = "1"
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"resolvente"))
from linea import dn, up, suma, run as operador
import numpy as np
from casillas import momentos


def pesos(lo,hi,wl,wh):
    """Multiplica un intervalo por un peso positivo incierto."""
    return dn(np.minimum(lo*wl,lo*wh)), up(np.maximum(hi*wl,hi*wh))


def producto(lo,hi,psi):
    """Cota de [lo,hi] @ psi, con psi exacto en binary64.

    Dos productos BLAS y una adición por extremo. Una cota absoluta por
    entrada usa los máximos de su fila y columna y el presupuesto n².
    """
    n=psi.shape[0]
    # Alejar del régimen subnormal los extremos que ya recubren un cero.
    # Las cuatro sustituciones sólo ensanchan el intervalo.
    lo=np.where((lo<0)&(lo>-1e-100),-1e-100,np.where((lo>0)&(lo<1e-100),0.,lo))
    hi=np.where((hi>0)&(hi<1e-100),1e-100,np.where((hi<0)&(hi>-1e-100),0.,hi))
    p, m = np.maximum(psi,0), np.minimum(psi,0)
    fila=np.maximum(np.max(np.abs(lo),axis=1),np.max(np.abs(hi),axis=1))
    col=np.max(np.abs(psi),axis=0)
    e=up(up(up(fila[:,None]*col[None,:])*float(n*n))*2.0**-48 + n*n*1e-300)
    izq=dn((lo@p + hi@m)-e)
    der=up((hi@p + lo@m)+e)
    return izq,der


def guardar_compacto(path,lo,hi,diag0,diag1,n2,ys,m):
    # La resolución 2^-20 amplía cada límite como máximo 2^-20. El entero
    # permanece dentro de int32 por la validación antes de convertir.
    ia,ib=np.triu_indices(len(lo))
    def entero(z, inferior):
        w=(np.floor if inferior else np.ceil)(z*(2**20))
        assert np.max(w)<2**31 and np.min(w)>=-2**31
        return w.astype(np.int32)
    assert not path.exists()
    with path.open("xb") as f:
        np.savez_compressed(f, L_min=entero(lo[ia,ib],True), L_max=entero(hi[ia,ib],False),
                            diagonal_min=entero(diag0,True),diagonal_max=entero(diag1,False),
                            potencia_dos=np.int32(-20),n2_sup=n2, m=np.int32(m),
                            hoja=np.concatenate([np.full(len(y),s,np.int8) for s,y in enumerate(ys)]),
                            y0_ticks=np.concatenate(ys).astype(np.int32))
    with np.load(path) as check:
        assert np.all(check["L_min"]*2.**-20<=lo[ia,ib])
        assert np.all(check["L_max"]*2.**-20>=hi[ia,ib])
        assert np.all(check["diagonal_min"]*2.**-20<=diag0)
        assert np.all(check["diagonal_max"]*2.**-20>=diag1)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(m, perfil, fuente, tag, destino=None, linea=None):
    t0=time.process_time()
    raw=fuente.read_bytes()
    j=json.loads(raw)
    nodo=j["nodos"][tag]
    a,b=map(F,nodo["x_GL"])
    gamma=dn(float(nodo["gamma_min"]))
    global_l0=up(float(nodo["L0_modulo_sup"]))
    kl,kh,wl,wh,v,ys=operador(m,perfil,float.fromhex(nodo["x_almacenado"]),a,b,solo_operador=True)
    N=len(wl)
    p=.5*np.outer(v,v)
    ol,oh=pesos(dn(kl+p),up(kh+p),wl,wh)
    candidata=(ol+oh)*.5
    candidata[np.abs(candidata)<1e-100]=0.
    rhs=(kl+kh)*.5
    rhs[np.abs(rhs)<1e-100]=0.
    psi=np.linalg.solve(np.eye(N)+candidata,rhs)
    psi[np.abs(psi)<1e-90]=0.
    del candidata,rhs
    el,eh=producto(ol,oh,psi)
    del ol,oh
    rl=dn(dn(kl-psi)-eh)
    rh=up(up(kh-psi)-el)
    del el,eh
    mag=np.maximum(np.abs(rl),np.abs(rh))
    n2=suma(up(wh[:,None]*up(mag*mag)),0)[1]
    del mag
    assert np.all(n2>=0.)
    k2=suma(up(wh[:,None]*up(kh*kh)),0)[1]
    # <k_a,psi_b> + <psi_a,r_b>. El segundo grupo se forma transpuesto.
    wl_k,wh_k=pesos(kl,kh,wl,wh)
    bl,bh=producto(wl_k,wh_k,psi)
    del wl_k,wh_k
    wlr,whr=pesos(rl.T,rh.T,wl,wh)
    cl,ch=producto(wlr,whr,psi)
    del rl,rh,wlr,whr,psi
    center_lo=dn(dn(bl+cl.T)-3*p)
    center_hi=up(up(bh+ch.T)-3*p)
    del bl,bh,cl,ch
    err=up(up(np.sqrt(up(n2[:,None]*n2)))/gamma)
    pre_lo,pre_hi=dn(center_lo-err),up(center_hi+err)
    l0= np.maximum(pre_lo,pre_lo.T)
    l1= np.minimum(pre_hi,pre_hi.T)
    # Dos mayoraciones a priori que valen para el representante canónico.
    cauchy=up(up(np.sqrt(up(k2[:,None]*k2)))/gamma)
    l0=np.maximum(l0,np.maximum(-global_l0,dn(-3*p-cauchy)))
    l1=np.minimum(l1,np.minimum(global_l0,up(-3*p+cauchy)))
    # La diagonal geométrica a=b tiene resto variacional no negativo; el
    # cuadrado del mismo panel también cubre a!=b y conserva ambos signos.
    diag0=np.maximum(l0.diagonal(),np.maximum(center_lo.diagonal(),-3*p.diagonal()))
    diag1=l1.diagonal().copy()
    assert np.all(np.isfinite(l0)) and np.all(np.isfinite(l1))
    assert np.all(l1>=l0) and np.all(diag1>=diag0)
    assert np.array_equal(l0,l0.T) and np.array_equal(l1,l1.T)
    width=up(l1-l0)
    cota_masa=up(np.sqrt(suma(up(wh*n2),0)[1]))
    info={"nodo":tag, "m":m, "paneles":int(N),"pares_ordenados":int(N*N),
          "pares_independientes":int(N*(N+1)//2),
          "norma_residuo_HS_sup_d_rho_a_d_rho_t":float(cota_masa),
          "max_norma_residuo_sup":float(up(np.sqrt(np.max(n2)))),
          "max_error_bilateral_sup":float(np.max(err)),
          "L0_todos_los_pares":[float(l0.min()),float(l1.max())],
          "ancho_maximo":float(width.max()),"ancho_mediano_diagnostico":float(np.median(width)),
          "max_semiancho_diagonal":float(up(np.max(up(diag1-diag0))*.5)),
          "perfil_sha256":hashlib.sha256(perfil.read_bytes()).hexdigest(),
          "funcional_sha256":hashlib.sha256(raw).hexdigest()}
    info["integrales_casilla"]=momentos(m,perfil,a,b,l0,l1,diag0,diag1)
    if tag=="GLb_n10":
        # 3/8 coincide con extremo de panel. La función continua se ha
        # encerrado en ambas cajas cerradas, también en fronteras del soporte.
        i=3*m//8
        hh=[i-1,i]
        cr=[float(max(diag0[hh])),float(min(diag1[hh]))]
        assert cr[0]<=cr[1]
        info["R_3_8_diagonal_independiente"]=cr
        if linea:
            previo=json.loads(linea.read_text("utf8"))["L0_diag"]
            inter=[max(previo[0],cr[0]),min(previo[1],cr[1])]
            assert inter[0]<=inter[1]
            info["interseccion_control_una_linea"]=inter
    if destino:
        info["modelo"]=destino.name
        info["modelo_sha256"]=guardar_compacto(destino,l0,l1,diag0,diag1,n2,ys,m)
        info["ancho_maximo_guardado_sup"]=float(up(width.max()+2**-19))
    info["cpu_s"]=time.process_time()-t0
    assert info["cpu_s"]<300
    return info


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("m",type=int)
    ap.add_argument("perfil",type=Path)
    ap.add_argument("funcional",type=Path)
    ap.add_argument("tag")
    ap.add_argument("salida",type=Path)
    ap.add_argument("--modelo",type=Path)
    ap.add_argument("--linea",type=Path)
    ar=ap.parse_args()
    resultado=run(ar.m,ar.perfil,ar.funcional,ar.tag,ar.modelo,ar.linea)
    with ar.salida.open("x",encoding="utf8") as f:
        json.dump(resultado,f,indent=2)
        f.write("\n")
    print(json.dumps({k:resultado[k] for k in ("nodo","m","max_error_bilateral_sup","ancho_maximo","cpu_s")}))
