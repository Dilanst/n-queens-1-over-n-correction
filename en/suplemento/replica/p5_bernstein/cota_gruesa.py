"""cota_gruesa.py -- cota analitica gruesa de |d|, |V|, |V'| y |k_6| (k_6 = d + V - x V' + F(0) - 1/12) en discos y en
contornos complejos, solo con normas de operadores.  [D] (salvo la transcripcion codigo -> estructura de las filas,
[O]) con constantes de constantes_iv.json [O].

Sucesión (notacion de D78/paso_limite, parte_02-04, y del motor):
  U_f(z) = u_f + z (1 - u_f), u_f en [u_min, 1]  (H3);  U_H = z.
  |1 + z lam| >= 1/sigma(z) para lam en [0, Lambda], Lambda = 2 sup m/u >= lambda_*  (Lema 2.3);
  ||S(z)^-1|| <= s = sigma/u_min;  ||A_HH^-1|| <= a = 1/(1 - ||B||);  ||N_1|| <= n = 2 sqrt(m_max);
  ||A(z)^-1|| <= alpha = || [[a + |z| a^2 n^2 s, a n s U+], [|z| a n s, s U+]] ||_F  (Prop. 3.1, bloques);
  L0 + 3 Pi = (K rho~) A^-T K  =>  |L0(a,b)| <= 3/2 + k~ k_* alpha  (k_* = sup_a ||K(a,.)||, k~ = sup_a ||(K rho~)(a,.)||);
  theta(a) = 3 m*(a) - sum_b K(a,b)^2 rho_b;  y el recuento fila a fila (filas_cota) sobre la estructura de
  codigo/q_c.py, rect/motor/filasA_malla.py, rect/f6/f6_malla.py, rect/q1/d1_cont.py, rect/demo/d2_c.py.
Todas las cotas valen en todo el disco D(z, r) (cotas de peor caso de cada ingrediente en el disco).
Redondeo: las operaciones son sumas, productos y cocientes de positivos (error relativo < 1e-12 en < 1e3 pasos) y
unas pocas restas bien condicionadas; el resultado final se multiplica por (1 + 1e-9).
Uso: python3 cota_gruesa.py  -> cota_gruesa.json (tablas en contornos)"""
import json
import math
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
CT = json.load(open(os.path.join(AQUI, "constantes_iv.json")))
U_MIN = CT["u"][0]                       # cota inferior rigurosa de u_min
M_MAX = CT["m_max_sup"]                  # 1 - u_min (cota superior)
LAM = CT["Lambda_sup"]                   # Lambda = 2 sup m/u (cota superior)
C_NU = CT["nu"][1]                       # sup nu
I_NU2 = CT["sup_r_int_nu2_dq"]           # sup_r int nu^2 dq
NB = CT["normB_HS_sup"]                  # ||B|| <= ||nu - 1||_HS
A_HH = 1.0 / (1.0 - NB)                  # ||A_HH^-1||
N1 = 2.0 * math.sqrt(M_MAX)              # ||N_1||
SEG = 1.0 + 1e-9
N_COMP = 6                               # |COMP[lambda]| (filasA_malla.tablas_estructurales)
N_D1 = 24                                # tipos de Delta_1
MULT_D2 = 72                             # sum de mult en los 48 tipos de Delta_2 (24 KSKS x 1 + 24 YtKS x 2)
XC2 = CT["abs_xc_mitad_inf"]             # |x_c|/2: el corte de A(x) es (-inf, -XC2]


def dist_seg(P, Q):
    """Distancia de 0 al segmento [P, Q] de C."""
    d = Q - P
    if abs(d) == 0:
        return abs(P)
    t = -(P.real * d.real + P.imag * d.imag) / (abs(d) ** 2)
    t = min(1.0, max(0.0, t))
    return abs(P + t * d)


def inv_sigma(x):
    """min_{lam in [0, Lambda]} |1 + x lam| (cota inferior)."""
    a, b = x.real, x.imag
    if a >= 0:
        return 1.0
    r2 = a * a + b * b
    l0 = -a / r2
    if l0 <= LAM:
        return abs(b) / math.sqrt(r2)
    return abs(1 + x * LAM)


