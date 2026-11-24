# Acta de revisión · W2_difusion: difusión y brecha sobre la llegada histórica corta (D04, A01)

**Objeto.** Los seis puntos de la revisión W2_difusion. La pieza es `rev_exp/r21/piezas_T2/04_difusion/`: la implicación «tablero de la clase histórica de C con L_max < ⌈αj⌉ ⇒ punto de torres positivo en el soporte, carga M₀/j, brecha y escalado exacto controlado», en cada máscara.

**Revisión.** 17-11-2026.

**Dictamen global sobre esta parte: CERTIFICADA CON PRECISIONES** (§3). No he encontrado ningún enunciado falso ni ningún hueco de prueba en D04:1–43 ni en A01:13–42. Las precisiones son de redacción, de notación y de cita; ninguna cambia un enunciado.

## 0. Alcance, integridad, convenciones y método

**Integridad** (código `codigo/c0_cotejo.py`, salida `resultados/c0_cotejo.txt`).
- SHA256 de los originales:
  - `fuentes/velocidad_via2_ronda10_20261116T103833Z/latex/04_difusion.tex` = a0464f3a…c5cecb;
  - `fuentes/velocidad_via2_margenes_y_atomos_20261117T083049Z/latex/01_clases.tex` = 387f0909…67d40d.
  
  Ambas coinciden con las declaradas en `prueba_fuente.md`:7 y :70.
- Transcripciones: los bloques de `prueba_fuente.md`:10–65 (56 líneas) y :73–132 (60 líneas) son idénticos, línea a línea, a los originales completos (1–56 y 1–60).
- Las copias `r21/fuentes/latex/D04.tex` y `A01.tex` tienen la misma huella. Las copias de r19 (`r19/expediente/originales/D/04_difusion.md` y `A/01_clases.md`) transcriben también literalmente los mismos textos.
- `sha256sum -c` en las dos carpetas de origen: 9/9 correctos en `margenes_y_atomos`; 11/11 archivos presentes correctos en la ronda 10. Esa copia es parcial: faltan 54 entradas de su manifiesto (cálculos, sellos e informes), que no uso.
- Repetí el cotejo: todo coincide.
- Pasajes públicos de B y C: los 18 archivos de `r21/fuentes/publicas/{B,C}/` coinciden con los identificadores de blob de `BLOBS.txt` (SHA-1 de blob git, recalculado).

**Convenciones de cita.**
- **D04:n** es la línea n del original `04_difusion.tex` (= línea n+9 de `prueba_fuente.md`). **A01:n** es la línea n de `01_clases.tex` (= línea n+72 de `prueba_fuente.md`).
- **GUIA:n** es `r21/piezas_T2/04_difusion/GUIA.md`.
- **C/07c, C/02, C/05d, B/08e** son los archivos de `r21/fuentes/publicas/C/` y `…/B/` (07c_escalado, 02_preliminares, 05d, 08e_meso).
- **N01, N02, N03, Z04, H01, H03** son `r21/fuentes/latex/*.tex`. **A02** se cita por la línea de `r21/piezas_T2/05_salidas/prueba_fuente.md`.
- **U01**, **F01** y **B03** se citan por la línea de `r19/expediente/originales/U/01_enunciado.md`, `F/01_enunciado.md` y `B/03_mascara_y_media.md`.
- **CONSTANTES** es `r21/consolidado/CONSTANTES.md`.

**Alcance.**
- Dictamino D04:1–43 (enunciado, proyector, contracción, máximo global, brecha) y A01:13–42 (lema de márgenes y escalado exacto).
- No dictamino:
  - D04:45–56 (menores y prefijos de veto), que usa W2_torres para la herencia;
  - A01:1–11 (transiciones bajo ν);
  - A01:43–60 (coste de la llegada larga), que pertenece a la pieza de salidas.
- Tampoco la probabilidad de visitar la máscara. Los resultados de B y C son premisas publicadas: sólo compruebo que sus hipótesis literales se cumplen.

**Estados.**
- *Demostrado*: comprobado aquí a mano.
- *Condicional*: depende de una premisa publicada o de otra pieza.
- *Numérico*: evidencia de cálculo, no prueba.

