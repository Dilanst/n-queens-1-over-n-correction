# Acta de revisión externa W2 · Recuento ponderado de tipos, lema de rango y media por grados

**Revisor.** Externo e independiente, ajeno al proceso que escribió la prueba. Fecha: 2026-11-17. Sin web y sin acceso a otros equipos; sólo esta carpeta. Cálculos propios y exactos, con `nice -n 10`, un proceso cada vez y tiempos medidos. No reviso E1 ni E2.

**Integridad.** Comprobé los manifiestos:
- `velocidad_via2_grados_ponderados…/SHA256SUMS`: 12 de 12 correctos;
- `velocidad_via2_patrones_finitos…/SHA256SUMS`: 12 de 12;
- `rev_exp/r19/SHA256SUMS`: 116 de 116.

Las transcripciones G01, G05, G06, G07, P01, P03, P04, P05 y P06 del expediente coinciden con las fuentes completas, salvo los finales de línea.

**Convenciones de cita.**
- [Gnn] es `rev_exp/fuentes/velocidad_via2_grados_ponderados_20261117T021217Z/latex/nn_*.tex` y [Pnn] es `rev_exp/fuentes/velocidad_via2_patrones_finitos_20261116T164355Z/latex/nn_*.tex`. Los números son líneas del propio archivo.
- [H01], [H02], [H03], [B02], [B03], [B05], [A02] y [V] son las transcripciones de `rev_exp/r19/expediente/originales/`. Los números son líneas originales; en el `.md`, súmese 7.
- [06c] es `rev_exp/r19/expediente/latex/06_corte.tex`, [TEO] es `expediente/TEOREMA.md` y [MAPA] es `expediente/MAPA_DEPENDENCIAS.md`.

**Notación.** Un *tipo* es la cuaterna de particiones de los v sitios etiquetados (filas, columnas, diagonales y antidiagonales). Sus igualdades son n_f·(P_i − P_k) = 0, con normales (1,0), (0,1), (1,−1) y (1,1), dos a dos no paralelas.
- β_g es el número ciclomático de la componente g del grafo de incidencia sitio–línea; β = Σ_g β_g.
- L_g es el exceso de rango de la componente g, de modo que su rango es v_g − 1 + L_g.
- D es la dimensión del espacio de soluciones en las 2v coordenadas.
- h es el número de índices RC distintos.
- p vale v+c+1, v+c o v+c−1 según β = 0, 1 o ≥ 2.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Naturaleza del resultado |
|---|---|---|---|
| 1 | Lema de rango: L_g ≥ mín(β_g,2) y D ≤ p−1 para todo tipo realizable, con varios ciclos o varias componentes [P06] | **Correcta** | Demostrado: rehíce cada paso. Verificado además por enumeración exhaustiva hasta v = 6. |
| 2 | Radios κ′/d_i por casilla y factor ∏d_i por Cauchy, uniformes para v ≤ 8 log n [G02, G05] | **Correcta con precisión** | La deducción es correcta y uniforme. Es condicional a entradas analíticas importadas: la holomorfía y la cota e^{O(v)} en el polidisco, y los órdenes de anulación en s. |
| 3 | Recuento ponderado (1/v!)Σ∏d_i ≤ C^v(4v²)^{L_s}/c!, con L_s ≤ p−D+1, y su uso en G07 [G06, G07] | **Correcta con precisión** | Demostrado. Falta en el texto una línea, d+b−1 ≥ (v−4)/3, que doy aquí. El factor (4v²)^{L_s} es imprescindible. |
| 4 | Prescripciones: masa ≤ δ^{−2v}(j/n)^h exp(C_L v²/j) bajo ν con indicador H_j [H02, H03] | **Correcta** | Demostrado como implicación de la transición de B–C, que es una entrada publicada y no la reviso aquí. |
| 5 | Suma final (C_L/n)(C₁δ⁻²)^v v^a δ_*^{(v−4)/3}: convergencia, C₁ independiente de b y ρ, orden de constantes [B03, H03, 06c] | **Correcta con precisión** | Demostrado. Las precisiones son de notación y de orden, sin consecuencias. |
| 6 | Pruebas pequeñas por ordenador | **Realizada** | Numérica y exacta. Ninguna violación; constantes efectivas moderadas. |

