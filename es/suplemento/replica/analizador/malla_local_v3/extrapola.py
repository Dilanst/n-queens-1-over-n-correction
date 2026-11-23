"""extrapola.py -- secuencias de mallas y extrapolacion en m de cada fila de k (tecnica B16).  Evidencia numerica [N].

Las secuencias y los ajustes son los que recomienda el INFORME.md de cada carpeta de B/rect:
  A, C3  (filas A y C3cuad, rect/motor):  m = 24, 48, 96, 192 (clase 3*2^k: f3F y f2E dependen de m mod 3);
          Richardson con potencias 2, 4, 6, 8; error = |R_k - R_(k-1)| de la ultima fila.
  V      (V y V', rect/motor):            m = 24 ... 384 (3*2^k), mismo Richardson.
  f6     (rect/f6):                        secuencias 32-64-128-256-512 y 24-48-96-192-384, R4 de cada una;
          valor = media de las secuencias; error = maxima diferencia entre secuencias + max |R4 - R3|.
  Q1, D1 (rect/q1):                        m multiplo de 24; ajuste (0, 2, 4) en m >= 48; error = dispersion
          entre (0,2,4), (0,2,3,4), (0,2,4) sin la malla menor y sin la mayor, y el residuo maximo.
  Q2     (rect/q2):                        m multiplo de 12 (24...144; 24...180 si x real y |x| < 0.035;
          24...132 si x complejo, por memoria).  [N] (B/rect/local, x = 0.5475): Q2(m) tiene dos ramas,
          m = 0 y m = 12 (mod 24), cada una limpia en (2, 4, 6) (residuos 2e-9 y 6e-10) y con el mismo limite a
          4e-8, pero con distinto coeficiente de m^-4 (8.9 y 9.5); mezcladas, el rango de ajustes del INFORME
          es ~1e-7.  Aqui: ajuste (2, 4, 6) en cada rama (desde m = 24); valor = media de las ramas; error =
          |diferencia entre ramas| + residuo maximo.  En info va tambien la receta del INFORME (mediana de
          (2,4), (2,4,6), (2,3) en m >= 36).
  D2     (rect/q2):                        m multiplo de 6; receta del INFORME para x = 0.5475: ajustes
          (2,4), (2,4,6) y (2,4,6,8) desde m = 36; valor = media de (2,4) y (2,4,6); error = max(|diferencia|,
          |(2,4,6,8) - media|, residuo maximo).  Con pocas mallas, la de los nodos: desde m = 18 y el criterio
          (2,3)/3.
  F      (rect/afinado/F_malla):           secuencias 48...768 y 64...1024, Richardson (2,4,6,8); valor = secuencia 3*2^k;
          error = max(|R4 - R3|, diferencia entre secuencias).
  J      (rect/afinado/J_malla):           mallas pares; no se extrapola por punto: analiza_local.py junta las mallas
          de la nube (m = 6...26) y las del PC y aplica los estimadores de J_analiza.py (clases m mod 6 y modelos C, D
          con m mod 3).
Con x complejo los mismos ajustes valen para la parte real y la imaginaria a la vez (el error es el modulo).
En el jet (x = 1e-20 i) analiza_local.py extrapola por separado el valor (parte real) y la pendiente (parte
imaginaria / 1e-20).
Las secuencias altas (confirmaciones) anaden mallas mayores a las mismas sucesiones.
"""
import numpy as np

FILAS = ("A", "C3", "V", "f6", "Q1", "D1", "Q2", "D2")      # las que pide k (con F)
FILAS_TODAS = FILAS + ("F", "J")
COMP_A = ["G_cof", "f2E", "f2z", "f2F", "f3F", "f3c", "f4_expl", "f4_L0", "f5c", "f5F", "f7", "f3var", "f3cov"]
PESO_A = {k: (2.0 if k == "f2F" else 1.0) for k in COMP_A[:11]}   # d_A: f2F cuenta en f2 y como C3par
CLAVES = {"A": COMP_A + ["dA_suma"], "C3": ["C3cuad"], "V": ["V", "Vp"], "f6": ["f6"], "Q1": ["Q1"],
          "D1": ["D1"], "Q2": ["Q2"], "D2": ["D2"], "F": ["F", "Fp"], "J": ["J", "menos_B2", "L2"]}
