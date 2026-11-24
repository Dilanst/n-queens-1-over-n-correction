# Acta de revisión · W2_norma (norma canónica en el álgebra de activaciones)

**Fecha:** 2026-11-17.

**Objeto:** la pieza `rev_exp/r21/piezas_T2/01_norma/` (GUIA, prueba_fuente, PARTES_LATEX) y sus originales: N01–N03 (Cola de activaciones, partes 01–03) y Z04 (Ciclo exterior, parte 04).

## 0. Alcance, integridad y método

- **Material leído íntegramente.**
  - La pieza: `GUIA.md`, `prueba_fuente.md` y `PARTES_LATEX.md`.
  - Las dos entregas originales completas:
    - `fuentes/velocidad_via2_cola_activaciones_20261116T165855Z/`: partes 01–05, main, LEEME, INFORME, REVISION_ADVERSARIAL y CONTINUAR;
    - `fuentes/velocidad_via2_ciclo_exterior_20261117T073122Z/`: partes 01–04, LEEME, INFORME, ACTA_ADVERSARIAL y CONTINUAR.
  - Las revisiones internas `r21/fuentes/revisiones_internas/N_REVISION_ADVERSARIAL.md` y `Z_ACTA_ADVERSARIAL.md`.
  - `r21/consolidado/` (TEOREMA, CONSTANTES, MAPA, CAMBIOS y NOTACION, y `latex/03_norma.tex`, `05_lineas_y_grados.tex` y `06_corte.tex`), `rev_exp/E1/ACTA.md` y `r21/fuentes/publicas/ENUNCIADOS.md`.
  - Para las dependencias y las ramas:
    - B, 08a_meso y 08e_meso, en sus transcripciones públicas de `r19/expediente/originales/BP/`;
    - `r21/fuentes/latex/B01.tex`, `H01.tex` y `A01.tex`;
    - de la ronda 18, `latex/02_grados_y_radio.tex` y `MAPA_DEPENDENCIAS.md`;
    - de Grupos interlínea, las partes 01–04.
- **Integridad** (`resultados/c0_cotejo.txt`).
  - `sha256sum -c SHA256SUMS` da 10/10 en Cola de activaciones y 8/8 en Ciclo exterior.
  - Las cuatro huellas declaradas en `prueba_fuente.md` (líneas 7, 58, 117 y 180) coinciden con los originales.
  - Las copias `r21/fuentes/latex/N01–N03.tex` y `Z04.tex` son idénticas byte a byte a los originales.
  - Los cuatro bloques de `prueba_fuente.md` reproducen literalmente los archivos completos (rangos 1–44, 1–52, 1–56 y 1–29).
  - Las revisiones internas N y Z de r21 son copias idénticas de las actas de origen.
  - Las filas de `r21/SHA256SUMS` de estos archivos (199–201, 225, 326, 332 y 335–337) cuadran.
  - **Material llegado durante la revisión.** Hacia las 13:24 UTC aparecieron en `r21/fuentes/publicas/` copias de secciones de B y C, con `BLOBS.txt`.
    - Comprobé que el SHA1 de blob de git de `B/07a_macro.txt`, `B/07i_macro.txt` y `B/08e_meso.txt` coincide con `BLOBS.txt` (commit cdc3936…).
    - `B/08e_meso.txt` es idéntico a la transcripción de r19.
    - Usé `B/07a_macro.txt`, que es §B4T01, sólo para la estructura del determinante canónico (punto 3).
- **Citas.**
  - `N01:k`, `N02:k`, `N03:k` y `Z04:k` remiten a la línea k de `01_resultado.tex`, `02_rama.tex`, `03_normalizador.tex` y `04_radios.tex`. En `prueba_fuente.md` son las líneas k+9, k+60, k+119 y k+182.
  - Para los demás archivos doy ruta y línea del propio archivo. En `08a_meso.md` y `08e_meso.md` cito la línea del `.md`; la línea original es la del archivo menos 7.
- **Desconfianza.** No usé como prueba los dictámenes internos (N_REVISION, Z_ACTA, MAPA). Rehíce cada paso contra las líneas citadas.
- **Cálculo.**
  - Cuatro programas propios en `codigo/`, ejecutados de uno en uno con `nice -n 10` y tiempo medido. Las salidas están en `resultados/`.
  - c1 y c2 usan racionales exactos.
  - c3 usa aritmética entera en coma fija con redondeo dirigido, es decir, intervalos con extremos racionales, y certificación de Krawczyk. Ningún número de coma flotante entra en los resultados; los decimales impresos representan racionales exactos.
  - No hay azar ni Monte Carlo.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Motivo breve |
