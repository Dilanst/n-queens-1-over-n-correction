# Acta de revisión externa · W4_rev: D1, el corrector O(K⁻²) del permanente sin Divoux–Wang

**Revisor.** Externo, ajeno al autor de `W4_d1/` y a los revisores de las actas anteriores. Fecha: 2026-11-17. Sin web y sin acceso al ordenador de nadie: sólo `rev_exp/`. Sólo he escrito en `rev_exp/W4_rev/`, incluidos los temporales. No he ejecutado el código del autor: todos los cálculos son míos.

**Encargo.** `rev_exp/encargos/comun_ext.md` y `rev_exp/encargos/W4_d1_rev.md`. Se revisa `rev_exp/W4_d1/`: la prueba en `latex/01–03` (con `main.tex`), `ESTADO.md`, `INTEGRACION.md`, `codigo/` y `resultados/`. Ignoro `tmp/`.

**Dictamen global: CERTIFICADA, con precisiones no bloqueantes. D1 queda descargado.** El Teorema 1 de W4_d1 es el enunciado literal de W/permanente, con constante C_*(A, r) uniforme para todo K ≥ 2. Se deduce de U01 con q = 2 y h = v = 0 (certificado por E1 y, para el descenso a q, por W2_cofactor) y de herramientas estándar, sin ningún resultado de Divoux–Wang (DW). La matemática nueva, V₁(y, 1/K) = V(y) exacto, es correcta. No he encontrado ningún hueco de prueba ni ningún enunciado falso. Las precisiones (§5) son de alcance, de redacción y documentales; ninguna cambia el enunciado ni las constantes.

## 0. Alcance, material, integridad, convenciones y método

**Material leído.**
- **Objeto:** `W4_d1/latex/01_corrector_sin_dw.tex` (137 líneas), `02_corrector_prueba.tex` (72), `03_uniformidad_y_usos.tex` (91) y `main.tex`; `ESTADO.md`; `INTEGRACION.md`; los cinco programas de `codigo/` y las ocho salidas de `resultados/`.
- **Fuentes:**
  - W/permanente: `r19/expediente/originales/W/permanente.md`;
  - U01–U08: `r19/expediente/originales/U/`, más los originales `fuentes/velocidad_via2_menores_uniformes_20261117T042237Z/latex/` y su FUENTES.md;
  - `r21/consolidado/latex/01_menores.tex` y `04_marginales.tex`;
  - para los usos: S02, S03, E01, M01, R05 y D04 (originales de r19), E02, K06–K08, K07, MM07, GI02 y, de la ronda 1, `mascara.tex` y `torres_fila.tex`.
- **Actas:** E1, E2, W2_cofactor, W2_torres, W2_difusion, W_global, W3_xi y W3_v2; `divoux_wang/NOTA.md`.
- **Para INTEGRACION:** `v2/` completo (las dos entregas) y los archivos de r21 que cita.
- **Encargo del autor:** `encargos/W4_d1_autor.md`, para contrastar lo que se le pidió.

**Integridad** (`codigo/c0_cotejo.py`, `resultados/c0_cotejo.txt`).
- **Manifiestos sin ninguna discrepancia:**
  - completos: r19 116/116, menores uniformes 14/14, ronda 8 30/30, ronda 9 98/98, media matriz 14/14, grupos interlínea 12/12, v2 integrado 34/34 y v2 cierre 14/14;
  - copias parciales: ronda 1 (17 presentes, entre ellos todos sus `.tex`), ronda 10 (11 presentes) y r21 (106 presentes). Las demás entradas faltan en la copia; ninguna discrepa.
- **Archivos citados.** Las huellas de 01_menores, 04_marginales, Wpermanente, D04 y U02 de r21, de permanente, mascara y torres_fila de la ronda 1 y de K06–K08 de la ronda 9 coinciden con sus manifiestos.
- **Transcripciones.** Son idénticas byte a byte a su original (bloque entre las cercas del `.md`):
  - U/01–08 frente a `menores_uniformes/latex/01–08`;
  - W/permanente frente a la ronda 1 y a `r21/fuentes/latex/Wpermanente.tex`;
  - E/01 (ronda 8), M/01 (media matriz) y D/04 (ronda 10 y r21), y U/02 frente a r21.
- **Registro.** Anoto las huellas SHA256 de los 19 archivos revisados de W4_d1 (`c0_cotejo.txt`, apartado 3).

**Convenciones de cita.** `archivo:n` es la línea n de `rev_exp/archivo`. Abreviaturas:
- **Objeto:** W4/01, W4/02 y W4/03 son las tres partes de `W4_d1/latex/`; EST e INT son `W4_d1/ESTADO.md` e `INTEGRACION.md`.
- **Originales de r19:** Wp, U01…U08, S02, S03, E01, M01, R05 y D04 son los `.md` de `r19/expediente/originales/`. Cito la línea del `.md`; la «orig.» de las actas es esa línea menos 7.
- **Consolidado:** 01m y 04m son `r21/consolidado/latex/01_menores.tex` y `04_marginales.tex`. 04m es idéntico en v2 (lo comprobé con `cmp`).
- **Fuentes de la ronda 9 y otras:** K06, K07 y K08 son `fuentes/…ronda9…/latex/06_torres.tex`, `07_coeficiente.tex` y `08_estabilidad.tex`; E02 es `fuentes/…ronda8…/latex/02_expansion.tex`; R1m es `fuentes/…ronda1…/latex/mascara.tex`; MM07 y GI02 son `07_vertices.tex` (media matriz) y `02_exterior.tex` (grupos interlínea).
- **Actas:** E1:n, E2:n, W2c:n, W2t:n, W2d:n, WG:n, W3x:n y W3v2:n son líneas del `ACTA.md` de E1, E2, W2_cofactor, W2_torres, W2_difusion, W_global, W3_xi y W3_v2.
- **v2:** V2 y CI son `v2/velocidad_expediente_integrado_20261117T173119Z` y `v2/velocidad_cierre_actas_20261117T172100Z`.

