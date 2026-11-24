# Acta de revisión externa · W2_torres: error puro de torres, extensiones de R8–R9 e identidad de Schur de T/08b

**Objeto.** Los cinco puntos de `rev_exp/encargos/W2_torres.md`, con la parte común de `rev_exp/encargos/comun_ext.md`. El coordinador amplió el encargo durante la revisión con dos preguntas sobre `rev_exp/r21/piezas_T2/03_torres/`:
- el atajo q = 2 para el uso puntual en H03;
- la separación entre ese uso y el de K08 y M07 en la prueba de M01.

No reviso E1, E2, el recuento de tipos, el exponente 7 ni la cota por soporte.

**Revisor.** Externo al proceso que escribió las pruebas. Sin web; sólo la carpeta de trabajo. 17-11-2026.

**Dictamen global sobre esta parte: CERTIFICADA CON PRECISIONES** (§3). No he encontrado ningún enunciado falso ni ningún hueco de prueba en las piezas de mi encargo. Las reservas son entradas previas que no dictamino y precisiones de enunciado y de cita.

## 0. Alcance, integridad, convenciones y método

**Integridad.**
- `sha256sum -c r19/SHA256SUMS`: 116/116 correctos.
- Fuentes completas con su propio manifiesto: ronda 8, 30/30; ronda 9, 98/98; `menores_uniformes`, 14/14; `media_matriz`, 14/14.
- `r21/piezas_T2/03_torres/`: sus cuatro archivos pasan el manifiesto de r21. La copia de r21 en esta carpeta es parcial: faltan las demás entradas de su manifiesto, entre ellas `fuentes/latex/G03.tex`. Leo G03 sólo como transcripción, en `prueba_fuente.md`:188–235, cuya huella de origen declarada (60d8f5f2…) no puedo recomputar.
- Copias de las rondas 1–3 fuera de `rev_exp/` (`via2r1/`, `via2r2/` y `via2r3/` de la carpeta de trabajo):
  - `mascara.tex`, `permanente.tex`, `traza.tex`, `07_triples.tex` y `10_corrector.tex` coinciden con las huellas que declara `fuentes/…ronda9…/FUENTES.md`:10–14;
  - `torres_fila.tex` pasa el manifiesto de su ronda;
  - `08b_exterior.tex` coincide con `CATALOGO_LITERAL.md`:33.

  Sólo las uso para comprobar las entradas que citan E01 y K07. No forman parte del expediente.
- La carpeta `r21/` apareció durante la revisión (12:42). Sólo consulté `piezas_T2/03_torres/`, por indicación del coordinador.
- No he modificado nada fuera de `rev_exp/W2_torres/`.

**Abreviaturas.** Cito la línea del archivo fuente, salvo para los originales del expediente.
- **E01, E02, E03, R8/04:** `fuentes/velocidad_via2_ronda8_20261116T072748Z/latex/01_enunciado.tex`, `02_expansion.tex`, `03_cancelacion.tex` y `04_rectangulo.tex`.
- **K02, K03, K06, K07, K08, K09, K11:** `fuentes/velocidad_via2_ronda9_20261116T082611Z/latex/02_quitar.tex`, `03_funcional.tex`, `06_torres.tex`, `07_coeficiente.tex`, `08_estabilidad.tex`, `09_rectangulo.tex` y `11_vetos.tex`.
- **U01–U05:** `fuentes/velocidad_via2_menores_uniformes_20261117T042237Z/latex/01…05`. Su numeración coincide con la «orig.» de `originales/U`.
- **MM01–MM09:** `fuentes/velocidad_via2_media_matriz_20261116T150154Z/latex/`.
- **G03:** `r21/piezas_T2/03_torres/prueba_fuente.md`. Su línea original es la del archivo − 192.
- **REP:** `r21/piezas_T2/03_torres/REPARACION_DE_DEPENDENCIA.tex`. **GUIA:** `r21/piezas_T2/03_torres/GUIA.md`.
- **R1/x:** `via2r1/copia/latex/x.tex`. **R2/10:** `via2r2/copia/latex/10_corrector.tex`.
- **Originales del expediente** (T05, T08b, D04, H03, A04, CP/07d): «orig. N» es la línea N+7 del archivo `.md`, como hace el expediente.

**Estados.**
- *Demostrado*: lo he comprobado aquí, a mano o con un cálculo exacto.
- *Condicional*: depende de una entrada que no dictamino.
- *Numérico*: es sólo evidencia de cálculo.

