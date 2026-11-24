# Acta de revisión · W2_pares: exponente 7 de los pares y resto de grado ≤ 4

**Objeto.** La dependencia que el dictamen de E2 dejó abierta (`rev_exp/E2/ACTA.md`, §4 líneas 224–230 y precisión P2, línea 236): la cota |w_bd| ≤ Cj⁻⁷ de M01 para dos conflictos con ocho coordenadas RC distintas, la media y la suma de esos pares, y la cota P05 del resto con tres o más conflictos y v ≤ 4. No reviso E1, E2 ni el recuento de tipos de grado ≥ 5.
**Revisión.** 17-11-2026.
**Dictamen global sobre esta parte: CERTIFICADA CON PRECISIONES** (§3).

## 0. Integridad, convenciones y método

- **Integridad.** `sha256sum -c r19/SHA256SUMS`: 116/116 correctos. Las tres entregas fuente (`rev_exp/fuentes/…`) pasan su propio `SHA256SUMS` (14, 12 y 12 archivos). No he modificado nada fuera de `rev_exp/W2_pares/`.
- **Abreviaturas de las fuentes completas** (cito la línea del archivo):
  - MM = `fuentes/velocidad_via2_media_matriz_20261116T150154Z/latex/`. Por ejemplo, MM06:34–36 es `06_truncacion.tex`, líneas 34–36.
  - GI = `fuentes/velocidad_via2_grupos_interlinea_20261116T161315Z/latex/`.
  - PF = `fuentes/velocidad_via2_patrones_finitos_20261116T164355Z/latex/`.
- **Originales del expediente** (`r19/expediente/originales/`). Doy la *línea original*, que es la línea del archivo de transcripción − 7, como hace el expediente. M/01, M/07 y M/09 coinciden literalmente con MM01, MM07 y MM09, con la misma numeración.
- **Estados.**
  - *Demostrado*: lo he verificado aquí.
  - *Condicional*: depende de una entrada que no dictamino.
  - *Numérico*: sólo es evidencia de cálculo.

  **No he encontrado ningún enunciado falso ni ningún hueco en los pasos propios de las pruebas revisadas.** Las reservas son dependencias de entradas previas, que M01 declara como hipótesis, y pasos escritos de forma esquemática.
- **Método.**
  1. Lectura línea a línea de MM01–09, GI01–05 y PF01–06, y su cotejo con T01, T04–T08c, K06–K07, P05, P06 y C02.
  2. Verificación algebraica exacta de las identidades que producen la séptima potencia.
  3. Conteos exactos deterministas con código propio, en máscaras no uniformes de la clase, hasta j = 180.

  Corrí un proceso cada vez, con `nice -n 10`; los tiempos están en §2.5. No hay azar en ningún cálculo.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Motivo breve |
|---|---|---|---|
| 1 | Exponente 7 de M01 (MM01–08) | **Correcta con precisión** | Las piezas que mejoran la potencia se verifican aquí: la cancelación +1/−1 de los cruces (D₃R + D₂A = O(s³)), la parte mixta O(s h₁h₂) de los restos Ψ, la fórmula del coeficiente cuadrilineal y Cauchy en cuatro actividades. Es condicional a R8–R9, usadas en dos extensiones que no están en su enunciado literal, a la identidad de Schur de R3 (08b) y a la herencia de clase. Numérico: pendiente −7 en siete máscaras no uniformes. |
| 2 | Media de pares (MM09) y suma en máscara fija | **Correcta** | La cuenta n⁶(j/n)⁸j⁻⁷ = Cj/n² es correcta, condicional a C §5.1. La ronda 19 usa, con razón, el recuento determinista ≤ Cj⁶, que da Σ\|w_bd\| = O(1/j). |
| 3 | Resto con ≥ 3 conflictos, v ≤ 4 (P05, orig. 47–54; GI01–04) | **Correcta con precisión** | Todos los tipos son conexos (c = 1) y basta la parte simple de P05: bosque, un ciclo, varios ciclos. Hay 28 clases geométricas, con p = D+1 en todas. Las parejas restadas tienen un exponente mayor. Numérico: pendientes −6, −5 y −4 en nueve tipos. |
| 4 | Mismo ambiente | **Correcta** | Misma máscara A, misma convención de activación, misma reoptimización y mismo exterior A∖S; las constantes y los campos son comunes a todas las activaciones. |
| 5 | Pruebas por ordenador (opcional) | **Evidencia numérica favorable** | Reconstruí el predictor y lo validé con los coeficientes publicados de R3 (4, −2, −10, −1, −3). En el tablero lleno, w·j⁷ → 30,00; en las máscaras no uniformes, w·j⁷ tiene límite finito. |