**Método.**
1. Lectura línea a línea de D04, A01, GUIA y de los usos: N01–N03, Z04, H01–H03, A02, U01, F01, E01 vía `W2_torres/ACTA.md`, y CONSTANTES.
2. Verificación a mano de cada paso, con constantes explícitas propias (§2.2).
3. Cálculo determinista en `decimal` a 40 cifras (§2.6): un proceso cada vez, con `nice -n 10` y tiempo medido. No había mpmath ni sympy y no instalé nada. No hay azar: las máscaras salen de rotaciones irracionales evaluadas con enteros exactos.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Motivo breve |
|---|---|---|---|
| 1 | Enunciado y cuantificadores | **Correcta con precisión** | ε_T, K_T y el umbral de tamaño dependen sólo de (C, γ); doy valores explícitos. M₀ = 2C, γ_T, 4C y γ_T/2 también. α sólo entra en condiciones monótonas. Ninguna constante depende de α, de la máscara ni de j. A01 no nombra el umbral de tamaño de D04 (se absorbe en K_T/j ≤ 1/4 o en «j grande»). |
| 2 | Proyector relativo (D04) | **Correcta** | Rehíce: Π proyector, ‖Π‖_∞ ≤ 3 + 2√(2C)/γ por la ecuación de vértice, sin cota inferior por casilla; gradientes de las dos entropías de Bethe; defecto ≤ 4A·max(1,C)(ε+1/k); jacobiano I + O(‖z‖_∞ + 1/k); contracción; concavidad por fila y unicidad global; herencia de la brecha. Sólo faltan constantes explícitas (γ′, C′). |
| 3 | Márgenes y brecha (A01) | **Correcta** | K_TCα ≤ 1/4 y K_T/j ≤ 1/4 dan P ∈ [p/2, 3p/2]. De ahí j·max P ≤ 3C/2 ≤ M₀, la carga en P ≤ M₀α y la forma cuadrática ≥ ½ la de p. En v^⊥ el espectro 1 ± σ_i(P) da ‖P − J‖_op = σ₂(P) ≤ 1 − γ/2 = 1 − γ_T. |
| 4 | Escalado exacto (A01; C, Lema 7.3) | **Correcta con precisión** | Las hipótesis literales de C/07c:3–8 se cumplen con K = j, M₀ = 2C y ρ_* = 1 − γ_T. La cota relativa entrada a entrada sale de los potenciales O(1/j) en supremo del enunciado, no de la norma HS. HS ⇒ op. Falta citar la unicidad del escalado de Sinkhorn para llamar a D_A «el» escalado exacto de A. |
| 5 | Ajuste con los usos | **Correcta con precisión** | Da exactamente la clase de N01 (r = 1 − γ_T), E01, F01, Z04 y H01, y la de U01 para D con (4C, 1 − γ_T/2). Las cargas en p, P y D_A quedan cubiertas (Cα, M₀α, 4Cα). Precisiones de notación: M₀ sobrecargado y ‖·‖₂ = norma espectral, no HS. |
| 6 | Cálculos (opcional) | **Evidencia numérica favorable** | 16 máscaras deterministas, k ≤ 48, en `decimal` a 40 cifras. max\|P/p−1\| ≤ 1,01(ε+1/k), lineal en ε; ‖Π‖_∞ ≈ 4; todas las cotas de A01 se cumplen; k·max\|D_A/P−1\| ≤ 0,25; Sinkhorn(A) = escalado de P(1−P) con error ≤ 9·10⁻³³. Una máscara con k = 16 y carga ≈ 0,4 no convergió (§2.6). |

## 2. Detalle por punto

### 2.1 Punto 1 · Enunciado y cuantificadores

**(a) Qué se afirma.**
- GUIA:3: dados C, γ históricos existen umbrales de carga y de tamaño y K_T, válidos en toda la clase, con P_T/p = 1 + O(ε + 1/j). En la llegada con L_max < ⌈αj⌉ se toman M₀ = 2C y γ_T = min(1,γ)/2, y para D_A, j·max D_A ≤ 4C y brecha γ_T/2, todo antes de reducir α.
- D04:2–7 lista las hipótesis: p positivo, masas uno, p_e ≤ C/k, brecha RC ≥ γ, masas diagonales ≤ ε, con umbral de ε reducible según (C, γ).
- A01:13–24 lo instancia.

**(b) Clase de partida.**
- H_j es la llegada histórica regular con L_max < ⌈αj⌉ (H03:3). La salida en el hijo de tamaño j pertenece a la primera salida (H03:4–5). Por tanto, en H_j el tablero de tamaño j es regular.
- Como j = ⌊bn⌋ < M, está en el tramo mesoscópico. Su punto de Bethe pertenece a la clase interior de C: difusión, vacancia, brecha y masa diagonal ≤ ε_hist (C/02:111–113).
- El soporte de p son todas las casillas disponibles, con 0 < p_e < 1/4 (C/02:8–11, 42–50). Es la máscara basal A de N01:2–3.
- La brecha de C es el segundo autovalor del laplaciano RC con pesos p (C/02:69–74). Cambiando el signo de las coordenadas de columna (C/05d:41–42) es el menor autovalor de S = D diag(p) Dᵗ en v^⊥, que es la hipótesis de D04:9–11.

**(c) Dependencia de las constantes (demostrado; valores explícitos propios).** Sea A = 3 + 2√(2C)/γ (cota de ‖Π‖_∞, §2.2).
- Se puede tomar:
  - K_T = 8A·max(1,C);
  - ε_T = 1/(96A²·max(1,C));
  - j_T = max(96A²·max(1,C), 24AC, 2C).
  
  Las tres dependen sólo de (C, γ) (derivación en §2.2(d)).
- M₀ = 2C y γ_T = min(1,γ)/2 son funciones de (C, γ).
- Las constantes del Lema 7.3 dependen sólo de (M₀, ρ_*) (C/07c:25), con ρ_* = 1 − γ_T; también el umbral «K suficientemente grande».
- 4C y γ_T/2 se alcanzan para j ≥ j_D(C, γ) (§2.4).
- α sólo aparece en Cα < ε_T y K_TCα ≤ 1/4 (A01:23). Son condiciones monótonas: reducir α las conserva.
- Las condiciones en j (K_T/j ≤ 1/4, j ≥ j_T, j ≥ j_D) se cumplen al final tomando n grande (CONSTANTES:8).
- **Respuesta:** ninguna constante depende de α, de la máscara ni de j. El orden de CONSTANTES:3, 7–8 y A02:199–201, 212–217 es compatible: clase (C, γ) → márgenes → α → b → n.

