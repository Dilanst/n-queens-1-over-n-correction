"""analiza_v3.py -- c y su presupuesto con las tareas de malla_local_v3 junto con la tanda anterior del PC.  [N]

Junta las tareas nuevas (resultados/tareas del paquete v3, o un JSON unido malla_local_*.json) con las de la tanda
anterior (pc_resultados/malla_local_20261122T070515.json) y recalcula c con las recetas de ens_final (nodal.py; las
formulas de r4_c.py, r6_presupuesto.py y r8_final.py van copiadas aqui, porque esos guiones escriben en ens_final al
importarlos).  c = F(1) - 1/12 + int_0^1 k/x^2 dx + P0 - S, F(1) = 0 [D], P0 de ens_final/r2_J.json.

Recetas por punto ('mejor' = la de ens_final; 'v3' = 'mejor' + las mallas nuevas):
  Q1, D1  con m = 192, 240 nuevas (x > 0.3): media de (2,4,6,8) m >= 48 y (2,4,6) m >= 72 (nodal.ext_q1_mejor) con
          todas las m multiplo de 24; en x = 0.5475 (m <= 240) acierta a 4e-10 con error declarado 4.9e-10.
  Q2      con mallas nuevas: (2,4,6) en cada rama m = 0 y m = 12 (mod 24) desde m = 72 (desde 48 si una rama no
          tiene 5 mallas desde 72); valor = media de las ramas; error = max(|diferencia de ramas|, |diferencia con la
          media desde el corte siguiente (96, o 48 / 24)|) + residuo maximo.  Sin mallas nuevas, la de ens_final.
  A       con m = 384: Richardson en 3*2^k con m = 24...384 (receta del PC); error = max(8 x el de Richardson,
          |R(<=384) - R(<=192)| x q), q = |R(<=384) - R(<=192)| / |R(<=192) - R(<=96)| (convergencia observada, <= 1).
          El factor 8 es la infraestimacion medida en x = 0.5475 con m <= 192 (ens_final §3.4).
Metodos: (control) Taylor (r = 0.06, n = 2...31) + GL20 solo con la tanda anterior: debe dar el c de ens_final;
  (antiguo) lo mismo con las mallas nuevas; (nuevo, punto 5) serie del circulo r = 0.03 en [0, 0.03] + GL6 en
  [0.03, 0.06] + GL20 en [0.06, 1]; controles cruzados con la serie de r = 0.06 en [0.03, 0.06] y en [0, 0.03].
Presupuesto (como ens_final §3.4): datos de la serie (cota de Cauchy-Schwarz y Parseval), error nodal de cada panel
de Gauss en suma lineal, A en x > 0.3 (x 8 si no hay m = 384), P0, cuadratura y truncacion; total cuadratico.
Muestras del punto 5 (fila k6): Richardson (24, 36, 48) en 1/m^2 y delta_j como balance.py; se exportan en el formato
de p5_bernstein/muestras_k6.py; en la nube, cotas de los Teoremas 4.3 (GL6) y 4.4 (serie) con refinamiento.py y
taylor_cotas.py de p5_bernstein ([D] si las muestras estan a delta_j de los valores verdaderos [C]).

Uso (nube):    python3 -B analiza_v3.py [tareas_v3 ...] [--salida DIR]   (tareas: carpeta de *.json o JSON unido)
Uso (paquete): python analiza_v3.py [carpeta]   (por defecto resultados/tareas; lo llaman lanzador.py y ANALIZAR.bat)
Sin tareas nuevas solo hace el control frente a ens_final.  Evidencia numerica, no prueba."""
import glob
import json
import math
import os
import sys
import time

sys.dont_write_bytecode = True
import numpy as np  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
EN_PAQUETE = os.path.exists(os.path.join(AQUI, "v", "ens_final", "nodal.py"))
if EN_PAQUETE:
    E_DIR = os.path.join(AQUI, "v", "ens_final")
    PR_JSON = os.path.join(AQUI, "datos", "malla_local_20261122T070515.json")
    PAQ, P5_DIR = AQUI, None
    SALIDA = os.path.join(AQUI, "resultados")
else:
    _S = os.path.dirname(AQUI)
    E_DIR = os.path.join(_S, "ens_final")
    PR_JSON = os.path.join(_S, "pc_resultados", "malla_local_20261122T070515.json")
    PAQ, P5_DIR = os.path.join(AQUI, "malla_local_v3"), os.path.join(_S, "p5_bernstein")
    SALIDA = os.path.join(AQUI, "analisis_v3")
for _p in (E_DIR, PAQ):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import extrapola as EX  # noqa: E402  (el del paquete; mismo SHA256 que ens_final/pc_codigo/extrapola.py)
import nodal as N  # noqa: E402

RJ = json.load(open(os.path.join(E_DIR, "r2_J.json"), encoding="utf-8"))["final"]
P0, EP0 = RJ["P0"], RJ["P0_err"]
C_E = 0.40550044604751534            # ens_final/resultado.json, c_recomendado (control)
PARTIDAS_E = {"Taylor": 6.941431361408242e-08, "GL20": 1.1562319292382851e-07, "extraA": 1.6604718023106193e-08}
FILAS9 = ("A", "C3", "V", "f6", "Q1", "D1", "Q2", "D2", "F")
FILAS_PRES = [("A", "dA_suma"), ("C3", "C3cuad"), ("f6", "f6"), ("Q1", "Q1"), ("D1", "D1"), ("Q2", "Q2"),
              ("D2", "D2"), ("V", "V"), ("V", "Vp"), ("F", "F"), ("F", "Fp")]
Q1_CIRC = [24, 48, 72, 96, 120, 144, 192]   # series del circulo r = 0.06 (y del circulo r = 0.03 en v3)
Q1_BASE_C3 = {"Q1": Q1_CIRC, "D1": Q1_CIRC}
INFRA_A = 7.9e-9                             # ens_final §3.4: A en x = 0.5475, m <= 192 (real frente a declarado)
CS = math.sqrt(sum(1.0 / (n - 1) ** 2 for n in range(2, 32)))


def c_de(I):
    return N.CTE["F1"] - 1.0 / 12 + I + P0 - N.CTE["S"]