def basicos(x, rad=0.0):
    """Cotas de peor caso en el disco D(x, rad).  Devuelve None si el disco toca el corte o un cero de U."""
    x = complex(x)
    X = abs(x) + rad
    Xl = abs(x) - rad
    Pm = U_MIN + x * (1 - U_MIN)
    Um = dist_seg(Pm, complex(1.0)) - rad * (1 - U_MIN)
    Up = max(abs(Pm) + rad * (1 - U_MIN), 1.0, X)          # U~ = max(U+, |z|, 1)
    isg = inv_sigma(x) - rad * LAM
    if Xl <= 0 or Um <= 0 or isg <= 0:
        return None
    Um *= 1 - 1e-12; Xl *= 1 - 1e-12; isg *= 1 - 1e-12
    s = 1.0 / (isg * U_MIN)
    a, n = A_HH, N1
    Uplus = max(abs(Pm) + rad * (1 - U_MIN), 1.0)
    alpha = math.sqrt((a + X * a * a * n * n * s) ** 2 + (a * n * s * Uplus) ** 2 + (X * a * n * s) ** 2
                      + (s * Uplus) ** 2)
    lam = max(1.0, Uplus / Xl)                               # |rho~| <= lam (H: 1; D, A: |U|/|z|)
    kH2 = I_NU2 * (1 + 2 * X * X / Um ** 2)
    kD2 = C_NU * M_MAX * (2 * X * X / Um ** 2 + X ** 4 / Um ** 4)
    k2 = max(kH2, kD2)
    kt2 = max(3 * I_NU2, 3 * (X / Um) ** 2 * C_NU * M_MAX)    # ||(K rho~)(a, .)||^2: el 1/x de rho~ se cancela
    PhiK = C_NU * max(1.0, X / Um, X * X / Um ** 2)
    PhiW = C_NU / Um ** 2
    PhiWpsi = C_NU * Up ** 4 / Um ** 2
    PhiL0 = 1.5 + math.sqrt(k2 * kt2) * alpha
    phiF = max(1.0, X * M_MAX / Um)
    PhiTh = 3 * PhiW * phiF + math.sqrt(k2 * kt2)
    iota = 1.0 + max(1.0 / Um, 1.0 / Xl)
    Phi = PhiL0 + PhiK + PhiWpsi + PhiTh + 1.0
    return dict(X=X, Xl=Xl, Um=Um, Up=Up, s=s, alpha=alpha, lam=lam, k2=k2, kt2=kt2, PhiK=PhiK, PhiW=PhiW,
                PhiWpsi=PhiWpsi, PhiL0=PhiL0, phiF=phiF, PhiTh=PhiTh, iota=iota, Phi=Phi)


def filas_cota(b):
    """Cotas fila a fila (continuo) en funcion de los ingredientes b (ver docstring y parte_05.tex)."""
    P, lam, phiF, X, Xl, io = b["Phi"], b["lam"], b["phiF"], b["X"], b["Xl"], b["iota"]
    PK, PW, PL0, PTh = b["PhiK"], b["PhiW"], b["PhiL0"], b["PhiTh"]
    Lt = 6.0 * lam                                           # int |rho~| sobre todas las lineas
    f = {}
    f["G_cof"] = 0.5 + 3 * P ** 2
    f["f2E"] = (16 ** 3 * P ** 3 + 3 * 16 * P * 16 * P ** 2 + 32 * P ** 3) / 6 + 1.5 * P * (256 * P ** 2 + 16 * P ** 2)
    f["f2z"] = (4.0 / Xl) * (64 * P ** 3 + 48 * P ** 3 + 8 * P ** 3) / 6
    f["2f2F"] = 2 * 4 * phiF * P ** 2
    f["f3F"] = 0.5 * 4 * phiF * ((12 * P) ** 2 + 12 * P ** 2 + N_COMP * io * P ** 2)
    f["f3c"] = 32 * P ** 2 + 8 * (P + 0.5) ** 2
    f["f4"] = 15 * P ** 2
    f["f5c"] = 18 * P ** 2
    f["f5F"] = 4 * phiF * 6 * P * 16 * P
    f["f7"] = 0.5 * (6 * P + 24 * phiF * P + 96 * P ** 2) ** 2
    f["C3cuad"] = 8 * P ** 4 * max(X, X ** 5)
    # f6 (f6_malla.f6_traza)
    mx = max(1.0, X / b["Um"])
    kap = C_NU * mx                                          # sup |rho~_w K(w, u)|: el 1/x de rho~ se cancela
    Zb = 6 * P * phiF + 24 * P ** 2                          # Z = Psi + G (om Psi), om Psi = P^T(beta w)
    Hm = 6 * P + 4 * Zb
    f["f6"] = 224 * P ** 2 * Hm + 192 * kap * P * Zb + 276 * Zb * mx * P
    # Q1 (codigo/q_c.py, primer termino)
    A1 = 96 * kap * P ** 2 + P                               # GPi om (-K o Et) + GPi om Pi
    GKl = P * (6 * kap + 1)                                  # GPi om (K + Pi)
    GKu = 6 * kap * P                                        # GPi om K
    EB = 0.5 + 4 * (P + 0.5) ** 2
    EBS = 2 * P ** 2 + 2 * P + 24 * P ** 2
    EC = A1 + GKu * 14 * P + 4 * GKl * (P + 0.5)
    f["Q1"] = 0.5 * 4 * phiF * 6 * (EB + EBS + EC)
    # Q2 (codigo/q_c.py, segundo termino)
    beta = 6 * P
    C0 = 16 * P ** 2 + 0.5 + A1 + 4 * ((P + 0.5) ** 2 + P * beta + GKl * (P + 0.5))
    A2 = 2 * P ** 2
    Pk = P + (P + 0.5) + beta + GKu + GKl
    T = C0 ** 2 + 4 * (2 * A2 * (2 * P + 0.5) * Pk + A2 ** 2) + PK ** 2 * (256 * P ** 2 + 8 * A2)
    f["Q2"] = 0.25 * Lt ** 2 * T
    # Delta_1 (rect/q1/d1_cont.py), Delta_2 (rect/demo/d2_c.py)
    f["D1"] = N_D1 * 0.5 * phiF * 2 * lam * P ** 3 * io
    f["D2"] = 0.25 * MULT_D2 * (2 * lam) ** 2 * PK ** 4 * io
    d = sum(f.values())
    # V (motor.Nivel.V)
    fib = 2 * PW ** 2 + 4 * (X / b["Um"]) * PW ** 2 * M_MAX ** 2
    V = 4 * PW ** 2 + 1.5 * 16 * PW * PL0 + 1.5 * 4 * PW * PTh + 2.25 * fib
    return f, d * SEG, V * SEG