**Precisiones.**
- **P1.1.** A01:14–19 sólo nombra ε_T y K_T; D04:28–29 exige además k grande. No es un hueco: basta tomar K_T ≥ 4j_T, y entonces K_T/j ≤ 1/4 implica j ≥ j_T. Con mis valores, K_T = 8A·max(1,C) < 4j_T, así que conviene escribir «j ≥ j_T(C,γ)» explícitamente, como hace GUIA:3 («umbrales de carga y tamaño»).
- **P1.2.** min(1, γ) es cosmético. Para k ≥ 2, en v^⊥ el autovalor 1 − σ₂ es ≤ 1, luego toda brecha admisible cumple γ ≤ 1 y γ_T = γ/2.
- **P1.3.** En GUIA:3 y A01:18, «max_f» recorre sólo las diagonales de las dos familias (D04:3–4; N01:19–23): en filas y columnas la masa es uno. Además, A01:23 da de hecho ε < Cα, estricta.

**Veredicto: correcta con precisión.**

### 2.2 Punto 2 · El proyector relativo (D04:9–43)

**(a) El proyector** (D04:12–19). D tiene dos entradas +1 por casilla, S = D diag(p)Dᵗ y v = (1, −1).
- Como Dᵗv = 0:
  - Π = I − DᵗS⁺D diag(p) cumple Π² = Π (usa S⁺SS⁺ = S⁺);
  - D diag(p)Π = 0, porque im D diag(p) = im S;
  - ΠDᵗ = 0.
  
  Es la proyección sobre T = ker D diag(p) a lo largo de im Dᵗ. **Demostrado.**
- **Cota en supremo.** Para ‖z‖_∞ ≤ 1, b = D diag(p)z cumple \|b_u\| ≤ 1 (masas uno) y ‖b‖₂ ≤ √(2k). Por la brecha, y = S⁺b tiene ‖y‖₂ ≤ √(2k)/γ.
- La ecuación de vértice, y_r = b_r − Σ_c p_rc y_c, junto con Σ_c p_rc² ≤ C/k, da \|y_r\| ≤ 1 + √(2C)/γ, y lo mismo en columnas (D04:16–19).
- Como (Πz)_e = z_e − y_r − y_c, resulta **‖Π‖_∞ ≤ A = 3 + 2√(2C)/γ**. No hace falta cota inferior de p_e. **Demostrado.**

**(b) Gradientes** (D04:21–24).
- La entropía de Bethe de reinas es H_B = −Σp log p + 3Σ(1−p)log(1−p) − Σh log h (C/02:46–49). La de torres es H_T = −ΣP log P + Σ(1−P)log(1−P): N02:47 con d = 2, o B/08e:94–95, representación de torres con diagonales de una sola casilla.
- Derivando: −∇H_B = log p + 3log(1−p) − log h_D − log h_A + 2 y −∇H_T = log P + log(1−P) + 2. Las constantes están en im Dᵗ. **Demostrado.**
- La estacionariedad de p da g_T(p) := log p + log(1−p) ∈ im Dᵗ + δ, con δ = −2log(1−p) + log h_D + log h_A.
- Si C/k ≤ 1/2 y ε ≤ 1/2, entonces ‖δ‖_∞ ≤ 4C/k + 4ε, luego **‖Πg_T(p)‖_∞ = ‖Πδ‖_∞ ≤ 4A·max(1,C)(ε + 1/k) =: d**. Es «su diferencia es O(ε+1/k)» de D04:24. **Demostrado.**

**(c) Jacobiano** (D04:24–26). Sea Φ(z) = z − Πg_T(p(1+z)) en T.
- Para h ∈ T, DΦ(z)h = Π[diag(z_e/(1+z_e) + p_e/(1 − p_e(1+z_e)))h].
- Si ‖z‖_∞ ≤ r ≤ 1/2 y k ≥ 2C, entonces **‖DΦ(z)‖_{∞,T} ≤ A(2r + 4C/k)**: es «identidad más O(‖z‖_∞ + 1/k)». **Demostrado.**

**(d) Contracción y punto fijo** (D04:27–33).
- Con r = 2d, ε ≤ ε_T y k ≥ j_T (valores de §2.1(c)):
  - d ≤ 1/(8A) y r ≤ 1/12;
  - la constante de Lipschitz es ≤ A(4d + 4C/k) ≤ 1/3 + 1/6 = 1/2;
  - ‖Φ(z)‖ ≤ d + r/2 = r.
- La bola cerrada de T es completa; su punto fijo z* cumple Πg_T(P) = 0 con P = p(1+z*).
- Por tanto g_T(P) ∈ im Dᵗ, es decir, P(1−P) = a_r b_c, con márgenes exactamente uno porque z* ∈ T.
- Además ‖z*‖_∞ ≤ 2d = K_T(ε + 1/k): **P_T/p = 1 + O(ε + 1/k)**, con P ≥ (11/12)p > 0 en todo el soporte. **Demostrado.**