# ------------------------------------------------------------------------------------------------ carga
def num(v):
    return complex(v[0], v[1]) if isinstance(v, list) else float(v)


def leer_tareas(ruta):
    """{id: tarea} de una carpeta de tareas (*.json), de un JSON unido ({id: tarea}) o de una tarea suelta."""
    out = {}
    rutas = sorted(glob.glob(os.path.join(ruta, "*.json"))) if os.path.isdir(ruta) else [ruta]
    for r in rutas:
        with open(r, encoding="utf-8") as fh:
            d = json.load(fh)
        if isinstance(d, dict) and "id" in d and "mallas" in d:
            out[d["id"]] = d
        elif isinstance(d, dict):
            out.update({k: v for k, v in d.items() if isinstance(v, dict) and "mallas" in v})
    return out


def juntar(fuentes):
    """{(grupo, etiqueta): {"x", "filas": {fila: {m: {clave: valor}}}, "origen": {fila: {m: fuente}}}}.
    Una malla repetida se queda con la primera fuente y se anota la diferencia (control de reproduccion)."""
    pts, avisos, repetidas = {}, [], []
    for nombre, tareas in fuentes:
        for tid in sorted(tareas):
            t = tareas[tid]
            x = complex(*t["x"]) if t["x"][1] != 0 else float(t["x"][0])
            p = pts.setdefault((t["grupo"], t["etiqueta"]), {"x": x, "filas": {}, "origen": {}})
            if abs(p["x"] - x) > 1e-14:
                avisos.append(f"{t['grupo']} {t['etiqueta']}: x distinto ({p['x']} frente a {x}) en {tid}")
                continue
            f = p["filas"].setdefault(t["fila"], {})
            o = p["origen"].setdefault(t["fila"], {})
            for m, e in t["mallas"].items():
                m = int(m)
                vals = {k: num(v) for k, v in e["valores"].items()}
                if m in f:
                    dif = max([abs(vals[k] - f[m][k]) / max(abs(f[m][k]), 1e-300) for k in vals if k in f[m]] + [0.0])
                    repetidas.append([t["grupo"], t["etiqueta"], t["fila"], m, o[m], nombre, dif])
                    continue
                f[m] = vals
                o[m] = nombre
    return pts, avisos, repetidas


# ------------------------------------------------------------------------------------------------ recetas
def rich_A(d):
    """A (y C3) con m = 384: Richardson en 3*2^k con todas las mallas; error de la cabecera del modulo."""
    ms = sorted(m for m in d if EX.es_3x2k(m))
    v, e = EX.richardson(ms, [d[m] for m in ms])
    v192 = EX.richardson([m for m in ms if m <= 192], [d[m] for m in ms if m <= 192])[0]
    v96 = EX.richardson([m for m in ms if m <= 96], [d[m] for m in ms if m <= 96])[0]
    d1, d0 = abs(v - v192), abs(v192 - v96)
    q = min(1.0, d1 / d0) if d0 > 0 else 1.0
    return v, max(8.0 * e, d1 * q), {"ms": ms, "err_richardson": e, "R384-R192": d1, "R192-R96": d0, "q": q}


def q2_v3(d):
    """Q2 con mallas mayores: ramas mod 24 con (2,4,6) desde m = 72 (o desde 48 si una rama no tiene 5 mallas desde
    72); se compara con la media desde el corte siguiente (96, o 48 / 24).  Cabecera del modulo."""
    ms = sorted(m for m in d if m % 12 == 0 and m >= 24)

    def ramas(lo):
        r0 = [m for m in ms if m % 24 == 0 and m >= lo]
        r1 = [m for m in ms if m % 24 == 12 and m >= lo]
        if min(len(r0), len(r1)) < 5:
            return None
        (v0, e0), (v1, e1) = N.fit(r0, d, (2, 4, 6)), N.fit(r1, d, (2, 4, 6))
        return v0, v1, max(e0, e1)
    prim = next(((lo, ramas(lo)) for lo in (72, 48) if ramas(lo) is not None), None)
    if prim is None:
        v, e, info = EX.ext_q2(d)
        return v, e, {"receta": "ext_q2 (pocas mallas)"}
    lo, a = prim
    otro = next((l2 for l2 in ((96, 48) if lo == 72 else (72, 24)) if ramas(l2) is not None), None)
    v = 0.5 * (a[0] + a[1])
    dm = 0.0
    if otro is not None:
        b = ramas(otro)
        dm = abs(v - 0.5 * (b[0] + b[1]))
    err = max(abs(a[0] - a[1]), dm) + a[2]
    info = {"desde": lo, "ramas": [a[0], a[1]], "residuo": a[2], "dif_ramas": a[0] - a[1], "comparado_con": otro,
            "dif_medias": dm, "mmax": max(ms)}
    return v, float(err), info


def _fit_o_none(d, ms, pots):
    return N.fit(ms, d, pots)[0] if len(ms) >= len(pots) + 2 else None


def _media(d, lo, pots):
    a = [_fit_o_none(d, [m for m in d if m % 24 == r and m >= lo], pots) for r in (0, 12)]
    return None if None in a else 0.5 * (a[0] + a[1])


VARIANTES_Q2 = {"rama 0, m>=72": lambda d: _fit_o_none(d, [m for m in d if m % 24 == 0 and m >= 72], (2, 4, 6)),
                "rama 12, m>=72": lambda d: _fit_o_none(d, [m for m in d if m % 24 == 12 and m >= 72], (2, 4, 6)),
                "media de ramas m>=48": lambda d: _media(d, 48, (2, 4, 6)),
                "media de ramas m>=96": lambda d: _media(d, 96, (2, 4, 6)),
                "media de ramas (2,4,6,8) m>=48": lambda d: _media(d, 48, (2, 4, 6, 8))}
VAR_Q2 = {}          # sensibilidad: {"Q2": nombre de VARIANTES_Q2} (solo puntos con mallas nuevas)


def base_de(fila, x, base_grupo=None):
    if base_grupo and fila in base_grupo:
        return sorted(base_grupo[fila])
    return sorted(EX.secuencia(fila, x, False))


