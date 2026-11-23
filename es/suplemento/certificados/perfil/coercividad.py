"""Cierre autónomo en variables logarítmicas. Constantes justificadas en PERFIL.md."""
import argparse
from fractions import Fraction as F
from pathlib import Path
import json
import platform
import sys
import time
from suelo import bound, digest


def run(p,c):
    t0,w0=time.process_time(),time.perf_counter()
    j=json.loads(p.read_text('utf8'))
    assert j['candidato_sha256']==digest(c)
    rs,ru=[max(F(v['abs_R_sup']) for v in j['regimenes'] if v['tipo']==k) for k in ('S','u')]
    S1,S2=map(F,j['rango_perfil']['S'])
    u1,u2=map(F,j['rango_perfil']['u'])
    assert 1<=S1<=S2<=5 and F(1,6)<=u1<=u2<=1
    r=max(rs,ru)
    assert r<F(1,2)
    beta,L=5000,40
    eta=beta*r
    rad=eta*F(1001,1000)
    assert rad<F(1,10**6)
    assert beta*L*rad<1 and eta+beta*L*rad**2/2<=rad
    # exp(rad)-1 <= rad/(1-rad), por la serie de exp.
    esp, eup=(z*rad/(1-rad) for z in (S2,u2))
    return dict(candidato_sha256=digest(c),residuo_certificado_sha256=digest(p),
                guion_sha256=digest(Path(__file__)),auxiliar_sha256=digest(Path(__file__).with_name('suelo.py')),
                max_R1=bound(rs,True),max_R2=bound(ru,True),beta_log=beta,L_log=L,
                radio_log=bound(rad,True),epsilon_S=bound(esp,True),epsilon_u=bound(eup,True),
                cpu_s=time.process_time()-t0,pared_s=time.perf_counter()-w0,
                python=sys.version,sistema=platform.platform(), hilos=1)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('residuo','candidato','salida'):
        p.add_argument(k,type=Path)
    a=p.parse_args()
    result=run(a.residuo,a.candidato)
    with a.salida.open('x',encoding='utf8') as f:
        json.dump(result,f,indent=1,ensure_ascii=False)
    print(json.dumps(result))