**(e) Máximo global y unicidad** (D04:33–40).
- −h″(t) = (1−2t)/(t(1−t)) para h(t) = −t log t + (1−t)log(1−t).
- Si t₁ > 1/2:
  - η(1−t) = −η(t);
  - η(t)/t = (1−t)/(1−2t) es creciente, con derivada 1/(1−2t)²;
  - de ahí Σ_{j>1}η(t_j) ≤ η(1−t₁) por superaditividad en [0, 1/2);
  - Cauchy–Schwarz con z₁ = −Σ_{j>1}z_j da \|c₁\|z₁² ≤ Σ_{j>1}c_j z_j².
  
  La hessiana negativa es semidefinida en cada fila.
- Si todos los t ≤ 1/2, los coeficientes son ≥ 0. Los bordes salen por continuidad de H_T en el politopo cerrado.
- H_T es cóncava en el producto de los símplices de fila, que contiene el politopo bistocástico del soporte.
- P_T está en el interior relativo y es estacionario, luego es máximo global.
- Como todas sus entradas son < 1/2, la hessiana es definida en un entorno, y eso da la unicidad. En particular, «el punto de torres» (único estacionario interior) está bien definido para todos los usos. **Demostrado.**

**(f) Brecha** (D04:41–43). La comparación de formas y el espectro 1 ± σ_j(P_T) dan la herencia de la brecha. D04 no explicita γ′ ni C′; A01 los fija (§2.3).

**Numérico** (§2.6): ‖Π‖_∞ ≈ 3,9–4,3, frente a la cota A ≈ 9,7–12,9. La predicción de primer orden z* ≈ −Πδ se cumple con resto ≤ 0,58(ε+1/k)² en todas las máscaras.

**Precisión P2.1.** Explicitar las constantes (las de §2.1(c) sirven) y γ′ = γ(1 − K_T(ε+1/k)).

**Veredicto: correcta.**

### 2.3 Punto 3 · Márgenes y brecha (A01:20–33)

- Con \|P/p − 1\| ≤ K_T(ε + 1/j), ε < Cα (A01:22–23), K_TCα ≤ 1/4 y K_T/j ≤ 1/4 se obtiene p/2 ≤ P ≤ 3p/2 (A01:24). Por tanto:
  - j·max P ≤ 3C/2 ≤ 2C = M₀;
  - la carga cumple max_f Σ_{e∈f}P_e ≤ (3/2)ε < 2Cα = M₀α, y también ≤ M₀L_max/j (H01:39–40);
  - Σ_e P_e(Dᵗy)_e² ≥ ½Σ_e p_e(Dᵗy)_e², es decir, D diag(P)Dᵗ ⪰ ½D diag(p)Dᵗ (A01:25–29).
  
  **Demostrado.**
- Las dos formas anulan v. En v^⊥ (Courant–Fischer), λ_min(S_P) ≥ γ/2.
- Para P cuadrada y bistocástica, S_P = (I P; Pᵗ I) tiene espectro 1 ± σ_i(P) (A01:30–32; C/07c:9–13). En v^⊥ quedan 2 = 1 + σ₁ y 1 ± σ_i para i ≥ 2. Luego 1 − σ₂(P) ≥ γ/2.
- Como P1 = Pᵗ1 = 1, ‖P − J_j‖_op = σ₂(P) ≤ 1 − γ/2 = 1 − γ_T (A01:33). **Demostrado.**

**Veredicto: correcta.**

### 2.4 Punto 4 · Escalado exacto (A01:35–42; C, Lema 7.3)

**(a) Hipótesis literales** (C/07c:3–8 y 15–17).
- P es una matriz bistocástica de orden K, con 0 ≤ P_ij ≤ M₀/K y ‖P − J_K‖_op ≤ ρ_* < 1.
- Se cumplen con K = j (P es j × j, nula fuera del soporte), M₀ = 2C y ρ_* = 1 − γ_T (§2.3).
- La frase «las cotas exteriores fijan constantes» (C/07c:4–5) es contextual: la prueba (C/07c:27–83) sólo usa la hipótesis desplegada.
- Las constantes dependen sólo de (M₀, ρ_*) (C/07c:25). Aplicarlo al punto de torres, y no al de reinas, es legítimo.
- Precisión: GUIA:5 dice «aplicado a P(1−P)». Las hipótesis se comprueban en P; P(1−P) no es bistocástica. A01:37 lo dice bien.

**(b) Factorización** (A01:36–37). Por §2.2(d), log P + log(1−P) = u_r + v_c en el soporte, es decir, W = P(1−P) = a_r b_c A_rc.

**(c) D_A como escalado de A** (A01:38–39).
- El lema da D = e^{α_i+β_j}W = diag(e^α a)·A·diag(e^β b), bistocástica, con el mismo soporte (C/07c:25). Es un escalado diagonal de A.
- Llamarlo «el escalado bistocástico exacto» (A01:35; U01:9) requiere la unicidad del escalado de Sinkhorn de una matriz con soporte total (Sinkhorn–Knopp; Brualdi–Parter–Schneider). Es clásica, pero A01 no la cita.
- **Numérico:** Sinkhorn de A y Sinkhorn de P(1−P) coinciden con error relativo ≤ 9·10⁻³³ en todas las máscaras.