No encontré ningún enunciado falso ni ningún hueco en mi parte. Las precisiones de los puntos 2, 3 y 5 no exigen cambios en la prueba.

## 2. Detalle por punto

### Punto 1 · Lema de rango [P06 2–42]

**Reducción a árboles de línea** [P06 2–6]. Cada línea con m ≥ 2 sitios se sustituye por un árbol de m − 1 aristas. La sustitución conserva:
- el espacio generado por las igualdades;
- las componentes;
- el número ciclomático, porque Σ_ℓ(m_ℓ − 1) − v + c coincide con E − V + c del grafo bipartito.

Las líneas con un solo sitio son hojas y no cuentan. El grafo resultante es simple, porque dos sitios distintos comparten a lo sumo una línea.

**Paso clave** [P06 10–25]. Una dependencia lineal asigna pesos λ_e a las aristas con Σ_{e∋i} ±λ_e n_{f(e)} = 0 en cada sitio. En su soporte:
- no hay hojas, porque λn = 0 obliga a λ = 0;
- en un vértice de grado 2, las normales son paralelas, luego hay una sola familia y una sola recta por el sitio [l. 13–14];
- un camino maximal de vértices de grado 2 está en una recta y |λ| es constante a lo largo de él, así que se suprime;
- una componente formada sólo por vértices de grado 2, o un lazo, sería un ciclo dentro del árbol de una línea [l. 16–17];
- dos aristas reducidas paralelas serían dos caminos rectos entre dos sitios distintos u, w; como u y w comparten a lo sumo una recta, ambos caminos están en el mismo árbol y cerrarían un ciclo [l. 18–19]. *Aquí se usa la realizabilidad con sitios distintos.*

El grafo reducido es simple, de grado mínimo ≥ 3 y con V ≥ 4, luego E − V + 1 ≥ V/2 + 1 ≥ 3 [l. 20–22]. Como el número ciclomático es monótono al pasar a subgrafos, un árbol generador con ≤ 2 cuerdas tiene ecuaciones independientes. Por tanto L_g ≥ mín(β_g, 2). Para β_g ≤ 2 hay igualdad, porque el rango no supera el número de aristas, v_g − 1 + β_g.

**D ≤ p−1** [P06 28–37]. Se tiene D = v + c − Σ_g L_g.
- β = 0: D = v + c = p − 1.
- β = 1: una sola componente tiene β_g = 1, así que ΣL_g = 1 y D = p − 1.
- β ≥ 2: Σ_g mín(β_g,2) ≥ 2, porque o bien algún β_g ≥ 2 o bien hay dos componentes cíclicas. Luego D ≤ v + c − 2 = p − 1. Esto cubre los tipos de varias componentes: cada componente cíclica aporta al menos 1.

Es exactamente la ganancia Σ_g mín(β_g,2) que cita [V 26]. El paso posterior «h < p ⇒ D ≤ h−1» [P06 38–40] también es correcto: una igualdad diagonal entre sitios distintos involucra cuatro variables RC distintas.

**Optimalidad.** El mínimo con 2 no se puede mejorar. Los cuatro vértices de un cuadrado de lados paralelos a los ejes forman un tipo con:
- filas {a,b} y {c,d}, columnas {a,c} y {b,d}, diagonal {a,d} y antidiagonal {b,c};
- β = 3, pero la igualdad diagonal y la antidiagonal dan la misma ecuación R₂−R₁ = C₂−C₁;
- D = 3, L = 2 < β y D = p − 1, b = 0.

En general D_g ≥ 3 en cada componente con ≥ 2 sitios, por traslaciones y homotecia. Por eso la clase β ≥ 2 sólo puede ganar 2, y p = v+c−1 es justo lo que el rango permite.