|---|---|---|---|
| 1 | Enunciado y cuantificadores (N01) | **Correcta con precisión** | El orden M₀, r → η_Λ, C, j₀ → máscara, ρ es correcto y lo prueba N03 (N01 sólo enuncia la versión de ρ fijo). ε_A se mide con el punto de torres de la propia máscara. La norma cubre de una vez todo el cubo de activaciones por sitio (las dos familias). P debe ser el punto **estacionario** de torres. |
| 2 | Punto estacionario simultáneo (N02) | **Correcta con precisión** | Inversa en supremo, levantamiento al álgebra y bola invariante bajo ρ²(ε_A+1/j) pequeño: verificados. Cada evaluación es el máximo global y la «rama pequeña» de B. La cota por soporte usa esta misma rama a través de N03 (no al revés). E1 no tiene punto de Bethe que casar. |
| 3 | Bloques de Schur (N03) | **Correcta con precisión** | Las cotas ‖E‖_∞ ≤ Cη < 1/2 y ‖E‖_Σ = O(ρ²j) y la serie de trazas no dependen del número de diagonales. ΣP\|log P\| ≤ j log j vale sin mínimo por sitio. Hay estimaciones holgadas (z_e² = z_e) y el término j log(ej) sobra: en realidad ‖Λ‖_ρ ≤ Cρ²j. |
| 4 | Paso a la cola (Z04) | **Correcta con precisión** | min(η_F, η_Λ), la cola C_ρ j²ρ^(−N), N = ⌈4 log n/log ρ⌉ ≤ 8 log n y el corte ⌊a_d log j⌋ con a_d log ρ > 3 son correctos. La carga se verifica en H_j mediante L_max < αj, difusión de A01/D04 y α elegido después de ρ: condicional a T2.4, que sigue pendiente. |
| 5 | Dependencias | **Correcta** | Importa: el punto de torres estacionario con difusión M₀ y brecha r, la carga en la propia máscara, j ≥ j₀ y la definición publicada del predictor (B). No importa E1, ni la cota por soporte, ni la ley de historias, ni G_j. No hay circularidad. |
| 6 | Cálculos (opcional) | Hechos; evidencia, no prueba | El álgebra, las identidades de B y N03 y Schur con gauge se comprobaron en exacto. ‖Λ‖_ρ se certificó en una familia de máscaras j×j (j = 8…1024), muy por debajo de j log(ej) + ρ²j. |

No encontré ningún enunciado falso ni ningún hueco de prueba en N01–N03 ni en Z04. Las precisiones son de cuantificadores, de alcance y de dependencia documental. La única parte que no pude verificar es §B3T01 de B (término de árbol y coeficiente del logaritmo), que no está en el material. §B4T01, llegado durante la revisión, confirma la matriz de líneas, el gauge y el producto ∏b·det que usa N03.

## 2. Detalle por punto

### Punto 1 · Enunciado y cuantificadores (N01)

**Qué se afirma.** `GUIA.md:3` enuncia la cota con este orden:
- para M₀ y r < 1 existen η_Λ, C y un tamaño mínimo;
- después, para toda máscara difusa, todo ρ ≥ 2 con ρ²(ε_A+1/j) ≤ η_Λ y toda subactivación, se tiene ‖Λ‖_ρ ≤ C{j log(ej) + ρ²j}.

**Comprobación.**
- **Dos versiones.**
  - N01 sólo enuncia la de ρ fijo: «Fijado ρ>1, existen ε₀, j₀ según ρ, M₀, r» (N01:24–26), con cota C_{ρ,M₀,r}·j log(ej) (N01:30–35).
  - La versión uniforme de la guía está en N03:16–21 y N03:49–53, con «C independiente de ρ» (N03:18–19).
  - Rehíce la dependencia en ρ de cada constante:
    - la inversa en supremo, con C′ = 1 + √(2M₀)/(1−r) (N02:15–18);
    - el radio y la constante de Lipschitz de Π, que sólo usan la inversa escalar y las series exponenciales (N03:19–20);
    - ‖H(0)‖ y Lip(H) ≤ C(ρ²ε_A + ρM₀/j) ≤ C·max(1,M₀)·ρ²(ε_A+1/j) para ρ ≥ 2;
    - el umbral e^(−4) del argumento de tangentes, que sólo exige j ≥ e^(4+a)M₀;
    - S₀ − D₀ = O(M₀/j).
  - Ninguna depende de ρ. El orden M₀, r → η_Λ, C, j₀ → máscara, ρ es correcto.
  - La versión de N01 se deduce de la uniforme tomando ε₀ = η_Λ/(2ρ²), j₀ ≥ 2ρ²/η_Λ y ρ²j ≤ C_ρ·j log(ej). Para 1 < ρ < 2 basta la monotonía en ρ (N03:52).
  - El teorema consolidado fija ρ antes que α y n (`consolidado/CONSTANTES.md:6–8`), así que incluso la versión de ρ fijo le bastaría.
- **ε_A.**
  - P es el punto de torres de A, positivo en el soporte y bistocástico (N01:17–18).
  - ε_A es el máximo, sobre las diagonales de cualquiera de las dos familias y en coordenadas originales, de Σ_{e∈A∩f} P_e (N01:19–23).
  - Z04 conserva la carga medida con P también al combinar con E1 (Z04:2–4 y 11–12). Coincide con `consolidado/latex/03_norma.tex:8–9` y con E1 (`E1/ACTA.md:167–168`).
  - El umbral precede al radio: η = η(M₀, r) (N03:17; `CONSTANTES.md:5`).