**Método.**
1. Leí línea a línea W4/01–03, EST e INT, y cada línea de fuente o acta que citan.
2. Rehíce a mano cada paso, cada desigualdad y cada constante.
3. Comprobé cada cita.
4. Escribí siete programas propios (`codigo/`, con el módulo `exacto.py`), en aritmética racional exacta (`Fraction`) y racional gaussiana Q(i), sin azar. Se ejecutaron con `nice -n 10`, uno cada vez, con el tiempo medido (§3). Son evidencia, no prueba.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Motivo breve |
|---|---|---|---|
| 1 | El teorema: enunciado literal, cuantificadores y C_*(A, r) para todo K ≥ 2 | **Correcta** | Misma clase y misma fórmula que Wp:9–11 y 25–29. C_* sólo depende de (A, r). Pasos 1–3 para K ≥ K_* y paso 0, con cotas groseras, para 2 ≤ K < K_*. |
| 2 | Paso 1: U01 con q = 2 y h = v = 0 | **Correcta con precisión** | Con h = v = 0, la prueba certificada de U01 (01m:12–83, enunciada en 01m:4 para D bistocástica) no usa que D sea escalado de máscara: lo comprobé paso a paso. Además, en todos los usos D es el escalado exacto de una máscara binaria. Basta en todos los usos. |
| 3 | Paso 2: desarrollo de H₂(1/K) | **Correcta** | Formas cerradas de μ₂, …, μ₅ y cota 0 ≤ μ_i ≤ 32u² en (0, 1/8] (128/21, 64/5, 3328/105). \|V₂\| ≤ C₂/K² en Ω. Cauchy en \|y − 1\| = ρ. Descomposición exacta de E₂ y cota C_E/K². Logaritmo con \|x\| ≤ 1/2. |
| 4 | Lema 3: V₁(y, 1/K) = V(y) exacto | **Correcta** | Inversión de Möbius correcta; sólo sobreviven las g inyectivas; factor s!. Grupos (1,2,(4)) y (2,3,(3,3)) con 3, 9 y 6 emparejamientos, a₃ = 1/3 y a₄ = −1/4. El término en u² vale −(5/6)K²ΣH_ii³ y anula la diagonal en u = 1/K. Comprobado en exacto en 31 casos. |
| 5 | Cotas propias: \|H_ij\| ≤ c_H/K, e^{−L} ≤ \|d\| ≤ e^L, \|W_l\| ≤ C_l K^{−l} | **Correcta** | Rehechas a mano. Comprobadas en exacto en 5 matrices y 13 puntos (12 en ∂Ω): ninguna falla. |
| 6 | Ningún uso de DW fuera de los cuatro elementos que rehízo E1 | **Correcta** | Todas las citas comprobadas. Las cuatro herramientas de U01:37–39 corresponden a 01m y a E1:74–77, 86–91. No se usan Lema 3.7, cotas (5)–(8), suma binomial ni Prop. 3.1. |
| 7 | Uniformidad en cada uso: S02–S03, E01, K08, menores con ≤ 4 supresiones, M01 y GI02 | **Correcta con precisión** | Los parámetros de clase son correctos. La replicación conserva exactamente la clase (c5), y K = bk no acotado está cubierto. El rango de K en el telescopio es [j − d − 2, j − d]; el autor escribe [j − 2d − 2, j], que lo contiene. |
| 8 | INTEGRACION.md: los 32 cambios | **Correcta con precisión** | Las 32 referencias de línea son correctas y cubren todo lo que localiza W3v2:187–224. Cuatro precisiones documentales (8a–8d). La más importante: A3–A5 reescribirían originales sellados con manifiesto. |
| 9 | Cálculos propios | **Realizados; evidencia favorable** | c0–c6, 0 fallos. En cuatro familias por bloques con permanentes exactos (tres de ellas con D que no es escalado de máscara), K²·ε_K queda acotado. |

## 2. Detalle por punto

### 2.1 Punto 1 · El teorema

**Comparación con el original.**
- **Clase.** W4/01:10–13 define 𝒟_K(A, r): D ≥ 0 bistocástica, B = D − J_K, max\|B_ij\| ≤ A/K, ‖B‖_op ≤ r < 1, con ceros admitidos. Es la clase de Wp:9–11.
- **Objetos.** d, O, H y V (W4/01:14–21) son los de Wp:15–24. V suma sobre los 2K índices de filas y columnas, con i < j.
- **Conclusión.** W4/01:22–28 es la fórmula de Wp:25–29.

**Cuantificadores.** Wp dice «uniformemente en la clase … O_{A,r}(K⁻²)», con parámetros fijos. El autor lo formaliza así: para todo A > 0 y todo r ∈ [0, 1) existe C_*(A, r) tal que la cota C_*/K² vale para todo K ≥ 2 y toda D ∈ 𝒟_K(A, r). Es la lectura más fuerte de Wp e implica cualquier lectura con un umbral K₀. Hace falta K ≥ 2 por el denominador K − 1.

**Uniformidad en K ≥ 2.**
- C_* (W4/02:53–56) es el máximo de dos expresiones.
  - La primera depende de (K_U, C_U, c_U), que sólo dependen de (1 + A, r) por U01:19–20 y 43.
  - La segunda depende de ρ, θ, c_H, L, C₁, C₂, C_S, C_E, C_x y K_*, todas explícitas en (A, r) (W4/02:2–8).
- **Pasos 1–3**, para K ≥ K_* = max{K_U, 8, ⌈2C_x⌉}:
  - K ≥ K_U para U01;
  - u ≤ 1/8 para las cotas de μ_i;
  - \|x\| ≤ 1/2 para el logaritmo.
