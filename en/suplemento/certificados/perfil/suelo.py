"""Residuo exacto del candidato binario G6 en r=0 y suelo para sus radios."""
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
import argparse
import hashlib
import json
import platform
import sys
import time


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def bound(x, upper):
    with localcontext() as ctx:
        ctx.prec = 18
        ctx.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def power_cheb(cs):
    """Coeficientes en x (de -1 a 1), convertidos exactamente."""
    n = len(cs)
    s = [F(0)] * n
    prev, now = [], [1]
    for k,c in enumerate(cs):
        for j, v in enumerate(now):
            s[j] += c*v
        nxt = [0,1] if k == 0 else [0] + [2*v for v in now]
        for j,v in enumerate(prev):
            nxt[j] -= v
        prev, now = now, nxt
    return s


def product(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def run(base):
    start, wall = time.process_time(), time.perf_counter()
    candidate = base/'resultados'/'candidato_coeficientes.json'
    j = json.loads(candidate.read_text('utf8'))
    cS,cU,cV = [[F.from_float(float(v)) for v in j[k]] for k in ('cS','cu0','cu1')]
    S,U,V = map(power_cheb, (cS,cU,cV))
    # En 0<=q<=1/2 ponemos x=4q-1; el panel alto de u(1-q) tiene variable -x.
    coeff = product(product(S,U), [(-1)**k*v for k,v in enumerate(V)])
    A0 = sum(coeff[k]/(k+1) for k in range(0,len(coeff),2))
    S0 = sum((-1)**k*c for k,c in enumerate(cS))
    residual = S0*A0-1
    cap = F(1,10**6)
    out = {}
    for name,g in [('ponderada',F(1,20)),('uniforme_conjunta',F(1))]:
        # Si E<=cap, |S|<=M, |u|<=Umax en el segmento candidato--solución.
        M = sum(map(abs,cS)) + cap
        Umax = max(sum(map(abs,cU)),sum(map(abs,cV))) + cap*g
        # R1=S(0)A-1; A está cerca del valor EXACTO A0 por el mismo límite de DA.
        DA = Umax**2 + 2*M*Umax*g
        C = abs(A0) + cap*DA + (abs(S0)+cap)*DA
        low = min(cap, abs(residual)/C)
        out[name] = dict(gamma=str(g), cota_sup_derivada=bound(C,True),
                         cota_inferior_error_candidato=bound(low,False))
    return dict(candidato=candidate.name, sha256_candidato=digest(candidate),
                sha256_guion=digest(Path(__file__)), version_python=sys.version,
                sistema=platform.platform(), punto="r=0",
                R1=[bound(residual,False),bound(residual,True)],
                G1=[bound(residual/A0,False),bound(residual/A0,True)],
                normas=out, cpu_s=time.process_time()-start, pared_s=time.perf_counter()-wall)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('base',type=Path)
    ap.add_argument('salida',type=Path)
    args = ap.parse_args()
    result=run(args.base)
    with args.salida.open('x',encoding='utf8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps(result,ensure_ascii=True))