## 2. Detalle por punto

### 2.1 Punto 1 · El exponente 7 (MM01–08)

**Enunciado y alcance** (MM01:2–16):
- dos conflictos b = 12 y d = 34 en líneas distintas, con cuatro filas y cuatro columnas distintas;
- w_bd = Δ_bΔ_d(log Q − L), con las cuatro activaciones sobre la misma máscara y el predictor reoptimizado.

Hipótesis declaradas: difusión y brecha; su herencia al suprimir cuatro casillas o hasta cuatro filas y columnas; la normalización por Schur de R3; el desarrollo uniforme de torres de R8–R9. Conclusión: |w_bd| ≤ Cj⁻⁷, con constantes de la clase y sin mínimo de masa.

Es la única fuente de la séptima potencia: R3 sólo prueba k⁻⁶ (T01 orig. 33–34; T07 orig. 44–46) y deja abierta la potencia óptima (T08 orig. 42–43).

**(a) Exterior y prefactor** (MM02:2–33). Comprobé que H_E + R reproduce la entropía de Bethe de torres. En efecto, Σ_v t_v log t_v = 2Σ_i(1−x_i)log(1−x_i), y para E = ∅ resulta Σ_i[−x_i log x_i + (1−x_i)log(1−x_i)] + H_ext. La forma del prefactor, A − ½ log det(I − V_E R″), es la de T08b (orig. 17–20). **Condicional** a esa identidad de R3. Mi cálculo directo del predictor no la usa, y es coherente con ella (§2.5).

**(b) Familia de equilibrio** (MM03:4–37). Se desdobla cada índice marcado en un tipo ordinario de masa s − h_g y una copia de masa h_g, con t = 1 − x_i. Se resuelve para |h_g|, |σ| ≤ c y |x_i| ≤ 2. En σ = 0, z_x depende sólo de las cuatro cantidades h_g x_i (MM03:34–37). Es la misma construcción de Newton con inverso congelado que K06 (orig. 13–27), con una medida perturbada en variación total O(c). El texto es esquemático, pero no encuentro ningún error.

**(c) Acción** (MM04). Verifiqué cinco cosas:
1. La sustitución p = s t_r t_c v cancela Σ t log t, y log s, log z y los márgenes dan términos afines (MM04:8–10).
2. La fórmula de ℛ (MM04:12–14) sale de (1−p)log(1−p) = −p + Σ_{l≥2} p^l/(l(l−1)).
3. La derivada del integrando en v es −log(v/z) − 2 − log(1 − σt_r t_c v) = −α_r − β_c − 2. Por los márgenes fijos, el teorema de la envolvente da ∂_σℛ|₀ = ½∫∫ z_x² dM₂dM₂ = ½E₂₂ (MM04:18–30).
4. Con h_g = 0 desaparece toda dependencia del grupo g. Por tanto, la parte de Ψ_R que depende de ambos grupos se anula en {h₁h₂ = 0} y es O(h₁h₂) en el bidisco (MM04:32–37).
5. Con esto, R = afín + s⁻¹ℛ₀(sx) + ½E₂₂ + sΨ_R.

**Demostrado**, dado (b).

**(d) Prefactor** (MM05). Verifiqué cuatro cosas:
1. pdet S_ext = (2/d̄)∏_v(t_v d_v)·det(I − WᵗW). En la congruencia S = Δ^{1/2}MΔ^{1/2}, el pseudodeterminante adquiere el factor |Δ^{−1/2}k̂|² = 2j/(2·jd̄) = 1/d̄. El término ½Σ log t_v se cancela exactamente (MM05:13–22).
2. log b₂(y) = −y² + O(y³) da ½E₂₂.
3. d_r = 1 + σt_r∫t_c² z_x² dμ_C + O(σ²) da −½E₁₂ y −½E₂₁ (MM05:38–49).
4. En un vértice con m filas, A toma el valor F_T(menor) + ½log(m/j), lo que conserva la constante ½log(4πm) (MM05:53–57).

