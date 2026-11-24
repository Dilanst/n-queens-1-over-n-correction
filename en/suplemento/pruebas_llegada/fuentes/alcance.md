# Acta de revisión externa W2_t4 · Paso al alcance logarítmico (r22/02) y corolario de la pendiente (r22/01)

**Revisor.** Externo e independiente, ajeno al equipo que escribió la prueba. Fecha: 2026-11-17. He trabajado sin web y sin acceso a otros equipos, sólo con `rev_exp/`. Los cálculos son míos, exactos (racionales, o enteros con redondeo dirigido), deterministas, con `nice -n 10`, uno cada vez y con el tiempo medido. No reviso E1, E2, el recuento de tipos ni las entradas analíticas ya dictaminadas en W2_jets; las uso como importadas.

**Objeto.**
- `r22/latex/02_continuacion_de_los_coeficientes.tex` (en adelante [02]) escribe el paso de v fijo a 5 ≤ v ≤ 8 log n en la cota por soporte. W2_jets lo dio por válido pero no escrito: precisión 2.1, [W2j 159–164].
- `r22/latex/01_corolario.tex` (en adelante [01]) deduce del teorema consolidado de R21 la respuesta a la disyuntiva O(1/n) frente a c·(log n)/n, y discute a(0).

**Integridad.**
- Los dos textos coinciden con `rev_exp/r22/SHA256SUMS_entrega`:
  - `latex/01_corolario.tex`: c3810f1c…89e5;
  - `latex/02_continuacion_de_los_coeficientes.tex`: 17807d0a…9b9c.

  Los otros siete archivos de ese manifiesto no están en el material, entre ellos `TABLA_CIERRE_DEPENDENCIAS.md` y `PRECISIONES_PARA_EL_CONSOLIDADO.md`.
- Fuentes usadas, contrastadas con su `SHA256SUMS`. Todos los archivos presentes coinciden y ninguno discrepa:
  - cotejo_adenda2 7/7, grados_ponderados 12/12, patrones_finitos 12/12, menores_uniformes 14/14;
  - ciclo_exterior 8/8, ronda18 14/14, margenes_y_atomos 9/9, grafo_termino 24/24;
  - ronda10: los 11 archivos presentes (entre ellos `latex/01–06`) coinciden; faltan otros 54 listados (cálculos, T2a, T2b), que no uso;
  - r21: los 106 presentes coinciden (`consolidado/`, `piezas_T2/`, `anexo_T1/` y los documentos raíz); faltan 248 listados (`actas_externas/`, `archivo_r19/`, …).