**(d) De HS a entrada a entrada.**
- No se pasa de HS a la cota relativa, ni se puede: una cota O(1/j) en HS permite errores absolutos O(1/j) en una entrada de tamaño ~1/j.
- La cota relativa sale del enunciado: max(‖α‖_∞, ‖β‖_∞) = O(1/K) (C/07c:21). Por tanto D_e/P_e = e^{α_i+β_j}(1 − P_e) ∈ [e^{−2c/j}(1 − 2C/j), e^{2c/j}], es decir, **\|D_A/P − 1\| ≤ c′/j** con c′ = c′(C, γ). Es lo que hace A01:37–39.
- La norma HS (C/07c:23) da ‖D_A − P‖_op ≤ ‖D_A − P‖_HS = O(1/j) (A01:40). También saldría de la cota entrada a entrada por el test de Schur, como hace F01:30–31.
- La prueba del lema contiene \|D − P\| ≤ C₃P/K (C/07c:80–81), pero no hace falta citarla. **Demostrado.**

**(e) Márgenes del escalado** (A01:41–42).
- j·max D_A ≤ (1 + c′/j)(3C/2) ≤ 4C.
- ‖D_A − J‖_op ≤ 1 − γ_T + c″/j ≤ 1 − γ_T/2 para j ≥ 2c″/γ_T.

Ambos umbrales dependen sólo de (C, γ). **Demostrado** (condicional al lema publicado).

**Veredicto: correcta con precisión** (unicidad de Sinkhorn; la redacción de GUIA:5).

### 2.5 Punto 5 · Ajuste con los usos

| Uso | Clase que supone | Lo que da la pieza | ¿Encaja? |
|---|---|---|---|
| N01:17–26; N03:17; guía de la norma, `01_norma/GUIA.md`:3 | P de torres positivo en el soporte de A, bistocástico, max P ≤ M₀/j, ‖P − J_j‖₂ ≤ r < 1; ε_A en P con ε_A ≤ ε₀ y ρ²(ε_A+1/j) ≤ η(M₀, r) | P ≥ p/2 > 0; M₀ = 2C; r = 1 − γ_T; ε_A < M₀α. Umbrales fijados antes de α (CONSTANTES:7; A02:212–215) | Sí |
| Z04:2–4, 8–16 | Las mismas, con la convención ‖P − J‖_op ≤ r explícita | Igual | Sí |
| E01 (`W2_torres/ACTA.md`:74–76; condicionado en :97 y :271) | P estacionario interior bistocástico, P ≤ M/k, ‖P − J‖_op ≤ r | M = 2C, r = 1 − γ_T, unicidad (§2.2(e)) | Sí |
| U01:9–13 y 43 (menores; usados por U05/G03 y por B03:13, 37–38) | D escalado exacto, j·max D ≤ M₀^U, ‖D − J‖_op ≤ r^U, mismos (M₀^U, r^U) en la familia | M₀^U = 4C, r^U = 1 − γ_T/2 (§2.4) | Sí, con la notación de P5.1 |
| F01:18–31 (E1, certificada) | P con M₀, r; ε_A en P; D/P = 1 + O(1/j) | Igual; F01 rehace D/P por su cuenta | Sí |
| H01:38–44 | j·max P ≤ M₀ ⇒ ε_A ≤ M₀L_max/j | A01:26 | Sí |
| Cota por soporte (B03:66–67; A02:199–201) | Clase de referencia con márgenes (M₀, γ_T) y una cota fija de masa admisible | Márgenes de A01:21. Cargas < Cα (en p), < M₀α (en P) y < 4Cα (en D_A, A02:216–217), con α posterior | Sí |

**Convenciones.**
- **Brecha frente a ‖P − J‖₂ ≤ r.** Para una tabla bistocástica, brecha ≥ γ equivale a ‖P − J‖_op ≤ 1 − γ (C/07c:9–13). La pieza da r = 1 − γ_T para P y 1 − γ_T/2 para D_A.
- **Carga.** D04 y GUIA miden ε en el punto de reinas p. N01:19–23, F01:22, Z04:4 y H01:40 miden ε_A en el punto de torres P. El puente es A01:28 (max_f Σ P ≤ M₀α), o directamente H01:40. Es la cota que hay que usar, no la de D04.
- **Tamaño.** La clase se da para la máscara de llegada de tamaño j. Los menores de tamaño m = j − h los hereda U02 (o D04:45–56 para un número fijo de supresiones), fuera de esta pieza.

**Precisiones.**
- **P5.1.** El símbolo M₀ está sobrecargado: 2C para P en A01, N01, E01 y F01; «M₀» de U01 para D, que aquí vale 4C; y el M₀ del Lema 7.3 de C. Al invocar U01 debe decirse M₀^U = 4C y r^U = 1 − γ_T/2.
- **P5.2.** ‖·‖₂ en N01:18 y en la guía de la norma es la norma espectral (Z04:3–4; C/07c:7). Leída como Hilbert–Schmidt sería falsa en la clase: ‖P − J‖²_HS = ΣP² − 1 puede llegar a M₀ − 1 > 1.