- **Paso 0**, para 2 ≤ K < K_* (W4/02:48–51). Lo rehíce:
  - K!/K^K ≤ per D ≤ 1 (van der Waerden; desarrollar ∏_i Σ_j D_ij = 1), luego 0 ≤ log(K^K per D/K!) ≤ log(K^K/K!) ≤ K;
  - 0 ≤ log d(1) ≤ L;
  - \|V(1)\| ≤ C₁/K ≤ C₁, porque el Lema 3(c) no tiene umbral de tamaño;
  - \|d″(1)/(2(K − 1)d(1))\| ≤ e^L ρ^{−2}.
- B = 0 da igualdad exacta (W4/02:57–58; Wp:30).

**Veredicto: correcta.**

### 2.2 Punto 2 · Paso 1: U01 con q = 2 y h = v = 0

**(a) ¿Sólo para el escalado exacto de una máscara?**
- **El texto de las fuentes.**
  - U01:9 habla del «escalado bistocástico exacto de la máscara binaria basal».
  - El acta de E1 formula sus veredictos «en cada máscara de la clase» (E1:24, 226 y 238).
  - En cambio, 01m:4 enuncia la hipótesis para «D bistocástica, jD_rc ≤ M₀, ‖D − J_j‖₂ ≤ r < 1». Esa línea es igual en r19 y en r21, y E1 leyó 01_menores íntegramente (E1:9, 31–101).
- **Lo que usa la prueba con h = v = 0.** Recorrí 01m:12–83, U02:46–62, U03:9–61 y U04:9–57.
  - *Representación de Wick por la SVD:* B real con B𝟙 = Bᵗ𝟙 = 0 (01m:13–22).
  - *Cota en módulo:* \|R_B(z)\| ≤ E(1 + \|z\|W/m)^m es la desigualdad aritmético-geométrica. Además log E e^{\|z\|W} ≤ CΣσ_l ≤ C√m, que sólo usa ‖B‖_HS ≤ A y \|z\|r < 1 (01m:23–29). d^{±1} acotados por Σσ² ≤ A² (01m:29).
  - *Identidad formal de Wick:* es algebraica (01m:35–42).
  - *Cota de V_l:* núcleo puntualmente acotado (01m:48, por U02:46–55). Sólo usa \|jB\| ≤ A y la brecha en L².
  - *Identidad de mezcla:* es algebraica para toda D = J + B (01m:56–58): basta desarrollar per(J + B).
  - *Cola gamma ponderada:* W y la brecha (01m:59–66).
  - *Momentos y Taylor:* sólo cotas de clase (01m:68–80).
  - *Logaritmo:* van der Waerden, que pide D ≥ 0 bistocástica (U04:54–55; 01m:80–83).
- **Dónde entraría la máscara.** La estructura de máscara sólo interviene en el balanceo de menores (U02:13–33), que con h = v = 0 es vacío (D′ = D).
- **Conclusión.** La aplicación a una D cualquiera de la clase es legítima. El autor lo dice bien (W4/01:49–56) y lo señala (EST:47).

**Precisión 2a.** Es una extensión del texto literal de U01:9 y del alcance que formula E1. La respaldan 01m:4 y la comprobación anterior, pero conviene escribirlo como tal. La alternativa, que basta para todos los usos, es enunciar el Teorema 1 para escalados exactos de máscaras.

**Precisión 2b.** W4/01:53–54 dice que «el núcleo acotado de 01m:48 es aquí el Lema 1(a)». La prueba de U01 necesita esa cota en \|yw\| ≤ r₁(1 + d₀) (U02:49; 01m:30–31), no en Ω. El argumento del Lema 1(a) la da igual, sustituyendo ρ por 1 − r₁(1 + d₀)r > 0. Es una cuestión de redacción: el paso 1 importa el enunciado de U01, no su cota de núcleo.

**(b) ¿Basta en todos los usos?** Sí. Comprobé uso por uso la afirmación de W4/03:32–35: en todos, D es el escalado exacto de una máscara binaria.
- *S02:* D es el escalado de P∘(1 − P), que es separable en el soporte (S02:9–11). Por la unicidad del escalado de Sinkhorn (W2d, punto 4), D es el escalado de la máscara.
- *S02, menor:* D′ es el reescalado del menor de D (S02:43–46), es decir, el escalado del menor de la máscara.
- *Telescopio de 04m:58–62:* menores de la máscara.
- *E01:* D es el escalado de P∘(1 − P) (R1m:4–5).
- *K08:* replicaciones (K08:2–3) y menores (K08:11–14).
- *M01 y GI02:* menores del exterior, que es una máscara binaria (MM07:2–3; GI02:2–3).

Así que, aun con la lectura literal de U01:9, todos los usos quedan cubiertos. Las constantes de U01 son de clase (U01:19–20 y 43), lo que da la uniformidad en K que pide K08. Evidencia: en c4 las tres familias que no son escalado de máscara se comportan como la que sí lo es (§3).

**Veredicto: correcta con precisión** (2a, 2b).

### 2.3 Punto 3 · Paso 2: el desarrollo de H₂(1/K)

**Lo que se importa** (W4/01:40–47). H₂(u) = Σ_{i≤5} μ_i ∂_y^i S₂(1, u)/i! con S₂ = d(1 + V₁ + V₂), por U04:24–28 y U03:61. La recurrencia de U04:27 y el descenso de U04:44–46 son los de U01 con q = 2.

**Momentos (Lema 2, W4/01:85–95).**
- Rehíce μ₂ = u/(1 − u), μ₃, μ₄ y μ₅. En u = 1/K, μ₂ = 1/(K − 1).
- **Cota.** Divididos por u², los numeradores tienen coeficientes ≥ 0, y los denominadores ∏_{a<i}(1 − au) son positivos y decrecientes en [0, 1/8]. Luego μ_i/u² crece, y en u = 1/8 vale 128/21, 64/5 y 3328/105 < 32.
- **Comprobado en c2:**
  - las formas cerradas;
  - la igualdad con E(X − 1)^i para 6 ≤ K ≤ 120 e i ≤ 7;
  - la igualdad, como funciones racionales, con la fórmula de K07:37–38, de modo que H₂ = H_*;
  - la cota, también en la rejilla u = k/4000.