**Demostrado**, dado (b).

**(e) Truncación: aquí se gana la potencia** (MM06). Las fuentes de órdenes s² que ven ambos grupos y tienen grado > 3 en R (o > 2 en A) son sólo los cruces fila de un grupo × columna del otro, con multiplicador común s²z_rc²/2. Su contribución es:
- en R: f₂(X)f₂(Y), con D₃ = 1;
- en A: f₂f₂ − f₁f₂ − f₂f₁, con D₂ = −1.

He comprobado ambos valores en aritmética racional exacta (V5). También verifiqué la contabilidad de grados de los términos con cero, una y dos masas distinguidas (MM06:15–33) y que ℛ₀, A₀ y sΨ sólo dejan O(s³) (MM06:7–10). De ahí D₃R + D₂A = O(s³) (MM06:34–36). **Demostrado**, dados (c) y (d).

**(f) Vértices** (MM07):
- **u_T.** Se usa u_T = s_m[−1/12 + φ(v)] (K07 orig. 6–10 y 56), prolongado en (h₁, h₂) mediante la medida μ_h, que en h_g ∈ {0, s} es la uniforme de cada menor. Como |u_T| ≤ Cs en un bidisco fijo, la diferencia mixta es O(s³) (MM07:16–44).
- **R_T.** Su variación es O(s³) por vértice, por K06 (orig. 2–6).
- **Resultado.** Se obtiene Δ_{u,v*}g = h + A″[u,v*] + ½(U₃[u,u,v*] + U₃[u,v*,v*]) + O(s³) (MM07:52–56).

**Condicional** a R9, con las precisiones P1.1 y P1.2.

**(g) Actividades y cierre** (MM08). Verifiqué los pasos siguientes:
1. ζ_i = e^{r_i} = (P_i/(1−P_i))·e^{−∂_iR_c(P)} = O(s) (MM08:4–7). Basta como cota superior: no se usa ningún mínimo de masa.
2. En un polidisco fijo, el error de cada caso es O(s²) (MM08:20–33). La identidad V₀ + x₀x₀ᵗ = E[XXᵗ] lleva el desarrollo exacto al del predictor.
3. El coeficiente multilineal de Δ_bΔ_d sólo ve los átomos 0, u, v y u+v (MM08:35–43). Por inversión sobre particiones, el coeficiente exacto es w(1234) − w(12)w(34) = e^{g(u)+g(v)}(e^{Δg} − 1) (MM08:44–47).
4. El coeficiente del predictor (MM08:48–54) lo recalculé a mano, módulo S² y T². Cada término contribuye así:
   - K: +2h;
   - −λ·x: −2h;
   - R_c: +h;
   - A_c: h·a[u+v] + A″[u,v];
   - −½log det: ½{U₃[u,u,v] + U₃[u,v,v] + h(H[u,u] + H[v,v])} + ½h².

   Además lo comprobé numéricamente, con un cuártico añadido que no debe contribuir: la diferencia es 1,2·10⁻¹¹, del orden del error de diferencias finitas (V5).
5. Con H, a = O(s) y U₃, A″ = O(s²), los dos coeficientes coinciden hasta O(s³) (MM08:57–58).
6. D se anula en cada ζ_i = 0, así que D̃ = D/∏ζ_i es holomorfa. |D| ≤ Cs² en el polidisco da |∂D̃| ≤ Cs² en un radio menor, y D̃(0) = O(s³). Por tanto |D| ≤ C s⁴·s³ = Cs⁷ (MM08:59–62).
7. D = w_bd en el punto físico (MM08:63–64).

**Demostrado**, dado (f).

**Por qué la potencia pasa de 6 a 7.** El método de R3 controla cada caso a O(s²), y la divisibilidad por ∏ζ_i da s⁶. La séptima potencia exige que el coeficiente cuadrilineal sea O(s³). Las únicas contribuciones de orden s² a Δ_{u,v}g que no recogen los coeficientes de Taylor en 0 son tres, y cada una queda controlada:
- los cruces, que se cancelan (+1 − 1);
- la parte mixta de Ψ, que es O(s h₁h₂) gracias al desdoblamiento;
- la diferencia mixta de u_T, que es O(s³) por holomorfía en (h₁, h₂).

R_T sólo aporta O(s³).