**Veredicto: correcta con precisión.**

### 2.6 Punto 6 · Cálculos

El código está en `codigo/` y las salidas en `resultados/`. Todo esto es **evidencia, no prueba**: no mide la uniformidad de las constantes en toda la clase.

**Qué calcula `c1_puntos_torres.py`** (con `puntos.py`), en `decimal` a 40 cifras. En cada máscara:
- **p de reinas:** Newton en los potenciales (λ, μ) con vacancias h retardadas, en la rama p < 1/4. Tolerancia 10⁻³² en márgenes y vacancias.
- **P de torres:** Newton en potenciales, con P = raíz pequeña de t(1−t) = e^{a_r+b_c}.
- **D_A:** escalado de Sinkhorn de A.
- **σ₂:** bisección de 52 pasos, con el éxito de Cholesky de λI − (XᵗX − J) como test de positividad; se da la cota superior.
- **‖Π‖_∞:** sumas exactas por fila de la matriz \|E\|×\|E\|.
- **Primer orden:** −Πδ.
- **Unicidad:** Sinkhorn de A frente a Sinkhorn de P(1−P).

**Máscaras.** Todas se construyen con aritmética entera exacta.
- **A(k,m):** filas 0..k−1, columnas m·(0..k−1) y un hueco rectangular (i < k/2, j < k/4). La carga es ε ≈ 0,4, 0,2 y 0,1 para m = 4, 8 y 16.
- **B(n,k):** pseudo-residuales genéricos. Filas y columnas por rotaciones de √2 y √3 en [0, n); diagonales y antidiagonales bloqueadas por rotaciones de √5 y √7 con fracción 2/10. Densidad ≈ 0,63 y grados irregulares.

| Máscara | k | \|E\| | L_max | C = k·max p | ε | γ ≥ | max\|P/p−1\| | K_eff | ‖Π‖_∞ (cota A) | k·max\|D_A/P−1\| | σ₂(p) / σ₂(P) / σ₂(D_A) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A(32,4) | 32 | 896 | 8 | 2,168 | 0,389 | 0,421 | 0,186 | 0,443 | 4,21 (12,9) | 0* | 0,579 / 0,577 / 0,577 |
| A(48,4) | 48 | 2016 | 12 | 2,186 | 0,390 | 0,421 | 0,182 | 0,443 | 4,28 (12,9) | 0* | 0,579 / 0,577 / 0,577 |
| A(16,8) | 16 | 224 | 2 | 2,000 | 0,203 | 0,422 | 0,110 | 0,415 | 3,94 (12,5) | 0* | 0,578 / 0,577 / 0,577 |
| A(32,8) | 32 | 896 | 4 | 2,052 | 0,203 | 0,423 | 0,102 | 0,435 | 4,14 (12,6) | 0* | 0,578 / 0,577 / 0,577 |
| A(48,8) | 48 | 2016 | 6 | 2,064 | 0,202 | 0,423 | 0,098 | 0,439 | 4,21 (12,6) | 0* | 0,578 / 0,577 / 0,577 |
| A(32,16) | 32 | 896 | 2 | 2,000 | 0,103 | 0,423 | 0,055 | 0,413 | 4,13 (12,5) | 0* | 0,577 / 0,577 / 0,577 |
| A(48,16) | 48 | 2016 | 3 | 2,086 | 0,109 | 0,422 | 0,052 | 0,402 | 4,24 (12,7) | 0* | 0,578 / 0,577 / 0,577 |
| B(768,24) | 24 | 374 | 4 | 2,883 | 0,230 | 0,546 | 0,274 | 1,006 | 3,97 (11,8) | 0,209 | 0,454 / 0,455 / 0,455 |
| B(1536,24) | 24 | 357 | 2 | 3,284 | 0,198 | 0,575 | 0,109 | 0,452 | 3,90 (11,9) | 0,244 | 0,425 / 0,428 / 0,428 |
| B(512,32) | 32 | 646 | 5 | 2,465 | 0,244 | 0,563 | 0,188 | 0,683 | 4,00 (10,9) | 0,075 | 0,437 / 0,436 / 0,436 |
| B(1024,32) | 32 | 650 | 4 | 2,502 | 0,180 | 0,618 | 0,132 | 0,624 | 3,99 (10,2) | 0,153 | 0,382 / 0,378 / 0,378 |
| B(2048,32) | 32 | 644 | 2 | 2,747 | 0,115 | 0,557 | 0,077 | 0,529 | 4,06 (11,4) | 0,223 | 0,443 / 0,443 / 0,444 |
| B(1280,40) | 40 | 1026 | 3 | 2,302 | 0,125 | 0,643 | 0,090 | 0,597 | 4,02 (9,7) | 0,068 | 0,357 / 0,358 / 0,358 |
| B(768,48) | 48 | 1456 | 6 | 2,582 | 0,190 | 0,621 | 0,175 | 0,827 | 4,14 (10,3) | 0,132 | 0,379 / 0,384 / 0,384 |
| B(1536,48) | 48 | 1447 | 4 | 2,652 | 0,151 | 0,604 | 0,100 | 0,578 | 4,16 (10,6) | 0,152 | 0,396 / 0,397 / 0,397 |
| B(3072,48) | 48 | 1469 | 2 | 2,681 | 0,077 | 0,661 | 0,058 | 0,596 | 4,07 (10,0) | 0,126 | 0,339 / 0,340 / 0,340 |