**Comprobación exacta** (punto 6). Enumeré todos los tipos etiquetados realizables hasta v = 6: 14 920 286 tipos, de los cuales 5 760 tienen ≥ 2 componentes cíclicas.
- No hay ninguna violación de L_g ≥ mín(β_g,2), de la igualdad para β_g ≤ 2 ni de D ≤ p−1.
- L < β sólo aparece con β ≥ 3. Para v = 4 son 24 componentes con β = 3 y L = 2: el cuadrado y su análogo girado 45°, 12 etiquetados de cada uno. Para v = 6 el caso extremo es β = 6, L = 4.
- El rango 2v − D coincide con una eliminación gaussiana independiente con fracciones en los 153 597 tipos con v ≤ 5.

### Punto 2 · Radios por casilla y factor ∏d_i [G02, G05; uso en B02 52–58 y B03 39–58]

- **Fibras.** Se tiene Σ_{i∈f∩U} 1/d_i ≤ 1, porque d_i ≥ |f∩U| para cada i ∈ f [G02 6–9]. De ahí:
  - |t_b − 1| ≤ a Σ1/d_i ≤ a [G02 12–13];
  - la carga de cada fibra es Σ_{l∈f}|ζ_l| ≤ κ′, y la de una vecindad es ≤ 4κ′, porque N(i) está contenido en las cuatro fibras de i [G04 7–10].
- **Derivadas cruzadas** [G02 43–47]. Con h_l = e^{iθ_l}/d_l se tiene ‖h‖_* = 1, y Cauchy en el parámetro escalar sobre |λ| ≤ a/2 da Σ_l|∂_l∂_iR_c|/d_l ≤ 2B/a. Es correcto y no pierde el número de vecinos.
- **Silla local** [G02 49–56]. En la norma ponderada, d_i|lado derecho| ≤ Cκ′ y la norma de operador del jacobiano, máx_i d_iΣ_l|J_il|/d_l, es ≤ Cκ′. Por tanto hay contracción para κ′ pequeño.
- **Determinante** [G02 57–61]. Al multiplicar la Hessiana a la derecha por diag(x(1−x)), las sumas por fila quedan ≤ C‖x‖_*. Entonces |log det(I+Δ)| ≤ vΣ_k‖Δ‖^k/k ≤ 2v‖Δ‖_∞, usando |tr A| ≤ v‖A‖_∞.
- **Cauchy** [G05 6–17].
  - H = [U]e está acotada por 2^v M y se anula en cada cara ζ_i = 0 [G05 7–8; P05 38–40].
  - Los coeficientes con todos los exponentes ≥ 1 están acotados por 2^vM∏R_i^{−α_i}, con R_i = κ′/d_i.
  - Para |ζ_i| ≤ C/j la suma es ≤ 2^vM∏(2Cd_i/(κ′j)), siempre que Cd_i/(κ′j) ≤ 1/2.
  - Una repetición cuesta Σ_i Cd_i/j ≤ Cv²/j.
  - En s, con radio κ/v, la cola desde el orden w es ≤ 2(v/(κj))^w si v/(κj) ≤ 1/2.
- **Exponentes.** Con los órdenes de partida (bosque, w = c+1; un ciclo, w = c con el jet c−1 repetido; varios ciclos, w = c−1) [G05 19–22] salen p = v+c+1, v+c y v+c−1, con prefactor ≤ C^v(Cv)^{c+1}. El error físico es e^{Cv}Δ_q, con Δ_q ≤ j^{−(2v+6)} ≤ j^{−(c+1)} [G05 22–23; G04 36–44]. Así se obtienen las cotas de [G05 24–28] y [B03 55–58].
- **Uniformidad.** κ, κ′, B₀, B₁, K₁ y C no dependen de v. Las condiciones usadas son:
  - v/j ≤ κ/2;
  - Cd_i/j ≤ κ′/2, con d_i ≤ v;
  - Cq ≤ √j, con q = 4v+12;
  - e^{Cv}Δ_q < 1/2.

  Todas valen para v ≤ 8 log n y j ≥ √n, con n grande; en el expediente j = ⌊bn⌋.