- Sólo se usan los valores de la recurrencia. Que sean momentos sólo hace falta para K > i, y no interviene en la prueba.

**Cotas en Ω** (W4/02:16–23).
- S₂(y, 1/K) = d(1 + V + W₂), por el Lema 3(a)–(b).
- \|S₂\| ≤ C_S y \|S₂ − d\| ≤ e^L(C₁ + C₂)/K.
- S₂ es holomorfa cerca de Ω: H es racional sin polos en \|y\| < 1/r y Ω ⊂ {\|y\| ≤ (3 − r)/2} ⊂ {\|y\| < 1/r}, porque (r − 1)(r − 2) > 0.
- Cauchy en \|y − 1\| = ρ da las dos cotas de W4/02:21–22.

**Descomposición** (W4/02:25–34).
- H₂ = d(1)(1 + V(1)) + d″(1)/(2(K − 1)) + E₂, con E₂ como en W4/02:30–31. Es exacta: la comprobé en exacto en c4, en cuatro familias y en todos los K (columna «identidad E2»).
- **Cota de E₂.** Las tres cotas de W4/02:33–34 son correctas: 1/(K − 1) ≤ 2/K, μ_i ≤ 32/K² y ρ ≤ 1/2, de modo que ρ^{−i} ≤ ρ^{−5}. Luego \|E₂\| ≤ C_E/K².

**Paso 3** (W4/02:36–46).
- En y = 1 todos los datos son reales.
- \|x\| ≤ C_x/K ≤ 1/2: \|V(1)\| ≤ C₁/K, \|d″\| ≤ 2e^Lρ^{−2}, d(1) ≥ 1 y C_E/K² ≤ C_E/K.
- \|log(1 + x) − x\| ≤ x² para \|x\| ≤ 1/2.
- E₃ = E₂/d(1) + (log(1 + x) − x), y sup_t t²e^{−ct} = 4/(ec)².

**Observación (no es un hueco).** Las constantes (e^L, 96C_Sρ^{−5}, K_* ≥ 2C_x) son enormes, lo cual es admisible en un enunciado existencial. En c4, K²·E₂/d(1) tiene una fase transitoria grande hasta K ≈ 100 en tres familias; en la cuarta (F3a) se acerca lentamente a un límite finito (−0,27 en K = 60). En cambio, el error del enunciado final se estabiliza enseguida (§3).

**Veredicto: correcta.**

### 2.4 Punto 4 · Lema 3: V₁(y, 1/K) = V(y), exacto

**(a) La inversión de Möbius** (W4/01:111–125). La rehíce.
- **Núcleo físico.** En los datos físicos, la medida de cada lado da masa 1/K a cada punto (U02:9). El operador O tiene núcleo z − 1 = KB, así que su matriz es B y la del propagador es H(y). Su núcleo respecto de la medida es K·H(y) (U02:48–55; U03:39–40).
- **Potencias de K.** La integral de U03:37 vale K^{E−\|π\|}Σ_f ∏H, y u^{E−\|π\|} = K^{−(E−\|π\|)} la compensa.
- **Cambio de suma.** Σ_π Σ_f = Σ_g Σ_{π≤ker g}. ker g es automáticamente de un mismo lado, porque los dos lados son conjuntos de índices disjuntos, y el intervalo [0̂, ker g] queda dentro del subretículo de particiones de un mismo lado.
- **Möbius.** c_π es la función de Möbius μ(0̂, π) del retículo de particiones, y Σ_{π≤τ} μ(0̂, π) = [τ = 0̂]. Lo comprobé exhaustivamente para n ≤ 6 (c1). Sólo quedan las g inyectivas.
- **Factor s!.** Los pares (σ, g) son las g inyectivas, y cada (S, 𝐝) procede de s! pares, lo que compensa el 1/s! de U03:18. Queda W_l.
- **Coherencia con otras fuentes.** Coincide con U03:26–27, con K07:30–32 («exactamente la suma de índices distintos») y con torres_fila.tex:4–9 («V₁ = V»).

**(b) Sólo exceso uno** (W4/01:126–132).
- E − s = 1 y Σd ≥ 3s dan (s, E, 𝐝) = (1, 2, (4)) o (2, 3, (3, 3)).
- Con cuatro patas en un vértice hay 3 emparejamientos (H_ii²). Con grados (3, 3), de los 15 emparejamientos, 9 tienen un lazo en cada vértice y una arista cruzada, y 6 tienen tres aristas cruzadas.
- r₀ = exp(z³/3 − z⁴/4 + z⁵/5 − …) da a₃ = 1/3, a₄ = −1/4, a₅ = 1/5 y a₆ = −1/9.
- Sale −(3/4)ΣH_ii² + Σ_{i<j}(H_iiH_jjH_ij + (2/3)H_ij³), que es Wp:21–23.

**(c) El término en u².** V₁(y, u) = c₁u + c₂u².
- c₂ procede de π = {{1, 2}} con los dos vértices en el mismo lado: (1/9)(1/2)(−1)·15, de modo que c₂ = −(5/6)K²Σ_iH_ii³.
- En u = 1/K anula exactamente la diagonal i = j del término de singletons. Por eso V usa i < j (EST:64).

**Comprobación exacta propia** (c1).
- Implementé la fórmula literal de U03:30–40: vértices etiquetados con lados, grados ordenados, emparejamientos de patas etiquetadas, particiones de un mismo lado, polinomio en u e integral literal con pesos 1/K y núcleo K·H.
- Comparé con W_l, sumado por conjuntos S y funciones de grados, sin el factor s!, y con V de Wp.
- **Exceso uno:** 25 casos, con K = 2, 3, 4, 5, una D con ceros y cinco valores de y, dos de ellos complejos. Todos dan igualdad, y la estructura c₁u + c₂u² se confirma.
- **Exceso dos:** V₂ = W₂ en 6 casos (K = 2, 3, 4, uno con y complejo).
- **Controles negativos:** u = 1/(K + 1) y a₃ = 1/2 fallan, como deben.