F6_SECUENCIAS = ([32, 64, 128, 256, 512], [24, 48, 96, 192, 384])
F6_SECUENCIA_ALTA = [40, 80, 160, 320, 640]

# secuencias por defecto (config.json puede cambiarlas en "secuencias")
SECUENCIAS = {
    "A": {"base": [24, 48, 96, 192], "alta": [384]},
    "C3": {"base": [24, 48, 96, 192], "alta": [384]},
    "V": {"base": [24, 48, 96, 192, 384], "alta": [768]},
    "f6": {"base": sorted(set(F6_SECUENCIAS[0] + F6_SECUENCIAS[1])), "alta": F6_SECUENCIA_ALTA},
    "Q1": {"base_cerca": [24, 48, 72, 96, 120, 144, 192, 240, 288], "base_medio": [24, 48, 72, 96, 120, 144, 192],
           "base_lejos": [24, 48, 72, 96, 120, 144], "alta": [336, 384, 432, 480, 528, 576]},
    "D1": {"base_cerca": [24, 48, 72, 96, 120, 144, 192, 240, 288], "base_medio": [24, 48, 72, 96, 120, 144, 192],
           "base_lejos": [24, 48, 72, 96, 120, 144], "alta": [336, 384, 432, 480, 528, 576]},
    "Q2": {"base": list(range(24, 145, 12)), "base_cerca": list(range(24, 181, 12)),
           "base_complejo": list(range(24, 133, 12)), "alta": [156, 168, 180, 192]},
    "D2": {"base": list(range(18, 73, 6)), "alta": [84, 96, 108, 120, 132, 144]},
    "F": {"base": [48, 64, 96, 128, 192, 256, 384, 512, 768, 1024], "alta": []},
    "J": {"base": list(range(28, 53, 2)), "alta": []},
}
X_CERCA, X_MEDIO = 0.035, 0.3        # Q1, D1: m hasta 288 si |x| < 0.035, hasta 192 si |x| < 0.3, si no hasta 144


def secuencia(fila, x, alta=False, secuencias=None):
    """Lista de m de la fila en el nivel x (|x| decide la secuencia de Q1 y D1)."""
    c = (secuencias or SECUENCIAS)[fila]
    if fila in ("Q1", "D1"):
        ax = abs(x)
        base = c["base_cerca"] if (ax < X_CERCA or alta) else (c["base_medio"] if ax < X_MEDIO else c["base_lejos"])
    elif (isinstance(x, complex) or x < 0) and "base_complejo" in c:   # x < 0: se calcula con x complejo
        base = c["base_complejo"]           # Q2 con x complejo: la memoria crece como m^3 (m = 132: ~1.9 GB)
    elif abs(x) < X_CERCA and "base_cerca" in c:
        base = c["base_cerca"]              # Q2 real cerca de 0 (pesa w/x^2): m hasta 180
    else:
        base = c["base"]
    return sorted(set(base + (c["alta"] if alta else [])))


# ------------------------------------------------------------------------------------------- ajustes
def _num(v):
    return complex(v) if isinstance(v, complex) or np.iscomplexobj(v) else float(v)


def richardson(ms, vals, pot=(2, 4, 6, 8)):
    """v(m) = v + sum_p c_p m^-p con ajustes exactos en puntos consecutivos (motor.richardson).
    Devuelve (valor, error = |T[-1][-1] - T[-1][-2]|)."""
    ms = np.asarray(ms, float)
    vals = np.asarray(vals)
    n = len(ms)
    fila = [vals[-1]]
    k = n - 1
    for j in range(1, min(k, len(pot)) + 1):
        sl = slice(k - j, k + 1)
        Mx = np.ones((j + 1, j + 1), dtype=complex if np.iscomplexobj(vals) else float)
        for c, p in enumerate(pot[:j]):
            Mx[:, c + 1] = ms[sl] ** (-float(p))
        fila.append(np.linalg.solve(Mx, vals[sl])[0])
    if len(fila) == 1:
        return _num(fila[0]), float("nan")
    return _num(fila[-1]), float(abs(fila[-1] - fila[-2]))