- **«Toda subactivación».**
  - ‖Λ‖_ρ es un único número para la función Y ↦ Λ(Y) sobre todo el cubo {0,1}^A de activaciones por sitio. Cada z_e activa las dos diagonales de e: d_e = 2 + 2z_e (N02:27) y D_ef = z_e·1_{e∈f} para las dos pendientes (N03:2–3).
  - La cota es, pues, simultánea para todos los Y ⊆ A. Da |Λ(Y)| ≤ ‖Λ‖_ρ en cada Y y la misma cota para la restricción a cualquier subcubo.
  - Las activaciones por familia (una sola pendiente de un sitio) no forman parte del cubo, y no las usan ni V, ni la cota por soporte (`B01.tex:6`), ni Grupos interlínea 01:9–10.
  - La prueba se extendería con d ∈ {2,3,4}: B admite esas multiplicidades (`08a_meso.md:36`) y la tangente vale para d ≤ 4. Pero no está enunciado.
  - **Precisión 1a.** El «para toda subactivación» de `GUIA.md:3` debe leerse como «Λ está definido en todo el cubo de activaciones por sitio y su norma cumple…».
- **Premisa implícita (precisión 1b).**
  - P debe ser el punto **estacionario** de Bethe de torres, P_e(1−P_e) = a_r·b_c, y no una bistocástica positiva cualquiera. N02:33–34 divide por «la de torres para P_e(1−P_e)».
  - N01:17 sólo dice «punto de torres». `A01.tex:66` y 82 lo precisan.
- **Marco.**
  - N01 está redactada para la banda j = ⌈tK⌉ ≤ ⌈δn⌉ y la ley E_* (N01:2–5).
  - La cota de N02–N03 es determinista por máscara (tablero fijo) y no usa ni G_j ni la ley. Se aplica a j = ⌊bn⌋ ≤ δn.
  - La historia ν sólo entra después, a través del indicador 1_{H_j} (`consolidado/latex/06_corte.tex:59–61`).
  - No intervienen menores: el tamaño es el de la máscara, j, y no hay m = j − h.

**Veredicto:** correcta con precisión.

### Punto 2 · Punto estacionario simultáneo (N02)

**Comprobación.**
- **Álgebra** (N02:2–5).
  - z_S z_T = z_{S∪T} es el producto puntual de funciones del cubo (z_e² = z_e).
  - La norma es submultiplicativa para ρ ≥ 1, porque \|S∪T\| ≤ \|S\|+\|T\|.
  - Cada evaluación es un carácter con \|f(Y)\| ≤ ‖f‖_ρ.
  - Verificado exhaustivamente en c1, con control negativo en ρ = 1/2, que falla como debe.
- **Ecuación de estacionariedad** (N02:27–35).
  - La rehíce: ∂Φ_Y/∂x_e = −log x_e − (d_e−1)log(1−x_e) + z_e Σ_f log h_f − 2. La constante −2 es la misma para sitios activos e inactivos (c2, punto 5).
  - Al restar la ecuación de torres sale v = H + a_i + b_j, con H como en N02:31.
- **Inversa en supremo** (N02:13–19).
  - D₀ = [[I,P],[Pᵗ,I]] tiene espectro {2, 0, 1 ± σ_k(P)}, con σ_k ≤ r para k ≥ 2. En el complemento de (1,−1), ‖D₀⁺‖₂ ≤ 1/(1−r).
  - La ecuación de una coordenada, a_i = y_i − Σ_j P_ij b_j, con Σ_j P_ij² ≤ M₀/j, da \|a_i\| ≤ ‖y‖_∞(1 + √(2M₀)/(1−r)).
  - Proyectar cuesta a lo sumo 2. Por tanto la máxima suma por fila de \|D₀⁺\| es ≤ 2(1 + √(2M₀)/(1−r)).
  - c2, punto 9: D₀⁺ exacta para cinco bistocásticas racionales; todas quedan dentro de la cota, con r acotado exactamente por trazas de potencias.
- **Levantamiento** (N02:20).
  - Para una matriz escalar M, max_i ‖(My)_i‖ ≤ (máxima suma por fila de \|M\|)·max_l ‖y_l‖ (c1, punto e).
  - El defecto de márgenes en el álgebra es compatible: los totales de filas y de columnas coinciden idénticamente.
  - El punto fijo de la iteración con D₀⁺ anula el defecto: D₀⁺M = 0 obliga a M ∈ span(1,−1), y la compatibilidad da M = 0.
- **Π** (N02:21–25). Es Newton–Kantorovich con el inverso basal en el espacio de vectores de elementos del álgebra con norma máximo. ‖D₀ − DM‖ ≤ 2(e^R − 1) porque cada margen es una media con pesos P_ij de suma uno. Es correcto y estándar, aunque comprimido.
- **Bola invariante** (N02:36–43 y N03:16–21).
  - ‖1−h_f‖ ≤ ρe^a ε_A y ‖q_e‖ ≤ e^a P_e.
  - El término de carga z_e Σ_f log h_f cuesta ρ·2·Cρe^a ε_A; el término local (1+2z_e)log(1−q_e) cuesta O(ρP_e).
  - Luego ‖H(0)‖, Lip(H) ≤ C′ρ²(ε_A+1/j) ≤ C′η para ρ ≥ 2.
  - Con L_Π la constante de Lipschitz de Π, el mapa compuesto contrae con razón ≤ 1/2 en una bola de radio 2L_Π‖H(0)‖ si L_Π C′η ≤ 1/2 y 2L_Π C′η ≤ a.
  - **Precisión 2a.** N02 escribe O_ρ (N02:39). La dependencia explícita en ρ, imprescindible para la versión uniforme, sólo aparece en N03:18–19. La verifiqué.
