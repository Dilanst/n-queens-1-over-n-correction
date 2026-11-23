"""refinamiento.py -- teorema de muestreo para el error de Gauss-Legendre (Teorema 4.3 de parte_04.tex).  [D] + [C]

f analitica dentro de la elipse E_rho2 de [a, b]; g(w) = f(c + h (w + 1/w)/2), g(w) = g(1/w), coeficientes de Laurent
beta_k = beta_{-k}; f = beta_0 + sum_k 2 beta_k T_k.  Cauchy en |w| = rho2 con la MEDIA en theta de |g|:
|beta_k| <= Cbar rho2^-|k|.  Muestras en w_j = rho e^{2 pi i j/N} con error |e_j| <= delta_j ([C]).
DFT: bhat_k = rho^-k (1/N) sum_j f_j e^{-2 pi i j k/N} = beta_k + A_k + rho^-k ehat_k,
  |A_k| <= Cbar [rho2^-k q^N/(1 - q^N) + rho2^k (rho rho2)^-N / (1 - (rho rho2)^-N)],  q = rho/rho2.
Error de Gauss (n nodos): E_n[f] = h sum_{k >= 2n, par} 2 beta_k E_n[T_k],  |E_n[T_k]| <= e_k = 2 + 2/(k^2 - 1)
(k par; 0 si k es impar).  Cota:
  |E_n[f]| <= h sum_{k=2n, par}^{K} 2 e_k (|bhat_k| + |A_k| + rho^-k |ehat_k|) + h sum_{k>K, par} 2 e_k Cbar rho2^-k,
con K <= N/2 - 1 y sum_k |ehat_k|^2 <= mean_j |e_j|^2 (Parseval).
Uso: python3 refinamiento.py  -> refinamiento.json (N necesario frente a (rho, rho2) con la cota gruesa)"""
import json
import math
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
sys.dont_write_bytecode = True


def e_k(k):
    return 2.0 + 2.0 / (k * k - 1.0)


def partes(h, n, rho, rho2, Cbar, N, delta_rms):
    """Partes de la cota que no dependen de los valores muestreados: solapamiento, ruido y cola."""
    K = N // 2 - 1
    ks = np.arange(2 * n, K + 1, 2)
    q = rho / rho2
    lA = np.logaddexp(-ks * math.log(rho2) + N * math.log(q) - math.log1p(-q ** N),
                      ks * math.log(rho2) - N * math.log(rho * rho2) - math.log1p(-(rho * rho2) ** -N))
    A = Cbar * np.exp(lA)
    alias = h * float(np.sum(2 * e_k(ks) * A))
    ruido = h * 2 * float(np.sqrt(np.sum((e_k(ks) * rho ** -ks) ** 2))) * delta_rms     # Cauchy-Schwarz + Parseval
    k0 = K + 1 if (K + 1) % 2 == 0 else K + 2
    cola = h * 2 * e_k(k0) * Cbar * rho2 ** -k0 / (1 - rho2 ** -2)
    return alias, ruido, cola


def N_necesario(h, n, rho, rho2, Cbar, delta_rms, objetivo):
    for N in range(4 * n, 4000, 2):
        a, r, c = partes(h, n, rho, rho2, Cbar, N, delta_rms)
        if a + r + c <= objetivo:
            return N, (a, r, c)
    return None, None


if __name__ == "__main__":
    CG = json.load(open(os.path.join(AQUI, "cota_gruesa.json")))["contornos"]
    out = {}
    h, n = 0.47, 20
    for rho2 in (2.0, 2.1, 2.15, 2.2):
        Cbar = CG[f"elipse[0.06,1.0] rho={rho2}"]["media_h6"]
        for delta in (0.003, 0.01, 0.03, 0.1):
            best = None
            for rho in np.arange(1.30, rho2 - 0.015, 0.02):
                N, p = N_necesario(h, n, rho, rho2, Cbar, delta, 3e-10)
                if N is not None and (best is None or N < best[0]):
                    best = (N, round(float(rho), 2), p)
            out[f"rho2={rho2} delta={delta}"] = best
            print(f"rho2={rho2} Cbar={Cbar:.2e} delta_rms={delta}: N={best[0]} rho={best[1]} partes={best[2]}")
    json.dump(out, open(os.path.join(AQUI, "refinamiento.json"), "w"), indent=1)
