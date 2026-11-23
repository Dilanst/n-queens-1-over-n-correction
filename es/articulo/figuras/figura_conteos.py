"""Figura de nR_Q(n) para 16 <= n <= 27.
Uso: python3 figura_conteos.py <carpeta con suplemento/datos> [es|en] [salida.pdf]"""
import json, math, sys
import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter, MultipleLocator

base = sys.argv[1]
idioma = sys.argv[2] if len(sys.argv) > 2 else "es"
sep = "," if idioma == "es" else "."
datos = {r["n"]: r["nR"] for r in json.load(open(f"{base}/suplemento/datos/c_n.json"))}
aj = json.load(open(f"{base}/suplemento/datos/ajuste_finito.json"))["ajuste"]
c, a, kap, A = aj["c"], aj["a"], aj["kappa"], aj["A16"]

fam = "TeX Gyre Pagella" if any("Pagella" in f.name for f in font_manager.fontManager.ttflist) else "serif"
plt.rcParams.update({"font.family": fam, "font.size": 9, "mathtext.fontset": "custom",
                     "mathtext.rm": fam, "mathtext.it": f"{fam}:italic", "pdf.fonttype": 3,
                     "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6})
coma = FuncFormatter(lambda v, _: f"{v:.1f}".replace(".", sep))

fig, ax = plt.subplots(figsize=(5.6, 2.9))
x = np.linspace(15.6, 27.4, 400)
deriva = c + a / x
amp = A * np.exp(-kap * (x - 16))
ax.fill_between(x, deriva - amp, deriva + amp, color="#9AA0A6", alpha=0.18, lw=0, zorder=1)
ax.plot(x, deriva, color="#5F6368", lw=1.0, zorder=2)
ax.axhline(c, color="#202124", lw=0.9, ls=(0, (5, 3)), zorder=2)

clases = [(lambda n: n % 2 == 1, "o", "#202124", (r"$n$ impar" if idioma == "es" else r"$n$ odd")),
          (lambda n: n % 4 == 0, "^", "#0072B2", r"$n\equiv 0 \ (\mathrm{mod}\ 4)$"),
          (lambda n: n % 4 == 2, "v", "#D55E00", r"$n\equiv 2 \ (\mathrm{mod}\ 4)$")]
ns = [n for n in sorted(datos) if 16 <= n <= 27]
for cond, mk, col, lab in clases:
    sel = [n for n in ns if cond(n)]
    ax.plot(sel, [datos[n] for n in sel], ls="none", marker=mk, ms=6.0, mfc=col, mec="white",
            mew=0.7, color=col, label=lab, zorder=3)

ax.text(27.45, c + 0.012, (r"$c_{\mathrm{err}}\approx 0{,}40550$" if idioma == "es" else r"$c_{\mathrm{err}}\approx 0.40550$"), ha="right", va="bottom", fontsize=8.5)
ax.text(27.45, c + a / 27.45 - 0.012, r"$c_{\mathrm{err}} + a/n$", ha="right", va="top", fontsize=8.5, color="#5F6368")
ax.set_xlim(15.5, 27.6); ax.set_ylim(-0.02, 0.62)
ax.xaxis.set_major_locator(MultipleLocator(1)); ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_formatter(coma)
ax.set_xlabel(r"$n$"); ax.set_ylabel(r"$n\,R_Q(n)$")
ax.grid(axis="y", color="#DADCE0", lw=0.5); ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper center", ncol=3, frameon=False, fontsize=8.5, handletextpad=0.3, markerscale=1.1,
          columnspacing=1.4, bbox_to_anchor=(0.5, 1.13))
fig.tight_layout(pad=0.3)
salida = sys.argv[3] if len(sys.argv) > 3 else f"{base}/paper_es/figuras/conteos.pdf"
fig.savefig(salida)
print("ok", fam, "c=%.8f a=%.3f kappa=%.3f A=%.3f" % (c, a, kap, A))