def cota_dV(x, rad=0.0):
    b = basicos(x, rad)
    if b is None:
        return None
    f, d, V = filas_cota(b)
    return dict(b=b, filas=f, d=d, V=V)


def cota_k6(x, rad, rc, c0):
    """|k_6| en D(x, rad): |d| + |V| + |z| |V'| + |c0|, con |V'| <= sup_{D(x, rad + rc)} |V| / rc (Cauchy)."""
    a = cota_dV(x, rad)
    big = cota_dV(x, rad + rc)
    if a is None or big is None:
        return None
    Vp = big["V"] / rc
    return (a["d"] + a["V"] + (abs(x) + rad) * Vp + c0) * SEG


def recubrir(z):
    """Puntos de un contorno cerrado (array) -> radios de discos que lo cubren (mitad de la distancia al
    siguiente punto, con margen)."""
    dz = np.abs(np.diff(np.r_[z, z[:1]]))
    return np.maximum(dz, np.r_[dz[-1:], dz[:-1]]) * 0.5 * 1.001          # arco <= 1.001 cuerda


def f0_cota():
    """|F(0)| con F(0) = Fr(nu - 1) (filas_jet.torres_F en x = 0): b = ||B|| <= ||B||_HS, beta2 = sup_r ||B(r,.)||_2 =
    (sup_r int nu^2 - 1)^(1/2); |jd| <= b^2 beta2^2/(1-b^2); tr T^2 <= (b^2/(1-b^2))^2; |T| <= beta2^2 + |jd|;
    |U| <= b beta2^2/(1-b^2); |z| <= max(1 - c_nu, C_nu - 1); mix, cubT, bu, cubU por sup x HS^2."""
    b = NB
    beta2 = math.sqrt(I_NU2 - 1.0)
    jd = b * b * beta2 * beta2 / (1 - b * b)
    trT2 = (b * b / (1 - b * b)) ** 2
    Tm = beta2 ** 2 + jd
    Um_ = b * beta2 ** 2 / (1 - b * b)
    zm = max(1 - CT["nu"][0], C_NU - 1)
    mix = jd ** 2 * (zm + Um_ + Tm)
    cubT = Tm * trT2
    bu = zm * trT2 * b * b
    cubU = Um_ * trT2 * b * b
    F0 = 0.5 * jd ** 2 + trT2 + 1.5 * jd + 1.5 * jd ** 2 + mix + (2 / 3) * cubT + 2 * bu + (2 / 3) * cubU
    return F0 * 1.01


def c0_cota_principio_maximo(R=0.09, npt=400):
    """|F(0) - 1/12| = |d(0) + V(0)| <= max_{|x| = R} (|d| + |V|) (maximo de la funcion analitica d + V)."""
    z = R * np.exp(2j * np.pi * np.arange(npt) / npt)
    rr = recubrir(z)
    m = 0.0
    for zz, r in zip(z, rr):
        a = cota_dV(zz, r)
        assert a is not None
        m = max(m, a["d"] + a["V"])
    return m * SEG


def elipse(a, b, rho, npt):
    th = 2 * np.pi * np.arange(npt) / npt
    w = rho * np.exp(1j * th)
    return 0.5 * (a + b) + 0.25 * (b - a) * (w + 1 / w)