**Precisiones.**
- **P1.1 · Extensión de K06.** K06 (orig. 2–6) enuncia la estabilidad de F₂ para «menores puros de una fila». MM07:9–14 la usa para menores del exterior cuyo cruce suprimido no está en el soporte, y para hasta cuatro supresiones sucesivas, con una justificación de una frase. Es una extensión de la entrada, no un paso de M01. Conviene declararla como entrada.
- **P1.2 · Prolongaciones esquemáticas.** La prolongación holomorfa de φ (K07 orig. 6–9) a las medidas complejas μ_h (MM07:28–44) y la del equilibrio desdoblado hasta |x_i| ≤ 2, pasando por t = 0 (MM03:9–29), están escritas de forma esquemática: Newton en supremo, Neumann, Fredholm, Hadamard. No encuentro ningún error. Son las construcciones de K06 (orig. 13–27).
- **P1.3 · Transcripción pendiente.** La prueba sigue sin estar transcrita en el expediente: sólo M01, M07 y M09. La precisión P2 de E2 queda cubierta por esta revisión de MM02–08, salvo P1.1 y P1.2.

### 2.2 Punto 2 · Media de los pares y suma en máscara fija

**(a) Parte 09.** Los pasos son estos:
- Σ_{r,c} M_rc = Σ_{b,d} w_bd (MM09:2–4).
- Hay O(n⁶) pares geométricos (MM09:4–5): cada conflicto se fija con una casilla (n²), una distancia y una pendiente (≤ 2n·2).
- La masa de retención de las ocho coordenadas es ≤ C(j/n)⁸ (MM09:6–8). Es una entrada (C §5.1 y la comparación parada de R12) que no dictamino.
- La cota M01 se aplica sólo sobre G_j, donde la máscara está en la clase.
- La cuenta da C n⁶(j/n)⁸j⁻⁷ = Cj/n² (MM09:9–13). Es correcta.
- Consecuencias (MM09:15–17): con j ≤ δn + 1 se obtiene C(δ + 1/n)/log(2+t); a t fijo, j = ⌈t⌈√n⌉⌉ da O_t(n^{−1/2}). Son correctas.

La ley ν̄ entra sólo después de la cota puntual.

**(b) Uso en la ronda 19.** En una máscara fija de orden j con índices vivos no consecutivos, el número de pares con ocho coordenadas RC distintas es ≤ Cj⁶. Lo da la proyección inyectiva sobre D coordenadas (C02 orig. 15–22; `latex/05_lineas_y_grados.tex`:67–74). Con M01, Σ|w_bd| ≤ C/j de forma determinista, y ν sólo entra por 1_{H_j}. La media de la parte 09 pertenece al suelo √n y la ronda 19 no la usa, como ya observó E2 (`E2/ACTA.md`:192).

**Correcta**, condicional a M01 y, para la parte 09, a C §5.1.

### 2.3 Punto 3 · Resto con tres o más conflictos y v ≤ 4

**(a) Qué tipos hay.**
- **v = 3.** Tres conflictos fuerzan la colinealidad: con sólo dos direcciones diagonales, dos pares que salen del mismo sitio por la misma pendiente comparten recta (L01 orig. 29–30). Esos casos son líneas y quedan fuera.
- **v = 4, conexos y no colineales.** Son tres formas: el camino (3 conflictos), la terna colineal con una hoja, o «forma en T» (4 conflictos), y el 4-ciclo (4 conflictos).
- **Soportes con un sitio aislado.** Dan cero (PF01:43–46; GI01:35–37).
- **Dos pares puros.** [S]V = 0 exactamente. Lo comprobé: e(Y) sólo depende de (1[b ⊆ Y], 1[d ⊆ Y]), así que [S]e = w_bd, aunque compartan filas o columnas.

**(b) La cota.** Todos estos tipos son conexos (c = 1). La fórmula de P05 (orig. 47–54; PF05:47–54) da entonces p = 6, 5 o 4 según el grafo sitio–línea, con filas y columnas incluidas, sea un bosque, tenga un ciclo o tenga varios. Para c = 1 la prueba sólo usa tres casos:
- **Bosque.** Bethe es exacto en el bosque local, y los términos exteriores de primer orden coinciden por E[XXᵗ] = V + mmᵗ. El error de cada subcaso es O(s²) (GI03:58–73), y las caras con Cauchy dan s^{v+2} (PF05:32–46; GI03:53–56).
- **Un ciclo.** El error local es log(1 − θ²), con potencia doble de las actividades del ciclo, y la reacción exterior es O(s). Resulta s^{v+1} (GI04:2–41; PF05:18–30).
- **Varios ciclos.** Basta la proyección, que da s^v (GI04:41–42).