**Convenciones de cita.** Todos los números son líneas del propio archivo.
- [02 n] y [01 n] son los dos textos revisados.
- [X03] es `fuentes/velocidad_via2_cotejo_adenda2_20261117T072100Z/latex/03_truncacion.tex`.
- [Pnn], [Unn], [Gnn] y [Znn] son `latex/nn_*.tex` de patrones_finitos, menores_uniformes, grados_ponderados y ciclo_exterior, respectivamente.
- [B02] y [B03] son los originales `fuentes/velocidad_via2_ronda18_…/latex/02_grados_y_radio.tex` y `03_mascara_y_media.tex`. No uso las transcripciones de r19.
- [A03] es `fuentes/velocidad_via2_margenes_y_atomos_…/latex/03_atomos_fisicos.tex`.
- [R10-0n] es `fuentes/velocidad_via2_ronda10_…/latex/0n_*.tex`, y [S04] es `fuentes/velocidad_via2_grafo_termino_…/latex/04_suelos.tex`.
- [TEO], [MAPA], [CONST] y [NOT] son `r21/consolidado/TEOREMA.md`, `MAPA.md`, `CONSTANTES.md` y `NOTACION.md`. [T2.2] es `r21/piezas_T2/02_cofactor/GUIA.md`.
- [W2j] es `rev_exp/W2_jets/ACTA.md` y [W2t] es `rev_exp/W2_tipos/ACTA.md`.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Naturaleza del resultado |
|---|---|---|---|
| 1 | Paso de v fijo a 5 ≤ v ≤ 8 log n [02] | **Correcta con precisión** | Demostrado como implicación de las identidades locales y de los mayorantes de clase importados. Rellena correctamente [W2j 164]. |
| 1a | Qué se prolonga y desde qué datos comunes | **Correcta con precisión** | Se prolongan los coeficientes f_l = [s^l]H_q como funciones de las activaciones, por el teorema de identidad. Falta citar, en lugar de una tabla ausente, la identificación del germen con la rama del origen (precisión 1.1). |
| 1b | Corte de X03 para el cambio de q | **Correcta** | (u^{q+1}) entre aproximantes y (s^{q−1}) tras Stirling y la división por s. Se conservan los coeficientes hasta s^{4v+10}, y los grados leídos son ≤ c+1 ≤ v/2+1. El corte es nítido en un modelo exacto (c1). |
| 1c | Uniformidad de las constantes | **Correcta** | Constantes de clase y n₀(b). El radio ρ_v del germen no interviene. Condicional a los mayorantes G02–G04 y B02 y a T2.2. |
| 1d | Ideal del ciclo y ganancia de rango en varios ciclos | **Correcta** | El ideal (∏_U ζ_i·∏_𝒞 ζ_i) pasa al polidisco por restricciones a caras. El sector β ≥ 2 conserva p = v+c−1 con el factor ∏d_i, sin suponer ninguna cancelación. |
| 2 | Corolario [01] | **Correcta con precisión** | El límite nulo se sigue sólo de R21. a(0) = 0 exige además la reducción de R10 (H2–H3 en K) y la expansión. |
| 2a | n·R_Q/log n → 0 y c = 0 | **Correcta** | Consecuencia inmediata de R21. |
| 2b | Expansión ponderada ⇒ (a(0)/2)(log n)/n + O(1/n) ⇒ a(0) = 0: suma armónica, Dini, nivel M | **Correcta con precisión** | Cuentas correctas. Dini es suficiente pero no necesaria para a(0) = 0 (precisión 2.2). |
| 2c | Identificación con el criterio de suelos | **Correcta con precisión** | Transcripción fiel y lógica condicional correcta. «Usa Pr(S_M∖G) = O(1/K)» debe leerse «supone» (precisión 2.3). |
| 2d | Qué da sólo el teorema y qué exige la hipótesis | **Correcta con precisión** | La lista de hipótesis de [01 50] omite H2–H3 en el nivel K, que R21 no aporta (precisión 2.1). |
| 3 | Cálculos exactos pequeños | **Realizados** | Dos programas, 12,9 s de CPU en total. Son evidencia, no prueba, y no muestran ninguna discrepancia. |

**No he encontrado ningún enunciado falso ni ningún hueco de prueba.** Las precisiones (1.1–1.3 y 2.1–2.3) son de redacción, de cita o de alcance de las hipótesis. Ninguna obliga a cambiar enunciados ni constantes.

## 2. Detalle por punto

### Punto 1 · De v fijo a 5 ≤ v ≤ 8 log n [02]

**Por qué hace falta el paso.** Las identidades se prueban localmente:
- en un polidisco cuyo radio puede depender de v, y sin exigir que las activaciones de tamaño creciente estén dentro [P01 22–25; P03 14, 49–51; P05 32–37, con ρ_v en 33];
- como implicación formal a campo fijo, en la rama local cerca de campos nulos [U06 2, 7, 76–78; Z01 6–7, 56–59; Z02 45].

En cambio, la cota se estima en el polidisco de clase |s| < κ/v, |ζ_i| < κ′/d_i [G02 22–24, 52–56; B02 52–60; U08 9–23]. G05 18–19, B03 47–51 y U08 31–34 pasan de lo primero a lo segundo sin escribirlo; es la precisión 2.1 de [W2j 159–164]. El radio por sitio importa: con un radio común κ′/v, Cauchy daría un factor v^v que ningún recuento compensa [W2t 98].

**1a. Qué se prolonga exactamente, y desde qué datos comunes.**
- **Qué se prolonga.** Para cada U fijo, en una máscara fija:
  - los coeficientes f_l(ζ) = [s^l]H_q(s,ζ) del aproximante de orden q = 4v+12, con l < w;
  - en la clase unicíclica, además, las restricciones f_{c−1}|_{ζ_i=0} y ∂_{ζ_i}f_{c−1}|_{ζ_i=0} para i ∈ 𝒞 [02 42–45, 56–58].

  Son funciones holomorfas de las activaciones independientes en el polidisco de clase: Cauchy en s sobre la holomorfía conjunta en |s| < κ/v [02 39–43; G04 34–35; B02 52–59]. El polidisco y sus caras son conexos, así que el teorema de identidad lleva el germen nulo en el origen a todo el dominio.
- **La pertenencia al ideal monomial.** En un polidisco, f ∈ (∏ζ_i^{m_i}) equivale a ∂^k_{ζ_i}f|_{ζ_i=0} ≡ 0 para k < m_i. La serie de Taylor converge en todo el polidisco y sólo contiene monomios con esas multiplicidades. Por eso basta prolongar las restricciones a las caras, como hace [02 56–59]. La observación de que no bastaría una identidad comprobada sólo en las activaciones físicas [02 59] es correcta.
- **Qué no se prolonga.**
  - Nada en s del conteo exacto: sólo el aproximante es holomorfo en s [02 81; B03 36–37; G04 44; Z02 65–66].
  - Nada en v ni en j: cada U se trata por separado, la identidad es cualitativa y el radio ρ_v desaparece [02 46].