def _rich_f6(vals):
    T = [list(vals)]
    for fac in (4, 16, 64, 256):
        p = T[-1]
        if len(p) < 2:
            break
        T.append([(fac * p[i + 1] - p[i]) / (fac - 1) for i in range(len(p) - 1)])
    return T


def ajuste(d, ms, pots, constante=True):
    """Minimos cuadrados v(m) = c0 + sum c_p m^-p (pots sin el 0 si constante=True).  Devuelve (c, residuos)."""
    cols = ([0] if constante else []) + list(pots)
    m0 = float(min(ms))                                  # columnas (m/m0)^-p: bien escaladas (m^-8 incluido)
    A = np.array([[(float(m) / m0) ** (-p) for p in cols] for m in ms], float)
    y = np.array([d[m] for m in ms])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ c
    return c * np.array([m0 ** p for p in cols]), r


def ext_rich(d, clase=None):
    ms = sorted(m for m in d if (clase is None or clase(m)))
    v, e = richardson(ms, [d[m] for m in ms])
    return v, e, {"ms": ms}


def ext_f6(d):
    cads = [c for c in (F6_SECUENCIAS[0], F6_SECUENCIAS[1], F6_SECUENCIA_ALTA) if all(m in d for m in c)]
    if not cads:                                       # respaldo: Richardson sobre lo que haya
        return ext_rich(d)
    r4, r3 = [], []
    for c in cads:
        T = _rich_f6([d[m] for m in c])
        r4.append(T[4][0])
        r3.append(T[3][-1])
    est = sum(r4) / len(r4)
    dif = max([abs(a - b) for a in r4 for b in r4] + [0.0])
    err = dif + max(abs(a - b) for a, b in zip(r4, r3))
    return _num(est), float(err), {"secuencias": cads, "R4": [_num(v) for v in r4]}


def ext_q1(d):
    ms = sorted(m for m in d if m % 24 == 0 and m >= 48)
    if len(ms) < 4:
        ms = sorted(m for m in d if m % 24 == 0)
    if len(ms) < 3:
        return ext_rich(d)
    c0, r0 = ajuste(d, ms, (2, 4))
    alt = []
    if len(ms) >= 5:
        alt.append(ajuste(d, ms, (2, 3, 4))[0][0])
        alt.append(ajuste(d, ms[1:], (2, 4))[0][0])
        alt.append(ajuste(d, ms[:-1], (2, 4))[0][0])
    err = max([abs(a - c0[0]) for a in alt] + [float(np.max(np.abs(r0)))])
    return _num(c0[0]), float(err), {"ms": ms, "coef_m2": _num(c0[1]), "coef_m4": _num(c0[2])}


def q2_informe(d):
    """Receta de rect/q2 (nodos): mediana de los ajustes (2,4), (2,4,6), (2,3) en m >= 36; error = rango."""
    ms = sorted(m for m in d if m % 12 == 0 and m >= 36)
    vals = [ajuste(d, ms, p)[0][0] for p in ((2, 4), (2, 4, 6), (2, 3))]
    orden = sorted(range(3), key=lambda i: np.real(vals[i]))
    return vals[orden[1]], max(abs(a - b) for a in vals for b in vals), vals