def sup_contorno(z, rc, c0, dividir_x2=True):
    """sup de |k_6| (o |k_6/x^2|) en un contorno dado por puntos z, cubierto por discos."""
    rr = recubrir(z)
    m = 0.0
    arg = None
    for zz, r in zip(z, rr):
        v = cota_k6(zz, r, rc, c0)
        if v is None:
            return math.inf, zz
        if dividir_x2:
            v = v / (abs(zz) - r) ** 2
        if v > m:
            m, arg = v, zz
    return m * SEG, arg


def perfil_contorno(z, rc, c0, dividir_x2=True):
    """Cotas por disco en los puntos z (equiespaciados en el parametro): array; inf si un disco toca el corte."""
    rr = recubrir(z)
    v = np.empty(len(z))
    for i, (zz, r) in enumerate(zip(z, rr)):
        c = cota_k6(zz, r, rc, c0)
        if c is None:
            v[i] = math.inf
            continue
        v[i] = c / (abs(zz) - r) ** 2 if dividir_x2 else c
    return v * SEG


def rho_max(a, b, corte=None):
    """Mayor rho tal que la elipse de [a, b] no toca (-inf, corte]."""
    corte = -XC2 if corte is None else corte
    c, h = 0.5 * (a + b), 0.5 * (b - a)
    t = (c - corte) / h
    return t + math.sqrt(t * t - 1)


if __name__ == "__main__":
    out = {"constantes": {"u_min_inf": U_MIN, "m_max_sup": M_MAX, "Lambda_sup": LAM, "C_nu": C_NU, "I_nu2": I_NU2,
                          "normB_sup": NB, "a": A_HH, "n": N1, "abs_xc_mitad_inf": XC2}}
    F0 = f0_cota()
    c0 = F0 + 1.0 / 12
    out["F0_cota"] = F0
    out["c0_cota"] = c0
    print("|F(0)| <=", f"{F0:.3e}", " |c0| = |F(0) - 1/12| <=", f"{c0:.4f}")
    # rho maximos admisibles
    out["rho_max"] = {"[0.06,1]": rho_max(0.06, 1.0), "[0,1]": rho_max(0.0, 1.0)}
    print(out["rho_max"])
    # tabla en puntos sueltos
    tab = {}
    for x in (-0.05, -0.08, -0.09, -0.095, -0.1, 0.09j, 0.3 + 0.3j, 0.5, 1.0, 1.1):
        a = cota_dV(x, 0.0)
        tab[str(x)] = {"Phi": a["b"]["Phi"], "alpha": a["b"]["alpha"], "s": a["b"]["s"], "Um": a["b"]["Um"],
                       "d": a["d"], "V": a["V"], "filas_mayores": sorted(a["filas"].items(), key=lambda t: -t[1])[:4]}
        print(x, f"Phi={a['b']['Phi']:.3e} alpha={a['b']['alpha']:.3e} d<={a['d']:.3e} V<={a['V']:.3e}",
              [(k, f"{v:.1e}") for k, v in sorted(a['filas'].items(), key=lambda t: -t[1])[:3]])
    out["puntos"] = tab
    # contornos
    con = {}
    for (a_, b_, rho) in ((0.06, 1.0, 1.8), (0.06, 1.0, 2.0), (0.06, 1.0, 2.1), (0.06, 1.0, 2.15), (0.06, 1.0, 2.2),
                          (0.06, 1.0, 2.24), (0.0, 1.0, 1.6), (0.0, 1.0, 1.8), (0.0, 1.0, 1.85), (0.0, 1.0, 1.88)):
        z = elipse(a_, b_, rho, 2000)
        rc = 0.25 * min(np.min(np.abs(z + XC2)), 0.05)
        v = perfil_contorno(z, rc, c0)
        i = int(np.argmax(v))
        con[f"elipse[{a_},{b_}] rho={rho}"] = {"sup_h6": float(v.max()), "media_h6": float(v.mean()),
                                              "donde": [z[i].real, z[i].imag], "rc": rc}
        print(f"elipse [{a_},{b_}] rho={rho}: sup|k6/x^2| <= {v.max():.3e} (media en theta {v.mean():.3e}) en {z[i]:.3f}")
    for R in (0.06, 0.07, 0.08, 0.09, 0.095, 0.1):
        z = R * np.exp(2j * np.pi * np.arange(2000) / 2000)
        rc = 0.25 * min(XC2 - R, 0.05)
        m, arg = sup_contorno(z, rc, c0, dividir_x2=False)
        con[f"circulo R={R}"] = {"sup_k6": m, "sup_h6": m / R ** 2, "donde": [arg.real, arg.imag], "rc": rc}
        print(f"circulo R={R}: sup|k6| <= {m:.3e}, sup|h6| <= {m / R ** 2:.3e}")
    out["contornos"] = con
    json.dump(out, open(os.path.join(AQUI, "cota_gruesa.json"), "w"), indent=1, default=str)