- **Datos comunes a las 2^v caras.**
  - El exterior A∖U, sin los v sitios incluso en las caras que desactivan exclusiones [U07 2–3].
  - El campo afín, que sólo depende del exterior [U07 53; B03 10].
  - El cofactor de U07: en ζ_i = 0 se tiene x_i = 0 y la columna i tiende a e_i [U07 51–58].
  - Los datos balanceados y la misma rama [X03 2; 02 19], con el mismo valor basal del logaritmo [02 29; X03 21, 28].
  - El mismo q en las dos evaluaciones [B03 19–20].
  - c y β, que se calculan en el grafo de incidencia completo de U y son comunes a todas las caras [P01 41–43].
- **Precisión 1.1 (identificación del germen).** La hipótesis de [02 44] se refiere al germen en el origen de la función definida en todo el polidisco de clase, pero las fuentes prueban las identidades para la «rama del origen» en un polidisco menor. Ambas coinciden por tres razones:
  - la silla local es única en la caja y se obtiene por contracción [G02 55–56];
  - el equilibrio exterior es único y holomorfo [B02 43–50], y en ζ = 0 se tiene x = 0;
  - la rama del logaritmo se fija por continuación desde el centro real [B02 50; U02 54–55].

  [02 15–16] remite para esto a una «tabla de cierre» que no está en el material. Con las citas anteriores la identificación es verificable. Se repara con una frase; no es un hueco.

**1b. El corte que identifica X03.**
- **Antes de sustituir.** Para Q ≥ q, H_Q − H_q y log H_Q − log H_q están en (u^{q+1}) [X03 18–21]. Usa tres hechos:
  - V_l es divisible por u^l [X03 6];
  - ord_u μ_i ≥ ⌈i/2⌉ [X03 9–14], de modo que los índices i ≥ 2q+1 ya llevan u^{q+1};
  - H(0) = d(1) ≠ 0.

  Rehíce la inducción: ord μ_{i+1} ≥ 1 + mín(⌈i/2⌉, ⌈(i−1)/2⌉) = ⌈(i+1)/2⌉, porque 1 − iu es una unidad.
- **Después de sustituir.** Los pasos son:
  - u = s/(1−θ_0), con θ_0 = s|X|; es el tamaño m = j − |X| del menor [G03 12–14, 41; B03 4];
  - la sustitución común de parámetros holomorfos y la suma finita de átomos;
  - el logaritmo con valor basal invertible;
  - Stirling truncado antes del grado q y una división por s.

  Al final la diferencia está en (s^{q−1}) [X03 26–30]. Los coeficientes [s^l] coinciden, pues, para l ≤ q−2 = 4v+10.
- **Lo que añade [02].** [02 24–31] lo reproduce fielmente y añade, con razón, que la congruencia es de gérmenes conjuntos en (s, ζ). Por eso pasa a las restricciones a caras y a las derivadas en los campos: F = s^{q−1}G con G holomorfa, por división de Hadamard.
- **Grados leídos.**
  - Son ≤ c+1. Todo sitio pertinente tiene un vecino diagonal en U, porque si no su proyección es nula [P01 43–46; G05 30–31; W2t 110]. Cada componente tiene, pues, al menos dos sitios, c ≤ v/2 y c+1 ≤ v/2+1 ≤ v < q−1 [02 33–35].
  - El margen es amplio. Incluso sin esa observación, c ≤ v da c+1 ≤ v+1 ≤ 4v+10.
- **La advertencia de [02 33].** «No se compara con un corte antiguo menor que el grado leído» es necesaria. En un modelo genérico exacto (c1), el orden de H_Q − H_q es exactamente q+1. Tras Stirling y la división por s es exactamente q−1 cuando q es impar, y q cuando es par. El corte de X03 es, pues, óptimo en general, y [02] sólo usa grados muy por debajo.
- **Alcance de X03.** X03 se limita al álgebra y no da mayorantes [X03 32–34]. Es coherente con [02 35–36]: las constantes de un aproximante de orden Q no entran, y H_Q sólo hace falta como germen cerca del origen.