Verifiqué tres puntos de ese argumento:
- la identidad del ciclo para exclusiones binarias: θ = (−1)^d ∏ x_i/(1−x_i) en la corrección de lazo, y jacobiano 1 − θ de las innovaciones gaussianas;
- que una coincidencia RC entra como un factor de cupo del mismo tipo (GI03:2–10, 35–38), de modo que el ciclo cerrado por una fila compartida queda cubierto;
- que la cancelación delicada entre grupos (PF04:26–64) no se necesita aquí: sólo hace falta para c ≥ 2, por ejemplo para los pares puros, donde da p = 7.

**(c) p ≥ D + 1.** Enumeré exhaustivamente, con la geometría real de cuatro familias de líneas y |desplazamientos| ≤ 7 y ≤ 9, con el mismo resultado (V4, V4b). Sale lo siguiente:
- hay 28 clases geométricas de cuatro sitios con ≥ 3 conflictos;
- en todas, p = D + 1 exactamente:

  | Tipo | (D, p) |
  |---|---|
  | camino, 0 / 1 / 2 coincidencias | (5,6) / (4,5) / (3,4) |
  | T, 0 / 1 / 2 coincidencias | (5,6) / (4,5) / (3,4) |
  | 4-ciclo, 0 coincidencias | (4,5) |
  | 4-ciclo, 2 coincidencias dependientes | (3,4) |
- el 4-ciclo con exactamente una coincidencia no es realizable: si a–d comparten columna, b–c comparten fila, y es la misma ecuación;
- de paso salen los pares (6,7), (5,6), (4,5), (3,4), (3,4) y las cuñas (4,5), (3,4), como en C02 (orig. 42–44).

**(d) Sustracciones.** [S]V = [S]e − Σ w_bd, sumando sobre las parejas de conflictos disjuntos en líneas distintas cuya unión es S:
- en el camino y en la T hay una pareja;
- en el 4-ciclo hay dos. `E2/ACTA.md`:160 escribe «− w_bd» en singular; es una imprecisión sin efecto.

El exponente de cada pareja restada es ≥ D_S + 2 (7 frente a 6; 6 frente a 5; 5 frente a 4), así que no cambia el orden.

**Precisiones.**
- **P3.1.** La cota es condicional a los desarrollos del exterior (GI02:16–27 y 29–68), que usan las mismas entradas de R9 que M01: variación O(s²) de u_T y O(s³) de R_T.
- **P3.2.** La «segunda justificación» de p = 7 para pares puros (`latex/05_lineas_y_grados.tex`:59–62) no es independiente de MM. Usa los mismos desarrollos (PF03:5–9) y la identidad P + B = 0 en átomos binarios (PF04:54–63), que es la misma cancelación +1/−1 de MM06. Comprobé que P(m) + B(m) + ½tr(VP″) = 0 en racionales (V5).

**Correcta con precisión.**

### 2.4 Punto 4 · El mismo ambiente

Comparé las convenciones fuente a fuente:
- M01 activa sólo b y/o d sobre la misma máscara y reoptimiza el predictor (MM01:4–5, 9).
- GI y PF definen e(Y) con la cupo uno restringida a los sitios de Y y los demás sitios de A disponibles para las torres (GI01:9–16; PF01:6–11). Lo mismo hace C02 (orig. 4–6: «el mismo tablero basal»).
- El exterior es A menos las cuatro casillas (MM02:2), que coincide con D₀ = A∖S, el mismo para todas las submáscaras (GI02:2–3), cuando |S| = 4.
- Las constantes y los campos afines retirados son comunes a todas las activaciones (MM08:63–64; GI02:13–15; PF03:10).
- El exterior es un recurso de la prueba: w_bd y [S]e son diferencias de la misma función e(Y) sobre A. Así lo usa E2 (`latex/05_lineas_y_grados.tex`:76–84).

**Correcta.**

### 2.5 Punto 5 · Cálculos (código en `W2_pares/codigo/`, salidas en `W2_pares/resultados/`)