def filas_v3(p, receta="v3", base_grupo=None):
    """{fila: {clave: (valor, error)}} y {fila: info}.  'mejor' = nodal.filas (ens_final) con la secuencia base (o la
    del grupo); 'v3' = 'mejor' + mallas nuevas de A (384), Q1/D1 (192, 240) y Q2 (> 144)."""
    out, info = {}, {}
    for fila, cr in p["filas"].items():
        if fila in ("J", "k6"):
            continue
        base = base_de(fila, p["x"], base_grupo)
        if not all(m in cr for m in base):
            continue
        res = {k: (v["valor"], v["error"]) for k, v in EX.extrapolar(fila, cr, base).items()}
        if fila in ("Q1", "D1", "D2"):
            dd = {m: cr[m][fila] for m in base}
            v, e, _ = (N.ext_q1_mejor if fila != "D2" else N.ext_d2_mejor)(dd)
            res[fila] = (v, e)
        if fila == "Q2" and N.VARIANTE.get("Q2"):
            dd = {m: cr[m]["Q2"] for m in base}
            res["Q2"] = (N.ext_q2_variante(dd, N.VARIANTE["Q2"]), res["Q2"][1])
        extra = sorted(m for m in cr if m not in base)
        if receta == "v3" and extra:
            if fila in ("A", "C3") and 384 in cr and all(m in cr for m in (24, 48, 96, 192)):
                for k in list(res):
                    dd = {m: cr[m][k] for m in cr if k in cr[m]}
                    if not all(m in dd for m in (24, 48, 96, 192, 384)):
                        continue
                    v, e, inf = rich_A(dd)
                    res[k] = (v, e)
                    if k in ("dA_suma", "C3cuad"):
                        info[fila] = inf
            elif fila in ("Q1", "D1") and max(cr) >= 192:
                dd = {m: cr[m][fila] for m in cr if m % 24 == 0 and fila in cr[m]}
                v, e, nom = N.ext_q1_mejor(dd)
                res[fila] = (v, e)
                info[fila] = {"ms": sorted(dd), "receta": nom}
            elif fila == "Q2" and max(cr) > max(base):
                dd = {m: cr[m]["Q2"] for m in cr if m % 12 == 0 and "Q2" in cr[m]}
                v, e, inf = q2_v3(dd)
                if VAR_Q2.get("Q2"):
                    vv = VARIANTES_Q2[VAR_Q2["Q2"]](dd)
                    v = v if vv is None else vv
                res["Q2"] = (v, e)
                info["Q2"] = inf
        out[fila] = res
    return out, info