- **Máximo físico** (N02:45–52). Verificado:
  - s_d es cóncava en [0, 1/d] (c2, punto 2).
  - En [0, 1/d] la tangente en q < e^(−4) domina por concavidad estricta.
  - En [1/d, 1], g = tangente − s_d es cóncava, con g(1/d) > 0 y g(1) = −log q − d(1−q) > 4 − d ≥ 0 (c2, punto 3).
  - Se suman los términos cóncavos −h log h y se usan los multiplicadores RC: q maximiza la mayorante cóncava Ψ en el politopo factible, y Φ_Y ≤ Ψ ≤ Ψ(q) = Φ_Y(q) con igualdad sólo en q.
  - Hace falta max q_e < e^(−4): \|q_e(Y)\| ≤ ‖q_e‖ ≤ e^a M₀/j, independiente de ρ.
- **¿La misma rama que E1 y que la cota por soporte?**
  - B define el predictor en la «rama pequeña»: el único punto estacionario en la región convexa p < 1/4 con vacancias positivas (`08e_meso.md:83–85`; `08a_meso.md:20`).
  - El punto de N02 tiene q < e^(−4) < 1/4 y h_f > 0, así que es ese punto, además del máximo global.
  - La cota por soporte identifica su silla holomorfa en las caras físicas con este punto mediante el control de N03:21: ‖q_i/P_i − 1‖_ρ ≤ Cη y q_i = O(1/j) en la caja de unicidad (`fuentes/velocidad_via2_ronda18_20261117T091817Z/latex/02_grados_y_radio.tex:56–58`; su `MAPA_DEPENDENCIAS.md:41`).
  - Por tanto es la misma rama. La identificación se hace en B02, fuera de esta pieza, y depende de N03, no al revés. No dictamino la «caja de unicidad» de B02, que pertenece a otra pieza.
  - E1 no tiene punto de Bethe. F(Y) = log(Q_Y/per A) es el logaritmo real, tomado después de la positividad (`consolidado/latex/03_norma.tex:75–79`; `E1/ACTA.md:160–166`).
  - Lo único que Z04 necesita de E1 es compatibilidad: el mismo cubo, F(∅) = Λ(∅) = 0 y la misma carga medida con P (Z04:11–12).
- **Activaciones híbridas.** Los sitios de A∖Y tienen d = 2. Es la representación de torres de B, con diagonales privadas de una casilla eliminadas por su identidad (`08a_meso.md:55–56`). Concuerda con N02:35 y N03:54–56.

**Veredicto:** correcta con precisión.

### Punto 3 · Bloques de Schur (N03)

**Comprobación.**
- **Estructura** (N03:2–14).
  - En B: τ_d = pq/(1−dp) y b_d = (1−dp)/q^d (`08a_meso.md:36–39`), y la matriz de líneas con gauge es S̃₀ = S₀ + vvᵗ/(2k), v = (1_R, −1_C, 0_D) (`08e_meso.md:99–100`).
  - La T de N03 es τ_{d_e}(q_e), y por Schur det S̃ = det(S_R+P_g)·det S_d, porque las columnas de CᵗTD son ortogonales al gauge.
  - Verificado en exacto en una máscara 5×5 con coincidencias diagonales y valores racionales arbitrarios (c2, punto 6), junto con S_R(S_R+P_g)⁻¹CᵗTD = CᵗTD.
  - La eliminación de líneas unitarias en el determinante completo, ∏b_{d_e}·det = ∏b_{d_e′}·det′ (`08a_meso.md:40–46`; N03:54–56), también se verificó en exacto (c2, puntos 1 y 7).
  - **Confirmación con §B4T01** (`r21/fuentes/publicas/B/07a_macro.txt`, llegado durante la revisión):
    - S = diag(0_RC, h) + AᵗTA, τ = pq/(1−4p) y v = (1_R, −1_C, 0_D) (líneas 6–9);
    - el gauge se trata con el cofactor RC, y pdet S = 2k·det S_gf (líneas 13 y 54–55);
    - la magnitud del predictor es 𝒟 = ∏_e[(1−4p_e)/q_e⁴]·det S_gf (línea 72), es decir, ∏b₄·det.
  - Es exactamente la estructura de N03. Su det(S_R+P_g) es pdet S = 2j·det S_gf, que difiere por una constante en la máscara fija.
  - **No verificable.** §B3T01 (término de árbol y coeficiente de log 𝒟) no está en el material. `B01.tex:44–51` da −½ log b y −½ log det, coherente con lo anterior.
- **Bloque RC** (N03:22–27).
  - ‖T_e/T_{0,e} − 1‖ = O(η); el término 2z_e q_e cuesta O(ρ/j) ≤ O(η).
  - S₀ − D₀ = O(1/j) en sumas por fila.
  - ‖(S₀+P_g)⁻¹‖_∞ ≤ C, por (D₀+P_g)⁻¹ = D₀⁺ + P_g y Neumann.
  - log det relativo = tr log(I+E_R) con ‖E_R‖_∞ ≤ Cη; cuesta ≤ 2j·(−log(1 − ‖E_R‖_∞)) = O(ηj). ✓