**Material de cálculo.**
- **Máscaras.** Son explosiones de patrones 0/1 totalmente indescomponibles, con grupos de filas y columnas de tamaños proporcionales a k. Todas están en la clase: max jP_e ∈ [1,33; 2,25] y σ₂(P) ∈ [0,33; 0,62].
- **Recuentos exactos.** Los permanentes de A y de sus menores son enteros exactos: per = ∏r_a!·Σ_N ∏_b multinom(c_b; N_·b), sumando sobre las matrices de transporte N.
- **Predictor.** Lo reconstruí a partir de T01 (orig. 10–24), T04 (orig. 2–3) y T05 (orig. 28–39), porque el Artículo B no está en el expediente:
  - L_E = máx Φ_E + F_T(P*) − ½log J_E(P*);
  - J = c·det(I + (D_I − D_I G D_I)H).

  Lo reduje por simetría y lo resolví en aritmética decimal de 60 cifras.

| Id | Archivo | Qué comprueba | Resultado | Tiempo |
|---|---|---|---|---|
| V0 | v0_validacion.py | permanentes por bloques frente a Ryser; predictor reducido frente a una implementación completa independiente (numpy); Q frente a fuerza bruta | 16/16; diferencia ≤ 7·10⁻¹⁵; 11/11 | 2,6 s |
| V1 | v1_tablero_lleno.py | coeficientes de R3 en el tablero lleno, j = 8…64 | cuñas 4,000 y −2,000; una coincidencia −10,000; tres −1,000; cuatro −3,000; dos coincidencias k⁻⁵ (4,0 y 3,0); pares RC-disjuntos: w·j⁷ → **30,00** | 5,9 s |
| V2 | v2_pares_bloques.py | exponente de w_bd en siete máscaras no uniformes (B1a–c, B2a, B3a, B4a, B4b), j hasta 96–180 | pendiente local en el j mayor entre −7,010 y −7,041; w·j⁷ → 44,85, 43,78, −36,84, 50,32, 54,34, 49,43, 47,13; w·j⁶ → 0 como 1/j | 185,3 s |
| V3, V3b | v3_resto_grado4.py, v3b_extrapola.py | [S]e y [S]V de nueve tipos de cuatro sitios en dos máscaras, j hasta 120 | pendientes → −p con p = 6, 5, 4 según P05; [S]e·jᵖ y [S]V·jᵖ con límite finito no nulo (de −94,6 a +17,1) | 144,1 s + 0,1 s |
| V4, V4b | v4_tipos_grado4.py (W = 7), v4b_… (W = 9) | clases geométricas de cuatro sitios; pares y cuñas | 28 clases, p = D+1 en todas; pares y cuñas como en C02 | 11,0 s + 30,7 s |
| V5 | v5_algebra.py | D₃ = 1, D₂ = −1; P + B = 0; coeficiente ST del predictor (MM08) y del exacto | exacto; diferencia 1,2·10⁻¹¹ | 0,05 s |

**Lectura.**
- Si el exponente fuera 6, w·j⁷ crecería linealmente en j. En las siete familias decrece hacia un límite finito, con corrección a + b/j y la extrapolación estable entre tres y cuatro puntos.
- Mis valores del tablero lleno coinciden con los de la implementación independiente de E2 (`E2/resultados/c5_series.txt`: 70,044 y 38,756 con 0 coincidencias; −15,574 con una). Es decir, dos reconstrucciones del predictor coinciden y reproducen los coeficientes de R3.

Todo esto es **evidencia numérica, no prueba**. No mide la uniformidad de las constantes en toda la clase.

**Incidencias.**
- La primera ejecución de V2 falló en una función auxiliar de diagnóstico: un Sinkhorn tosco divergió. La sustituí por el resolvedor reducido; se perdieron 14,7 s.
- Una segunda ejecución (72,4 s) tenía la familia B1b equivalente por simetría a B1a. La cambié por una colocación no equivalente y añadí dos familias 4×4.
- El 4-ciclo con una sola coincidencia de V3 no es geométrico (§2.3c). Lo mantengo como prueba analítica de P05: también da p = 4.

## 3. Dictamen global

**Parte W2_pares: certificada con precisiones.** No he encontrado ningún enunciado falso ni ningún hueco en los pasos propios.