**Veredicto: correcta.**

### 2.5 Punto 5 · Las cotas propias del autor

**Lema 1(a)** (W4/01:71–76). Lo rehíce.
- Los autovalores de O(1) están en [−r, r], y I + O(y) es normal, con autovalores de módulo ≥ 1 − θ = (1 − r)(1 − r/2) ≥ ρ.
- H es simétrica: Oᵗ = O, y (I + O)^{−1} conmuta con O.
- H = O − O(I + O)^{−1}O, con \|O_ij\| ≤ (3/2)A/K y ‖Oe_i‖ ≤ (3/2)A/√K.
- Por tanto \|H_ij\| ≤ ((3/2)A + (9/4)A²/ρ)/K ≤ c_H/K.

**Lema 1(b)** (W4/01:77–82).
- Σσ_i² = ‖B‖²_HS ≤ A², y la rama es holomorfa en \|y\| < 1/r.
- Con \|Log(1 − x)\| ≤ \|x\|/(1 − \|x\|) y \|yσ_i\| ≤ θ resulta \|log d\| ≤ (9/8)A²/(1 − θ²) ≤ (9/8)A²/ρ ≤ L, porque 1 − θ² ≥ 1 − θ ≥ ρ.
- d(1) ≥ 1, y Cauchy da las cotas de d^{(i)}(1).

**Lema 3(c)** (W4/01:133–136).
- Hay a lo sumo C(2K, s) ≤ (2K)^s/s! conjuntos y (2E − 1)!! emparejamientos.
- Con l ≤ 2, d_i ≤ 6 y \|a_d\| ≤ 1.
- Como E = s + l, la potencia de K es K^{s−E} = K^{−l}.

**Comprobación exacta propia** (c3).
- r es racional, con r²I − BᵗB semidefinida comprobada por LDLᵀ exacta.
- En 5 matrices (K = 2, …, 5, una con ceros) y 13 puntos (y = 1 y 12 puntos racionales gaussianos de ∂Ω) se cumplen todas las cotas:
  - ‖(I + O)^{−1}‖ ≤ 1/ρ, por semidefinición de la inmersión real;
  - Hᵗ = H y \|H_ij\| ≤ c_H/K;
  - e^{−L′} ≤ \|d\| ≤ e^{L′}, con L′ = (9/8)A²/(1 − θ²) ≤ L, usando cotas de Taylor de la exponencial;
  - d(1) ≥ 1 y \|d^{(i)}(1)\| ≤ i! e^L ρ^{−i};
  - \|W_l\| ≤ C_l K^{−l}.
- **Holgura:** max K\|H_ij\|/c_H ≤ 0,30; las cotas de W_l tienen cinco o más órdenes de margen.

**Veredicto: correcta.**

### 2.6 Punto 6 · Ningún uso de Divoux–Wang

**Menciones de DW.** Las del LaTeX son W4/01:1 y 30, W4/02:69, W4/03:79, 82 y 91 y `main.tex`:12. Ninguna usa un resultado de DW.

**Las cuatro herramientas de U01:37–39.** W4/03:84–89 las identifica con lo que rehízo E1:
- la identidad de mezcla: 01m:56–58 y E1:86;
- la fórmula de Wick: 01m:35–42 y E1:75;
- la cota en módulo con Cauchy: 01m:23–32, 51–53 y E1:74, 77;
- la cola gamma ponderada: 01m:59–66 y E1:87–91.

E1:232 y WG:142 lo confirman.

**Lo que sustituye a DW.** La cota (8) de DW, sobre las entradas del propagador, la sustituye el Lema 1(a). La suma del Lema 3.7 y de la suma binomial la sustituyen el Lema 3(c) y el enunciado de U01. La extracción Wp:32–66 no interviene.

**Las citas de Wp.** Wp:39–40 sólo se cita por los valores a₃ y a₄, que son elementales (c1). Las demás citas de Wp (9–11, 15–30 y 73–75) son el enunciado, las definiciones y los momentos.

**Las demás citas.** Comprobé todas las de W4/01–03; cada una dice lo que se le atribuye. Ejemplos: U01:19–20, 25 y 43; U04:24–30, 44–46 y 55; U03:26–27, 30–40 y 47; E1:19–21, 31–101 y 93; W2c:219–227; W2t:106 y 122–128; WG:139–142, 168 y 191–205.

**Veredicto: correcta.**

### 2.7 Punto 7 · Uniformidad en cada uso

| Uso | Clase que da el autor | Comprobación |
|---|---|---|
| S02–S03: D (W4/03:39–42) | 𝒟_j(max(4C, 1), 1 − γ_T/2) para j ≥ j_D | W2d:57, 84 y 212. A = max(M, 1) sale de \|B_ij\| ≤ max(D_ij, 1/K), que rehíce. **Correcto.** |
| S02–S03: D′ (W4/03:43–44) | 𝒟_{j−2}(A′, (1 + r′)/2) para j ≥ j₁ | S02:31–32 da r′ ≥ ‖G‖, con r′ ≤ ‖D − J‖; S02:43–47 da max D′ = O(1/k) y ‖D′ − J‖ ≤ r′ + O(1/k). **Correcto.** |
| Telescopio, 04m:58–64 (W4/03:45–48) | Clase común; K ∈ [j − 2d − 2, j] | R05:13–23 da un déficit de márgenes y una pérdida de brecha O(d/j) para d ≤ A₀ log j/log log j. **Correcto, con precisión 7a.** |
| E01 (W4/03:50–53) | 𝒟_k(max(2M, 1), (1 + r)/2) para k ≥ k₀(M, r) | R1m:5–7: D = P(1 + O(1/K)) en el soporte y ‖D − P‖_HS = O(1/K). Las constantes de C 7.3 son de clase (W2d, punto 4). **Correcto.** |
| K08, replicación (W4/03:56–61) | La misma clase; K = bk no acotado | D^{(b)} − J = B ⊗ Π_b conserva el máximo escalado y la norma. Comprobado en exacto en c5 con el polinomio característico. La uniformidad en K es esencial, y el Teorema la da. **Correcto.** |
| K08, menores con hasta cuatro supresiones (W4/03:62–65) | Clase heredada; K ∈ [k − 4, k] y sus replicaciones | D04:52–63, K02 y U02:34–45 (W2t:148–159 y 225). **Correcto.** |
| M01 (W4/03:67–68) | Como el anterior | MM07:2–14 y W2t:225. **Correcto.** |
| GI02 (W4/03:69–71) | r′ común si v/j es pequeño; también con v ≤ 8 log n | GI02:4–5 (orden fijo), U02:44–45 y W2_t4 para v ≤ 8 log n (WG:56). C_* no depende de v. **Correcto.** |

