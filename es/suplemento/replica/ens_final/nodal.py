"""nodal.py -- valores de las filas de k en los puntos del PC (GL24, GLb, circulo, confirma) y en los 16 nodos de GL16
de la nube, con dos recetas de extrapolacion en m.  [N]
  'pc'    : la de extrapola.py (secuencia base); reproduce analiza_local.py.
  'mejor' : igual salvo
     Q1, D1 con secuencia hasta m >= 192 (|x| < 0.3): media de los ajustes (2,4,6,8) m >= 48 y (2,4,6) m >= 72; error
            max(|diferencia|, |(2,4,6) m>=48 - (2,4) m>=96| / 2, 1.5e-13 |valor|) (suelo calibrado en r3b/r3c: con
            m <= 144...288 estas recetas aciertan a <= 1.6e-10 en los nodos 1 y 2 de GL16, y la del PC, (2,4) m >= 48,
            se desvia +1.7e-9...+5.9e-9);  con m <= 144 (|x| >= 0.3), la del PC.
     D2: (2,4,6) en m >= 36 (mallas 18...72); error max(|frente a (2,4,6) m >= 24|, |frente a (2,4,6,8) m >= 24|,
            residuo); la del PC (media de (2,4) y (2,4,6)) se desvia +2e-11 y +9e-11 en los nodos 1 y 2.
  'alta'  : confirmaciones (todas las mallas): referencias de r3b_calibra.referencia.
k = dA_suma + C3cuad + f6 + Q1 + D1 + Q2 + D2 + V + F - 1/12 - x (V' + F')."""
import json
import math
import os
import sys

import numpy as np

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
SP = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(AQUI, "pc_codigo"))
import extrapola as EX  # noqa: E402

PARTES = (("A", "dA_suma"), ("C3", "C3cuad"), ("f6", "f6"), ("Q1", "Q1"), ("D1", "D1"), ("Q2", "Q2"), ("D2", "D2"))
CTE = {"F1": 0.0, "S": 15.6334582804, "S_err": 2e-12, "P_T": 0.4452313836, "P_T_err": 3e-11}
_PTS = None


def cargar():
    """{(grupo, etiqueta): {"x": x, "filas": {fila: {m: {clave: valor}}}}} desde el JSON unido del PC."""
    global _PTS
    if _PTS is None:
        d = json.load(open(os.path.join(SP, "pc_resultados", "malla_local_20261122T070515.json"), encoding="utf-8"))
        pts = {}
        for key in sorted(d):
            r = d[key]
            x = complex(*r["x"]) if r["x"][1] != 0 else float(r["x"][0])
            p = pts.setdefault((r["grupo"], r["etiqueta"]), {"x": x, "filas": {}})
            for m, e in r["mallas"].items():
                p["filas"].setdefault(r["fila"], {})[int(m)] = {
                    k: (complex(v[0], v[1]) if isinstance(v, list) else float(v)) for k, v in e["valores"].items()}
        _PTS = pts
    return _PTS


def fit(ms, d, pots):
    """Minimos cuadrados v(m) = v + sum c_p m^-p.  Devuelve (v, residuo maximo)."""
    m0 = float(min(ms))
    A = np.array([[1.0] + [(m / m0) ** -p for p in pots] for m in ms])
    y = np.array([d[m] for m in ms])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    return c[0], (float(np.max(np.abs(y - A @ c))) if len(ms) > A.shape[1] else 0.0)


VARIANTE = {}       # sensibilidad (r6): {"Q1": "v1".."v4", "D2": "v1".."v3", "Q2": "v1".."v4"}; vacio = receta 'mejor'