- **Por qué importa el radio por sitio.** Con un radio común κ′/v, Cauchy daría (Cv/j)^v, un factor v^v que ningún recuento compensa. Con κ′/d_i sale ∏d_i, que el recuento sí compensa (punto 3).

**Precisión.** Lo verificado aquí es el mecanismo de radios, Cauchy y uniformidad. Son entradas importadas, con su revisión interna [G ACTA_ADVERSARIAL 7–8], y quedan fuera de mi encargo:
- la existencia y acotación del equilibrio exterior y del cofactor para v|s| ≤ κ [G02 19–24, G03];
- el gas [G04];
- las cancelaciones algebraicas que fijan el orden inicial en s [G05 18–19; P03–P05; B02–B03].

### Punto 3 · Recuento ponderado de tipos [G06 1–48; uso en G07 2–21]

**Consecuencias elementales** [G06 6–13]. Se definen d = h−D, b = p−D−1 y L_s = (2v−D)−(v−c) = Σ_g L_g.
- b ≥ 0 por el punto 1.
- L_s ≤ b+2 equivale a p ≥ v+c−1. De hecho L_s − b vale 0, 1 o 2 según β = 0, 1 o ≥ 2.
- d ≥ 1. Un sitio sin vecino diagonal anula el coeficiente [G05 30–31; P01 43–46]. Una igualdad diagonal entre sitios distintos es una ecuación no trivial en las h variables RC.
- h ≤ 4d. d es el rango de las igualdades diagonales en esas variables. Una base escogida entre ellas cubre todas las variables, porque cada una aparece con coeficiente ±1, y cada ecuación tiene ≤ 4 variables.

**Paso omitido** («Así d+b−1 ≥ (v−4)/3» [G06 13]). Es cierto, y se deduce así:
- de h ≤ 4d sale D = h−d ≤ 3d, luego d+b = d+p−D−1 ≥ p−1−2d;
- junto con d+b ≥ d, se obtiene 3(d+b) ≥ p−1 ≥ v+c−2 ≥ v−1.

Es una omisión de redacción, no un hueco. La cota es óptima en v = 4: el cuadrado tiene h = 4, D = 3, d = 1 y b = 0.

**La cuenta** [G06 14–48]. Rehíce el argumento:
1. Al asignar a cada sitio una fibra donde alcanza d_i, se tiene exactamente ∏_i d_i = ∏_f D_f^{a_f}. Las estrellas son disjuntas.
2. El bosque de estrellas y conexiones tiene v−c ecuaciones independientes, por eliminación de hojas. Bastan L_s igualdades del tipo para completar una base: hay ≤ (4v²)^{L_s} elecciones, e incluso (2v²)^{L_s} bastaría.
3. El tipo es el conjunto de igualdades por pares contenidas en el espacio generado [l. 31–33]. Esto exige que el tipo sea la pauta *exacta* de una realización, lo que la nota impone [l. 5].
4. Hay ≤ C₀^{2v+1}v! árboles planos con ≤ 2v+1 nodos, alfabetos acotados y v sitios etiquetados.
5. Cada tipo tiene al menos c!·∏_f(a_f−1)! códigos distintos: las permutaciones de los hijos de la superraíz y de cada nodo estrella. Los hijos son sitios etiquetados, y exactamente un miembro de cada estrella es su padre. Tipos distintos dan códigos distintos.
6. D^a/(a−1)! = aD^a/a! ≤ 2^a e^D y Σ_f D_f ≤ 4v.

Por tanto Σ_T ∏d_i ≤ (2^v e^{4v}/c!)·C₀^{2v+1}v!(4v²)^{L_s}, y al dividir por v! queda el enunciado. El 1/c! procede de la superraíz y se conserva hasta G07: allí compensa el (Cv)^{c+1} de la cota por soporte, porque v^c/c! ≤ e^v.