**Datos sólo reales** (W4/03:73–76). Las prolongaciones complejas no usan el Teorema:
- φ en μ_h (MM07:16–44);
- Γ_z en discos (K08:19–20);
- H_*.

El resto O(s³) de K07:54–55 sale de U04 con q = 2 (W2t:106), no del Teorema. **Correcto.**

**Orden de constantes.** C_* es de clase y se fija con los márgenes (W4/03:25–27; V2/consolidado/CONSTANTES.md:3–4), antes que b, ρ, α y n. Todo es determinista en una matriz fija: no interviene la ley ν.

**Evidencia para K08.** Las familias por bloques de c4 son exactamente replicaciones de una base c × c, y K²·ε_K queda acotado cuando n → ∞.

**Precisión 7a.** Un menor que prescribe d sitios tiene tamaño j − d, y su menor de dos sitios, j − d − 2. El rango es [j − d − 2, j − d], no [j − 2d − 2, j] (W4/03:48). Lo escrito lo contiene, así que no afecta a nada.

**Precisión 7b.** La lista de actas que certifican la pertenencia a la clase (EST:50) omite E1, que es la que certifica U02.

**Veredicto: correcta con precisión.**

### 2.8 Punto 8 · INTEGRACION.md

**Número.** A1–A7, B1–B16 y C1–C9 suman 32 cambios.

**Referencias de línea.** Comprobé las 32 contra los archivos (v2 34/34 y CI 14/14 en sus manifiestos; r21 y r19 en el suyo). Todas son exactas:
- 04m:16–18 y 72 son idénticas en r21 y en V2;
- DIVOUX_WANG.md de r21 y de V2 sólo difieren en la línea 3 (A7);
- E01:36–37 corresponde a la línea original 29–30 de la ronda 8;
- U01:36–44 y U03:11 / U04:13 corresponden a las líneas originales 29–37 y 4 / 6;
- FUENTES.md:5 es la fila de DW;
- TEO:3, MAPA:15 y 44, 00:4–5, CONTINUAR:5, PREF:40–42, coeficiente/03:6–8, CI/00_teorema:7–8, CI/LEEME:16–17, CI/ACTA_ADVERSARIAL:40–41, CI/INFORME:18–19 y CI/MAPA_CIERRE:15 y 44 dicen lo que se les atribuye;
- en r21: MAPA:16, TEOREMA:11, CAMBIOS:11, ACTA_ADVERSARIAL:12 y GUIA:9;
- C1–C9: Wp:12–14 y `r21/fuentes/latex/Wpermanente.tex`, S03:10 y 15, E02:17, R1m:27–28, K06:2, K07:54–55, D04:62–63, `prueba_fuente.md`:308 y 374, enunciados 02:168 y 03:14, y torres_fila:4–36.

**Contenido.**
- Las sustituciones propuestas son correctas.
- El texto D (INT:68–82) describe bien el nuevo estado.
- La sección E (INT:86–91) es correcta: la arista DW → N6 se sustituye por N1 → N6, que ya existe (WG:191–192), así que el grafo sigue acíclico. D2 lo descargó W3x:11.

**Cotejo con W3v2:187–224.**
- *Dónde se declara DW* (W3v2:207): DWm:5–14, MAPA:15, 00:4–5, TEO:3, 06:14 y PREF:40–42. Están en A6, B2, B4, B1, B16 y B9.
- *Dónde se usa directamente:* 04:6–8, 16–18 y 72. Están en A1–A2; 04:6–8 no nombra DW.
- *La vía de E01:* está en A3, C3, C5 y C6.

**Precisión 8a: no reescribir originales sellados.**
- A3, A4 y A5 proponen cambiar el texto de originales con manifiesto:
  - `fuentes/…ronda8…/latex/01_enunciado.tex`:29–30;
  - `fuentes/…menores_uniformes…/latex/01_enunciado.tex`:29–37, `03_wick.tex`:4 y `04_mezcla.tex`:6, y `FUENTES.md`:5.
- Pero INT:10 declara que las transcripciones son literales y no se modifican.
- Aplicar A3–A5 a los originales rompería sus manifiestos (30/30 y 14/14) y la identidad entre transcripción y original, que comprobé en c0.
- Deben tratarse como C1–C9: como anotaciones en el consolidado, el MAPA o el catálogo, o como una versión nueva de la pieza con su propio manifiesto. El encargo del autor pedía «qué hay que cambiar para citar la nueva prueba» (`encargos/W4_d1_autor.md`:35–40), no reescribir originales.

**Precisión 8b: lugares sin cambio.** W3v2:182 y 299 señalan además [V2]LEEME.md:7, [V2]ACTA_ADVERSARIAL.md:35 y 06:6–7. No nombran DW. Con B1–B4 aplicados, quedan exactos respecto de D1. INT debería listarlos como «sin cambio», igual que hace con B16.

**Precisión 8c: la redacción de B1.** B1 conserva «allí indicados», que sigue siendo inexacto mientras MAPA no enumere los resultados de B y C (W3v2:57, 175 y 303). Mejor la redacción de W3v2:224 y WG:321: «condicional sólo a B, C y herramientas estándar», junto con la lista de WG §2.7.