def ext_q1_mejor(d):
    ms = sorted(m for m in d if m % 24 == 0)
    if max(ms) < 192:
        v, e, _ = EX.ext_q1(d)
        return v, e, "pc"
    a = fit([m for m in ms if m >= 48], d, (2, 4, 6, 8))[0]
    b = fit([m for m in ms if m >= 72], d, (2, 4, 6))[0]
    c = fit([m for m in ms if m >= 48], d, (2, 4, 6))[0]
    dd = fit([m for m in ms if m >= 96], d, (2, 4))[0]
    v = 0.5 * (a + b)
    e = max(abs(a - b), abs(c - dd) / 2, 1.5e-13 * abs(v))
    v = {"v1": a, "v2": b, "v3": c, "v4": dd}.get(VARIANTE.get("Q1"), v)
    return v, float(e), "(2,4,6,8)m>=48 + (2,4,6)m>=72"


def ext_d2_mejor(d):
    ms = sorted(m for m in d if m % 6 == 0)
    w36 = [m for m in ms if m >= 36]
    if len(w36) < 6:
        v, e, _ = EX.ext_d2(d)
        return v, e, "pc"
    v, r = fit(w36, d, (2, 4, 6))
    a = fit([m for m in ms if m >= 24], d, (2, 4, 6))[0]
    b = fit([m for m in ms if m >= 24], d, (2, 4, 6, 8))[0]
    e = float(max(abs(v - a), abs(v - b), r))
    if VARIANTE.get("D2") == "v3":
        v = EX.ext_d2(d)[0]
    v = {"v1": a, "v2": b}.get(VARIANTE.get("D2"), v)
    return v, e, "(2,4,6)m>=36"


def ext_q2_variante(d, var):
    """Variantes de Q2 para la sensibilidad: v1 (2,4,6) con todas las m >= 48; v2 rama m = 0 (mod 24); v3 rama 12;
    v4 receta del INFORME (mediana de (2,4), (2,4,6), (2,3) en m >= 36)."""
    ms = sorted(m for m in d if m % 12 == 0)
    if var == "v1":
        return fit([m for m in ms if m >= 48], d, (2, 4, 6))[0]
    if var in ("v2", "v3"):
        r = 0 if var == "v2" else 12
        return fit([m for m in ms if m >= 24 and m % 24 == r], d, (2, 4, 6))[0]
    return EX.q2_informe(d)[0]


def filas(p, receta="mejor"):
    """{fila: {clave: (valor, error)}} con la secuencia base del punto (receta 'pc' o 'mejor')."""
    out = {}
    for fila, cr in p["filas"].items():
        if fila == "J":
            continue
        base = sorted(EX.secuencia(fila, p["x"], False))
        if not all(m in cr for m in base):
            continue
        res = {k: (v["valor"], v["error"]) for k, v in EX.extrapolar(fila, cr, base).items()}
        if receta == "mejor" and fila in ("Q1", "D1", "D2"):
            dd = {m: cr[m][fila] for m in base}
            v, e, _ = (ext_q1_mejor if fila != "D2" else ext_d2_mejor)(dd)
            res[fila] = (v, e)
        if receta == "mejor" and fila == "Q2" and VARIANTE.get("Q2"):
            dd = {m: cr[m]["Q2"] for m in base}
            res["Q2"] = (ext_q2_variante(dd, VARIANTE["Q2"]), res["Q2"][1])
        out[fila] = res
    return out


def k_de(x, e):
    """(k, error de k, error de d, d, G, G') en x real con las filas e."""
    d = sum(e[f][k][0] for f, k in PARTES)
    ed = math.sqrt(sum(abs(e[f][k][1]) ** 2 for f, k in PARTES))
    V, eV = e["V"]["V"]
    Vp, eVp = e["V"]["Vp"]
    F, eF = e["F"]["F"]
    Fp, eFp = e["F"]["Fp"]
    G, Gp = V + F - 1.0 / 12, Vp + Fp
    eG = math.sqrt(eV ** 2 + eF ** 2 + (x * eVp) ** 2 + (x * eFp) ** 2)
    k = d + G - x * Gp
    return float(np.real(k)), math.sqrt(ed ** 2 + eG ** 2), ed, d, G, Gp