**1c. Uniformidad de las constantes.**
- **Constantes de clase.** Son de clase, independientes de v, b y ρ [02 75; CONST 4; W2j 91–93]:
  - los radios κ/v y κ′/d_i;
  - la cota C^v de H_q, obtenida de 2^v caras con un logaritmo O(v) cada una [02 39–41];
  - la cota física |ζ_i| ≤ C/j [G02 65–66].

  Son entradas importadas que W2j certificó en su punto 1, con su precisión 1.1 sobre K₁.
- **Lo que no añade constantes.** Ni la continuación ni X03 añaden constantes, y ρ_v no aparece en la cota final.
- **Condiciones en el punto físico.** Son Cv/j ≤ 1/2, Cd_i/j ≤ 1/2 (con d_i ≤ v) y Cq ≤ √j, con q ≤ 32 log n + 12 [02 76–77]. Se cumplen en todo 5 ≤ v ≤ 8 log n desde un n₀(b). Para sumar los átomos físicos de todos los soportes se usa Cq ≤ j^{1/3} [02 80–81; A03 36–39], es decir, T2.2. Su dictamen externo sigue pendiente [T2.2 7], así que es una entrada importada.
- **Rehíce Schwarz y Cauchy** [02 64–73].
  - Bosque: C^v∏t_i·z^{c+1}.
  - Un ciclo: la cola C^v∏t_i·z^c y el término aislado C^v z^{c−1}∏t_i∏_𝒞t_i, con ∏_𝒞 t_i ≤ Σ_U t_i ≤ Cv²/j (basta t_i ≤ 1).
  - Varios ciclos: C^v∏t_i·z^{c−1}.

  Con z ≤ Cv/j y t_i ≤ Cd_i/j salen los exponentes p = v+c+1, v+c y v+c−1, todos dentro de C^v(Cv)^{c+1}∏d_i·j^{−p}.
- **Error físico.** 2^v·e^{Cv}((Cq/j)^q + Ce^{−c₀j}) ≤ C^v j^{−(2v+6)} ≤ C^v j^{−p}, porque p ≤ v+c+1 ≤ 3v/2+1 [02 78–79; G04 36–44; W2j 86]. Para átomos positivos, A03 18–21 da incluso η_v sin el factor e^{Cv}.
- **Orden de elección.** Clase, después ρ y b, después n₀(b) [02 75–77; CONST 4, 8]. Es coherente.

**1d. Ideal del ciclo y ganancia de rango.**
- **Ideal.**
  - Como germen, f_{c−1} ∈ (∏_U ζ_i·∏_𝒞 ζ_i). Viene de log(1−θ²) ∈ (∏_𝒞 ζ_i²) [Z01 56–59; Z02 45–48; U06 62–69; P05 27–30] y de la proyección 𝒰 [Z02 58–64; P05 38–44].
  - Los operadores ζ_i∂_{ζ_i} conservan (ζ_i²) [02 55; B02 25–26].
  - La continuación por caras [02 56–58] y la congruencia de X03 [02 30–31] lo llevan a todo el polidisco de clase.

  El factor adicional ∏_𝒞 t_i [02 66, 69–72] es, pues, legítimo con los radios de clase.
- **Rango.** El lema de rango [P06 24, 28–30, 36–37; W2t 28, 57–62] es combinatorio, sobre tipos: L_g ≥ mín(β_g,2) y D ≤ p−1. Lo que el análisis tiene que aportar en el sector β ≥ 2 es p = v+c−1 con el prefactor C^v(Cv)^{c+1}∏d_i y constantes de clase. [02] da exactamente eso:
  - sólo prolonga la anulación por debajo de c−1, que viene de la cuenta de incidencias [P03 42–53; P05 1–6; W2j 121–123];
  - no supone ninguna cancelación del coeficiente s^{c−1}, que puede sobrevivir [02 60–61];
  - trabaja en una máscara fija, antes de integrar en ν [02 82];
  - conserva el factor ∏d_i del radio por sitio.

  La ganancia Σ_g mín(β_g,2) ≥ 2 sigue cerrando, por tanto, b = p−D−1 ≥ 0 en el uso de G06–G07 [W2t 129–133].

**Precisión 1.2 (notación).**
- H_q denota en [02 7] la proyección alternada en (s, ζ), y en [X03 16] el aproximante de la mezcla de un menor ([NOT 8] lo llama H_Q).
- d_i es en [02 3] y [G02 6] el máximo tamaño de una fibra (el d_i* de U08 3), y en [U07 9] y [Z01 5] el número de factores incidentes.

No tiene consecuencias matemáticas.

**Precisión 1.3 (fuentes ausentes).** [02 15–16] y [02 87] remiten a la «tabla de cierre» y a la «lista de precisiones» de r22, que no están en el material; sólo figuran sus huellas. He identificado su contenido pertinente en las fuentes (1a). No hace falta para la validez del paso.