En la tabla, K_eff = max\|P/p−1\|/(ε+1/k). \*En la familia A, P = D_A exactamente (residuo ~10⁻³¹), por la estructura de bloques: la matriz bistocástica constante por bloques es única. Esa familia es degenerada para comparar D_A con P, pero no para comparar P con p.

**Comprobaciones superadas en las 16 máscaras.**
- P/p ∈ [1/2, 3/2]; el rango real es [0,81, 1,27].
- k·max P ≤ 2C; en realidad ≈ C.
- σ₂(P) ≤ 1 − γ/2.
- k·max D_A ≤ 4C.
- σ₂(D_A) ≤ 1 − γ/4.
- ε_A(P) ≤ 2C·L_max/k.
- Residuo de márgenes ≤ 10⁻³².
- Resto de primer orden ≤ 0,58(ε + 1/k)².
- Unicidad del escalado: ≤ 9·10⁻³³.
- k·‖D_A − P‖_HS ≤ 0,083 y k·max\|α+β\| ≤ 2,94 (potenciales O(1/k)).
- En tres máscaras con k ≤ 24, la brecha RC de p en v^⊥, calculada en la matriz 2k×2k, coincide con 1 − σ₂(p) hasta la resolución de la bisección (≤ 7·10⁻¹⁷).

**Lectura.**
- P/p − 1 crece linealmente con ε: en la familia A, a m fijo, vale ≈ 0,5ε (entre 0,47ε y 0,54ε) y es estable en k. El término ε de O(ε + 1/k) se alcanza; no es un artefacto de la prueba. K_eff ≤ 1,01.
- ‖Π‖_∞ ≈ 4 de modo uniforme, un tercio de la cota a priori.
- σ₂(P) difiere de σ₂(p) en ≤ 0,005: γ_T = γ/2 es muy conservador.
- En la familia B, k·max\|D_A/P − 1\| ∈ [0,07, 0,25], coherente con O(1/k).

**Tiempos** (`nice -n 10`, un proceso cada vez).

| Id | Archivo | Resultado | Tiempo |
|---|---|---|---|
| C0 | `c0_cotejo.py` | huellas y transcripciones: todo coincide | 0,04 s (13:26 UTC) y 0,10 s (16:05 UTC) |
| C1r | `c1_puntos_torres.py rapido` | prueba con A(16,8) y B(768,24) | 0,3 s (fallo), 3,3 s (fallo) y 9,8 s (correcta); el archivo `_tiempo` guarda sólo la última |
| C1 | `c1_puntos_torres.py` | tabla anterior | 323,8 s reales (315,0 s de usuario), 15:58:39–16:04:03 UTC |
| — | exploraciones de grados y L_max; depuración de B(192,24); huellas de blobs de B y C; cotejo de las copias de r19 | sin archivo (resultados en §0 y en las incidencias) | ≈ 1 s las tres primeras; instantáneas las dos últimas |

**Incidencias.**
1. **C0, primer intento.** No existe `/usr/bin/time`; salida vacía. Lo rehíce con el `time` de bash (`codigo/ejecutar.sh`) y borré el archivo vacío.
2. **C1r, primera ejecución.** «phi no converge»: el arranque desde los potenciales de torres daba w ≥ 27/256, sin raíz pequeña. Lo corregí desplazando los potenciales en 2·log(1 − max P) y amortiguando el paso.
3. **C1r, segunda ejecución.** B(192,24), con fracción bloqueada 3/10, tiene L_max = 7 y carga del punto de torres ≈ 0,8, fuera del régimen de D04; falló el paso de reinas. Pasé a fracción 2/10 y n/k ≥ 16 tras explorar grados y L_max.
4. **C1.** A(16,4) no convergió («paso nulo»): k = 16 y carga ≳ 0,4. No determiné si allí existe el punto de reinas en la rama; queda fuera del régimen de carga pequeña y no se usa.


**Veredicto: evidencia numérica favorable.**

## 3. Dictamen global

**Parte W2_difusion: certificada con precisiones.**
- No hay enunciados falsos ni huecos de prueba en D04:1–43 ni en A01:13–42.
- La implicación «clase histórica de C (C, γ) en el tablero de llegada y L_max < ⌈αj⌉ ⇒ P positivo en el soporte, j·max P ≤ 2C, ‖P − J‖_op ≤ 1 − γ_T, carga en P ≤ 2Cα, D_A con j·max D_A ≤ 4C, ‖D_A − J‖_op ≤ 1 − γ_T/2 y D_A/P = 1 + O(1/j)» es correcta.
- Vale para α ≤ α_T(C, γ) y j ≥ j_*(C, γ), con todas las constantes fijadas antes de α.

**Condicional a:**
- el Lema 7.3 de C (premisa publicada; sus hipótesis literales se cumplen, §2.4);
- que el tablero de llegada sea regular en la clase interior de C, que es la definición de H_j (H03:3–5). La probabilidad de visitarlo es de otra pieza.