def nodos_gl(n, a=0.0, b=1.0):
    xg, wg = np.polynomial.legendre.leggauss(n)
    return a + (b - a) * 0.5 * (xg + 1), (b - a) * 0.5 * wg


def grupo_gl(nombre, n, a=0.0, b=1.0, receta="mejor"):
    """k, errores y filas en los n nodos de un grupo GL del PC."""
    pts = cargar()
    X, W = nodos_gl(n, a, b)
    out = []
    for i in range(n):
        p = pts[(nombre, f"n{i + 1:02d}")]
        assert abs(p["x"] - X[i]) < 1e-13
        e = filas(p, receta)
        k, ek, ed, d, G, Gp = k_de(float(X[i]), e)
        out.append({"x": float(X[i]), "w": float(W[i]), "k": k, "ek": ek, "ed": ed, "filas": e})
    return X, W, out


# ------------------------------------------------------------------------------------------------ circulo
def circulo(receta="mejor", r=0.06, M=32):
    """Coeficientes de Taylor k_n (n = 0..M-1) por la regla del trapecio en x_j = r e^(2 pi i j / M), j = 0..M/2
    (simetria conjugada), y los errores maximos de d y de G en los puntos."""
    pts = cargar()
    ext = [filas(pts[("circulo", f"j{j:02d}")], receta) for j in range(M // 2 + 1)]

    def serie(vals):
        f = np.zeros(M, complex)
        for j in range(M // 2 + 1):
            f[j] = vals[j]
            if 0 < j < M // 2:
                f[M - j] = np.conj(vals[j])
        return np.fft.fft(f) / M / r ** np.arange(M)

    d_n = sum(serie([complex(ext[j][f][k][0]) for j in range(M // 2 + 1)]) for f, k in PARTES)
    g_n = serie([complex(ext[j]["V"]["V"][0]) + complex(ext[j]["F"]["F"][0]) for j in range(M // 2 + 1)])
    g_n[0] -= 1.0 / 12
    n = np.arange(M)
    k_n = d_n + (1 - n) * g_n
    ed = [math.sqrt(sum(abs(ext[j][f][k][1]) ** 2 for f, k in PARTES)) for j in range(M // 2 + 1)]
    eG = [math.hypot(abs(ext[j]["V"]["V"][1]), abs(ext[j]["F"]["F"][1])) for j in range(M // 2 + 1)]
    por_fila = {f"{f}:{k}": max(abs(ext[j][f][k][1]) for j in range(M // 2 + 1)) for f, k in PARTES}
    coef_filas = {f"{f}:{k}": serie([complex(ext[j][f][k][0]) for j in range(M // 2 + 1)]) for f, k in PARTES}
    return {"r": r, "M": M, "k_n": k_n, "d_n": d_n, "g_n": g_n, "ed_max": max(ed), "eG_max": max(eG),
            "ed_puntos": ed, "error_max_por_fila": por_fila, "coef_filas": coef_filas}


def taylor_integral(cir, b=None, N=None):
    """int_0^b k/x^2 dx = sum_{n=2}^{N} k_n b^(n-1)/(n-1) con k_0 = k_1 = 0 [D].  Cota del error por los datos del
    circulo (Cauchy-Schwarz + Parseval, b = r): (1/r) [ (sum 1/(n-1)^2)^(1/2) ed + (N-1)^(1/2) eG ]."""
    r, M = cir["r"], cir["M"]
    b = r if b is None else b
    N = M - 1 if N is None else N
    nn = np.arange(2, N + 1)
    terms = cir["k_n"][2:N + 1].real * b ** (nn - 1) / (nn - 1)
    I = float(np.sum(terms))
    q = b / r
    cs = math.sqrt(float(np.sum(q ** (2 * nn - 2) / (nn - 1) ** 2)))
    cota = (cs * cir["ed_max"] + math.sqrt(float(np.sum(q ** (2 * nn - 2)))) * cir["eG_max"]) / r
    return I, cota, terms