**Uso en G07** [G07 2–21].
- n^D x^h j^{−p} = n^{−1}x^{d−1}j^{−b}: comprobado.
- Por clase, la cota es ≤ (C_L/n)C^v(Cv)^{c+1}(4v²)^{L_s}x^{d−1}j^{−b}/c! ≤ (C_L/n)C₁^v v^5 x^{d−1}(v²/j)^b. Se usa (4v²)^{L_s} ≤ 16v⁴(4v²)^b y 4^b ≤ 16^v, porque b ≤ 2v.
- Hay ≤ Cv³ clases.
- Con x ≤ δ_* < 1, v²/j ≤ δ_* y d ≥ 1 sale δ_*^{(v−4)/3}. El factor v^a final tiene exponente fijo, por ejemplo a = 9.

**Precisión de alcance.** El recuento por sí solo no tiene base exponencial: el factor (4v²)^{L_s} es imprescindible.
- *Familia.* La cuadrícula k×k de casillas consecutivas, con v = k², tiene:
  - todo sitio con vecino diagonal;
  - β = 3(k−1)², D = 3, h = 2k, d = 2k−3, L_s = v−2 y b = v−4;
  - un grupo de automorfismos de orden 2.

  Sus tipos etiquetados aportan (1/v!)(v!/2)k^v = v^{v/2}/2 a la clase (c = 1, L_s = v−2). Ese crecimiento por grado es superexponencial.
- *Cobertura.* La familia queda cubierta por (4v²)^{v−2} en la cuenta. Su aportación a la suma de grado v es ≤ (C_L/n)C^v v^{2+v/2}x^{2k−4}j^{−(v−4)}, despreciable.
- *Consecuencia.* La base C^v aparece sólo al combinar la cuenta con j^{−b} y v²/j ≤ δ_*. Por eso el argumento se limita a v² ≪ j, lo que se cumple con v ≤ 8 log n y j ≍ n.

Numéricamente, en dos familias, la suma sin normalizar Σ_{c,L} W·c! crece más deprisa que cualquier exponencial: sus cocientes van de 5,2 a 11,1, con incrementos ≈ 0,86 casi constantes. La suma normalizada no lo hace.

No encontré ningún tipo ni familia de tipos sin cubrir.

### Punto 4 · Prescripciones bajo la historia [H02 5–26; H03 35–50]

**Cota de H02.** Rehíce la derivación.
- Filas: la siguiente es uniforme entre las k restantes [H02 5], de modo que el producto da (j)_s/(M)_s ≤ (j/M)^s.
- Columnas: al promediar p_rc(1+O(1/k)) sobre la fila uniforme, con columnas de suma 1, P(columna marcada) ≥ t/k − Ct/k² [H02 15–16].
- La intersección es ≤ (s/k)(Ct/k).
- Luego P(evitar) ≤ (1−s/k)(1−t/k)·exp(C′(st+t)/k²) para s, t ≤ j/2, y el producto de k = j+1 a M da (j/M)^{s+t}exp(C(st+t)/j) [H02 21–25].
- Matar en la salida sólo disminuye la masa, y no se divide por la probabilidad de llegada [H02 26].

**Paso a H03.**
- H_j ⊆ H_j⁰ ∩ S_M [H03 2–3; H02 13], y que las marcas estén vivas en M es F_M-medible.
- M = ⌈δn⌉ ≥ δn da (j/M)^h ≤ δ^{−h}(j/n)^h ≤ δ^{−2v}(j/n)^h, porque h ≤ 2v.
- st + t ≤ v² + v da el factor exp(C_L v²/j).
- El enunciado [H03 39–42] es, pues, correcto.

**Uso.** E_ν[1_{H_j}Σ_{U⊆A_j}|Δ_U|] ≤ Σ_{U⊆[n]²} B(U)·ν(H_j ∩ {índices de U vivos en j}).
- B(U) es la cota determinista por soporte. Sólo depende del tipo de U y de j, y vale en H_j porque allí la máscara está en la clase (entrada importada).
- No se condiciona en H_j ni se usa independencia [H03 44; B03 73–74].

**Entrada no revisada.** La transición p_rc(1+O(1/k)), bistocástica y con máx p_rc ≤ C/k en padres regulares [H02 5–10], viene de B–C.

### Punto 5 · La suma final [B03 64–74; H03 46–53; 06c 14–27, 47–68]