**Método.**
1. Lectura línea a línea de E01–E03, K02, K06–K08, K11, U01–U05, G03, REP, GUIA, MM01–MM03, MM05, MM07, T01, T04–T08c y D04, y de las entradas R1/permanente, R1/mascara, R1/traza, R1/torres_fila y R2/10.
2. Verificación a mano de las identidades exactas.
3. Cálculos propios (`codigo/`, salidas en `resultados/`):
   - conteos de permanentes enteros exactos;
   - resto en `decimal` a 80 cifras o en fracciones exactas;
   - sólo C3 usa complejos en doble precisión.

   Un proceso cada vez, con `nice -n 10` y el tiempo medido (§2.6). No hay azar en ningún cálculo. No había mpmath ni sympy y no instalé nada.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Motivo breve |
|---|---|---|---|
| 1 | Error puro de torres O(1/j) en la máscara de llegada (E01; U05; papel de K06–K07) | **Correcta con precisión** | E01 da \|g_T\| ≤ C(M,r)/k. Verifiqué a mano su cota \|Ξ\| ≤ Cq₄/k, las identidades de E02–E03 y el cero de U05. El orden k⁻² de E01 se confirma con conteos exactos en cinco familias, una de ellas con P ≠ D. Es condicional a la extracción de R1 desde Divoux–Wang y a la clase en H_j (D04/A01). K06–K07 no hacen falta para la cota puntual. |
| 1b | Atajo q = 2 de r21 (G03/U05) para H03 | **Correcto y suficiente para ese uso** | \|g_T − G₂(1/j)\| = O(j⁻³) + Ce^{−cj}. G₂(0) = 0 y G₂ es holomorfa y acotada en un disco fijo, así que \|G₂/u\| ≤ C′ por Schwarz. No sustituye las diferencias entre menores que usa M01. |
| 2 | K06/K08 extendido a menores con la casilla de cruce ausente y a cuatro supresiones | **Correcta con precisión** (de enunciado, no de prueba) | Ningún paso de K08 usa que el cruce esté en el soporte. Cuatro supresiones son cuatro aplicaciones con constantes de clase heredadas (D04 orig. 45–56; K02). Numérico: O(k⁻³) en un paso, en sucesiones de cuatro y en el montaje de M07. |
| 3 | Fórmula de K07 prolongada a medidas complejas μ_h | **Correcta con precisión** | Hay holomorfía y \|u_T\| ≤ Cs en un bidisco fijo: Newton con inverso congelado en supremo, Neumann y φ definida por integrales bilineales. En los vértices coincide con u_T de los menores. Está escrita de forma esquemática. Numérico: los vértices coinciden con error ≤ 3·10⁻¹⁸, sup\|u_T\|/s es estable en k y la diferencia doble es O(s³). |
| 4 | Identidad de Schur de T/08b y herencia de clase | **Correcta** | Verificada a mano y en aritmética exacta: det V_E del bosque, V_E(−H_E″) = I, K_I + Σ1/t = −H_E″ y el lema del determinante en el gauge RC. Con el perfil real se comprobaron R″ = Σ1/t − g, la composición completa con base de ciclos y la coincidencia con la J de T05. La herencia la dan D04 orig. 45–56, K02 y U02. |
| 5 | Cálculos propios (opcional) | **Evidencia numérica favorable** | k·g_T = O(1); k²R tiene límite, con −63/256 y −208/729 en los rectángulos; k³ por la variación de R entre menores, acotado; diferencias dobles O(s³). |

## 2. Detalle por punto

### 2.1 Punto 1 · El error puro de torres O(1/j) en la máscara de llegada

**(a) Dónde entra y qué se necesita.**
- **Usos:** `latex/06_corte.tex`:34–36 (definición de g_T y log X = Y_D + g_T en H_j) y 71–73; H03 orig. 18–22; A04 orig. 3 y 6–10; `MAPA_DEPENDENCIAS.md`:11; `TEOREMA.md`:13.
- **Lo que hace falta:** para toda máscara A de H_j, de tamaño j = ⌊bn⌋, \|log per A − L_T(A)\| ≤ C/j con C de clase, fijada antes de b, y j ≥ j₀(clase).
- **Coste:** aporta C/j = O_b(1/n) a E_ν[\|X−1\|; H_j] por \|e^z − 1\| ≤ e^{z⁺}\|z\|. El uso es puntual.

**(b) Enunciado de E01** (E01:2–5 y 18–27).
- **Cuantificadores.** Para todo M y todo r < 1 existen C y k₀ tales que, para todo k ≥ k₀ y toda máscara de tamaño k con punto estacionario interior P bistocástico, p ≤ M/k y ‖P−J‖_op ≤ r:
  - \|g_T + 1/(12k) − Ξ(P)\| ≤ C/k²;
  - \|Ξ\| ≤ Cq₄/k.