### Punto 2 · El corolario [01]

**2a. Sólo del teorema.** [TEO 3] da δ y b admisibles, C_{b,δ} y n₀ con |R_Q(n)| ≤ C_{b,δ}/n.
- **El límite.** De ahí sale |n·R_Q/log n| ≤ C_{b,δ}/log n → 0 [01 17].
- **El coeficiente c.** Si R_Q = c(log n)/n + O(1/n), el cociente tiende a c, luego c = 0 [01 12, 18]. Es correcto. De hecho n·R_Q = O(1), así que c = 0 incluso si el resto es sólo o((log n)/n).
- **Alcance.** Q(n) y Q_pred(n) no dependen de (b, δ), así que basta un par admisible.
- **Lo que no da.** La convergencia de n·R_Q no se sigue [01 20; TEO 11].

**2b. La expansión ponderada.**
- **Transcripción.** Coincide con la fuente:
  - K, M, ν̄, G, ω_{k,i} y el estimador de fila [01 23–27] coinciden con [R10-06 4–6, 28–30];
  - los corchetes ⟨·⟩ llevan el indicador del padre vivo (la convención de subprobabilidad) [R10-02 14];
  - V_e^{(3)} es la de [R10-02 36];
  - la reducción R_Q = Σ_{k=K+1}^M m_{n,k} + O_δ(1/n) es el recuadro de [R10-06 34–36];
  - R10 ya anunciaba c_log = a(0)/2 [R10-06 44–45].
- **Suma armónica.** Σ_{K<k≤M} 1/k = log(M/K) + O(1/K), y log(M/K) = ½ log n + log δ + O(n^{−1/2}) porque K/√n ∈ [1, 1+1/√n) y M/n ∈ [δ, δ+1/n). Por tanto (a(0)/n)Σ1/k = (a(0)/2)(log n)/n + O_δ(1/n) [01 46–48]. Es correcto. En c2, K·E(n) ∈ [−0,500; −0,433] para n entre 10³ y 10⁸+1, con E(n) = Σ_{K<k≤M}1/k − log(M/K).
- **Cota de Dini** [01 39–41]. Con η no decreciente, ∫_{k/n}^{(k+1)/n}η(u)du/u ≥ η(k/n)·log(1+1/k) ≥ η(k/n)/(k+1) ≥ η(k/n)/(2k). Al sumar queda ≤ 2∫_0^{x₀}η(u)du/u. Si «monótona» significase no creciente, la condición de Dini obligaría a η ≡ 0 cerca de 0 y la desigualdad sería trivial. No hay problema.
- **Parte alejada de cero.** Es ≤ 2 sup|a|·(log(δ/x₀) + O(1)), una suma armónica de razón fija [01 42]. Usa que a está acotada en la banda [01 34].
- **Nivel redondeado M** [01 43–44]. Como (M−1)/n < δ, sólo el término k = M puede tener k/n > δ: es un único término. Su tamaño es O(1/n²), por cualquiera de dos vías:
  - la cota absoluta |D_i| ≤ C/k² [R10-06 14–15], que sigue valiendo con el peso ω [R10-06 31–32];
  - una prolongación acotada de a.

  En c2 su aportación a n·S(n) es ≈ 5/n.
- **Restos.** Σ O(k^{−3} + n^{−2}) = O(K^{−2} + M/n²) = O_δ(1/n) [01 45]. Es correcto.
- **Conclusión.** R_Q = (a(0)/2)(log n)/n + O_δ(1/n), y con 2a se obtiene a(0) = 0 [01 50]. Es correcto bajo las hipótesis; véase 2d.
- **Precisión 2.2 (Dini no es necesaria para a(0) = 0).** Basta que a sea continua en 0, acotada e independiente de n, con resto uniforme. En efecto, para cada ε,
  - Σ_{K<k≤M}(a(k/n) − a(0))/k ≤ ε(½ log n + 1) + C_ε, así que es o(log n);
  - luego n·R_Q = (a(0)/2)·log n + o(log n);
  - y R21 obliga a a(0) = 0.

  Dini (o Hölder [R10-05 19–20, 39–40]) sólo hace falta para la forma con resto O(1/n). Lo ilustra c2 con un módulo continuo que no es de Dini:
  - el resto crece como log log n: T_N pasa de 0,535 a 1,179;
  - pero T_N/log n pasa de 0,078 (n = 10⁴) a 0,064 (n = 10⁸), y R_N/log n de −0,127 (n = 10³) a −0,011, hacia 0.

  Es coherente con [R10-05 40]: la mera existencia de a(0) no da el resto O(1/n).

