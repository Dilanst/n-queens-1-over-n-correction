"""taylor_cotas.py -- error de la parte de Taylor (circulo de radio r, N puntos, coeficientes de d y de V por DFT,
k_n = d_n + (1 - n) v_n, integral sum_{n=2}^{N-1} k_n r^(n-1)/(n-1)) en funcion de (R, M_k, M_V, N, r).  [D]
Teorema 3.3 de parte_03.tex (parte de seis hojas, k_6; la parte F se trata aparte, parte_F.py):
  E_T = sum_{n=2}^{N-1} r^(n-1)/(n-1) sum_{l>=1} (k_{n+lN} + l N v_{n+lN}) r^(lN) - sum_{n>=N} k_n r^(n-1)/(n-1),
  |k_m| <= M_k R^-m, |v_m| <= M_V R^-m  (Cauchy en |x| = R, M_k = max|k_6|, M_V = max|V|).
Evaluacion puntual de la serie (control GL24): |k(x) - sum_{n=2}^{N-1} khat_n x^n| con la misma estructura.
Version con muestras baratas en |x| = R_s (Teorema 4.4): coeficientes m >= N estimados por DFT de N_s muestras,
con solapamiento M R^-m Q/(1-Q), Q = (R_s/R)^N_s, y ruido delta R_s^-m.
Uso: python3 taylor_cotas.py -> taylor_cotas.json"""
import json
import math
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.dont_write_bytecode = True
import cota_gruesa as CG  # noqa: E402


def pesos(r, N, mmax):
    """c_m (coeficiente de |k_m|) y c'_m (de |v_m|) para m = 0..mmax en la cota de E_T."""
    m = np.arange(mmax + 1)
    c = np.zeros(mmax + 1)
    cp = np.zeros(mmax + 1)
    for mm in range(N, mmax + 1):
        c[mm] = r ** (mm - 1) / (mm - 1)                      # truncacion
        n, l = mm % N, mm // N
        if 2 <= n <= N - 1 and l >= 1:
            c[mm] += r ** (mm - 1) / (n - 1)                  # solapamiento sobre k_n
            cp[mm] = r ** (mm - 1) * l * N / (n - 1)
    return m, c, cp


def E_T_cruda(r, N, R, Mk, MV, mmax=4000):
    m, c, cp = pesos(r, N, mmax)
    with np.errstate(over="ignore", invalid="ignore"):
        lw = np.log(np.where(c > 0, c, 1)) - m * math.log(R)
        lwp = np.log(np.where(cp > 0, cp, 1)) - m * math.log(R)
    t1 = float(np.sum(np.where(c > 0, np.exp(lw), 0.0)))
    t2 = float(np.sum(np.where(cp > 0, np.exp(lwp), 0.0)))
    return Mk * t1 + MV * t2


def E_punto_cruda(x, r, N, R, Mk, MV, mmax=4000):
    """|k(x) - serie| en 0 < x < r: sum_{n=2}^{N-1} x^n sum_l (|k_{n+lN}| + lN|v_{n+lN}|) r^{lN} + sum_{m>=N} |k_m| x^m."""
    tot = 0.0
    for mm in range(N, mmax + 1):
        a = Mk * math.exp(mm * math.log(x / R))
        n, l = mm % N, mm // N
        if 2 <= n <= N - 1 and l >= 1:
            fac = math.exp(n * math.log(x) + l * N * math.log(r) - mm * math.log(R))
            a += (Mk + l * N * MV) * fac
        tot += a
        if a < 1e-300 and mm > 4 * N:
            break
    return tot


def sup_circulo(R, npt=1000):
    """(sup |k_6|, sup |V|) en |x| = R con la cota gruesa (discos que recubren el circulo)."""
    z = R * np.exp(2j * np.pi * np.arange(npt) / npt)
    rr = CG.recubrir(z)
    rc = 0.25 * min(CG.XC2 - R, 0.05)
    c0 = CG.f0_cota() + 1.0 / 12
    mk = mv = 0.0
    for zz, r_ in zip(z, rr):
        a = CG.cota_dV(zz, r_)
        mv = max(mv, a["V"])
        mk = max(mk, CG.cota_k6(zz, r_, rc, c0))
    return mk * CG.SEG, mv * CG.SEG


def E_T_muestras(r, N, R, Mk, MV, Rs, Ns, delta_k, delta_v, kmax_true=0.0, mmax=3000):
    """Cota con N_s muestras baratas en |x| = R_s (coeficientes m <= N_s - 1 de la DFT; m >= N_s crudos).
    kmax_true: cota de |khat_m| (valores muestreados; 0 en el diseno, se suma aparte con datos)."""
    m, c, cp = pesos(r, N, mmax)
    Q = (Rs / R) ** Ns
    lQ = Ns * math.log(Rs / R) - math.log1p(-Q)
    tot = 0.0
    for mm in range(N, mmax + 1):
        if c[mm] == 0 and cp[mm] == 0:
            continue
        lc = math.log(c[mm]) if c[mm] > 0 else -math.inf
        lcp = math.log(cp[mm]) if cp[mm] > 0 else -math.inf
        if mm <= Ns - 1:
            la = math.log(Mk) - mm * math.log(R) + lQ
            ln_ = math.log(delta_k) - mm * math.log(Rs)
            lav = math.log(MV) - mm * math.log(R) + lQ
            lnv = math.log(delta_v) - mm * math.log(Rs)
            t = [lc + la, lc + ln_, lcp + lav, lcp + lnv]
        else:
            t = [lc + math.log(Mk) - mm * math.log(R), lcp + math.log(MV) - mm * math.log(R)]
        tot += sum(math.exp(v) for v in t if v > -700)
    return tot


if __name__ == "__main__":
    out = {"circulos": {}, "diseno_actual": {}, "control": {}}
    for R in (0.07, 0.08, 0.09, 0.095, 0.1):
        mk, mv = sup_circulo(R)
        out["circulos"][str(R)] = {"M_k6": mk, "M_V": mv}
        e = E_T_cruda(0.06, 32, R, mk, mv)
        out["diseno_actual"][str(R)] = e
        print(f"R={R}: M_k6 <= {mk:.3e}, M_V <= {mv:.3e};  E_T(r=0.06, N=32) <= {e:.3e}")
    # M_k necesario para 1e-9 con el diseno actual, si M_V fuera 0
    for R in (0.09, 0.1):
        e1 = E_T_cruda(0.06, 32, R, 1.0, 0.0)
        out["diseno_actual"][f"Mk_necesario_R{R}"] = 1e-9 / e1
        print(f"R={R}: M_k necesario para 1e-9 (sin V): {1e-9 / e1:.3e}")
    # control: serie en los 3 nodos de GL24 con x < 0.035
    xg, wg = np.polynomial.legendre.leggauss(24)
    X, W = 0.5 * (xg + 1), 0.5 * wg
    R = 0.09
    mk, mv = out["circulos"][str(R)]["M_k6"], out["circulos"][str(R)]["M_V"]
    tot = 0.0
    for i in range(3):
        e = E_punto_cruda(X[i], 0.06, 32, R, mk, mv)
        tot += W[i] / X[i] ** 2 * e
    out["control"]["serie_3_nodos_R0.09"] = tot
    print(f"control: sum w/x^2 |error serie| (3 nodos, R = 0.09) <= {tot:.3e}")
    json.dump(out, open(os.path.join(AQUI, "taylor_cotas.json"), "w"), indent=1)