- **Convenciones.** P puede tener ceros. Las sumas recorren las k² posiciones (E01:6). Lo comprobé: con esa lectura el resto es O(k⁻²) (§2.6).
- **Normalización.** L_T = H_T(P) + log Γ₂(P), con log Γ₂ = ½(log 4πk − C₂ − log pdet S₂) (CP/07d orig. 103–106).
- **Paso a O(1/k).** q₄ = Σσ⁴ ≤ r²Σσ² = r²(Σp² − 1) ≤ r²(M − 1). Con \|Ξ\| ≤ Cq₄/k da \|g_T\| ≤ C/k.

**(c) Prueba (E02–E03 a partir de R1).**
- **Identidad exacta de partida.** log per A − H_T = log per W − Σlog(1−P), con W = P(1−P) separable en el soporte (R1/mascara:21–27). Además log per W = log per D − b. Rehíce las dos. Con la normalización de C resulta la fórmula de E02:17–23 antes de sustituir el desarrollo del permanente.
- **E02:5–6.** S₀⁺ = I − H − Π₊/2 − Π₋. Lo comprobé por bloques: S₀ = I + O_P + Π₊ − Π₋ y O_P anula (1,±1).
- **E03:22–29.** Comprobé ‖t‖² = Z − 4s/k + 2/k, M_z = Z − s²/k − zᵀHz, ΣB³ = l − 3s/k + 2/k, C(p∘U) = j, ⟨U,p⟩ = j₀, 1ᵀj = 2j₀ y 2⟨B∘B − p∘p, U⟩ = −4j₀/k.
- **E03:40–48 (cota uniforme).** Comprobé j₀ ≤ q₄/(1−r²), tr T_R² y ‖U‖²_HS ≤ q₄/(1−r²)², ‖j‖² ≤ 2j₀‖j‖_∞ (j ≥ 0) y entradas O(1/k). Cada término de Ξ es ≤ Cq₄/k. **Demostrado.**
- **Lo que no rehíce término a término.** El resto de los desarrollos (E02:30–71, E03:1–21 y 30–39). **Numérico** (C1, C1b):
  - k²R, con R = g_T + 1/(12k) − Ξ, está acotado y converge en cinco familias;
  - en los rectángulos, k(g_T + 1/(12k)) → h(a,b) (R8/04:12–15), con −11/192 y −13/108, y k²R → Ξ₂(a,b) (K09:6–9), con −63/256 y −208/729;
  - en la escalera, P ≠ D (\|P/D − 1\| ≈ 0,087/k) y todos los sumandos de Ξ son no nulos.

  Si un coeficiente de Ξ fuera erróneo, k²R crecería linealmente.
- **Tablero lleno.** A mano obtuve g_T = −1/(12k) − 1/(4k²) + O(k⁻³), coherente con 12Ξ₂ = −3 en u = 0. Comprobado numéricamente.

**(d) Entradas.**
- **R1/permanente** (= W/permanente, orig. 1–75): desarrollo uniforme log(k^k per D/k!) = log d(1) + V(1) + d″/(2(k−1)d) + O(k⁻²). Se extrae de las cotas intermedias de Divoux–Wang (preprint). La coordinación cotejó esas cotas (`divoux_wang/NOTA.md`:5–20); no las dictamino. **Condicional.** Numérico: k²E₁ acotado en las cinco familias (C1).
- **R1/traza y R1/mascara:** paso de P a D y normalizador con resto O(1/K). Los leí y no encuentro errores.
- **Clase en H_j:** que la máscara de llegada tenga punto interior difuso con brecha es una implicación de clase de otras filas del mapa (D04, A01). **Condicional.**

**(e) Papel de U05 y K06–K07.** Para la cota puntual no hacen falta: basta E01. Aun así los comprobé, porque sostienen el atajo de §2.2 y la prueba de M01.
- **Cero de U05** (U05:16–25). Diferenciando el sistema de márgenes, ⟨α′+β′⟩ = −∫z². Los grados dan +∫z² en (⟨log a⟩+⟨log b⟩)/(2u). Además c(y) = y − (2/3)y³ + …, y en u = 0, W = z − 1, ℓ̄ = 1, de modo que ½log det(I−WᵀW) = −log d(1). Lo rehíce a mano. **Numérico:** (N(u) + log d(1))/u tiene límite finito cuando u → 0 en las cinco familias (C1); en el tablero lleno vale −1/6.
- **Fórmula del cofactor de K06** (K06:30–46).
  - Para una congruencia de corango uno, pdet(GNG) = det G²·pdet N·v₀ᵀG⁻²v₀, por la adjunta.
  - Aquí v₀ᵀD₀⁻¹v₀ = 1/ℓ̄ y pdet N = 2det(I−WᵀW).
  - **Demostrado.** Numérico (V0b): la identidad física g_T = log(k^k per D/k!) + σ(k) + N(1/k) se cumple con residuo ≤ 10⁻⁷⁰ en cuatro familias. Esto comprueba K06:13–46 y la parte exacta de K07:51–57.