- **Cota por grado.** Es la de G07 con C₁ sustituido por C₁δ⁻². El factor δ^{−2v} viene del punto 4, y exp(C_L v²/j) ≤ e^{C_L} entra en el prefactor.
- **Serie.** Σ_{5≤v≤N}(C₁δ⁻²)^v v^a δ_*^{(v−4)/3} = δ_*^{−4/3}Σ r^v v^a, con r = C₁δ⁻²δ_*^{1/3} < 1. Es O(1), así que la aportación es O_{b,δ}(1/n).
- **C₁ no depende de b ni de ρ.** C₁ reúne:
  - la constante por soporte de la clase de referencia (márgenes y radios locales κ/v, κ′/d_i), sin ρ ni b [B03 59–60];
  - la constante combinatoria del recuento, que es absoluta;
  - 2^v, e^v y 16^v.

  ρ sólo interviene cualitativamente, al identificar la rama física [B02 57–58]. A02 fija C₁ antes de a, ρ, α, δ_* y b [A02 13–15, 24–31].
- **Orden de elección.** Es δ → clase (M₀, r, ε_D, κ, κ′, C_L, C_pres) y L = 8 → C₁ → a_d → ρ → α → δ_* → b → n. Así figura en [TEO 11], [MAPA 22], [06c 14–27] y [B05 14–19]. Es coherente: cada constante depende sólo de las anteriores.
  - G07 fijaba ρ₀ antes de L, con L > 4/log ρ₀ + 1 [G07 14–15]. El expediente fija L = 8 antes, y vale para todo ρ ≥ 2 porque 4/log 2 + 1 ≈ 6,77 < 8 [H03 52–53].
  - La condición adicional sobre δ_* para la excepción D∖D′ [G07 39] ya no hace falta: H_j impone L_max < ⌈αj⌉, con M₀α < η/(2ρ²) [H01 40–41].
  - x ≤ b < δ_* se cumple. v²/j ≤ δ_* sólo pide n ≥ n₀(b, δ_*), y n se toma al final.

**Precisión de notación.** «v^d» en [B03 68] y en [06c 56, 64] es un exponente fijo, el v^a de [G07 20] y [H03 48]. No es d = h−D [G06 7] ni d_i. Del mismo modo, el b de G06 no es la fracción b del corte, y los b_i de P06 son números ciclomáticos. No es un error.

### Punto 6 · Pruebas exactas por ordenador

Código propio en `rev_exp/W2_tipos/codigo/`, resultados en `resultados/`. Sin azar, aritmética entera exacta y una sola ejecución cada vez con `nice -n 10`.

**Enumeración en cuatro familias** (`tipos4.py` de referencia y `tipos4.c`).
- *Método.* Se genera cada tipo etiquetado realizable una sola vez, extendiendo su restricción a v−1 sitios. Se lleva una parametrización entera del espacio de soluciones, de modo que D es el número de parámetros. La realizabilidad exige que las formas de línea sean distintas en bloques distintos.
- *Contraste.* Las dos implementaciones coinciden en v ≤ 5: los recuentos, la distribución de (β_g, L_g) y las sumas.

**Prueba en dos familias** (`tipos2.c`). Aquí un tipo es un par de particiones con encuentro trivial y no hay dependencias, de modo que L_s = β.

**Análisis** (`analiza.py`). Con Fraction calcula W(v,c,L_s) = (1/v!)Σ∏d_i y R = W·c!/(4v²)^{L_s}.

| Cálculo | Alcance | CPU medida |
|---|---|---|
| `tipos4.py 5 --verif-rango 5` | 4 familias, v ≤ 5, 153 597 tipos; rango contrastado con Fraction | 33,2 s |
| `tipos4 5`, `tipos4 6` | 4 familias, v ≤ 6, 14 920 286 tipos | 0,23 s y 23,4 s |
| `tipos2 8`, `tipos2 10` | 2 familias, v ≤ 10, 3,10·10⁹ tipos | 0,41 s y 264,6 s |
| `analiza.py` | análisis exacto | 0,03 s |

