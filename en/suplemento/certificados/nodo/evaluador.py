"""Segundo término de Q_c del continuo en un nodo. Las partidas incluyen signo y 1/4."""
import numpy as np

from iv import I


def recorre_partidas():
    return [f"S{i}{k}" for i in range(1, 6) for k in range(i, 6) if (i, k) != (3, 3)]


TRAZAS = tuple(recorre_partidas())
PARTIDAS = TRAZAS + ("SII", "SIII", "SIVp")


def interseccion(a, b):
    lo, hi = np.maximum(a.lo, b.lo), np.minimum(a.hi, b.hi)
    if np.any(lo > hi):
        raise ArithmeticError("Expresiones equivalentes de Q2 tienen recintos disjuntos")
    return I(lo, hi)


def envolvente_ultima(a):
    return I(np.min(a.lo, axis=-1), np.max(a.hi, axis=-1))


def si_valido(mask, a):
    return I(np.where(mask, a.lo, 0.), np.where(mask, a.hi, 0.))


class Evaluador:
    """Los índices de centro son los de geo.peso. No se presupone simetría diédrica."""

    def __init__(self, geo):
        self.geo = geo
        self.oo = geo.om[:, None] * geo.om[None, :]
        self.GK = -geo.GPi - geo.Pi
        self.kap = (geo.om[:, None] * geo.K.sq()).sum(axis=0)
        self.columnas = {}
        self.beta_panel = {}

    def beta(self, j):
        """Matriz (v,u): suma de GPi(v,w) en las otras dos familias de u^j."""
        if j not in self.beta_panel:
            geo = self.geo
            bj = I(0)
            for f, ids in enumerate(geo.cruces):
                if f == geo.familia[j]:
                    continue
                # ids[u,j,:] recorre los paneles de una misma familia del cruce.
                opciones = geo.GPi[:, ids[:, j, :]]
                valido = geo.posible[:, j] & (geo.familia != f)
                bj += si_valido(valido[None, :], envolvente_ultima(opciones))
            self.beta_panel[j] = bj
        return self.beta_panel[j]

    def datos_columna(self, ids):
        js = tuple(sorted(set(int(j) for j in ids)))
        if js not in self.columnas:
            geo = self.geo
            j = np.asarray(js, dtype=int)
            def col(A):
                return envolvente_ultima(A[:, j])
            beta = self.beta(js[0])
            for jj in js[1:]:
                beta = I.hull(beta, self.beta(jj))
            self.columnas[js] = (col(geo.G), -col(geo.GPi), col(geo.K),
                                  col(geo.Pi), col(geo.V), beta)
        return self.columnas[js]

    def traza(self, A, B):
        return (self.oo * (A * B.T)).sum()

    def centro(self, c):
        geo = self.geo
        cols = [self.datos_columna(ids) for ids in geo.J[c]]
        g = sum((col[0] for col in cols), I(0))
        Et = sum((envolvente_ultima(g[ids]) for ids in geo.cruces), I(0))
        # Para un cruce no garantizado, también se admite el integrando nulo.
        Et = I(np.where(geo.seguro, Et.lo, np.minimum(0., Et.lo)),
               np.where(geo.seguro, Et.hi, np.maximum(0., Et.hi)))
        Et = si_valido(geo.posible, Et)
        P3 = -(geo.K * Et)
        P4 = geo.GPi @ (geo.om[:, None] * P3)
        P2, P5 = I(0), I(0)
        sii, siii, a2s = I(0), I(0), I(0)
        for _, Fj, Kj, Pij, A2, beta in cols:
            Vb = Kj + Pij
            P2 += Fj[:, None] * Vb[None, :]
            P5 -= Kj[None, :] * beta
            Pk = self.GK + Fj[:, None] - beta
            sii += (self.oo * A2[None, :] * (geo.K + Vb[:, None]) * Pk).sum() * 2
            siii += (geo.om * A2).sum().sq()
            a2s += A2
        # K(v,u)=K(u,v) permite combinar los dos sumandos lineales en A2.
        sivp = (geo.om * self.kap * a2s).sum() * (-2)

        P = {1: geo.Pi, 2: P2, 3: P3, 4: P4, 5: P5}
        t = {"S11": I(1), "S12": I(0), "S14": I(0), "S15": I(0)}
        for i in range(1, 6):
            for k in range(i, 6):
                nombre = f"S{i}{k}"
                if nombre in t or (i, k) == (3, 3):
                    continue
                t[nombre] = self.traza(P[i], P[k]) * (1 if i == k else 2)
        b = P2 + P4 + P5
        combinado = self.traza(b, b) + 2*self.traza(b, P3) + t["S13"]
        separado = sum((t[k] for k in TRAZAS if k != "S11"), I(0))
        i_sin_11 = interseccion(combinado, separado)
        t.update(SII=sii, SIII=siii, SIVp=sivp, grupo_I_sin_S11=i_sin_11,
                 Q2_sin_S11=i_sin_11+sii+siii+sivp)
        peso = geo.peso[c] * 0.25
        t = {k: peso * a for k, a in t.items()}
        t["grupo_I"] = t["S11"] + t["grupo_I_sin_S11"]
        t["Q2"] = t["S11"] + t["Q2_sin_S11"]
        return t


def evaluar(geo, callback=None):
    """Integra todos los centros. El callback recibe índice y partidas ya ponderadas."""
    motor = Evaluador(geo)
    totales = {}
    for c in range(len(geo.peso)):
        piezas = motor.centro(c)
        if callback is not None:
            callback(c, piezas)
        for k, p in piezas.items():
            totales[k] = totales.get(k, I(0)) + p
    totales["S11"] = interseccion(totales["S11"], I(.25))  # integral nu = 1
    totales["grupo_I"] = interseccion(totales["grupo_I"],
                                      totales["S11"] + totales["grupo_I_sin_S11"])
    totales["Q2"] = interseccion(totales["Q2"], totales["S11"] + totales["Q2_sin_S11"])
    totales["S"] = totales["Q2"] * 4
    return totales