- **kΞ(P) = φ(v)** (K07:10–12). Es una correspondencia de escalas, con entrada = s·núcleo y suma = (1/s)·integral. La comprobé término a término.
- **Resto O(s³) de K07:54–55.** K07 cita R2/10, que es un diagnóstico (R2/10:2–3), aunque su desarrollo da O(k⁻³) (R2/10:15–18). El respaldo demostrado es R1/torres_fila:22–36 (K^K per D/K! = H_K + O(K⁻³), con H_K = H_*). También vale U04:34–39 con q = 2, que da (3C/m)³. En cambio, el enunciado U01:18–21, (Cq/m)^q, es un orden más débil del que prueba U04.

**Precisiones.**
- **P1.1.** E01:29–30 dice «admitido en la ronda 1». Conviene decir que el desarrollo se deduce de cotas intermedias publicadas de Divoux–Wang (cotejo en NOTA) y que no es una hipótesis.
- **P1.2.** `MAPA_DEPENDENCIAS.md`:11 cita K06–K07 para la cota O(1/j). No se usan ahí; se usan en M01 (§2.3–2.4) y en la estructura de los átomos.
- **P1.3.** U05:10–12 escribe «Cambiar log H_* por log H_q … cuesta (Cq/m)^q». Debe referirse al logaritmo exacto del permanente normalizado, como dice G03 orig. 43. Es una errata de redacción.

### 2.2 Ampliación 1 · El atajo q = 2 de la ronda 21 (REP:1–18; GUIA:3–7)

**Afirmación.** Para j ≥ 2/c₀ se tiene \|g_T\| ≤ C′/j + 4C²/j² + Ce^{−cj}, y esto basta para H03.

**Comprobación paso a paso.**
1. **Identidad exacta en u = 1/j.** g_T = log(j^j per D/j!) + σ(j) + N(1/j), con σ el resto de Stirling y N la suma de los términos de balanceo, local, grados y cofactor. Verificada (§2.1e y V0b).
2. **Definición de G₂** (G03 orig. 25–33). G₂(u) = u/12 + log H₂(u) + N(u). Con q = 2 sólo se retiene el término u/12 de Stirling, y H₂ = H_* (U04:19 con k = 2, igual que K07:38–40).
3. **Error del aproximante.** \|g_T − G₂(1/j)\| ≤ \|log(j^j per D/j!) − log H₂(1/j)\| + \|σ(j) − 1/(12j)\| ≤ Cj⁻³ + Ce^{−cj}. Usa U03, U04:34–39 y el primer término omitido de Stirling, −1/(360j³). La cota escrita (2C/j)² vale a fortiori.
4. **Cero en el origen.** G₂(0) = 0. Por un lado H₂(0) = d(1), porque μ_i(0) = 0 para i ≥ 1 y V_l(y,0) = 0, ya que E − \|π\| ≥ l (K07:33). Por otro, N(0) = −log d(1) por el punto (e) de §2.1.
5. **Holomorfía.** G₂ es holomorfa y acotada en \|u\| ≤ ρ con constantes de clase:
   - K06:13–29 para v, α y β;
   - U02 para los datos complejos;
   - U04:41–48 para log H₂;
   - reduciendo c₀, c₀/2 cae dentro del disco de K06.

   El lema de Schwarz da \|G₂(u)/u\| ≤ sup\|G₂\|/ρ. Con q fijo, la pérdida O(q) de U05:30–31 es una constante.
6. **Conclusión.** La cota de REP:15 es correcta. Basta para `06_corte.tex`:72, H03 orig. 20 y A04 orig. 3, que sólo usan la cota puntual en H_j.

**Precisiones.**
- G03 no está en el expediente r19; dentro de r19 el uso puntual ya lo cubre E01. El atajo evita el álgebra de E02–E03, pero no la entrada de Divoux–Wang (U03–U04) ni la interpolación y el cofactor de K06.
- **No da diferencias entre menores.** Una cota puntual O(1/j) sólo da diferencias O(1/j). Para el orden s³ que pide M01 hacen falta la estructura explícita de u_T y la estabilidad de R_T (§2.3–2.4). Coincido con REP:18 y GUIA:7.

### 2.3 Punto 2 · Primera extensión: K06/K08 con cruce ausente y cuatro supresiones

**Uso.**
- MM07:9–14: variación O(s³) de R_T = log per − L_T − u_T entre menores sucesivos del exterior D = A sin las cuatro casillas.
- La fila y la columna que se retiran son las de una casilla especial, que no está en el soporte de D.
- Hipótesis de MM01:12–14. Precisión P1.1 y recomendación PW2 de `rev_exp/W2_pares/ACTA.md`:110 y :228.