**2c. Identificación con el criterio de suelos** [01 53–75; S04 2–16, 27–47].
- **Transcripción.** Es fiel:
  - B_n(t) y H_n(t) [S04 4, 31] y la composición de Φ [S04 28–29];
  - el criterio límite [S04 37–38], con a_s para la hipótesis sin peso E[D_k; vivo, S_M] = a_s(k/n)/(nk) + … [S04 10–12], distinta de la de m_{n,k};
  - el resto diádico C_δ/t² [S04 15];
  - la resta de potenciales, O(1) uniforme en t, en los dos extremos [S04 33, 40–41].

  El orden de los límites es el correcto: primero m fijo, luego limsup en n, luego m → ∞.
- **Qué exige la identificación de a_s(0) con a(0).** Comparar las sumas con peso y sin peso hasta o((log n)/n). Como |X| ≤ C/K, |E[X; S_M∖G]| ≤ (C/K)·Pr(S_M∖G) [R10-06 15, 39–41]:
  - Pr(S_M∖G) = O(1/K) da O(1/n) [01 71–73];
  - bastaría o(log n/√n).

  La conclusión a_s(0) = 0 [01 74] es correcta bajo la identificación y la expansión ponderada.
- **Precisión 2.3.**
  - En la fuente, la condición es un supuesto («Si Pr(S_M∖G) ≤ C/K» [R10-06 39]), y [R10-06 49] advierte que H3 sola no acota la probabilidad de ese suceso. En [01 72], «usa» debe leerse «supone».
  - El criterio vive en j = ⌈tK⌉ ≍ √n, donde R21 no da ninguna estimación (su j es ⌊bn⌋). Los controles de R12 [S04 7–8, 22–23] son hipótesis. El texto lo reconoce [01 62–63, 75], pero conviene no reutilizar la letra j.

**2d. Qué da sólo el teorema y qué exige la hipótesis.**

| Conclusión | Qué la sostiene |
|---|---|
| n·R_Q = O(1), luego n·R_Q/log n → 0 y c = 0 en todo desarrollo c(log n)/n + o(log n/n) | Sólo R21 [TEO 3] |
| Existencia o valor de lím n·R_Q | No se sigue [01 20; TEO 11] |
| R_Q = Σ_{K<k≤M} m_{n,k} + O_δ(1/n) | H2–H3 en el nivel K = ⌈√n⌉ [R10-06 10–13, 24–25] y la identidad por fila [R10-02 35–38]. La versión por historia exige además el control centrado de salidas [R10-05 15–17]. |
| a(0) = 0 | R21, la reducción anterior y la expansión con resto uniforme, a acotada e independiente de n, y continuidad en 0 (Dini es suficiente, no necesaria) |
| R_Q = (a(0)/2)(log n)/n + O_δ(1/n) | La reducción, la expansión y Dini (sin R21) |
| a_s(0) = 0 | Lo anterior, más la identificación (por ejemplo Pr(S_M∖G) = O(1/K)), los controles de R12 y la expansión sin peso con a_s continua en 0 |

**Precisión 2.1 (lista de hipótesis).** [01 50] dice que «la expansión y la condición de Dini son hipótesis», pero la reducción [01 35–36] es sólo una implicación bajo H2 y H3: «no prueba estas dos entradas» [R10-06 24–25]. R21 no las aporta:
- su extremo está en j = ⌊bn⌋ [TEO 9; CONST 8];
- sus errores terminales son O(1/j): las torres [TEO 9; MAPA 9] y los pares con resto de grado ≤ 4 [MAPA 13];
- en j = K esos errores son O(n^{−1/2}), mientras que H2 pide C/n.

El texto sí dice que la reducción usa H2–H3 [01 35], así que no es un hueco oculto. Pero [01 50] debería decir: «la reducción (H2–H3 en K), la expansión y la continuidad o Dini son hipótesis». Hay una lectura equivalente e informativa: bajo R21, si la expansión vale con a(0) ≠ 0, entonces H2 o H3 fallan en el nivel K.

### Punto 3 · Cálculos (código en `codigo/`, salidas en `resultados/`)