- **Bloque diagonal** (N03:29–38).
  - Sumas por fila:
    - DᵗTC ≤ 2ρΣ_{e∈f}‖T_e‖ ≈ 2ρε_A;
    - CᵗTD ≤ 2ρ;
    - diag h − I: O(ρε_A).
  - Luego ‖S_d − I‖_∞ ≤ Cη < 1/2.
  - Normas Σ:
    - DᵗTC: 4ρΣ_e‖T_e‖ = O(ρj);
    - diag h − I: 2ρe^a j;
    - el producto DᵗTC(S_R+P_g)⁻¹CᵗTD, por ‖BC‖_Σ ≤ ‖B‖_Σ‖C‖_∞: O(ρj)·C·O(ρ) = O(ρ²j). ✓
  - **Precisión 3a.** Como z_e² = z_e, las entradas de DᵗTD son z_e T_e, de norma ρ‖T_e‖. Sus normas son O(ρε_A) y O(ρj). Las O(ρ²ε_A) y O(ρ²j) de N03:30 y 35 son sobreestimaciones válidas.
- **Serie de trazas y número de diagonales.**
  - \|tr Eᵖ\| ≤ ‖Eᵖ‖_Σ ≤ ‖E‖_Σ‖E‖_∞^(p−1). Luego ‖log det S_d‖ ≤ ‖E‖_Σ·Σ_p 2^(1−p)/p = 2 log 2·‖E‖_Σ = O(ρ²j).
  - La dimensión no interviene. Puede haber hasta 2(2n−1) > j diagonales; las que no tienen casillas activas aportan pivote 1 (`08a_meso.md:50`; N03:3).
  - Coincide con B, cuyas constantes «no dependen del número de diagonales» (`08a_meso.md:21`; `08e_meso.md:96`).
  - c2, punto 8, comprueba las desigualdades escalares en el ejemplo.
  - En cada evaluación, ‖ev_Y E‖ ≤ ‖E‖_∞ < 1/2, así que las series son los logaritmos reales (N03:39–40). ✓
- **Acción y factor local** (N03:42–48).
  - Σ_e P_e\|log P_e\| = Σ_filas H(fila) ≤ j log j, porque cada fila tiene a lo sumo j casillas. No hace falta un mínimo por sitio. ✓
  - Los demás términos cuestan O(ρj). ✓
  - **Precisión 3b (holgura).** Ese término sobra:
    - q y P tienen márgenes uno en el álgebra, y log P_e + log(1−P_e) = α_r + β_c por la estacionariedad de torres;
    - por tanto Σ_e (q_e − P_e) log P_e = −Σ_e (q_e − P_e) log(1−P_e) exactamente, de norma O(ηM₀);
    - la acción cuesta O(ρj), y de hecho ‖Λ‖_ρ ≤ Cρ²j para ρ ≥ 2.
  - La cota enunciada es más débil y correcta.
- **Positividad** (N03:13–14). Se sigue de T > 0 (q < 1/4), de h > 0 y de la conexión RC por la brecha. ✓

**Veredicto:** correcta con precisión.

### Punto 4 · Paso a la cola (Z04)

**Comprobación.**
- **La implicación** (Z04:6–25).
  - E1 da ‖F‖_ρ ≤ C(1 + jρ²(ε_A+1/j)), certificado en `E1/ACTA.md:238–241`. N03 da la cota de Λ.
  - η = min(η_F, η_Λ) sirve, porque las dos cargas se miden con el mismo P (Z04:11–12).
  - Σ_{\|U\|>N} \|`[U](F−Λ)`\| ≤ ρ^(−N)(‖F‖_ρ + ‖Λ‖_ρ) ≤ C_ρ j² ρ^(−N).
  - Con N = ⌈4 log n/log ρ⌉ y j ≤ n, eso es ≤ C_ρ n^(−2). ✓
  - La subfamilia no colineal hereda la cota (Z04:24–25). Las sustracciones de líneas y pares no tocan soportes no colineales de tamaño > N ≥ 5 (`cola_activaciones/latex/05_pendiente.tex:3–7`; Grupos interlínea 01:29–34).
- **Elección de N y de ρ en el consolidado.**
  - Se fija a_d log max(2, C₁) < 1/4 y después ρ ≥ 2 con a_d log ρ > 3 (`CONSTANTES.md:6`).
  - Corte determinista (`consolidado/latex/06_corte.tex:48–50`): C_ρ j² ρ^(−⌊a_d log j⌋) ≤ C_ρ ρ j^(2 − a_d log ρ) = O_ρ(1/j). ✓
  - Media: N = ⌈4 log n/log ρ⌉ ≤ 8 log n (06_corte.tex:53). Ya ρ ≥ 2 da 4/log 2 ≈ 5,77 < 8; de hecho log ρ > 3/a_d > 12 log 2. ✓
  - Grados altos O_ρ(n^(−2)), integrados contra 1_{H_j} (06_corte.tex:59–61). ✓
  - Como ρ > 2¹², la carga exige ε_A ≤ η/(2ρ²): es diminuta pero fija, y la cubre α con M₀α < η/(2ρ²) (`CONSTANTES.md:7`).