**Lo que enuncian K06 y K08.**
- K06:2–12 habla de «menores puros de una fila».
- K08:11–52 trata un «cofactor puro sin vetos» y concluye \|R(A) − R(A⁻_c)\| ≤ C/k³ (K08:51).

**¿Cubre la prueba la extensión tal cual?** Sí. Recorrí cada paso.
- **Márgenes** (K08:12–14, que remite a K02:9–35).
  - Cada margen superviviente pierde la entrada de la columna (o fila) retirada, que es ≤ M₀/k, esté o no la casilla de cruce en el soporte.
  - El déficit total, 1 − p_rc repartido en k−1 líneas, sigue siendo O(1/k) por línea.
  - La contracción y la cota del inverso en supremo no cambian.
- **Distancias.** La variación total de cada medida es ≤ 1/k (K08:15–16) y η_k = O(1/k) (K08:16–18). Ninguna de las dos usa A_rc = 1.
- **Pasos 1–3** (K08:21–45). Potenciales, resolventes en supremo y Fredholm–Hadamard usan núcleos acotados, distancia en variación total y la brecha. No interviene el valor de A_rc.
- **Replicación** (K08:1–10). Se aplica a toda máscara de la clase, incluidos el exterior y sus menores. Requiere el resto O(k⁻³) uniforme de K08:48–49 (entrada de §2.1e).

**Cuatro supresiones.** Son cuatro aplicaciones del lema, cada una con constantes de clase heredadas:
- D04 orig. 45–56 trata un número fijo de filas y columnas emparejadas y a lo sumo dos sitios por línea, tomados directamente desde el padre;
- K02:2–8 y 36–40, y U02 orig. 28–38 para el escalado D.

Por tanto \|R_T(D_{−X}) − R_T(D)\| ≤ 4Cs³ y la diferencia doble es O(s³).

**Numérico** (C2):
- un paso: k³[R(A) − R(A⁻)] → 0,303 con el cruce ausente, frente a 0,297–0,717 con el cruce presente;
- sucesión de cuatro supresiones con el cruce ausente: cada paso tiene k³·Δ ≈ 0,30 y el total k³(R₀ − R₄) → 1,22;
- montaje de M07 (16 vértices, permanentes exactos por inclusión–exclusión): máx_X k³\|R_T(X) − R_T(0)\| ≈ 2,08. La diferencia doble de R_T es incluso O(s⁴): k³·DD → 0 como −7,5/k.

**Veredicto: correcta con precisión.** No es un hueco de prueba: el texto de K08 prueba la afirmación extendida. Falta enunciarla. Propuesta de enunciado: «para A en la clase y una fila r y una columna c cualesquiera, esté o no (r,c) en el soporte, \|R(A) − R(A_{−r,−c})\| ≤ C/k³, iterable un número fijo de veces con constantes de clase».

### 2.4 Punto 3 · Segunda extensión: la fórmula de K07 en medidas complejas

**Uso** (MM07:16–44). Se escribe u_T(h₁,h₂) = s_m[−1/12 + φ(v)], con μ_h = (μ⁰ − h₁Σ_{u}δ − h₂Σ_{v*}δ)/(1−2h₁−2h₂) y s_m = s/(1−2h₁−2h₂). Se exige \|u_T\| ≤ Cs en un bidisco fijo para obtener, por Cauchy, una diferencia mixta O(s³) en h_g ∈ {0, s}.

**Comprobaciones.**
1. **Medidas.** μ_h está definida para \|2h₁+2h₂\| < 1 y dista O(\|h\|) de μ⁰ en variación total. En h_g ∈ {0, s} es la medida uniforme de cada menor, con s_m = 1/m.
2. **Núcleo v.** Es holomorfo en (s, h₁, h₂) en un polidisco fijo: Newton con inverso congelado en supremo (MM03:9–29; K06:21–27). Los índices de masa cero conservan su ecuación de margen (MM07:40).
3. **Vértices.** En un vértice, P = s_m·v restringido a los supervivientes cumple P(1−P) separable con márgenes uno. Por unicidad en la rama pequeña (K02:30–35) es el punto de torres del menor, y φ(v) = mΞ(P_menor).
4. **Definición de φ.** Para h complejo, φ se define por las fórmulas integrales de K07:5–9, con transpuestas bilineales (K06:48; MM07:31). Comprobé que en medidas uniformes reproduce kΞ.
5. **Cotas en supremo.**
   - En el origen, (I−G)⁻¹ = I + G + G(I−G)⁻¹G está acotado en supremo por la brecha en L² y la cota puntual de los núcleos.
   - Una perturbación de tamaño O(\|h\|+\|s\|) en la norma supremo→supremo (supremo del núcleo por variación total) se absorbe por Neumann.
   - Las diagonales de T − G = G²(I−G)⁻¹ están bien definidas: no hay parte identidad.
   - Todos los términos de φ son integrales finitas de núcleos acotados.