| Programa | Qué comprueba | CPU medida |
|---|---|---|
| `c1_truncacion_X03.py` | X03 en un modelo genérico, con series racionales exactas. (a) ord μ_i = ⌈i/2⌉ exactamente para i = 2…88. (b) ord(H_Q−H_q) = ord(log H_Q − log H_q) = q+1 exactamente, para 11 pares (q, Q) hasta q = 32 = 4·5+12. (c) La composición con átomos h = 0, 1, 2, u = s/(1−hs), logaritmo basal, Stirling y división por s da orden ≥ q−1, exacto q−1 con q impar. (d) Margen c+1 ≤ v/2+1 frente a q−2 = 4v+10. | 7,18 s |
| `c2_armonica_dini.py` | Cotas rigurosas con enteros de 96 bits y redondeo dirigido, con log rigurosos por series racionales, para δ = 1/4 y n entre 10³ y 10⁸+1. K·E(n) ∈ [−0,500; −0,433]. Con el módulo de Dini escalonado η_D = 1/(m+1)²: T_D ∈ [0,146; 0,224], muy por debajo de la cota de Dini 0,894, y R_D(n) = n·S(n) − ½ log n acotado (de −1,265 a −1,163). Con el módulo no Dini η_N = 1/(m+1): T_N crece de 0,535 a 1,179, pero R_N/log n → 0. El término k = M, para 4 ∤ n, aporta ≈ 5/n a n·S(n). | 5,67 s |

Es evidencia en casos concretos, no una prueba. Las afirmaciones se prueban en el punto 1 (1b) y en el punto 2 (2b).

## 3. Cuantificadores, ley y tamaño

- **[02].**
  - Es determinista: una máscara fija de la clase de referencia y un U fijo.
  - s es complejo sólo en el aproximante; en el punto físico s = 1/j, con j = ⌊bn⌋ y b fijo.
  - Los átomos son menores de tamaño m = j−|X|, con s_m = s/(1−θ_0) y θ_0 = s|X| [G03 41]. Todos usan el mismo q = 4v+12 [B03 19–20].
  - No interviene ninguna ley. La integración contra ν con el indicador H_j es posterior [02 82] y pertenece a [W2t].
  - Orden de las constantes: clase, luego ρ y b, luego n₀(b).
- **[01].**
  - R21 vale para (b, δ) admisibles fijos (enunciado existencial [TEO 3]) y n ≥ n₀. R_Q es un número que no depende de la ley.
  - La reducción vive bajo ν̄: ν hasta M y ν^{u_T} en la banda. Sus sumandos son subprobabilidades con el peso ω, y k recorre (K, M], con K = ⌈√n⌉ y M = ⌈δn⌉.
  - El criterio de suelos usa j = ⌈tK⌉, que no es el j de R21. Los límites se toman con m fijo, luego limsup en n, luego m → ∞.

## 4. Estados

- **Demostrado (cada paso rehecho):**
  - la continuación en las activaciones y la pertenencia al ideal por caras;
  - la transferencia de X03 entre órdenes de truncación;
  - las cotas de Schwarz y Cauchy con los tres exponentes y la uniformidad para 5 ≤ v ≤ 8 log n;
  - el corolario 2a;
  - en 2b, la suma armónica, la cota de Dini, el nivel M y los restos.
- **Condicional (entradas importadas, fuera de mi parte):**
  - los mayorantes de clase G02–G04 y B02 (W2j, punto 1);
  - las identidades locales P03–P05, U06–U07 y Z01–Z02 (W2j, punto 2);
  - T2.2, con dictamen externo pendiente;
  - Δ_q y los menores (E1);
  - el teorema de R21 mismo [TEO 11];
  - H2–H3 en K (R9 y R10), el control de salidas y los controles de R12;
  - la expansión ponderada y la regularidad de a.
- **Evidencia exacta en casos concretos:** c1 y c2.
- **No verificable aquí:** la tabla de cierre y la lista de precisiones de r22, que no están en el material. Su contenido pertinente es localizable en las fuentes.
- **Heurístico:** nada.

## 5. Dictamen global sobre mi parte

**Certificada con precisiones.**
- **[02].** Escribe correctamente el paso que W2j había dejado implícito: la continuación analítica de las identidades locales al polidisco de clase, con X03 para el cambio de q y constantes uniformes en 5 ≤ v ≤ 8 log n. Conserva el ideal del ciclo y la ganancia de rango del sector β ≥ 2.
- **[01].** Deduce correctamente de R21 que la pendiente logarítmica es nula, y, bajo hipótesis explícitas, que a(0) = 0.

Las precisiones son seis, y ninguna obliga a cambiar enunciados ni constantes:
- 1.1: citar la unicidad de la rama (G02 55–56, B02 43–50, U02 54–55) para identificar el germen, en vez de una tabla ausente;
- 1.2: las colisiones de notación de H_q y d_i;
- 1.3: las referencias a documentos de r22 que no están en el material;
- 2.1: añadir H2–H3 en el nivel K, y el control de salidas en la versión por historia, a la lista de hipótesis de [01 50];
- 2.2: para a(0) = 0 basta la continuidad de a en 0, y Dini sólo hace falta para el resto O(1/n);
- 2.3: Pr(S_M∖G) = O(1/K) es un supuesto, no un resultado de R10.