def ext_q2(d):
    ms = sorted(m for m in d if m % 12 == 0 and m >= 24)
    ramas = [[m for m in ms if m % 24 == 0], [m for m in ms if m % 24 == 12]]
    if min(len(r) for r in ramas) >= 5:                  # ajuste (2, 4, 6) por rama (m mod 24)
        vr, res = [], []
        for r in ramas:
            c, rr = ajuste(d, r, (2, 4, 6))
            vr.append(c[0])
            res.append(float(np.max(np.abs(rr))))
        v = 0.5 * (vr[0] + vr[1])
        err = abs(vr[0] - vr[1]) + max(res)
        vi, ei, _ = q2_informe(d)
        return _num(v), float(err), {"ms": ms, "ramas_mod24": [_num(a) for a in vr], "residuos": res,
                                     "receta_informe": [_num(vi), float(ei)]}
    if len([m for m in ms if m >= 36]) >= 5:
        vi, ei, vals = q2_informe(d)
        return _num(vi), float(ei), {"ms": ms, "ajustes": [_num(a) for a in vals]}
    return ext_rich(d)


def ext_d2(d):
    ms36 = sorted(m for m in d if m % 6 == 0 and m >= 36)
    if len(ms36) >= 6:                                   # receta de x = 0.5475 del INFORME de rect/q2
        c24, _ = ajuste(d, ms36, (2, 4))
        c246, r246 = ajuste(d, ms36, (2, 4, 6))
        c2468, _ = ajuste(d, ms36, (2, 4, 6, 8))
        v = 0.5 * (c24[0] + c246[0])
        err = max(abs(c24[0] - c246[0]), abs(c2468[0] - v), float(np.max(np.abs(r246))))
        return _num(v), float(err), {"ms": ms36, "ajustes": [_num(c24[0]), _num(c246[0]), _num(c2468[0])]}
    ms = sorted(m for m in d if m % 6 == 0 and m >= 18)  # receta de los nodos (m = 18...48)
    if len(ms) < 5:
        return ext_rich(d)
    a24 = ajuste(d, ms, (2, 4))[0][0]
    a246 = ajuste(d, ms, (2, 4, 6))[0][0]
    a23 = ajuste(d, ms, (2, 3))[0][0]
    v = 0.5 * (a24 + a246)
    err = max(abs(a24 - a246), abs(a23 - v) / 3)
    return _num(v), float(err), {"ms": ms, "ajustes": [_num(a24), _num(a246), _num(a23)]}


def es_3x2k(m):
    q = m // 3
    return m % 3 == 0 and q > 0 and (q & (q - 1)) == 0


def ext_F(d):
    c1, c2 = [48, 96, 192, 384, 768], [64, 128, 256, 512, 1024]
    if not all(m in d for m in c1):
        return ext_rich(d)
    v, err = richardson(c1, [d[m] for m in c1])      # = F_malla.main: |R4 - R3| sobre las mallas mas finas
    info = {"secuencia_3x2k": _num(v)}
    if all(m in d for m in c2):
        v2 = richardson(c2, [d[m] for m in c2])[0]
        err = max(err, abs(v - v2))
        info["secuencia_2k"] = _num(v2)
    return _num(v), float(err), info


def ext_J(d):
    """Por punto solo se devuelve la malla mayor (la extrapolacion de J va en analiza_local.estima_J)."""
    m = max(d)
    return _num(d[m]), float("nan"), {"m": m}


METODO = {"A": lambda d: ext_rich(d, es_3x2k), "C3": lambda d: ext_rich(d, es_3x2k),
          "V": lambda d: ext_rich(d, es_3x2k), "f6": ext_f6, "Q1": ext_q1, "D1": ext_q1, "Q2": ext_q2, "D2": ext_d2,
          "F": ext_F, "J": ext_J}


def extrapolar(fila, crudos, ms=None):
    """crudos: {m: {clave: valor}} de una fila en un nivel x.  ms: subconjunto de mallas (None = todas).
    Devuelve {clave: {"valor", "error", "info"}} para cada clave de la fila presente en todas las mallas."""
    usa = sorted(m for m in crudos if (ms is None or m in ms))
    out = {}
    if not usa:
        return out
    claves = [k for k in CLAVES[fila] if all(k in crudos[m] for m in usa)]
    for k in claves:
        d = {m: crudos[m][k] for m in usa}
        v, e, info = METODO[fila](d)
        out[k] = {"valor": v, "error": e, "info": info}
    return out