6. **Diferencia mixta.** \|u_T\| ≤ 2C\|s\| en el bidisco. Cauchy da \|∂_{h₁}∂_{h₂}u_T\| ≤ Cs/c² cerca del origen, luego la diferencia mixta es O(s³).

**Numérico** (C3; doble precisión, exterior de la escalera, c = 0,05):
- la prolongación coincide con u_T físico de los cuatro menores con error ≤ 3·10⁻¹⁸;
- la solución existe en todo el toro \|h₁\| = \|h₂\| = c;
- sup\|u_T\|/s = 0,1749, 0,1747, 0,1746 y 0,1746 para k = 48, 96, 192 y 384;
- k³·DD u_T → −2,06, que coincide con k³s²c₁₁ (coeficiente de Cauchy, −2,057).

**Veredicto: correcta con precisión.** Coincido con la precisión P1.2 de W2_pares: la redacción es esquemática. Conviene decir explícitamente que φ(v; μ_h) se *define* por esas fórmulas para h complejo (como hace U03 para V_l) y escribir las cotas de Neumann en supremo.

### 2.5 Punto 4 · Identidad de Schur de T/08b y herencia de clase

**Enunciado.** T08b orig. 1–39.
- R y R″ en orig. 10–14.
- Prefactor A − ½log det(I − V_E R″) en orig. 17–21.
- Factor de Schur, D_i y b_Dτ_D en orig. 22–30.
- det V_E y cociente de escalares en orig. 31–39.

Lo usa MM02:19–33, en la versión sin coincidencias: bosque de componentes de uno o dos sitios. Es la dependencia que W2_pares dejó condicional (`W2_pares/ACTA.md`:50).

**Convención.** Leo «producto local y pseudodeterminante» como
exp(−2F) = Π_e p_e(1−p_e)^{1−D_e} · Π_l t_l · det(K\|ker C), salvo constantes comunes,
con K = diag(1/τ_{D_e}) + Σ_l 1_l1_lᵀ/t_l, la hessiana en casillas de T05 orig. 37. El cociente completo/torres de esta convención es exactamente la J de T05 orig. 28–39 (comprobado en C4(g)). W2_pares validó esa J con los coeficientes publicados de R3.

**Comprobado a mano.**
1. **Acción.** La de torres es H_E + R, con R = H_ext + Σt log t (orig. 10–12). Las sumas de (1−x)log(1−x) cuadran exactamente.
2. **Hessiana del exterior.** R″_ij = Σ_{v∈i∩j}1/t_v − g_ij (orig. 13): por la envolvente, ∇²_t H_ext = −S_ext⁺ y t = 1 − C_I x.
3. **Dualidad.** −H_E″ = V_E⁻¹ (orig. 30).
4. **Hessiana en casillas.** K_I + [Σ_{v∈i∩j}1/t_v] = −H_E″, entrada a entrada.
5. **Lema del determinante.** Las columnas u_i son ortogonales a (1,−1), así que pdet(S_ext + C_I K_I⁻¹C_Iᵀ) = pdet S_ext · det(I + K_I⁻¹g). Luego det K·pdet(CK⁻¹Cᵀ) = Π_ext τ⁻¹ · pdet S_ext · det(V_E⁻¹ − R″).
6. **Cociente de escalares.** Con det V_E = Πx(1−x)·Π_{E}(1−x_i−x_j)/((1−x_i)(1−x_j)) y b_Dτ_D = p(1−p)^{1−D}, el cociente deja exactamente ½Σ_v log t_v (orig. 37–38). La cuenta se reduce a Σ_i D_i log(1−x_i) − Σ_{ij∈E}[log(1−x_i)+log(1−x_j)] + log(1−x_a−x_c).

**Comprobado por cálculo** (C4):
- **(a)–(c), exacto:** det V_E, la ley y sus marginales, V_E(−H_E″) = I y K_I + Σ1/t = −H_E″. Se hizo en los cuatro bosques de 08b y en los cuatro de MM02, con tres vectores x racionales.
- **(d), exacto:** el lema del determinante.
- **(e)–(g), con el perfil exterior real en una máscara 6×6:**
  - R″ por diferencias finitas frente a Σ1/t − g: diferencia ≤ 5·10⁻³⁰;
  - det(K\|ker C)·pdet(CCᵀ), con base de ciclos e independiente del lema, frente al lado derecho: relativo ≤ 4·10⁻³¹;
  - prefactor completo frente a A − ½log det(I − V_E R″): ≤ 2·10⁻³¹;
  - J de T05: relativo ≤ 3·10⁻⁷⁸.

  Se probaron tres conjuntos de enlaces en la configuración de 08b y dos en la de MM02.