## 6. Resumen final

- Las huellas de 01 y 02 coinciden con `r22/SHA256SUMS_entrega`. Las fuentes usadas no tienen discrepancias; los archivos ausentes no se usan.
- **Punto 1 [02]: correcta con precisión.**
  - Para cada U fijo, en una máscara fija, se prolongan los coeficientes f_l = [s^l]H_q del aproximante, y en un ciclo las restricciones a caras de f_{c−1} y sus derivadas normales. Son funciones holomorfas de las activaciones en el polidisco |ζ_i| < κ′/d_i, y la prolongación es por el teorema de identidad.
  - Los datos comunes son el exterior A∖U, el campo afín, el cofactor U07, la rama, el valor basal y q = 4v+12.
  - Nada se prolonga en s del conteo exacto, ni en v ni en j.
  - X03 da (u^{q+1}), y (s^{q−1}) tras θ_0, los átomos, el logaritmo basal, Stirling y la división por s. Se conservan los coeficientes hasta s^{4v+10}; los grados leídos son ≤ c+1 ≤ v/2+1.
  - Las constantes son de clase; ρ_v no interviene; n₀(b) da Cv/j, Cd_i/j ≤ 1/2 y Cq ≤ √j (j^{1/3} en T2.2).
  - El ideal (∏_Uζ·∏_𝒞ζ) pasa al polidisco. En varios ciclos queda p = v+c−1 con ∏d_i y sin cancelación, así que el lema de rango sigue cerrando.
  - Precisiones: la identificación del germen con la rama del origen debe citarse (G02 55–56, B02 43–50) en vez de una tabla ausente; colisiones de notación.
- **Punto 2 [01]: correcta con precisión.**
  - R21 da n·R_Q = O(1), luego n·R_Q/log n → 0 y c = 0.
  - Suma armónica, cota de Dini, nivel M (un solo término, O(1/n²)) y restos O(K⁻² + M/n²): correctos. De ahí a(0) = 0.
  - Precisión 2.1: la reducción R_Q = Σm_{n,k} + O(1/n) exige H2–H3 en K = ⌈√n⌉, que R21 no da (su extremo es ⌊bn⌋ y sus errores O(1/j) valen O(n^{−1/2}) en K). Hay que añadirlas a la lista de [01 50].
  - Precisión 2.2: para a(0) = 0 basta la continuidad de a en 0; Dini sólo da el resto O(1/n).
  - Precisión 2.3: la identificación con el criterio de suelos es correcta como condicional, pero Pr(S_M∖G) = O(1/K) es un supuesto de R10, no un resultado.
- **Cálculos (12,9 s de CPU, exactos).**
  - c1: el orden de H_Q − H_q es exactamente q+1, y q−1 tras Stirling con q impar. El corte de X03 es nítido, y [02] usa grados muy inferiores.
  - c2: K·E(n) ≈ −½; el resto con el módulo de Dini queda acotado; con un módulo no Dini crece como log log n, pero es o(log n).
- **Dictamen global: certificada con precisiones.** No hay ningún enunciado falso ni ningún hueco. Es condicional a las entradas importadas: G02–G04 y B02, P03–P05, U06–U07, Z01–Z02, T2.2, E1, R21, H2–H3 y R12.

## Anexo · Huellas de los archivos de esta revisión (SHA256)

```
00a6394855a1ca97ea6cfef69a9160ed4a957a13bc80266d0b669a2b5d33d45c  codigo/c1_truncacion_X03.py
dbfcb641d34118c8ce96027cd1688ab58f61e2fba0ce93af8e9d594b40576b14  codigo/c2_armonica_dini.py
aa41fd3697a7d2d47a4c266f088ef784c29a919fbf045d642b73946565c789d2  resultados/c1_truncacion_X03.txt
17f045877db2cc928869dfb7ba3edff4508050f9960ab0c2064cecb39527be74  resultados/c1_truncacion_X03_tiempo.txt
abeeaacb69b5d8211e461529f03de3ac394751d8fc278c5cbba41447b8b64393  resultados/c2_armonica_dini.txt
3aa29c33cb3019f7d319acca91525a3617c356bd3276859e98fa484551976861  resultados/c2_armonica_dini_tiempo.txt
```

Para reproducir, desde `rev_exp/W2_t4/`: `nice -n 10 python3 -I codigo/<programa>.py`. Los tiempos de cada ejecución están en `resultados/*_tiempo.txt`.