# ------------------------------------------------------------------------------------------------ piezas
def circulo_v3(pts, grupo, r, M, receta, base_grupo=None):
    """Como nodal.circulo (coeficientes de Taylor por la regla del trapecio, simetria conjugada) con los puntos de
    cualquier grupo.  Devuelve (dict, None) o (None, motivo)."""
    ext, infos = [], []
    for j in range(M // 2 + 1):
        p = pts.get((grupo, f"j{j:02d}"))
        if p is None:
            return None, f"falta el punto j{j:02d}"
        e, inf = filas_v3(p, receta, base_grupo)
        falta = [f for f in FILAS9 if f not in e]
        if falta:
            return None, f"j{j:02d}: filas incompletas {falta}"
        ext.append(e)
        infos.append(inf)

    def serie(vals):
        f = np.zeros(M, complex)
        for j in range(M // 2 + 1):
            f[j] = vals[j]
            if 0 < j < M // 2:
                f[M - j] = np.conj(vals[j])
        return np.fft.fft(f) / M / r ** np.arange(M)
    d_n = sum(serie([complex(ext[j][f][k][0]) for j in range(M // 2 + 1)]) for f, k in N.PARTES)
    g_n = serie([complex(ext[j]["V"]["V"][0]) + complex(ext[j]["F"]["F"][0]) for j in range(M // 2 + 1)])
    g_n[0] -= 1.0 / 12
    n = np.arange(M)
    k_n = d_n + (1 - n) * g_n
    ed = [math.sqrt(sum(abs(ext[j][f][k][1]) ** 2 for f, k in N.PARTES)) for j in range(M // 2 + 1)]
    eG = [math.hypot(abs(ext[j]["V"]["V"][1]), abs(ext[j]["F"]["F"][1])) for j in range(M // 2 + 1)]
    por_fila = {f"{f}:{k}": max(abs(ext[j][f][k][1]) for j in range(M // 2 + 1)) for f, k in N.PARTES}
    por_fila["V:V"] = max(abs(ext[j]["V"]["V"][1]) for j in range(M // 2 + 1))
    por_fila["F:F"] = max(abs(ext[j]["F"]["F"][1]) for j in range(M // 2 + 1))
    return {"r": r, "M": M, "k_n": k_n, "d_n": d_n, "g_n": g_n, "ed_max": max(ed), "eG_max": max(eG),
            "ed_puntos": ed, "error_max_por_fila": por_fila,
            "V_n": serie([complex(ext[j]["V"]["V"][0]) for j in range(M // 2 + 1)]),
            "F_n": serie([complex(ext[j]["F"]["F"][0]) for j in range(M // 2 + 1)]), "infos": infos}, None


def grupo_gl_v3(pts, grupo, n, a, b, receta, base_grupo=None):
    X, W = N.nodos_gl(n, a, b)
    out = []
    for i in range(n):
        p = pts.get((grupo, f"n{i + 1:02d}"))
        if p is None:
            return X, W, None, f"falta el nodo n{i + 1:02d}"
        if abs(p["x"] - X[i]) > 1e-13:
            return X, W, None, f"n{i + 1:02d}: x = {p['x']} no es el nodo {X[i]}"
        e, inf = filas_v3(p, receta, base_grupo)
        falta = [f for f in FILAS9 if f not in e]
        if falta:
            return X, W, None, f"n{i + 1:02d}: filas incompletas {falta}"
        k, ek, ed, d, G, Gp = N.k_de(float(X[i]), e)
        a384 = "A" in p["filas"] and 384 in p["filas"]["A"]
        out.append({"x": float(X[i]), "w": float(W[i]), "k": k, "ek": ek, "ed": ed, "filas": e, "info": inf,
                    "A384": a384})
    return X, W, out, None


def prop(X, W, ek):                                   # = r4_c.prop
    a = W / X ** 2 * np.asarray(ek)
    return float(np.sqrt(np.sum(a ** 2))), float(np.sum(a)), a


def cota_GL_sub(n, a, b, M=2868.0, rho=2.0):          # = r4_c.cota_GL_sub (Bernstein, elipse dentro de E_2)
    c0, h = 0.5 * (a + b), 0.5 * (b - a)
    th = np.linspace(0, 2 * np.pi, 20001)
    z = c0 + h * 0.5 * (rho * np.exp(1j * th) + np.exp(-1j * th) / rho)
    u = (z - 0.5) / 0.5
    rho_u = np.abs(u + np.sqrt(u - 1) * np.sqrt(u + 1))
    rho_u = np.maximum(rho_u, 1 / rho_u)
    assert np.all(rho_u <= 2.0 + 1e-12), "la elipse no cabe en E_2"
    return h * (64.0 / 15) * M * rho ** (-2 * n) / (rho ** 2 - 1)


def pres_gl(nodos, X, W, kk):
    """Error nodal por fila en un panel de Gauss (r6_presupuesto): (cuadratico, lineal)."""
    f, k = kk
    eb = np.array([abs(t["filas"][f][k][1]) * (t["x"] if k in ("Vp", "Fp") else 1.0) for t in nodos])
    a = W / X ** 2 * eb
    return float(np.sqrt(np.sum(a ** 2))), float(np.sum(a))


def pres_taylor(cir, kk):
    """Datos de la serie por fila (r6_presupuesto): Cauchy-Schwarz; la parte G, (1 - n) g_n, con raiz de 30."""
    f, k = kk
    if k in ("Vp", "Fp"):
        return 0.0
    emax = cir["error_max_por_fila"].get(f"{f}:{k}", 0.0)
    return (math.sqrt(30) if f in ("V", "F") else CS) * emax / cir["r"]


def extra_A(nodos):
    """ens_final §3.4: A en x > 0.3 con m <= 192 (Richardson infraestimado, 7.9e-9 por nodo)."""
    return float(sum(t["w"] / t["x"] ** 2 * INFRA_A for t in nodos if t["x"] > 0.3 and not t["A384"]))


def serie_entre(cir, a, b, N_=31):
    """int_a^b k/x^2 por la serie del circulo (k_0 = k_1 = 0): sum k_n (b^(n-1) - a^(n-1))/(n-1)."""
    nn = np.arange(2, N_ + 1)
    return float(np.sum(cir["k_n"][2:N_ + 1].real * (b ** (nn - 1) - a ** (nn - 1)) / (nn - 1)))


# ------------------------------------------------------------------------------------------------ metodos
def metodo_antiguo(pts, receta):
    cir, msg = circulo_v3(pts, "circulo", 0.06, 32, receta)
    if cir is None:
        return None, f"circulo r = 0.06: {msg}"
    Xb, Wb, nb, msg = grupo_gl_v3(pts, "GLb", 20, 0.06, 1.0, receta)
    if nb is None:
        return None, f"GLb: {msg}"
    IT, cT, terms = N.taylor_integral(cir, N=31)
    kb = np.array([t["k"] for t in nb])
    IG = float(np.sum(Wb * kb / Xb ** 2))
    eq, el, _ = prop(Xb, Wb, [t["ek"] for t in nb])
    exA = extra_A(nb)
    part = {"serie [0, 0.06]: datos del circulo (Cauchy-Schwarz)": cT,
            "GL20 [0.06, 1]: error nodal, suma lineal": el,
            "A en x > 0.3 sin m = 384 (Richardson infraestimado x 8)": exA,
            "P0": EP0, "cuadratura GL20 (Bernstein, ens_final)": cota_GL_sub(20, 0.06, 1.0),
            "truncacion de la serie (N = 31)": max(abs(terms[-1]), 1e-13), "S": N.CTE["S_err"]}
    pres = {f"{f}:{k}": {"serie": pres_taylor(cir, (f, k)), "GL20": pres_gl(nb, Xb, Wb, (f, k))} for f, k in FILAS_PRES}
    return {"c": c_de(IT + IG), "I_serie": IT, "I_GL20": IG, "nodal_GL20_cuad": eq, "partidas": part,
            "error": math.sqrt(sum(v ** 2 for v in part.values())), "error_lineal": sum(part.values()),
            "por_fila": pres, "cir": cir, "nb": nb, "Xb": Xb, "Wb": Wb}, None


def metodo_nuevo(pts, receta, base_c3, cert=None):
    cir2, msg = circulo_v3(pts, "circulo3", 0.03, 32, receta, base_c3)
    if cir2 is None:
        return None, f"circulo r = 0.03: {msg}"
    X6, W6, n6, msg = grupo_gl_v3(pts, "GL6", 6, 0.03, 0.06, receta)
    if n6 is None:
        return None, f"GL6: {msg}"
    Xb, Wb, nb, msg = grupo_gl_v3(pts, "GLb", 20, 0.06, 1.0, receta)
    if nb is None:
        return None, f"GLb: {msg}"
    IT, cT, terms = N.taylor_integral(cir2, N=31)
    k6 = np.array([t["k"] for t in n6])
    I6 = float(np.sum(W6 * k6 / X6 ** 2))
    eq6, el6, _ = prop(X6, W6, [t["ek"] for t in n6])
    kb = np.array([t["k"] for t in nb])
    IG = float(np.sum(Wb * kb / Xb ** 2))
    eqb, elb, _ = prop(Xb, Wb, [t["ek"] for t in nb])
    exA = extra_A(nb)
    if cert and cert.get("serie") and cert.get("panel"):
        cuad = cert["serie"]["total"] + cert["panel"]["total"]
        nom_c = "serie [0, 0.03] y GL6: Teoremas 4.4 y 4.3 con las muestras [D] si muestras [C]"
    else:
        cuad = 5e-10 + 3e-10
        nom_c = "serie [0, 0.03] y GL6: objetivo del diseno (p5_bernstein, diseno.py) [C], sin muestras evaluadas"
    part = {"serie [0, 0.03]: datos del circulo r = 0.03 (Cauchy-Schwarz)": cT,
            "GL6 [0.03, 0.06]: error nodal, suma lineal": el6,
            "GL20 [0.06, 1]: error nodal, suma lineal": elb,
            "A en x > 0.3 sin m = 384 (Richardson infraestimado x 8)": exA,
            "P0": EP0, nom_c: cuad,
            "cuadratura GL20 en [0.06, 1] (p5_bernstein: 1.7e-11 [D] si muestras [C])": 1.7e-11,
            "S": N.CTE["S_err"]}
    pres = {f"{f}:{k}": {"serie": pres_taylor(cir2, (f, k)), "GL6": pres_gl(n6, X6, W6, (f, k)),
                         "GL20": pres_gl(nb, Xb, Wb, (f, k))} for f, k in FILAS_PRES}
    # parte F exacta (p5_bernstein, Lema de la parte F): int_0^1 k_F/x^2 = F(0) + F'(0) - F(1)
    nn = np.arange(2, 32)
    IF_num = float(np.sum(((1 - nn) * cir2["F_n"][2:32]).real * 0.03 ** (nn - 1) / (nn - 1)))
    for X, W, nod in ((X6, W6, n6), (Xb, Wb, nb)):
        for t, w in zip(nod, W):
            F, _ = t["filas"]["F"]["F"]
            Fp, _ = t["filas"]["F"]["Fp"]
            IF_num += w * (F - cir2["F_n"][0].real - t["x"] * Fp) / t["x"] ** 2
    IF_exacta = float(cir2["F_n"][0].real + cir2["F_n"][1].real - N.CTE["F1"])
    return {"c": c_de(IT + I6 + IG), "I_serie": IT, "I_GL6": I6, "I_GL20": IG, "nodal_GL6_cuad": eq6,
            "nodal_GL20_cuad": eqb, "partidas": part, "error": math.sqrt(sum(v ** 2 for v in part.values())),
            "error_lineal": sum(part.values()), "por_fila": pres, "ultimo_termino": abs(terms[-1]),
            "parte_F": {"cuadratura": IF_num, "exacta": IF_exacta, "exacta_menos_cuadratura": IF_exacta - IF_num},
            "cir2": cir2, "n6": n6, "nb": nb, "X6": X6, "W6": W6}, None


# ------------------------------------------------------------------------------------------------ muestras
def rich_p5(ms, vals, pots):                          # = p5_bernstein/balance.richardson
    Am = np.array([[1.0] + [m ** -p for p in pots] for m in ms])
    return np.linalg.solve(Am, np.array(vals))[0] if len(ms) == len(pots) + 1 else \
        np.linalg.lstsq(Am, np.array(vals), rcond=None)[0][0]


def valor_delta(v, ms=(24, 36, 48)):
    """Richardson en 1/m^2 con las mallas ms del grupo (3 o 4) y delta_j como balance.py:
    3 mallas: R3 y delta = 3 max(|R3 - R(m2,m3)|, |R(m2,m3) - R(m1,m2)|) + 1e-6 |R3|;
    4 mallas: R4 (potencias 2, 4, 6) y delta = 3 max(|R4 - R3(m2..m4)|, |R3(m2..m4) - R3(m1..m3)|) + 1e-6 |R4|."""
    ms = list(ms)
    if len(ms) == 4:
        r4 = rich_p5(ms, [v[m] for m in ms], (2, 4, 6))
        r3a = rich_p5(ms[:3], [v[m] for m in ms[:3]], (2, 4))
        r3b = rich_p5(ms[1:], [v[m] for m in ms[1:]], (2, 4))
        return complex(r4), float(3 * max(abs(r4 - r3b), abs(r3b - r3a)) + 1e-6 * abs(r4))
    r3 = rich_p5(ms, [v[m] for m in ms], (2, 4))
    r2a = rich_p5(ms[:2], [v[m] for m in ms[:2]], (2,))
    r2b = rich_p5(ms[1:], [v[m] for m in ms[1:]], (2,))
    return complex(r3), float(3 * max(abs(r3 - r2b), abs(r2b - r2a)) + 1e-6 * abs(r3))


def muestras(pts, cfg, salida, tareas_v3):
    """Muestras de k_6: valores, delta_j, exportacion (formato de muestras_k6.py) y, en la nube, cotas del punto 5."""
    out, L = {}, []
    gcfg = {g["nombre"]: g for g in (cfg or {}).get("grupos", []) if g.get("filas") == ["k6"]}
    for nombre, g in sorted(gcfg.items()):
        ptsg = {e: p for (gg, e), p in pts.items() if gg == nombre and "k6" in p["filas"]}
        MSG = sorted(g.get("mallas", {}).get("k6", [24, 36, 48]))
        if len(MSG) < 3:                          # p. ej. el grupo de la prueba rapida (una malla): como en v3
            MSG = [24, 36, 48]
        ok = {e: p for e, p in ptsg.items() if all(m in p["filas"]["k6"] for m in MSG)}
        n_esp = len(lanzador_puntos(g))
        out[nombre] = {"puntos": len(ok), "esperados": n_esp}
        if not ok:
            continue
        filas, recs = [], []
        for e in sorted(ok):
            p = ok[e]
            j = int(e[1:])
            x = complex(p["x"])
            k6 = {m: p["filas"]["k6"][m]["k6"] for m in MSG}
            V = {m: p["filas"]["k6"][m]["V"] for m in MSG}
            kv, dk = valor_delta(k6, MSG)
            vv, dv = valor_delta(V, MSG)
            hv, dh = valor_delta({m: k6[m] / x ** 2 for m in k6}, MSG)
            filas.append({"j": j, "x": [x.real, x.imag], "k6": [kv.real, kv.imag], "delta_k": dk,
                          "V": [vv.real, vv.imag], "delta_V": dv, "h6": [hv.real, hv.imag], "delta_h": dh})
            pt = g["puntos"]
            M_ = int(pt.get("M", g.get("elipse", {}).get("N", 0)))
            th = 2 * math.pi * j / M_ if M_ else None
            for m in MSG:
                vals = p["filas"]["k6"][m]
                recs.append({"j": j, "m": m, "theta": th, "x": [x.real, x.imag],
                             **{k: [complex(v).real, complex(v).imag] for k, v in vals.items()}})
        out[nombre]["filas"] = filas
        out[nombre]["delta_max_k"] = max(f["delta_k"] for f in filas)
        out[nombre]["delta_max_V"] = max(f["delta_V"] for f in filas)
        out[nombre]["delta_rms_h"] = float(np.sqrt(np.mean([f["delta_h"] ** 2 for f in filas])))
        os.makedirs(salida, exist_ok=True)
        if "elipse" in g:
            el = g["elipse"]
            fich = f"muestras_e{el['a']}_{el['b']}_r{el['rho']}_N{el['N']}.jsonl"
        else:
            fich = f"muestras_c{g['puntos']['r']}_N{g['puntos']['M']}.jsonl"
        with open(os.path.join(salida, fich), "w", encoding="utf-8") as fh:
            for rec in recs:
                fh.write(json.dumps(rec) + "\n")
        out[nombre]["archivo"] = fich
        L.append(f"  {nombre}: {len(ok)}/{n_esp} puntos; delta max k {out[nombre]['delta_max_k']:.1e}, V "
                 f"{out[nombre]['delta_max_V']:.1e}; delta_rms h {out[nombre]['delta_rms_h']:.1e}; -> {fich}")
    return out, L


def lanzador_puntos(g):
    p = g["puntos"]
    if p["tipo"] == "circulo":
        return list(p.get("j", range(int(p["M"]) // 2 + 1)))
    return list(p.get("etiquetas", []))


def limpio(o):
    """Para JSON: complejos -> [re, im], tipos de numpy -> de Python, tuplas -> listas."""
    if isinstance(o, dict):
        return {str(k): limpio(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [limpio(v) for v in o]
    if isinstance(o, np.ndarray):
        return limpio(o.tolist())
    if isinstance(o, (complex, np.complexfloating)):
        return [float(o.real), float(o.imag)]
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    return o


def certificacion(mu, cfg):
    """Teoremas 4.3 (GL6 con las muestras de la elipse) y 4.4 (serie r = 0.03 con las de |x| = 0.055), con las
    funciones de p5_bernstein (solo en la nube).  [D] si las muestras estan a delta de los valores verdaderos [C]."""
    if not P5_DIR or not os.path.exists(os.path.join(P5_DIR, "refinamiento.py")):
        return None, ["  certificacion: se calcula en la nube (necesita p5_bernstein)"]
    g = {x["nombre"]: x for x in cfg["grupos"] if x.get("filas") == ["k6"]}
    me, mc = mu.get("muestras_e", {}), mu.get("muestras_c", {})
    if me.get("puntos") != me.get("esperados") or mc.get("puntos") != mc.get("esperados") or not me or not mc:
        return None, ["  certificacion: faltan muestras"]
    if P5_DIR not in sys.path:
        sys.path.append(P5_DIR)
    import refinamiento as RF
    import taylor_cotas as TC
    res, L = {}, []
    # --- panel GL6 (Teorema 4.3): f = h_6 en la elipse E_rho de [0.03, 0.06]
    el = g["muestras_e"]["elipse"]
    Ne, rho, rho2 = int(el["N"]), float(el["rho"]), float(el["rho2"])
    a, b, n = el["a"], el["b"], int(el["n_gauss"])
    H0 = 0.5 * (b - a)
    dis = json.load(open(os.path.join(P5_DIR, "diseno.json"), encoding="utf-8"))["0.03"]["panel_n2_6"]["muestreo"]
    Cbar = float(dis[3])
    h = np.zeros(Ne, complex)
    dl = np.zeros(Ne)
    for f in me["filas"]:
        j = f["j"]
        h[j], dl[j] = complex(*f["h6"]), f["delta_h"]
        if 0 < j < Ne // 2:
            h[Ne - j], dl[Ne - j] = np.conj(h[j]), f["delta_h"]
    bhat = (np.fft.fft(h) / Ne)[: Ne // 2 + 1] / rho ** np.arange(Ne // 2 + 1)
    K = Ne // 2 - 1
    ks = np.arange(2 * n, K + 1, 2)
    datos = H0 * float(np.sum(2 * RF.e_k(ks) * np.abs(bhat[ks])))
    drms = float(np.sqrt(np.mean(dl ** 2)))
    alias, ruido, cola = RF.partes(H0, n, rho, rho2, Cbar, Ne, drms)
    res["panel"] = {"datos": datos, "solapamiento": alias, "ruido": ruido, "cola": cola,
                    "total": datos + alias + ruido + cola, "delta_rms": drms, "Cbar": Cbar, "rho": rho, "rho2": rho2,
                    "bhat_abs": [float(abs(v)) for v in bhat]}
    L.append(f"  GL6 (Teorema 4.3, N = {Ne}, rho = {rho:.3f}, rho2 = {rho2:.2f}): datos {datos:.1e}, solapamiento "
             f"{alias:.1e}, ruido {ruido:.1e}, cola {cola:.1e} -> {res['panel']['total']:.2e} [D] si muestras [C]")
    # --- serie r2 = 0.03, N2 = 32 (Teorema 4.4): muestras de k_6 y V en |x| = R_s
    ce = g["muestras_c"]["certificacion"]
    Rs, Ns, R, r2, N2 = float(ce["R_s"]), int(ce["N_s"]), float(ce["R"]), float(ce["r2"]), int(ce["N2"])
    tc = json.load(open(os.path.join(P5_DIR, "taylor_cotas.json"), encoding="utf-8"))["circulos"][str(R)]
    Mk, MV = float(tc["M_k6"]), float(tc["M_V"])
    kk = np.zeros(Ns, complex)
    vv = np.zeros(Ns, complex)
    for f in mc["filas"]:
        j = f["j"]
        kk[j], vv[j] = complex(*f["k6"]), complex(*f["V"])
        if 0 < j < Ns // 2:
            kk[Ns - j], vv[Ns - j] = np.conj(kk[j]), np.conj(vv[j])
    khat = np.fft.fft(kk) / Ns / Rs ** np.arange(Ns)
    vhat = np.fft.fft(vv) / Ns / Rs ** np.arange(Ns)
    _, c, cp = TC.pesos(r2, N2, Ns - 1)
    datosT = float(sum(c[m] * abs(khat[m]) + cp[m] * abs(vhat[m]) for m in range(N2, Ns)))
    resto = TC.E_T_muestras(r2, N2, R, Mk, MV, Rs, Ns, mc["delta_max_k"], mc["delta_max_V"])
    res["serie"] = {"datos": datosT, "resto": resto, "total": datosT + resto, "M_k6": Mk, "M_V": MV, "R": R,
                    "R_s": Rs, "N_s": Ns, "delta_k": mc["delta_max_k"], "delta_V": mc["delta_max_V"],
                    "khat_abs_Rs": [float(abs(khat[m]) * Rs ** m) for m in range(Ns)]}
    L.append(f"  serie r = {r2} (Teorema 4.4, N_s = {Ns} en |x| = {Rs}, R = {R}): datos {datosT:.1e}, resto "
             f"{resto:.1e} -> {res['serie']['total']:.2e} [D] si muestras [C]")
    return res, L


# ------------------------------------------------------------------------------------------------ informe
def fmt_part(part):
    return [f"    {v:.1e}  {k}" for k, v in part.items()]


def analizar(dir_t=None, cfg=None, salida=None, extra=()):
    """Lineas de resumen y dict de resultados.  dir_t: carpeta de tareas v3 (o JSON unido); extra: mas rutas."""
    if cfg is None and os.path.exists(os.path.join(PAQ, "config.json")):
        cfg = json.load(open(os.path.join(PAQ, "config.json"), encoding="utf-8"))
    salida = salida or SALIDA
    L, R = [], {"etiqueta": "[N]", "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                "fuentes": {"pc_resultados": os.path.basename(PR_JSON)}}
    pr = leer_tareas(PR_JSON)
    v3 = {}
    for ruta in ([dir_t] if dir_t else []) + list(extra):
        if ruta and os.path.exists(ruta):
            v3.update(leer_tareas(ruta))
    R["fuentes"]["v3_tareas"] = len(v3)
    # ---------------------------------------------------------------- control: ens_final con la tanda anterior
    pts0, _, _ = juntar([("PR", pr)])
    m0, msg = metodo_antiguo(pts0, "mejor")
    dif = m0["c"] - C_E
    L.append(f"Control (solo la tanda anterior, recetas de ens_final): c = {m0['c']:.10f}; ens_final {C_E:.10f}; "
             f"diferencia {dif:+.1e} " + ("[O] reproduce" if abs(dif) < 1e-14 else "NO REPRODUCE"))
    pe = list(m0["partidas"].values())
    L.append(f"  partidas: serie {pe[0]:.3e} (ens_final {PARTIDAS_E['Taylor']:.3e}), GL20 {pe[1]:.3e} "
             f"({PARTIDAS_E['GL20']:.3e}), A x > 0.3 {pe[2]:.3e} ({PARTIDAS_E['extraA']:.3e}); total {m0['error']:.2e}")
    R["control"] = {"c": m0["c"], "c_ens_final": C_E, "diferencia": dif, "partidas": m0["partidas"],
                    "error": m0["error"]}
    if not v3:
        L.append("Sin tareas nuevas: solo el control.")
        return L, limpio(R)
    # ---------------------------------------------------------------- juntar
    pts, avisos, rep = juntar([("PR", pr), ("v3", v3)])
    grupos = {}
    for (g, e) in pts:
        grupos[g] = grupos.get(g, 0) + 1
    L.append(f"Tareas nuevas: {len(v3)}; puntos por grupo: " + ", ".join(f"{g} {n}" for g, n in sorted(grupos.items())))
    for a in avisos:
        L.append("  AVISO " + a)
    if rep:
        L.append(f"  mallas repetidas (se usa la tanda anterior): {len(rep)}; max dif relativa {max(r[-1] for r in rep):.1e}")
    R["avisos"], R["repetidas"] = avisos, rep
    base_c3 = dict(Q1_BASE_C3)
    for g in (cfg or {}).get("grupos", []):
        if g["nombre"] == "circulo3" and g.get("prioridad", 0) == 1:
            base_c3 = {f: v for f, v in g.get("mallas", {}).items() if f in ("Q1", "D1")} or base_c3
    # ---------------------------------------------------------------- mallas nuevas por punto
    nuevos = []
    for (g, e), p in sorted(pts.items()):
        if g not in ("GLb", "circulo"):
            continue
        res, inf = filas_v3(p, "v3")
        resm, _ = filas_v3(p, "mejor")
        for fila, clave in (("Q2", "Q2"), ("Q1", "Q1"), ("A", "dA_suma")):
            if fila in inf and fila in res and fila in resm:
                v, er = res[fila][clave]
                v0, e0 = resm[fila][clave]
                nuevos.append({"grupo": g, "punto": e, "x": [complex(p["x"]).real, complex(p["x"]).imag],
                               "fila": fila, "v3": [float(np.real(v)), er], "antes": [float(np.real(v0)), e0],
                               "cambio": float(np.real(v - v0)), "info": inf[fila]})
    R["filas_con_mallas_nuevas"] = nuevos
    if nuevos:
        L.append("Filas con mallas nuevas (valor v3 - antes; error v3 / antes):")
        for t in nuevos:
            L.append(f"  {t['grupo']:8s} {t['punto']} x = {t['x'][0]:+.4f}{t['x'][1]:+.4f}i {t['fila']:2s} "
                     f"{t['cambio']:+.2e}  ({t['v3'][1]:.1e} / {t['antes'][1]:.1e})")
    # ---------------------------------------------------------------- esquema antiguo con mallas nuevas
    ma, msg = metodo_antiguo(pts, "v3")
    if ma:
        R["antiguo"] = {k: v for k, v in ma.items() if k in ("c", "I_serie", "I_GL20", "partidas", "error",
                                                              "error_lineal", "por_fila", "nodal_GL20_cuad")}
        L.append(f"Esquema anterior (serie r = 0.06 + GL20) con las mallas nuevas: c = {ma['c']:.10f} +- "
                 f"{ma['error']:.1e} (lineal {ma['error_lineal']:.1e}); cambio frente a ens_final {ma['c'] - C_E:+.1e}")
        L += fmt_part(ma["partidas"])
    else:
        L.append(f"Esquema anterior: no disponible ({msg})")
    # ---------------------------------------------------------------- muestras y certificacion
    mu, Lm = muestras(pts, cfg, os.path.join(salida, "muestras_p5"), v3)
    R["muestras"] = mu
    cert = None
    if Lm:
        L.append("Muestras del punto 5 (fila k6, Richardson con las mallas del grupo; delta como balance.py):")
        L += Lm
        cert, Lc = certificacion(mu, cfg) if cfg else (None, [])
        L += Lc
        R["certificacion"] = cert
    # ---------------------------------------------------------------- esquema nuevo
    mn, msg = metodo_nuevo(pts, "v3", base_c3, cert)
    if mn:
        R["nuevo"] = {k: v for k, v in mn.items() if k in ("c", "I_serie", "I_GL6", "I_GL20", "partidas", "error",
                                                           "error_lineal", "por_fila", "parte_F", "ultimo_termino",
                                                           "nodal_GL6_cuad", "nodal_GL20_cuad")}
        cir2 = mn["cir2"]
        R["nuevo"]["circulo3"] = {"k_n": [[float(z.real), float(z.imag)] for z in cir2["k_n"]],
                                  "ed_max": cir2["ed_max"], "eG_max": cir2["eG_max"],
                                  "error_max_por_fila": cir2["error_max_por_fila"]}
        L.append(f"Esquema nuevo (punto 5: serie r = 0.03 + GL6 [0.03, 0.06] + GL20): c = {mn['c']:.10f} +- "
                 f"{mn['error']:.1e} (lineal {mn['error_lineal']:.1e}); frente a ens_final {mn['c'] - C_E:+.1e}")
        L += fmt_part(mn["partidas"])
        k = cir2["k_n"]
        L.append(f"  circulo r = 0.03: k_0 = {k[0].real:+.1e}, k_1 r = {k[1].real * 0.03:+.1e} (deben ser 0 [D]); "
                 f"error max de d en los puntos {cir2['ed_max']:.1e}; ultimo termino de la serie {mn['ultimo_termino']:.0e}")
        L.append(f"  parte F exacta (F(0) + F'(0) - F(1)) menos su cuadratura: "
                 f"{mn['parte_F']['exacta_menos_cuadratura']:+.1e}")
        if ma:
            cir = ma["cir"]
            I_r6_a = serie_entre(cir, 0.03, 0.06)
            I_r6_b = serie_entre(cir, 0.0, 0.03)
            R["nuevo"]["controles"] = {"GL6 - serie r=0.06 en [0.03,0.06]": mn["I_GL6"] - I_r6_a,
                                       "serie r=0.03 - serie r=0.06 en [0,0.03]": mn["I_serie"] - I_r6_b,
                                       "nuevo - antiguo": mn["c"] - ma["c"]}
            L.append(f"  controles: GL6 - serie(r = 0.06) en [0.03, 0.06] = {mn['I_GL6'] - I_r6_a:+.1e}; serie(0.03) - "
                     f"serie(0.06) en [0, 0.03] = {mn['I_serie'] - I_r6_b:+.1e}; nuevo - antiguo = {mn['c'] - ma['c']:+.1e}")
        L.append("  presupuesto por fila (serie C-S | GL6 lineal | GL20 lineal), las mayores:")
        filas_ord = sorted(mn["por_fila"].items(), key=lambda kv: -(kv[1]["serie"] + kv[1]["GL6"][1] + kv[1]["GL20"][1]))
        for nom, v in filas_ord[:6]:
            L.append(f"    {nom:10s} {v['serie']:.1e} | {v['GL6'][1]:.1e} | {v['GL20'][1]:.1e}")
    else:
        L.append(f"Esquema nuevo: no disponible ({msg})")
    # ---------------------------------------------------------------- sensibilidad a la receta de Q2 (mallas nuevas)
    if ma and any(t["fila"] == "Q2" for t in nuevos):
        sens = {}
        for nom in VARIANTES_Q2:
            VAR_Q2["Q2"] = nom
            a = metodo_antiguo(pts, "v3")[0]
            b = metodo_nuevo(pts, "v3", base_c3, cert)[0]
            sens[nom] = [a["c"] - ma["c"] if a else None, (b["c"] - mn["c"]) if (b and mn) else None]
        VAR_Q2.clear()
        R["sensibilidad_Q2"] = sens
        L.append("Sensibilidad a la receta de Q2 en los nodos con mallas nuevas (cambio de c: antiguo / nuevo):")
        for nom, (a, b) in sens.items():
            L.append(f"  {nom:32s} {a:+.1e} / " + (f"{b:+.1e}" if b is not None else "-"))
    return L, limpio(R)


def guardar(L, R, salida, sello):
    os.makedirs(salida, exist_ok=True)

    def conv(o):
        if isinstance(o, complex):
            return [o.real, o.imag]
        if isinstance(o, np.ndarray):
            return [conv(v) for v in o.tolist()] if np.iscomplexobj(o) else o.tolist()
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, np.bool_):
            return bool(o)
        return str(o)
    rj = os.path.join(salida, f"analisis_v3_{sello}.json")
    with open(rj, "w", encoding="utf-8") as fh:
        json.dump(R, fh, indent=1, default=conv)
    rt = os.path.join(salida, f"resumen_v3_{sello}.txt")
    with open(rt, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\nEvidencia numerica, no prueba.\n")
    return rj, rt


def main(argv):
    salida = None
    rutas = []
    i = 0
    while i < len(argv):
        if argv[i] == "--salida":
            salida = argv[i + 1]
            i += 2
            continue
        rutas.append(argv[i])
        i += 1
    if EN_PAQUETE and not rutas:
        rutas = [os.path.join(AQUI, "resultados", "tareas")]
    L, R = analizar(rutas[0] if rutas else None, None, salida, extra=rutas[1:])
    print("\n".join(L))
    rj, rt = guardar(L, R, salida or SALIDA, time.strftime("%Y%m%dT%H%M%S"))
    print(f"(escrito {rj} y {rt})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