**Herencia de clase** (MM01:12–14; MM02:2–5; MM03:2–3). Suprimir cuatro casillas en filas y columnas distintas, y después hasta cuatro filas y columnas, entra en D04 orig. 45–56, directamente desde el padre. También lo cubren K02:2–8 y 36–40 (cambio del núcleo centrado O(k^{−1/2}) en Hilbert–Schmidt, brecha conservada) y, para el escalado D, U02 orig. 28–38. **Correcta.**

Las estimaciones de T08b orig. 41–92 no las usa M01: MM04–MM06 las sustituyen. No las dictamino en detalle.

**Veredicto: correcta.**

### 2.6 Punto 5 · Cálculos (código en `codigo/`, salidas en `resultados/`)

Las máscaras son explosiones de patrones 0/1 con proporciones fijas. La reducción por grupos es exacta y se validó contra matrices densas.

| Id | Archivo | Qué comprueba | Resultado | Tiempo |
|---|---|---|---|---|
| V0 | v0_validacion.py | permanente por bloques frente a fuerza bruta; P, log pdet S₂, Ξ y V por grupos frente a cálculo denso; tablero lleno | 6/6 casos; diferencias ≤ 1·10⁻¹⁴; k²(g_T + 1/(12k)) → −1/4 | 1,0 s |
| V0b | v0b_refinada_identidad.py | máscaras D_{−X}: inclusión–exclusión frente a permanente directo y fuerza bruta; identidad física de K06/K07 | 6/6; residuo ≤ 10⁻⁷⁰ en las cuatro familias | 1,3 s |
| C1 | c1_error_torres.py | k·g_T, k(g_T + 1/(12k)), kΞ, k²R, k²E₁ y kΞ/q₄ en cinco familias, k hasta 1536; cero de U05 | k·g_T ∈ [−0,22, −0,08]; rectángulos → h y Ξ₂ exactos; escalera k²R → ≈ −0,2357; k²E₁ acotado; (N + log d(1))/u con límite | 3,0 s |
| C1b | c1b_no_degenerado.py | P ≠ D en la escalera; sumandos de Ξ no nulos; tr(T_L − G_L) = tr(T_R − G_R) | \|P/D − 1\| = 9·10⁻⁴ a k = 96; todos los sumandos ≠ 0 | 0,3 s |
| C2 | c2_menores_K08.py | k³ΔR en un paso (cruce ausente o presente), sucesión de cuatro y montaje de M07 | acotado en todos; DD R_T = O(s⁴), DD u_T = O(s³), \|Δu_T\| = O(s²) | 13,1 s |
| C3 | c3_prolongacion_K07.py | u_T(h) con medidas complejas: vértices, toro \|h_g\| = 0,05 y coeficiente de Cauchy | ver §2.4 | 6,8 s |
| C4 | c4_schur_08b.py | identidad de T/08b, exacta y con el perfil real | 24/24 identidades exactas y el lema exacto; composición ≤ 4·10⁻³¹; J de T05 ≤ 3·10⁻⁷⁸ | 27,6 s |

**Incidencias.**
- V0 falló en su primera ejecución porque Newton arrancaba en w = 1/4, fuera de la rama pequeña. Lo corregí arrancando en 0,8·D y aceptando sólo pasos factibles (0,2 s perdidos).
- C3 falló una vez porque suprimía la ecuación de margen de un grupo de masa cero (2,7 s). Lo corregí suprimiendo la de una columna ordinaria. Hubo además tres ejecuciones breves de depuración (≈ 1 s cada una).

**Lectura.**
- Todo esto es **evidencia numérica, no prueba**: no mide la uniformidad de las constantes en toda la clase.
- Los conteos son exactos.
- En la familia 3×3 con un cero, P = D por simetría de soportes. La prueba no degenerada de E01 es la escalera.

## 3. Dictamen global

**Parte W2_torres: certificada con precisiones.** No hay enunciados falsos ni huecos de prueba en las piezas de mi encargo.