**Precisión 8d: la redacción de A4.** «Demostradas en U02–U04» sólo es exacto si se aplica también A5, porque U03:11 y U04:13 citan DW. Las pruebas sin DW de las dos cotas en módulo están en 01m:23–32 y 59–66. E1:232 usa la misma fórmula, así que basta añadir la referencia a 01m.

**Sobre EST.**
- Los recuentos son exactos: 137, 72 y 91 líneas.
- Se cumplen las restricciones del encargo del autor: como máximo 107 caracteres por línea, contados como caracteres, y ninguna aparición de la palabra excluida.
- Las afirmaciones de EST §1–§4 y §6 son correctas.
- La tabla de EST §5 coincide con `resultados/` y sus tiempos.
- El «punto que conviene que confirme el revisor» (EST:47) queda confirmado en el punto 2.

**Veredicto: correcta con precisión** (8a–8d).

### 2.9 Punto 9 · Cálculos

Están descritos en §3.

**Mi código es independiente del del autor.**
- La integral de U03 es literal, con pesos 1/K y núcleo K·H.
- W_l se suma por conjuntos, sin el factor s!.
- Los a_d salen de la exponencial de la serie logarítmica.
- Los permanentes se calculan por programación dinámica y se validan con Ryser.
- Uso números complejos racionales.

**Cotejo con los resultados del autor.**
- Mi familia F3z es la F3c del autor con las filas de bloques permutadas, que deja invariantes el permanente, BᵗB y V. Reproduce sus valores de K²ε y Kε_sinV (`W4_d1/resultados/c4_familias_bloques.txt`) a las cinco cifras decimales que imprimo, en los 11 valores de K comunes (c6). Eso valida los dos códigos.
- Las otras tres familias son nuevas. F3m es escalado exacto de su máscara (con ceros); F2b, F3a y F3z no lo son de ninguna.

**Veredicto: realizados; evidencia favorable, no prueba.**

## 3. Cálculos realizados

Se ejecutaron con `codigo/ejecutar.sh`: `nice -n 10 python3 -I -B`, un proceso cada vez, con el tiempo medido. Las salidas están en `resultados/`, y los tiempos en `resultados/*_tiempo.txt`.

| Programa | Qué comprueba | Resultado | Tiempo real |
|---|---|---|---|
| `c0_cotejo.py` | Manifiestos SHA256; transcripciones frente a originales; huellas de W4_d1 | 0 discrepancias; 15/15 transcripciones idénticas | 0,08 s |
| `c1_lema3.py` | Lema 3: fórmula literal de U03 frente a W_l y a V de Wp; Möbius para n ≤ 6; 3, 9 y 6; a_d; estructura en u; controles negativos | 31 casos (25 de exceso uno y 6 de exceso dos, con y complejo y una D con ceros), 0 fallos; los controles fallan | 19,3 s |
| `c2_momentos.py` | Lema 2: formas cerradas, recurrencia = K07, momentos exactos para 6 ≤ K ≤ 120, cota 32u² | 0 fallos; 128/21, 64/5, 3328/105 | 0,17 s |
| `c3_cotas.py` | Lema 1 y Lema 3(c) en 5 matrices × 13 puntos, con r racional certificado | 0 fallos; holgura en §2.5 | 24,8 s |
| `c4_familias.py` | Cuatro familias por bloques, K hasta 120 (c = 2) y 60 (c = 3); permanentes exactos; ε_U, E₂/d, ε_T, control sin V | Validaciones e identidad de E₂: OK | 50,1 s |
| `c5_replicacion.py` | Replicación de K08: bistocástica, max escalado, polinomio característico, det(I − G) | OK | 0,10 s |
| `c6_cotejo_c4.py` | Las dos ejecuciones de c4 coinciden en los K comunes; F3z frente a la F3c del autor | Idénticas; coincidencia a 5 decimales en 11 K | 0,04 s |

Tiempo total: 155 s, incluidas la ejecución fallida de c2 y la primera de c4.

**Lectura de c4.** La tabla da el valor en el mayor K calculado.

| Familia | ¿Escalado exacto de máscara? | K²·ε_T (Teorema) | K·ε sin V (control) | K³·ε_U (U01, q = 2) |
|---|---|---|---|---|
| F2b (c = 2, a = 2/3, r = 2/3) | no | −2,10 (K = 120) | −1,89 | −1337, decreciente |
| F3a (circulante, r = 1/3) | no | −0,755 | −0,343 | −12,6, decreciente |
| F3m (con ceros) | sí | −2,800 | −2,202 | −1490, decreciente |
| F3z (con ceros) | no | −6,645 | −3,259 | −5915, decreciente |

- **El enunciado.** K²·ε_T es acotado y estable en las cuatro familias: es evidencia del Teorema, también para D que no son escalado de máscara. Sin V, el error es de orden 1/K.
- **U01 con q = 2.** El error ε_U tiende a cero; K³·ε_U pasa por un máximo y decrece en todas las familias.
- **E₂.** K²·E₂/d se acerca a un límite finito en F3a (−0,27 en K = 60) y decrece en las demás, que siguen en fase transitoria. Es coherente con unas constantes enormes, admisibles en un enunciado existencial.

**Incidencias.**
- La primera ejecución de `c2_momentos.py` falló (0,05 s) por un error mío: un factorial de un número negativo para K < 7. Lo corregí y repetí.
- `c4_familias.py` se ejecutó dos veces. La primera, con K ≤ 40, tardó 60,2 s; la conservo en `resultados/c4_familias_primera*.txt`. La segunda amplió el rango de K; en los K comunes sus valores son idénticos a los de la primera (c6).
- No ejecuté el código del autor.

## 4. Demostrado, condicional y numérico

**Demostrado.** Rehíce cada paso a mano:
- los Lemas 1–3;
- los pasos 0–3 y la constante C_*;
- la reducción de U03 a la suma de índices distintos;
- la uniformidad para todo K ≥ 2.