- **La carga donde se invoca.**
  - La norma sólo se invoca en H_j (06_corte.tex:23–24, 49–50 y 59–61). Fuera de H_j únicamente intervienen costes de salida con peso 1+X (06_corte.tex:64–69).
  - En H_j:
    - L_max < ⌈αj⌉ implica L_max < αj, por integralidad;
    - luego ε_A ≤ M₀L_max/j < M₀α < η/(2ρ²) (`H01.tex:38–46`; `A01.tex:68–74`);
    - y ρ²/j ≤ η/2 para n grande, así que ρ²(ε_A+1/j) ≤ η. ✓
  - Esto usa:
    - la difusión j·max P ≤ M₀ y la brecha del punto de torres de la máscara de llegada. Las da `A01.tex:59–79` a partir de la clase de C para el punto de reinas y de la comparación D04, y pertenecen a la pieza T2.4, interna y pendiente de dictamen externo (`consolidado/MAPA.md:7`);
    - el orden ρ antes que α (`CONSTANTES.md:6–7`).
  - La advertencia de la revisión interna (`Z_ACTA_ADVERSARIAL.md:13`) queda atendida: la carga procede de la regularidad de llegada y no del crecimiento de j.

**Veredicto:** correcta con precisión. Es condicional a T2.4 (clase en la llegada) y a E1, ya certificado.

### Punto 5 · Dependencias

**Premisas que importa la pieza** (N01–N03):
1. **Punto de torres.** P es el punto estacionario de Bethe de torres de A: positivo en el soporte, márgenes uno y P(1−P) = a_r b_c (N01:17; N02:33–34).
2. **Difusión.** j·max_e P_e ≤ M₀. Se usa en Σ_j P_ij² ≤ M₀/j, en ‖H(0)‖, en q < e^(−4) y en S₀ − D₀ = O(1/j).
3. **Brecha.** ‖P − J_j‖_op ≤ r < 1. Da la inversa en supremo y la conexión RC (N02:15; N03:12–13).
4. **Dominio de carga.** ρ²(ε_A+1/j) ≤ η_Λ(M₀, r), con ε_A medido con P en coordenadas originales, para **cada** máscara (N01:27–28).
5. **Tamaño.** j ≥ j₀(M₀, r).
6. **Definición del predictor.** Es la publicada de B: término de árbol, factor local b_d, cofactor RC de S̃₀ y covolumen, en la rama pequeña (`08e_meso.md:80–85`; `08a_meso.md:36–56`; `publicas/B/07a_macro.txt:6–13` y 72). Se extiende a activaciones híbridas por la representación de torres de B (Grupos interlínea 01:9–16).
7. **Herramientas estándar.** Cálculo funcional en un álgebra de Banach, Neumann, Schur, punto fijo y la desigualdad de entropía.

**No importa:** E1, la cota por soporte, la ley ν, G_j ni la completabilidad (G_j sólo entra en F, N01:39–41), los menores, ni Divoux–Wang.

**Para aplicarla (Z04 y 06_corte), hacen falta además:**
- la cota de F de E1;
- la carga en H_j, que viene de A01/H01 con D04 y la clase de C (pieza T2.4);
- las elecciones a_d, ρ y N de `CONSTANTES.md:6–7`.

**Circularidad: no la hay.**
- Las flechas son E1 → Z04, N02–N03 → Z04 y N03 → cota por soporte (identificación de rama, `02_grados_y_radio.tex:56–58`).
- Ni E1 ni la cota por soporte alimentan N01–N03:
  - las fuentes de Cola de activaciones (`LEEME.md:9–15`) son todas anteriores (16-11 hasta las 16:43);
  - E1 (Media franjas, 17-11 01:29; Menores uniformes, 04:22) y la ronda 18 (09:18) son posteriores a N01–N03 (16-11 16:58);
  - las huellas fijan el contenido.

**Veredicto:** correcta.

### Punto 6 · Cálculos (evidencia, no prueba)

| Programa | Comprueba | Resultado | Tiempo |
|---|---|---|---|
| `codigo/c0_cotejo.py` | Huellas y cotejo literal de los cuatro bloques de `prueba_fuente.md` | Todo coincide | 0,03 s |
| `codigo/c1_algebra.py` | z_S z_T = z_{S∪T} ↔ producto puntual; ida y vuelta de Möbius; submultiplicatividad y \|f(Y)\| ≤ ‖f‖_ρ para ρ ∈ {1, 5/4, 2, 3}, con control negativo en ρ = 1/2; levantamiento de sumas por fila | OK. 72 722 pares exhaustivos; el control negativo falla como debe | 17,2 s |
| `codigo/c2_identidades.py` | Identidades de línea unitaria de B y N03 (polinomios); umbral 1/d; tangente en 1; cancelación unitaria en la acción; constante −2; Schur con gauge y eliminación de líneas unitarias en el determinante completo (máscara 5×5); desigualdades Σ; inversa de D₀ en supremo (5 matrices) | OK | 0,4 s |
| `codigo/c3_norma_lambda.py` | ‖Λ‖_ρ certificado (Krawczyk e intervalos de coma fija) en la familia de máscaras de abajo, j = 8, 16, 32, 64, 128, 256 y 1024; ρ = 2, 3, 4 | Véase la tabla | 345,8 s en total (45–55 s por valor de j) |