**Separación de usos** (pregunta del coordinador):
- **(A) Uso puntual en H_j** (`06_corte.tex`:72; H03 orig. 20; A04 orig. 3). Necesita \|g_T\| ≤ C/j. Lo dan E01 (con R1) o, como alternativa, el atajo q = 2 de G03/U05. Ninguno de los dos necesita K07 ni K08.
- **(B) Prueba de M01** (exponente 7). Necesita:
  - E01, porque define u_T = −1/(12k) + Ξ y porque K08 lo usa para obtener Γ_z(0) = Γ_z′(0) = 0;
  - K06–K08 con la primera extensión, que da R_T estable a O(s³) entre menores del exterior;
  - la segunda extensión, K07 en μ_h, que da la diferencia mixta de u_T a O(s³);
  - la identidad de T/08b y la herencia de clase.

  El atajo q = 2 no sustituye nada de (B).

**Condicional a:**
- la extracción de R1 a partir de las cotas intermedias de Divoux–Wang (cotejada por la coordinación, no por mí);
- el resto O(s³) del permanente (R1/torres_fila; U04 con q = 2);
- la pertenencia a la clase en H_j (D04/A01).

**Precisiones para la próxima entrega.**
- **PT1.** En E01:29–30, cambiar «admitido» por el estado real de la entrada R1 (P1.1).
- **PT2.** En `MAPA_DEPENDENCIAS.md`:11, separar los usos (A) y (B). K06–K07 sólo pertenecen a (B) (P1.2).
- **PT3.** Corregir la redacción de U05:10–12 y citar U04:34–39 o R1/torres_fila para el resto O(s³) de K07:54–55, en lugar de R2/10 o de la forma (Cq/m)^q de U01:18–21.
- **PT4.** Enunciar la extensión de K08 a una fila y una columna cualesquiera, iterable un número fijo de veces (§2.3).
- **PT5.** Escribir que φ(v; μ_h) se define por las integrales bilineales para h complejo, con las cotas de Neumann en supremo (§2.4).
- **PT6.** Declarar en T08b la convención del producto local y pseudodeterminante, que coincide con la J de T05.

## 4. Resumen final

```
W2_torres · error puro de torres, extensiones R8-R9 e identidad de T/08b
Integridad: r19 116/116; R8 30/30, R9 98/98, U 14/14, MM 14/14; r21 03_torres 4/4.
Punto                                                    Veredicto
1  Error puro O(1/j) en la llegada (E01; U05; K06-K07)   Correcta con precisión
1b Atajo q=2 de r21 (G03/U05) para H03                   Correcto y suficiente
2  K06/K08 con cruce ausente y 4 supresiones             Correcta con precisión
3  K07 prolongada a medidas complejas mu_h               Correcta con precisión
4  Identidad de Schur de T/08b y herencia de clase       Correcta
5  Cálculos exactos (opcional)                           Evidencia favorable
Dictamen global: CERTIFICADA CON PRECISIONES. Sin enunciados falsos ni huecos
de prueba en mi parte.
Demostrado aquí:
- E01 da |g_T| <= C(M,r)/k: |Xi| <= C q4/k y q4 <= r^2(M-1); identidades de
  E02-E03; cero de U05; fórmula del cofactor de K06; k Xi = phi(v).
- Atajo q=2: |g_T - G_2(1/j)| = O(j^-3), G_2(0)=0 y Schwarz dan C'/j; basta
  para el uso puntual; no da diferencias entre menores.
- La prueba de K08 no usa que el cruce esté en el soporte; 4 supresiones son
  4 pasos con clase heredada (D04 orig. 45-56, K02). Falta sólo el enunciado.
- K07 en mu_h: holomorfía y |u_T| <= Cs en un bidisco fijo; coincide con u_T
  de los menores en los vértices; diferencia mixta O(s^3).
- T/08b: det V_E, V_E(-H_E'')=I, K_I+Σ1/t=-H_E'', lema del determinante en el
  gauge RC, cociente que deja ½Σlog t_v; coincide con la J de T05.
Usos separados: (A) H03 necesita sólo E01 o el atajo q=2; (B) M01 necesita
E01, K06-K08 extendido, K07 en mu_h y T/08b; q=2 no sustituye (B).
Condicional a: extracción de R1 desde Divoux-Wang; resto O(s^3) del
permanente (R1/torres_fila, U04); clase en H_j (D04/A01).
Numérico (código propio, permanentes exactos):
- k g_T = O(1); k^2 R converge (-63/256, -208/729 en los rectángulos;
  escalera con P != D);
- un paso k^3 dR acotado, con o sin cruce; montaje M07: DD R_T = O(s^4),
  DD u_T = O(s^3);
- prolongación compleja: vértices exactos a 3e-18; sup|u_T|/s ≈ 0,175 en k.
Precisiones: PT1-PT6 (estado de R1; separar usos en el mapa; citas del resto
O(s^3); enunciar la extensión de K08; definir phi en mu_h; convención en 08b).
ACTA: rev_exp/W2_torres/ACTA.md (código en codigo/, salidas en resultados/).
```