**Resultados.**
- Tipos etiquetados realizables en cuatro familias, para v = 1, …, 6: 1, 5, 77, 2 529, 150 985 y 14 766 689. Son relevantes (todo sitio con vecino diagonal y soporte no colineal) 0, 0, 18, 858, 52 970 y 5 447 320.
- **Ninguna violación**, hasta v = 6, de:
  - L_g ≥ mín(β_g,2), con igualdad si β_g ≤ 2;
  - D ≤ p−1 y 0 ≤ L_s ≤ b+2;
  - en los relevantes: d ≥ 1, h ≤ 4d y d+b−1 ≥ (v−4)/3.
- El mínimo de 3(d+b−1)−(v−4) vale 0, 2 y 1 para v = 4, 5 y 6; h/d llega a 4.
- Constante efectiva C_ef(v) = máx_{c,L_s} R^{1/v}:
  - cuatro familias, tipos relevantes: 2,00, 3,40, 4,19 y 4,90 para v = 3, …, 6;
  - cuatro familias, todos los tipos: 7,04 en v = 6;
  - dos familias, para v = 2, …, 10: 2,00, 2,57, 3,09, 3,51, 3,87, 4,18, 4,45, 4,68 y 4,90, con incrementos decrecientes (0,57 → 0,21).
- El factor 1/c! es exacto en el extremo c = v (dos familias), donde W = 1/v!. Con L_s = 0, W·c! decrece en c, tanto en dos familias (v = 10) como en cuatro (v = 6, relevantes).

**Interpretación.** Es evidencia numérica en grados pequeños, no una prueba. Es coherente con una base exponencial moderada, muy por debajo de la constante explícita de la demostración (≥ 2e⁴C₀²). No hay ningún contraejemplo.

## 3. Cuantificadores, ley y tamaño

- La cota por soporte es determinista, en una máscara fija de la clase de referencia y de tamaño j. Los átomos internos de tamaño m = j−|I| y su sustitución O(j⁻⁸) [A03] no son de mi encargo.
- El recuento de tipos es puramente combinatorio y uniforme en v.
- Las colocaciones se cuentan en el tablero original, con a lo sumo n^D, y la prescripción se toma bajo la ley original ν, con el indicador H_j y sin condicionar.
- El alcance es 5 ≤ v ≤ N = ⌈4 log n/log ρ⌉ ≤ 8 log n, con j = ⌊bn⌋ y b, δ fijos antes de n → ∞.

## 4. Estados

- **Demostrado (lectura con cada paso rehecho):**
  - el lema de rango y D ≤ p−1;
  - las consecuencias d ≥ 1, h ≤ 4d y d+b−1 ≥ (v−4)/3;
  - el recuento ponderado con 1/c!;
  - el álgebra n^D x^h j^{−p};
  - la suma geométrica y el orden de constantes;
  - la cota de prescripción de H02 a partir de sus entradas.
- **Condicional (entradas importadas, fuera de mi parte):**
  - la holomorfía y la cota e^{O(v)} en el polidisco, y los órdenes en s (G02–G04, P03–P05, B02–B03);
  - la transición de B–C;
  - la pertenencia a la clase en H_j (A01, D04);
  - E1 y E2.
- **Numérico exacto:** las enumeraciones del punto 6.
- **Heurístico:** nada.

## 5. Dictamen global sobre mi parte

**Certificada con precisiones.** El recuento ponderado de tipos, el lema de rango, los radios por casilla, las prescripciones bajo ν y la suma media por grados son correctos como implicación de las entradas que se citan. Las precisiones son tres:
1. falta una línea en G06 13, que se da arriba;
2. el factor (4v²)^{L_s} es esencial y sólo se compensa con j^{−b}, lo que limita el método a v² ≪ j;
3. hay una colisión de notación en v^d, d y b.

Ninguna obliga a cambiar enunciados ni constantes.

## 6. Resumen final