1. **Exponente 7.** La prueba de |w_bd| ≤ Cj⁻⁷ (MM01–08) es correcta al nivel de detalle del expediente. Es condicional a lo que M01 declara: R8–R9, con las extensiones P1.1 y P1.2, la identidad de Schur de R3 (08b) y la herencia de clase. Sin ella, la suma de pares de E2 sería O(1) y no O(1/j).
2. **Suma de pares.** La media de la parte 09 es correcta, condicional a C §5.1. En la ronda 19, la suma en máscara fija es O(1/j).
3. **Resto de grado bajo.** La cota P05 del resto con ≥ 3 conflictos y v ≤ 4 se sostiene con la parte simple del argumento (c = 1), y p = D + 1 en las 28 clases.
4. **Ambiente.** Las restas se hacen en la misma máscara y con el mismo exterior.

Con esto queda cubierta la precisión P2 del dictamen de E2, salvo las entradas de R9 citadas.

**Precisiones para la próxima entrega.**
- **PW1.** Transcribir MM02–08 y GI01–04, o citar esta acta.
- **PW2.** Declarar como entradas dos usos de R9 que van más allá de su enunciado: la extensión de K06 a menores con cruce ausente y a hasta cuatro supresiones (MM07:9–14), y la prolongación de φ de K07 a medidas complejas deformadas (MM07:28–44).
- **PW3.** Indicar que la segunda justificación de p = 7 reorganiza la misma cancelación (PF04:54–63 ≡ MM06:26–36).
- **PW4.** En el resto de grado 4, enumerar las 28 clases con coincidencias RC y restar las dos parejas del 4-ciclo.
- **PW5.** Mantener separada la media de la parte 09, propia del suelo √n, del recuento determinista que usa la ronda 19.

## 4. Resumen final

```
W2_pares · exponente 7 de los pares y resto de grado <= 4
Integridad: r19 116/116; las tres fuentes completas pasan su SHA256SUMS.

Punto                                             Veredicto
1 Exponente 7 de M01 (MM01-08)                    Correcta con precisión
2 Media de pares (MM09) y suma en máscara fija    Correcta
3 Resto >=3 conflictos, v<=4 (P05, GI01-04)       Correcta con precisión
4 Mismo ambiente                                  Correcta
5 Cálculo exacto (opcional)                       Evidencia favorable

Dictamen global: CERTIFICADA CON PRECISIONES. Sin enunciados falsos ni huecos
en los pasos propios.
Demostrado aquí:
- La séptima potencia se gana porque:
  * los cruces dan +1 (acción, D3 f2f2) y -1 (prefactor, D2), y se cancelan;
  * la parte mixta de los restos Psi es O(s h1 h2) gracias al desdoblamiento;
  * la diferencia mixta de u_T es O(s^3) por holomorfía;
  * el coeficiente ST del predictor coincide con el exacto hasta O(s^3);
  * Cauchy en cuatro actividades da |w|<=Cs^7.
- MM09: n^6 (j/n)^8 j^-7 = Cj/n^2. La ronda 19 usa la suma determinista O(1/j).
- Resto v<=4: todos los tipos son conexos y bastan los casos bosque, un ciclo
  y varios ciclos de P05. 28 clases geométricas, p=D+1 en todas. El 4-ciclo con
  una sola coincidencia RC no existe. Las parejas restadas son de orden mayor.
Condicional a: R8-R9 (K06, extendida a cruces ausentes y a 4 supresiones; K07,
prolongada a medidas complejas), la identidad de Schur de R3 (08b) y la
herencia de clase; para MM09, también C §5.1.
Numérico (código propio, conteos exactos, j hasta 180):
- predictor reconstruido; reproduce 4, -2, -10, -1, -3 de R3;
- tablero lleno: w*j^7 -> 30,00;
- siete máscaras no uniformes: pendiente -7,01 a -7,04, w*j^7 con límite finito;
- resto de grado 4: pendientes -6, -5, -4 según P05.
Precisiones: transcribir MM02-08/GI01-04; declarar las extensiones de R9;
la 2.ª justificación de p=7 no es independiente; restar 2 parejas en el
4-ciclo; separar MM09 (suelo √n) del recuento determinista.
ACTA: rev_exp/W2_pares/ACTA.md (código en W2_pares/codigo, salidas en W2_pares/resultados).
```