**La familia de c3.**
- **La máscara.**
  - Es un tablero j×j completo en coordenadas originales. Las filas {0,1,2} y las columnas {s, s+1, s+2} forman un bloque con seis líneas de 2–3 casillas, con ciclos.
  - Las demás filas y columnas están lejos (7·1000^(2k+1) y s + 11·1000^(2k+2)), de modo que ninguna otra diagonal tiene dos casillas.
  - Lo verifiqué por enumeración exacta para j ≤ 64. Para j > 64 reduje módulo 2¹²⁷ − 1: una coincidencia verdadera no puede desaparecer al reducir.
  - P = J_j, M₀ = 1, r = 0 y ε_A = 3/j.
- **Reducción del cubo.**
  - Por la identidad de líneas unitarias de B (verificada en c2), las casillas fuera del bloque son inertes.
  - Así [S]Λ = 0 salvo para S dentro del bloque, y la norma sobre ese subcubo de 512 activaciones **es** la norma completa sobre {0,1}^A.
- **Certificación.**
  - Cada configuración efectiva se resolvió por Newton y se certificó por Krawczyk: existencia y unicidad en la caja.
  - En toda la caja q_e < 1/d_e y h_f > 0, es decir, la región estrictamente cóncava donde B selecciona su rama pequeña.
  - Una comprobación cruzada que mantiene las líneas unitarias, con cuatro incidencias por sitio, da el mismo L_Y.

En los siete valores de j se cumplen todas estas comprobaciones:
- la geometría tiene sólo las 6 líneas múltiples del bloque;
- se certificaron 190 configuraciones efectivas por Krawczyk;
- la región es la cóncava (q_e < 1/d_e, h_f > 0);
- la comprobación cruzada concuerda;
- los coeficientes de soportes con un sitio aislado son nulos (el enclave contiene 0), y los otros 189 son no nulos certificados;
- la anchura máxima de los enclaves es ≤ 8·10⁻²⁹.

Valores (enclaves de anchura despreciable; `resultados/c3_norma_lambda.txt`):

| j | ε_A = 3/j | ρ²(ε_A+1/j), ρ=2 | ‖Λ‖₂ | ‖Λ‖₃ | ‖Λ‖₄ | j log(ej)+4j | ‖Λ‖₂/cota | max_e ‖v_e‖₂ |
|---|---|---|---|---|---|---|---|---|
| 8 | 0,375 | 2 | 1,467 | 9,344 | 52,73 | 56,6 | 2,6·10⁻² | 4,55 |
| 16 | 0,1875 | 1 | 0,1957 | 0,5739 | 1,630 | 124,4 | 1,6·10⁻³ | 1,32 |
| 32 | 0,0938 | 0,5 | 4,218·10⁻² | 9,960·10⁻² | 0,1922 | 270,9 | 1,6·10⁻⁴ | 0,558 |
| 64 | 0,0469 | 0,25 | 1,009·10⁻² | 2,297·10⁻² | 4,152·10⁻² | 586,2 | 1,7·10⁻⁵ | 0,262 |
| 128 | 0,0234 | 0,125 | 2,478·10⁻³ | 5,600·10⁻³ | 1,001·10⁻² | 1261 | 2,0·10⁻⁶ | 0,128 |
| 256 | 0,0117 | 0,0625 | 6,148·10⁻⁴ | 1,386·10⁻³ | 2,468·10⁻³ | 2700 | 2,3·10⁻⁷ | 0,0631 |
| 1024 | 0,00293 | 0,0156 | 3,821·10⁻⁵ | 8,602·10⁻⁵ | 1,530·10⁻⁴ | 12218 | 3,1·10⁻⁹ | 0,01566 |

El cociente más alto de toda la tabla es 0,345 (j = 8, ρ = 4, carga 8), todavía por debajo de 1.

**Lectura.**
- En toda la familia, ‖Λ‖_ρ queda muy por debajo de j log(ej) + ρ²j, y el cociente cae al crecer j.
- ‖Λ‖₂ ≈ 40/j²: dominan los diez pares colineales del bloque, con [S]Λ ≈ −1/j² y peso ρ² = 4.
- max_e ‖v_e‖₂ ≈ ρ²(ε_A+1/j); en j = 1024 el cociente es 1,003. Ilustra N03:21 (‖q_e/P_e − 1‖_ρ = O(η)).
- Para j ≥ 64 se tiene P_e = 1/j < e^(−4), y con ρ = 2 la carga es 16/j ≤ 1/4.
- Las partes «log b» y «log det» son, por separado, unas diez veces mayores que Λ y se compensan. Ilustra que el objeto natural es el producto b·det de B, aunque N03 las acote por separado.
- Para j ≤ 16 la carga es ≥ 1, fuera del régimen, y max_e ‖v_e‖₂ > 1, como cabe esperar.
- Son máscaras con muy pocas interacciones. Prueban la coherencia de las fórmulas, no la cota general.

## 3. Demostrado, condicional y no verificable

- **Demostrado.** He rehecho el argumento al nivel de un esbozo detallado, sin encontrar pasos falsos ni pasos sin respaldo:
  - la cota ‖Λ‖_ρ ≤ C{j log(ej) + ρ²j}, de hecho ≤ Cρ²j, para cada máscara de la clase con ρ ≥ 2 y ρ²(ε_A+1/j) ≤ η_Λ, con constantes que sólo dependen de M₀ y r;
  - la identificación de cada evaluación con el punto de Bethe de B;
  - la implicación de Z04.