- Revisé, contra las líneas de las fuentes completas (huellas correctas), P06, G02 y G05–G07, H02–H03, B03, A02 y 06_corte.
- **Punto 1, lema de rango: correcta.** En el soporte de una dependencia, los vértices de grado 2 están en una recta. Tras suprimirlos queda un grafo simple de grado ≥ 3, con ≥ 3 ciclos. Por eso un árbol con ≤ 2 cuerdas es independiente, L_g ≥ mín(β_g,2) y D ≤ p−1, también con varias componentes cíclicas. El mínimo con 2 es óptimo: el cuadrado tiene β = 3 y L = 2.
- **Punto 2, radios κ′/d_i: correcta con precisión.** Σ_{i∈f}1/d_i ≤ 1, la contracción ponderada, el Cauchy direccional y el coste ∏(Cd_i/j) son uniformes para v ≤ 8 log n. La holomorfía y la cota e^{O(v)} son entradas importadas.
- **Punto 3, recuento: correcta con precisión.** El código de estrellas y superraíz da C^v(4v²)^{L_s}/c! y conserva 1/c!. G06 13 omite la deducción de d+b−1 ≥ (v−4)/3, que es cierta: 3(d+b) ≥ p−1. El factor (4v²)^{L_s} es imprescindible: las cuadrículas k×k pesan v^{v/2}/2, pero quedan cubiertas porque L_s = b+2 y v²/j ≤ δ_*. No encontré ningún tipo sin cubrir.
- **Punto 4, prescripciones: correcta.** Rehíce (j/M)^{s+t}exp(C(st+t)/j), de donde sale δ^{−2v}(j/n)^h exp(C_L v²/j). Se usa con el indicador H_j, sin condicionar ni suponer independencia.
- **Punto 5, suma final: correcta con precisión.** La razón C₁δ⁻²δ_*^{1/3} < 1 hace converger la serie. C₁ es de la clase de referencia, sin b ni ρ. El orden δ → clase y L = 8 → C₁ → a_d → ρ → α → δ_* → b → n es coherente. v^d denota un exponente fijo.
- **Punto 6, ordenador.** Enumeré todos los tipos realizables de cuatro familias hasta v = 6 (14,9 millones) y de dos familias hasta v = 10 (3,1·10⁹). No hay ninguna violación, y las constantes efectivas son moderadas (≤ 4,9 en los tipos relevantes).
- **Dictamen global sobre mi parte: certificada con precisiones**, como implicación de sus entradas. No examiné E1 ni E2.

## Anexo · Huellas de los archivos de esta revisión (SHA256)

```
9c8043e0e36ada0150e9ad8cb4f4247ebf8b8f992f7f30a1f07a15d11432cfb9  codigo/analiza.py
43edbaa19503fdf3c7c6a038edc0f363a1afc4854cb75cb0558e5f167b70505e  codigo/tipos4.py
79a4f65d512498bcbb21c6cedd66601afe1b5aad0640a428278ab73f423626a8  codigo/tipos2.c
71b5968e7294d34ac7b71f37f4cd569fad66870ff886325ff9819dc27837bb1b  codigo/tipos4.c
7677395297e195d3749f8b99bad91446a20b9a3d12ef67a20eb9250b56c6a02a  resultados/analisis_W.txt
101dabdd510f29343a469d64b6bcb3fc3b782a73f1bb4af2cd1817fdbd22bee2  resultados/tipos2_v10.txt
dce2b9307f2a0811e17a18ff0ee7f4eadef453b1fcd289404bb9f06285e5eec2  resultados/tipos2_v8.txt
5ae8aaf5e8784db865eed444d1a0d2f7df625ace446528939b62602ff4fed363  resultados/tipos4_v5.txt
621e3d740a71d9421fad563ecf849a3ade95c3c9cc47214d27f2ba5d57da2dd8  resultados/tipos4c_v5.txt
81f39eec4dc24eac38bc64a958f26855d20eaec105ab773547e5d117f427d458  resultados/tipos4c_v6.txt
```

Para reproducir: `gcc -O2 -o tipos4 tipos4.c`, `gcc -O2 -o tipos2 tipos2.c` y luego `nice -n 10` sobre cada orden de la tabla del punto 6.