**Condicional.** Son entradas certificadas por otras actas:
- U01 con q = 2 y h = v = 0: E1 (puntos 1–3) y W2c:219–227. Su alcance para D general está comprobado aquí (punto 2a).
- La pertenencia a la clase en cada uso: W2d, E2, W2t, W2_pares y W2_t4, más E1 para U02.
- Herramientas estándar: van der Waerden (Egorychev–Falikman), desigualdades de Cauchy, función de Möbius del retículo de particiones, unicidad del escalado de Sinkhorn y Wick/Isserlis formal (ya en E1).

**Numérico.** c1–c5 son identidades exactas en casos finitos y evidencia de las cotas. No miden la uniformidad en toda la clase.

## 5. Dictamen global sobre mi parte

**CERTIFICADA, con precisiones no bloqueantes. D1 queda descargado.** W/permanente se sostiene:
- con su enunciado literal;
- con C_*(A, r) uniforme para todo K ≥ 2;
- desde U01 con q = 2 y herramientas estándar;
- sin ninguna cota ni resultado de Divoux–Wang.

Junto con W3_xi (D2), queda cumplida la condición de WG:321 para estos dos huecos. El estado documental de v2 sigue sujeto a las correcciones C1–C6 de W3_v2 y a aplicar INTEGRACION con las precisiones 8a–8d.

**Precisiones.** Ninguna es un hueco ni cambia enunciados o constantes.
- **2a.** Declarar que el Teorema para D general usa U01 con h = v = 0 leído según 01m:4, como hace W4/01:49–56, o enunciarlo para escalados exactos de máscaras, que cubren todos los usos.
- **2b.** W4/01:53–54: la cota de núcleo de 01m:48 se necesita en \|yw\| ≤ r₁(1 + d₀), no en Ω. El argumento del Lema 1(a) la da con 1 − r₁(1 + d₀)r en lugar de ρ.
- **7a.** W4/03:48: el rango de tamaños es [j − d − 2, j − d]; lo escrito lo contiene.
- **7b.** EST:50: añadir E1 (U02) a las actas de clase.
- **8a.** A3–A5: anotar en el consolidado, el MAPA o el catálogo, o versionar la pieza; no reescribir originales sellados.
- **8b.** Listar [V2]LEEME.md:7, [V2]ACTA_ADVERSARIAL.md:35 y 06:6–7 como «sin cambio tras B1–B4».
- **8c.** B1: usar la redacción de W3v2:224 y WG:321 y añadir la lista de B y C.
- **8d.** A4: citar 01m:23–32 y 59–66 junto a U02–U04.

## 6. Resumen final

```
W4_rev · D1: corrector O(K^-2) del permanente sin Divoux–Wang · revisión externa · 2026-11-17
Integridad: r19 116/116, menores 14/14, R8 30/30, R9 98/98, MM 14/14, GI 12/12, v2 34/34 y
14/14; R1, R10 y r21 parciales sin discrepancias; 15/15 transcripciones idénticas al original.
Punto                                            Veredicto
1 Teorema = Wp:25-29; C_*(A,r) para todo K>=2    Correcta
2 U01 con q=2, h=v=0 (alcance; basta en usos)    Correcta con precisión (2a, 2b)
3 Desarrollo de H_2(1/K), mu_i, V_2, Cauchy       Correcta
4 Lema 3: V_1(y,1/K) = V(y) exacto               Correcta
5 Cotas |H_ij|, |d|, |W_l|                        Correcta
6 Sin Divoux–Wang (citas comprobadas)            Correcta
7 Uniformidad: S02-S03, E01, K08, M01, GI02      Correcta con precisión (7a, 7b)
8 INTEGRACION (32 cambios)                       Correcta con precisión (8a-8d)
9 Cálculos propios c0-c6                         Evidencia favorable, 0 fallos
Hallazgos:
- Con h=v=0, la prueba certificada de U01 (01m:12-83; 01m:4 para D bistocástica)
  sólo usa B1=B^t1=0, ||B||_HS<=A, la brecha, el núcleo acotado y D>=0. La máscara
  sólo entra en el balanceo de menores, vacío aquí. Además, todos los usos aplican
  el Teorema a escalados exactos de máscaras (S02, D', telescopio, E01, K08, M01, GI02).
- Lema 3: Möbius en el retículo de particiones de un mismo lado deja sólo índices
  distintos; el factor s! cuadra; exceso uno = (1,2,(4)) y (2,3,(3,3)) con 3, 9 y 6;
  el término en u^2, -(5/6)K^2 sum H_ii^3, anula la diagonal en u=1/K.
- Constantes explícitas en (A,r); paso 0 para K<K_*; C_* de clase, antes que b,rho,alpha,n.
- K08: D^(b)-J = B (x) Pi_b conserva la clase; la uniformidad en K=bk se usa y está.
- INTEGRACION: las 32 referencias son exactas y cubren W3v2:187-224. Precisiones:
  8a A3-A5 no deben reescribir originales sellados (manifiestos 30/30 y 14/14; INT:10);
  8b listar LEEME:7, ACTA_ADV:35 y 06:6-7; 8c B1 sin «allí indicados»; 8d A4 con 01m.
Cálculos (nice -n 10, uno cada vez, 155 s): c1 Lema 3 con la fórmula literal de U03,
31 casos con y complejo; c2 momentos; c3 cotas en ∂Omega con r certificado; c4 cuatro
familias por bloques con permanentes exactos (Ryser): K^2·eps acotado (-2,10, -0,755,
-2,800, -6,645), incluidas tres D que no son escalado de máscara; sin V es O(1/K);
c5 replicación exacta; c6 F3z = F3c del autor a 5 decimales. Evidencia, no prueba.
Ningún hueco de prueba ni enunciado falso.
Dictamen: CERTIFICADA con precisiones no bloqueantes; D1 queda DESCARGADO. Con D2 (W3_xi),
se cumple WG:321, sujeto a las correcciones documentales de W3_v2 y a aplicar INTEGRACION.
ACTA: rev_exp/W4_rev/ACTA.md
```
