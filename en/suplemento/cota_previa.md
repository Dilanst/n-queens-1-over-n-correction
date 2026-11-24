# Cota previa a corte fijo / Preliminary bound at a fixed cut-off

## Español

Sea \(R_Q(n)=\log Q(n)-\log Q_{\rm pred}(n)\) en el tablero inicial ordinario. Fijados los márgenes
y \(\delta\) de la clase regular, elíjase un corte admisible \(b>0\) y póngase \(j=\lfloor bn\rfloor\).
Existen \(C_{b,\delta}\) y \(n_0(b,\delta)\) tales que \(|R_Q(n)|\le C_{b,\delta}/n\) para
\(n\ge n_0(b,\delta)\). El argumento siguiente usa las estimaciones en la ley adaptativa ordinaria
\(\nu\) anteriores al cambio a \(\mu\).

**Entradas.** En una historia detenida escribimos \(X=Qe^{-L}\), con \(X=0\) si el tablero carece de
completaciones, y \(A\) para la suma de los logaritmos de las normalizaciones ordinarias de fila.
Sea \(S_M\) la entrada regular en \(M=\lceil\delta n\rceil\) y \(H_j\subset S_M\) la llegada histórica corta
del apéndice «Suma del resto en la llegada». Allí \(\log X=g_T+\Gamma+g^\flat\).
La parte de ese apéndice que trabaja bajo \(\nu\) da
\(\mathbb E_\nu[|g^\flat|;H_j]=O_{b,\delta}(n^{-1})\). La parte positiva de \(\log X\) está acotada en
\(H_j\) y \(|g_T|+|\Gamma|\le C/j\). Por \(|e^z-1|\le e^{z^+}|z|\),
\[
  \mathbb E_\nu[|X-1|;H_j]=O_{b,\delta}(n^{-1}).
\]
En \(S_M\), la consistencia hasta la parada da \(|A|\le C_\delta/M+C/j\). Las estimaciones de salida
del apéndice «Identidad con signo y estimación de llegada» y del artículo del término constante
(§§4, 5, 6 y 8) tienen dos usos. Primero, en \(S_M\setminus H_j\) el coste en media con peso \(1+X\)
es exponencialmente pequeño a \(b\) fijo, al sumar las bandas de tamaño al menos \(j/2\) y la llegada
larga. Segundo, tanto la probabilidad de \(S_M^c\) como su contribución con peso \(e^A X\) son
exponencialmente pequeñas. Para esta última, la cota es
\(C\exp(-c_\delta n+D_\delta n^{2/3}+O_\delta(n^{-1}))\).

**Deducción.** Para cada orden de filas, las completaciones se reparten entre los prefijos detenidos.
En la probabilidad adaptativa del prefijo los cocientes de predictores se cancelan al multiplicar por
\(e^A X\). Al promediar el orden de filas resulta \(e^{R_Q(n)}=\mathbb E_\nu[e^A X]\).
Las cotas anteriores dan \(\mathbb E_\nu[X;S_M]=1+O_{b,\delta}(n^{-1})\). En \(S_M\) podemos
multiplicar esta media por \(e^{\pm(C_\delta/M+C/j)}\) para acotar \(\mathbb E_\nu[e^A X;S_M]\)
por ambos lados, porque \(X\ge0\). Al añadir \(S_M^c\) queda \(e^{R_Q(n)}=1+O_{b,\delta}(n^{-1})\).
Tomar logaritmos prueba la cota. Basta elegir un solo \(b\) para obtener la acotación inicial;
el paso que identifica el límite compara después distintos cortes.

## English

Let \(R_Q(n)=\log Q(n)-\log Q_{\rm pred}(n)\) on the ordinary initial board. Fix the regularity
margins and \(\delta\), choose an admissible \(b>0\), and put \(j=\lfloor bn\rfloor\).
There are constants \(C_{b,\delta}\) and \(n_0(b,\delta)\) such that
\(|R_Q(n)|\le C_{b,\delta}/n\) for \(n\ge n_0(b,\delta)\). The proof uses the estimates under the
ordinary adaptive law \(\nu\) obtained before changing to \(\mu\).

**Inputs.** On a stopped history, write \(X=Qe^{-L}\), with \(X=0\) when the board has no
completions, and let \(A\) be the sum of the logarithms of the ordinary row normalizations.
Let \(S_M\) be regular entry at \(M=\lceil\delta n\rceil\), and let \(H_j\subset S_M\) be the short
historical arrival event in the appendix on the arrival remainder. On this event,
\(\log X=g_T+\Gamma+g^\flat\). The part of that appendix under \(\nu\) gives
\(\mathbb E_\nu[|g^\flat|;H_j]=O_{b,\delta}(n^{-1})\). The positive part of \(\log X\) is bounded on
\(H_j\), and \(|g_T|+|\Gamma|\le C/j\). Since \(|e^z-1|\le e^{z^+}|z|\),
\[
  \mathbb E_\nu[|X-1|;H_j]=O_{b,\delta}(n^{-1}).
\]
On \(S_M\), consistency up to the stopping time gives \(|A|\le C_\delta/M+C/j\). The exit estimates
in the appendix “Signed identity and arrival estimate” and in the constant-term paper (§§4, 5, 6, 8)
are used twice. First, on \(S_M\setminus H_j\) the expected cost with weight \(1+X\) is exponentially
small at fixed \(b\), summing over bands of size at least \(j/2\) and the long arrival. Second, both
the probability of \(S_M^c\) and its contribution with weight \(e^A X\) are exponentially small.
The latter is bounded by \(C\exp(-c_\delta n+D_\delta n^{2/3}+O_\delta(n^{-1}))\).

**Deduction.** For each row order, the stopped prefixes partition the completions. Multiplying the
adaptive prefix probability by \(e^A X\) cancels its predictor ratios. Averaging over the row order
gives \(e^{R_Q(n)}=\mathbb E_\nu[e^A X]\). The bounds above give
\(\mathbb E_\nu[X;S_M]=1+O_{b,\delta}(n^{-1})\). Since \(X\ge0\), multiplying this mean by
\(e^{\pm(C_\delta/M+C/j)}\) bounds \(\mathbb E_\nu[e^A X;S_M]\) from both sides. Adding the
contribution of \(S_M^c\) gives \(e^{R_Q(n)}=1+O_{b,\delta}(n^{-1})\). Taking logarithms proves
the bound. One fixed \(b\) suffices for initial boundedness. The subsequent comparison between
different cut-offs identifies the limit.

**Trazabilidad / Traceability.** El argumento sigue la identidad detenida y la aplicación de la
cota de llegada de la prueba previa / The argument follows the stopped identity and its use of the
arrival estimate in the earlier proof. See the [proof source table](traza_prueba.md), first entry.