**Con este dictamen** queda cubierta, como implicación, la «pertenencia a la clase en H_j (D04/A01)» que dejaron condicionada `W2_torres/ACTA.md`:97 y :271, `W2_norma/ACTA.md`:211–213 y `E1/ACTA.md`:170–174. Eso vale sólo para D04:1–43 y A01:13–42. D04:45–56 (menores) no se dictamina aquí.

**Observación de coherencia** (sin efecto en ningún dictamen). `W2_norma/ACTA.md`:89, :209 y :212 citan `A01.tex`:59–79, 66, 68–74 y 82. Esas líneas no existen: `r21/fuentes/latex/A01.tex` tiene 60. Con un desfase constante de +46, lo citado es A01:13–33, 20 y 36, que es lo que dictamino aquí.

**Precisiones para la próxima entrega.**
- **PD1.** En A01:14–19 y en GUIA:3, enunciar el umbral de tamaño j ≥ j_T(C, γ) de D04 (o tomar K_T ≥ 4j_T). Explicitar K_T, ε_T y j_T (§2.1(c)) (P1.1).
- **PD2.** Decir que «max_f» recorre las diagonales de las dos familias. Advertir que γ ≤ 1, así que min(1, γ) es cosmético (P1.2–P1.3).
- **PD3.** Citar la unicidad del escalado de Sinkhorn al identificar D_A con el escalado exacto de A. Decir que la cota relativa sale de los potenciales en supremo y que HS sólo se usa para la norma de operador. En GUIA:5, «aplicado a P», no «a P(1−P)» (§2.4).
- **PD4.** Fijar la notación de márgenes por objeto: (2C, 1 − γ_T) para P y (4C, 1 − γ_T/2) para D_A, y que ‖·‖₂ es la norma espectral (P5.1–P5.2).
- **PD5.** Explicitar γ′ y C′ en D04:43 (P2.1).

## 4. Resumen final

```
W2_difusion · difusión y brecha sobre la llegada histórica corta (D04, A01)
Integridad: huellas de D04 (a0464f3a…) y A01 (387f0909…) correctas;
transcripciones literales (56 y 60 líneas); copias r21 y r19 idénticas;
18/18 blobs de B y C.
Punto                                             Veredicto
1 Enunciado y cuantificadores                     Correcta con precisión
2 Proyector relativo (D04)                        Correcta
3 Márgenes y brecha (A01)                         Correcta
4 Escalado exacto (A01; C, Lema 7.3)              Correcta con precisión
5 Ajuste con N01, torres y cota por soporte       Correcta con precisión
6 Cálculos (opcional)                             Evidencia favorable
Dictamen global: CERTIFICADA CON PRECISIONES. Sin enunciados falsos ni huecos
de prueba en D04:1-43 ni en A01:13-42.
Demostrado aquí:
- ||Pi||_inf <= A = 3+2sqrt(2C)/gamma (ecuación de vértice, sin cota inferior
  por casilla); defecto <= 4A max(1,C)(eps+1/k); jacobiano I+O(|z|+1/k).
- Constantes explícitas: K_T = 8A max(1,C), eps_T = 1/(96A^2 max(1,C)),
  j_T = max(96A^2 max(1,C), 24AC, 2C). Sólo dependen de (C,gamma); alpha entra
  sólo en condiciones monótonas. Ninguna depende de alpha, de la máscara ni de j.
- Concavidad por fila (eta(t)/t creciente, Cauchy-Schwarz): el punto de torres
  es el único estacionario interior y el máximo global.
- P en [p/2,3p/2] => j max P <= 2C, carga en P <= 2C alpha, sigma2(P) <= 1-gamma/2.
- Lema 7.3 de C: hipótesis literales con K=j, M0=2C, rho*=1-gamma_T. D_A/P =
  1+O(1/j) sale de los potenciales O(1/j) en supremo, no de HS; HS da la norma
  de operador. j max D_A <= 4C y ||D_A-J||op <= 1-gamma_T/2.
- La clase resultante es exactamente la de N01/Z04/E01/F01/H01 (r = 1-gamma_T)
  y la de U01 para D con (4C, 1-gamma_T/2). Cargas en p, P y D_A: C alpha,
  2C alpha y 4C alpha.
Precisiones PD1-PD5: nombrar en A01 el umbral de tamaño de D04; max_f sólo en
diagonales y min(1,gamma) cosmético; citar la unicidad de Sinkhorn y escribir
«aplicado a P»; M0 sobrecargado (2C para P, 4C para D) y ||.||2 espectral;
explicitar gamma' y C' en D04:43.
Condicional a: Lema 7.3 de C (premisa publicada) y a que el tablero de llegada
esté en la clase interior de C (definición de H_j). D04:45-56 no dictaminado.
Numérico (decimal 40 cifras, 16 máscaras deterministas, k <= 48):
max|P/p-1| <= 1,01(eps+1/k), lineal en eps; ||Pi||_inf ~ 4; todas las cotas
de A01 se cumplen; k max|D_A/P-1| <= 0,25; Sinkhorn(A) = escalado de P(1-P).
ACTA: rev_exp/W2_difusion/ACTA.md (código en codigo/, salidas en resultados/).
```