- **Condicional:**
  - a las premisas 1–5 del punto 5 sobre la máscara;
  - a la definición del predictor en B;
  - para la aplicación, a E1 (certificado) y a la clase con carga en H_j (T2.4, pendiente).
- **No verificable con el material.**
  - El texto de B, §B3T01. §B4T01 (`publicas/B/07a_macro.txt`) sí confirma S, τ, el gauge y 𝒟 = ∏b₄·det S_gf. Lo demás, sólo por coherencia con 08a, 08e y B01.
  - La «caja de unicidad» de la cota por soporte (B02), que pertenece a otra pieza.
- **Grado de detalle.** Hay pasos comprimidos pero estándar: Newton–Kantorovich en el espacio de vectores del álgebra (N02:21–25) y la continuación de las series logarítmicas (N03:39–40). Una versión para publicación debería desarrollarlos y escribir explícitamente las precisiones 1a, 1b, 2a, 3a y 3b.

## 4. Dictamen global sobre la pieza

**Certificada con precisiones.** Para cada máscara cuyo punto de torres estacionario P tiene difusión M₀ y brecha r < 1, para ρ ≥ 2 y para ρ²(ε_A+1/j) ≤ η_Λ(M₀, r), donde ε_A es la carga diagonal de P en coordenadas originales y η_Λ y C se eligen antes que ρ:
- Λ está definido en todo el cubo de activaciones por sitio, y cada evaluación es el máximo global y la rama pequeña de B;
- ‖Λ‖_ρ ≤ C{j log(ej) + ρ²j};
- con E1 y N = ⌈4 log n/log ρ⌉, la cola de grados mayores que N cuesta O_ρ(n⁻²).

La carga se verifica en H_j mediante L_max < αj, con α elegido después de ρ, y la difusión y la brecha de la llegada (A01/D04, pieza T2.4). Esa pieza conserva su estado de pendiente. No hay circularidad con E1 ni con la cota por soporte. Las precisiones no son huecos ni enunciados falsos.

## 5. Resumen final

```
ACTA W2_norma (norma canónica de Λ: N01–N03 y Z04) · 2026-11-17
Integridad: SHA256 10/10 (Cola) y 8/8 (Ciclo). Los 4 bloques de prueba_fuente.md
coinciden literalmente con los originales completos; las copias de r21 son idénticas.

Veredictos:
 1 Enunciado y cuantificadores (N01) ............ correcta con precisión
 2 Punto estacionario simultáneo (N02) .......... correcta con precisión
 3 Bloques de Schur (N03) ....................... correcta con precisión
 4 Paso a la cola (Z04) ......................... correcta con precisión
 5 Dependencias ................................. correcta, sin circularidad
 6 Cálculos ..................................... evidencia, no prueba

Hallazgos:
- Ningún enunciado falso ni hueco de prueba.
- Orden M0, r → η_Λ, C, j0 → máscara, ρ: lo prueba N03:16–21. N01:24–26 sólo
  enuncia la versión de ρ fijo, que bastaría al consolidado (ρ fijo antes de α, n).
- P ha de ser el punto ESTACIONARIO de torres (N02:33–34). ε_A se mide con P,
  en coordenadas originales y en cada máscara.
- La norma cubre de una vez todo el cubo de activaciones por sitio (ambas familias).
- Verificados: inversa en supremo, levantamiento por sumas de fila, bola invariante
  con ρ²(ε_A+1/j) pequeño y máximo global por tangentes. Es la rama pequeña de B
  (08e:83–85). La cota por soporte la identifica a través de N03 (B02:56–58).
  E1 no tiene punto de Bethe.
- Schur: ‖E‖∞ ≤ Cη < 1/2 y ‖E‖Σ = O(ρ²j); la serie de trazas no ve el número de
  diagonales. Holguras: z_e² = z_e, y el término j log(ej) sobra (‖Λ‖ρ ≤ Cρ²j)
  por los márgenes uno y la estacionariedad de torres.
- Z04 correcto: min(η_F,η_Λ), cola C_ρ j²ρ^(−N) = O_ρ(n⁻²), N ≤ 8 log n y corte
  ⌊a_d log j⌋ con a_d log ρ > 3. La carga se verifica en H_j (L_max < αj, difusión
  de A01/D04, α después de ρ): condicional a T2.4, pendiente.
- No verificable: §B3T01 de B (término de árbol, coeficiente de log 𝒟). §B4T01,
  llegado durante la revisión (blob verificado), confirma S, τ, gauge y ∏b·det.
Cálculos (nice -n 10, uno a uno; racionales exactos o intervalos de coma fija):
 c0 cotejo; c1 álgebra (72 722 pares exhaustivos); c2 identidades de B y N03,
 Schur con gauge e inversa de D0; c3 ‖Λ‖ρ certificado por Krawczyk en máscaras j×j,
 j = 8…1024: ‖Λ‖₂/(j log(ej)+4j) va de 2,6e-2 a 3,1e-9. Unos 6 min en total.
Dictamen global: CERTIFICADA CON PRECISIONES.
Acta: rev_exp/W2_norma/ACTA.md
```
