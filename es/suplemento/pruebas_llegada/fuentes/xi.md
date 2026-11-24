# Acta de revisión · W3_xi (D2): verificación exacta de la deducción de Ξ en E01

**Objeto.** Los cuatro puntos de la revisión W3_xi, que nace del hueco D2 del dictamen global (`rev_exp/W_global/ACTA.md`:144–151): del resto de la deducción de Ξ (E02:30–71; E03:1–21 y 30–39) sólo había evidencia numérica (`rev_exp/W2_torres/ACTA.md`:86–91).

**Revisión.** 17-11-2026.

**Dictamen global sobre esta parte: CERTIFICADA CON PRECISIONES** (§3).
- He verificado término a término E02:30–71 y E03:1–21 y 30–39. Cada identidad exacta está demostrada a mano y comprobada en aritmética exacta. Toda la contabilidad de coeficientes está verificada simbólicamente. Cada resto está acotado a mano por O(k⁻²).
- No hay hueco de prueba ni enunciado falso. La fórmula (eq:xi) y la cota (eq:q) de E01 salen tal como están enunciadas, y de ellas se sigue Γ_z′(0) = 0 en K08:8–9.
- **D2 queda descargado.** E01 sigue condicionada a la entrada R1/permanente (el hueco D1), como declara su propio texto (E01:29–30). D1 no es de este encargo.

## 0. Alcance, integridad, convenciones y método

**Integridad.**
- `sha256sum -c r19/SHA256SUMS`: 116/116. Ronda 8: 30/30. Ronda 9: 98/98. `r21/piezas_T2/03_torres/`: 4/4 con el manifiesto de r21.
- Ronda 1: la copia es parcial. Están 17 de las 38 entradas del manifiesto y las 17 pasan; faltan los 17 archivos de `calculos/` y cuatro documentos de la raíz (consultas, diagnóstico y dos informes). `mascara.tex`, `permanente.tex` y `traza.tex` coinciden además con `fuentes/…ronda9…/FUENTES.md`:10–12. `torres_fila.tex` pasa el manifiesto de su ronda.
- E01: `r19/expediente/originales/E/01_enunciado.md`:8–50 coincide byte a byte con `01_enunciado.tex`:1–43 de la ronda 8 (huella 71dd6454…, la de `CATALOGO_LITERAL.md`:77 y de FUENTES ronda 9:18). K07: `originales/K/07_coeficiente.md`:8–68 coincide con `07_coeficiente.tex`:1–61.
- W_global:146 decía que R1/mascara y R1/traza no estaban en `rev_exp/`. Ahora están en `fuentes/…ronda1…/latex/` y las he leído ahí.

**Abreviaturas.** Cito la línea del archivo fuente.
- **E01, E02, E03:** `fuentes/velocidad_via2_ronda8_20261116T072748Z/latex/01_enunciado.tex`, `02_expansion.tex` y `03_cancelacion.tex`. En la transcripción del expediente, línea de E01 = línea del `.md` − 7.
- **R1/x:** `fuentes/velocidad_via2_ronda1_20261116T023056Z/latex/x.tex`.
- **K07, K08:** `fuentes/velocidad_via2_ronda9_20261116T082611Z/latex/07_coeficiente.tex` y `08_estabilidad.tex`. **K06:** `r19/expediente/originales/K/06_torres.md` (línea del `.md`).
- **CP/07d:** `r19/expediente/originales/CP/07d_permanente.md` (línea del `.md`; orig. = `.md` − 7). **U05:** `r19/expediente/originales/U/05_atomos.md` (línea del `.md`).
- **G03:** `r21/piezas_T2/03_torres/prueba_fuente.md` (línea del archivo). **GUIA:** `r21/piezas_T2/03_torres/GUIA.md`.
- **W2T:** `rev_exp/W2_torres/ACTA.md`. **WG:** `rev_exp/W_global/ACTA.md`.

**Notación.** La de E01:2–17 y E02:2–16:
- k es el tamaño; P es bistocástica, p ≤ M/k, B = P − J, ‖B‖_op ≤ r < 1;
- s = Σp², l = Σp³, z = Cp∘², Z = zᵀz, t = z − 𝟙/k, λ = CᵀΓz, M_z = zᵀΓz;
- G_s, T_s, U, H, j, j₀ y q₄ como en E01, y v = s − 1;
- c_e = e_i + e_{k+j} es la columna de incidencia de la casilla e = (i, j), y w_e = p_e²/(1 − 2p_e).

**Qué cuenta como verificado.**
- **Demostrado a mano (M):** argumento general, válido para todo k. Son identidades matriciales cortas y cotas explícitas, escritas en §2.
- **Simbólico (S):** identidad polinómica sobre ℚ entre símbolos abstractos, comprobada con mi propia aritmética de polinomios (`codigo/poli.py`). Una vez admitidas las relaciones estructurales demostradas a mano, es una prueba de la contabilidad.
- **Exacto en ejemplos (I):** igualdad exacta de racionales en 6 matrices deterministas. Es evidencia de las identidades matriciales; su prueba general es la de mano.
- **Evidencia de orden (R):** restos racionales exactos en una familia de k creciente. Es evidencia, no prueba.

**Método.**
1. Lectura línea a línea de E01–E03, R1/mascara, R1/traza, R1/permanente, R1/torres_fila, K06–K08, CP/07d, U05, G03 (G03:188–235), GUIA y REPARACION_DE_DEPENDENCIA.
2. Reconstrucción a mano de cada paso del alcance, separando las identidades exactas de los restos O(k⁻²) (§2.1–2.2).
3. Cálculos propios (§2.5). Un proceso cada vez, con `nice -n 10` y el tiempo medido. Sin azar ni coma flotante: los decimales mostrados son racionales exactos redondeados con aritmética entera.

## 1. Tabla de veredictos

| # | Punto | Veredicto | Motivo breve |
|---|---|---|---|
| 1 | E02:30–71: pesos del escalado y operador de líneas | **Correcta con precisión** | Están demostradas y comprobadas en exacto todas las identidades exactas: Σpξ = b; Σp²λ = Σpλ² = M_z; Σpλ = s; ⟨B, p∘(λ−p)⟩ = M_z − l; la diferencial de log d; c_eᵀ(Γ−I)c_e; pdet S₀ = 2det(I−BᵀB); tr(ΓΔ); tr Δ². Cada resto está acotado por O(k⁻²). E02:69–70 sale simbólicamente. Las precisiones son de cita y de pasos implícitos. |
| 2 | E03:1–21 y 30–39 | **Correcta con precisión** | Verificadas: la resolvente; V(D) = V(P) + O(k⁻²); d″/d, exacta para P; la estructura de V, con resto exacto (5/6)Σ(t+j)³; y las cuatro cancelaciones (−4j₀/k, (3−s)j₀/k, (s−½)j₀/k y −1/(12k)), en exacto y simbólicamente. Dos cancelaciones están implícitas y conviene escribirlas. |
| 3 | Conclusión: (eq:xi), (eq:q) y Γ_z′(0) = 0 en K08:8–9 | **Correcta con precisión** | g_T − (−1/(12k) + Ξ) es exactamente una combinación lineal de 12 restos O(k⁻²) (S). La igualdad exacta asociada se cumple en los 6 ejemplos (I). (eq:q) se sigue de E03:40–48. K08:8–9 es válida con E01 uniforme. Todo es condicional a D1, como declara E01:29–30. |
| 4 | Pasos no verificables; ruta alternativa por G₂ | **No aplica** | Ningún paso queda sin verificar. Aun así, la ruta alternativa no daría por sí sola Γ_z′(0) = 0: G₂′(0) = Γ_z′(0) + φ(z) − 1/12. Identificar G₂′(0) con φ − 1/12 equivale a lo que se quiere probar y exige un cálculo de primer orden equivalente a E02–E03 que no está escrito. |

## 2. Detalle por punto

### 2.1 Punto 1 · E02:30–71

**Entradas** (no las dictamino aquí).
- D = p(1+O(1/k)) en el soporte y ‖D−P‖_HS = O(1/k): R1/mascara:5–7, por el Lema 7.3 de C; también CP/07d:33.
- Fórmula de partida E02:19–23: la comprobó W2T:82. Cotejé su normalización con CP/07d:110–113. Con C₂ = Σ(log(1−2p) − 2log(1−p)), S₂ = S de E02:3 y log Γ₂ = (log 4πk − C₂ − log pdet S₂)/2, el término −Σlog(1−p) de R1/mascara:25 da exactamente la suma local de E02:21.
- Γ = I − H − Π₊/2 − Π₋ (E02:5–6; W2T:83) y las entradas O(1/k) de B, T_s y U (E03:42–44; R1/traza:15–17). Rehice ambas cosas: el Γ calculado de forma independiente, como (S₀+Π₋)⁻¹ − Π₋, coincide exactamente con la fórmula (I, 6/6).

**(a) Pesos del escalado (E02:30–48).**

| Líneas | Afirmación | Verificación |
|---|---|---|
| 31 | ξ = Cᵀv = O(1/k) | De D = p(1−p)e^ξ = p(1+O(1/k)) sale (1−p)e^ξ = 1 + O(1/k), y p ≤ M/k (M). |
| 32–33 | S₀v = z + O_∞(k⁻²) | Fila i: Σ_j p(1−p)e^ξ = 1. Con e^ξ = 1 + ξ + O(k⁻²) queda Σ_j p_ij ξ_ij = z_i + O(k⁻²), porque Σ_j p_ij²\|ξ_ij\| ≤ z_i·O(1/k) (M). La identidad C(p∘ξ) = S₀v es exacta (I) y el desarrollo de (1−p)e^ξ también (S). |
| 34–35 | ξ = λ + O_∞(k⁻²); el representante de v no importa | ΓS₀ = I − Π₋ y Cᵀ(𝟙,−𝟙) = 0 dan ξ = CᵀΓ(S₀v) exactamente (I). Además ‖Γ‖_{∞→∞} ≤ 1 + max_a Σ_b\|H_ab\| + 3/2 = O(1): las entradas de H son O(1/k) y Σ_j\|B_ij\| ≤ 2 (M). |
| 36–37 | Σpξ = b; Σp²λ = Σpλ² = M_z | Exactas. Σ_e p_e(v_i + v_{k+j}) = Σv por bistocasticidad; Σp²λ = (Cp∘²)ᵀΓz; Σpλ² = zᵀΓS₀Γz = zᵀΓz (M, I). |
| 38–39 | D = p + p∘(λ−p) + O(p/k²); b = s + M_z/2 + O(k⁻²) | Desarrollo exacto de p(1−p)e^ξ hasta grado 3 (S). Como Σ_e p^a ξ^b = O(k^{2−a−b}), se conservan los monomios con a + b ≤ 3. La masa total ΣD = k da b = s + Σp²ξ − ½Σpξ² + O(k⁻²) = s + M_z/2 + O(k⁻²) (S, M). |
| 41 | Diferencial de log d_P = ⟨B+U, ·⟩_F | d[−½ log det(I − BᵀB)] = ⟨B(I−G_R)⁻¹, δ⟩ y B(I−G_R)⁻¹ = B + U (M). En exacto: derivada en t = 0 de −½ log det(I − (B+tδ)ᵀ(B+tδ)), con el polinomio interpolado exactamente y δ = p∘(λ−p) (I, 6/6). |
| 42 | Resto cuadrático O(‖D−P‖²_HS) | La segunda derivada está acotada por C‖δ‖²_HS en el segmento, donde ‖D−J‖_op ≤ r + O(1/k). Además ‖D−P‖²_HS = O(k⁻²) (M). |
| 43–44 | B = p − J y Σp(λ−p) = 0 | Σpλ = (Cp)ᵀΓz = 𝟙ᵀΓz = ½𝟙ᵀz = s, porque Cp = 𝟙 y Γ𝟙 = ½𝟙 (M, I). La parte J del término con B se anula para D − P (ambas son bistocásticas) y para p∘(λ−p). Además p∘(λ−p) tiene márgenes nulos (I). |
| 45–47 | log d_D − log d_P = M_z − l + ⟨U, p∘λ − p∘²⟩ + O(k⁻²) | ⟨B, p∘(λ−p)⟩ = Σp²λ − l − (1/k)Σp(λ−p) = M_z − l (I, S). El error ε = D − P − p∘(λ−p) = O(p/k²) da \|⟨B+U, ε⟩\| ≤ O(1/k)·Σ\|ε\| = O(k⁻²) (M). |

**(b) Operador de líneas (E02:49–71).**

| Líneas | Afirmación | Verificación |
|---|---|---|
| 50 | Δ = S − S₀ = C diag{p²/(1−2p)} Cᵀ | p(1−p) − p(1−2p) = p² (S); la igualdad matricial también (I). |
| 51–53 | ½ log pdet S = ½ log pdet S₀ + tr(ΓΔ)/2 − tr(ΓΔΓΔ)/4 + O(k⁻²) | **Exacta:** pdet S = pdet S₀·det(I+ΓΔ), porque Δ anula (𝟙,−𝟙) y ΓΔ lleva al complemento. Se comprueba como det(S+Π₋) = det(S₀+Π₋)·det(I+ΓΔ) (I). **Cola:** en el complemento, Y = Γ^{1/2}ΔΓ^{1/2} ⪰ 0 tiene autovalores μ ≥ 0, \|log(1+μ) − μ + μ²/2\| ≤ μ³/3 y Σμ³ ≤ ‖Γ‖³‖Δ‖_op tr Δ² = O(k⁻²). Aquí ‖Γ‖ ≤ (1−r)⁻¹, ‖Δ‖_op ≤ 2 max_a (Cw)_a = O(1/k) y tr Δ² = O(1/k) (M). |
| 56, 59–61 | tr(ΓΔ) = 2s + 2l + Z − s/k − 2⟨U,p∘²⟩ + zᵀj + O(k⁻²) | **Exacta, en las k² posiciones:** c_eᵀΓc_e = 2 + t_i + t_{k+j} + j_i + j_{k+j} − 2B_ij − 2U_ij − 1/k. Sale de (T_L)_ii = t_i + j_i, (G_L)_ii = t_i, c_eᵀΠ₊c_e = 2/k y c_eᵀΠ₋c_e = 0 (M, I). **Con peso p²:** tr(Γ C diag(p²) Cᵀ) = 2s + Z − 2l − s/k − 2⟨U,p∘²⟩ + zᵀj (I, S). **Peso real:** el término 2p³ de w aporta 4l. El resto exacto, 2Σ(w − p² − 2p³) + Σ(w − p²)c_eᵀ(Γ−I)c_e, es O(Σp⁴) + O(l/k) = O(k⁻²) (M, I, R). |
| 57, 62–65 | tr(ΓΔΓΔ) = Z + O(k⁻²) | **Exacta, con E = Γ − I:** tr(ΓΔΓΔ) − Z = [tr Δ² − Z] + 2tr(EΔ²) + tr(EΔEΔ) (I). **Cotas:** tr Δ² = Σ(Cw)_a² + 2Σw² (I), que es Z + O(k⁻²). \|tr(EΔ²)\| ≤ max\|E\|·‖Δ𝟙‖² = O(k⁻²), porque Δ ≥ 0 por entradas. \|tr(EΔEΔ)\| ≤ ‖E‖²_HS‖Δ‖²_op = O(k⁻²) (M, R). |
| 66 | log pdet S₀/2 = log 2/2 − log d_P | Exacta: pdet S₀ = 2det(I − BᵀB) (I; CP/07d:76). |
| 67 | Stirling y suma local k − 2l/3 + O(k⁻²) | c(p) = p − (2/3)p³ − (3/2)p⁴ − … (S). Como \|c_n\| ≤ 2ⁿ, la cola es O(Σp⁴) = O(M³/k²). Stirling estándar: log(k!/k^k) − ½ log(4πk) = −k − ½ log 2 + 1/(12k) + O(k⁻³); el álgebra de logaritmos se comprueba en S. |
| 68–71 | Expresión resultante | La suma de E02:20–22, sin V(D) ni el término de d_D″, es exactamente E02:69–70 más una combinación de restos (S, «E02:67-71»). |

**Precisiones.**
- **PX1.1 (cita).** E02:31 usa D = p(1+O(1/k)) sin citarla. Es R1/mascara:5–7, por el Lema 7.3 de C.
- **PX1.2 (paso implícito).** E02:44 usa Σp(λ−p) = 0 sin justificarlo. Se sigue de Cp = 𝟙 y Γ𝟙 = ½𝟙.
- **PX1.3 (paso implícito).** En E02:51–53 conviene escribir la factorización exacta pdet S = pdet S₀·det(I+ΓΔ) y acotar la cola con la forma simetrizada Γ^{1/2}ΔΓ^{1/2} ⪰ 0, como hace CP/07d:91–96.

**Veredicto: correcta con precisión.** Ningún paso falla. Las precisiones son de redacción.

### 2.2 Punto 2 · E03:1–21 y 30–39

| Líneas | Afirmación | Verificación |
|---|---|---|
| 2–3 | H_D − H = (I − H_D)(O_D − O_P)(I − H) | H_X = I − (I+O_X)⁻¹ (M). Exacta con D = P + δ/10, bistocástica (I). |
| 3–4 | Norma HS O(k⁻¹) y entradas O(k⁻²) | ‖O_D − O_P‖_HS = √2‖D − P‖_HS y las entradas de D − P son O(k⁻²). Para las entradas, \|(XδY)_ab\| ≤ max\|δ\|·(Σ_c\|X_ac\|)(Σ_d\|Y_db\|), con sumas O(1) porque las entradas de H y H_D son O(1/k) (M). |
| 5–8 | V(D) = V(P) + O(k⁻²) | **Cubos:** Σ\|a³ − b³\| ≤ C max\|a−b\|·(‖H‖²_HS + ‖H_D‖²_HS) = O(k⁻²), con ‖H‖²_HS = O(v). **Diagonales:** ‖δh‖₂ = O(k^{−3/2}) y ‖h‖₂ = O(k^{−1/2}). **Forma cuadrática:** δ(hᵀHh) ≤ 2‖δh‖‖H‖‖h‖ + ‖h‖²‖H_D − H‖_op = O(k⁻²) (M). |
| 9–12 | d_D″/d_D = v + v² + (1+2v)j₀ + j₀² + 2tr T_R² + O(k⁻¹) | Para P es exacta: d″/d = (log d)″ + ((log d)′)² y tr T_R = v + j₀, porque tr G_R = s − 1 (I, S). El paso de P a D cuesta O(k⁻¹) por E03:14–16. |
| 13–14 | (log d_P)′(1) = tr T_R; (log d_P)″(1) = tr T_R + 2tr T_R² | Por autovalor x: f′ = yx/(1 − y²x) y f″ = (x + y²x²)/(1 − y²x)² (S). En exacto, con el polinomio det(I − xG_R) interpolado sin error (I). |
| 14–16 | Lipschitz en norma HS | ‖G_R(D) − G_R(P)‖₁ ≤ (‖B_D‖_HS + ‖B‖_HS)‖D − P‖_HS = O(k⁻¹), como en CP/07d:41–45. tr T y tr T² son Lipschitz en norma traza por la identidad de la resolvente (M). |
| 17 | diag H = −(t+j); H𝟙 = 0 | Exacta (M, I). |
| 18–21 | Cubos de bloques −[Σ₃T_L + Σ₃T_R]/3; cruzados (2/3)Σ(B+U)³; diagonales omitidas O(k⁻²) | Exacta: V(P) = −¾‖t+j‖² + ½(t+j)ᵀH(t+j) − ⅓[Σ₃T_L + Σ₃T_R] + ⅔Σ(B+U)³ + (5/6)Σ_a(t+j)_a³ (M, I). El último término es O(k⁻²): (t+j)_a = O(1/k) y hay 2k sumandos. |
| 30–31 | 2⟨B∘² − p∘², U⟩ = −4j₀/k | B² = p² − 2p/k + 1/k² entrada a entrada, ⟨p,U⟩ = j₀ y 𝟙ᵀU𝟙 = 0 (M, I, S). |
| 32–35 | (Γz)ᵀj + zᵀj/2 − 3tᵀj/2 + tᵀHj = (3−s)j₀/k | Γz = z − Hz − (s/(2k))𝟙, porque Π₊z = (s/k)𝟙 y Π₋z = 0. Además 𝟙ᵀj = 2j₀ y tᵀHj = zᵀHj (M, I, S). El primer término es ⟨U, p∘λ⟩ de E02:70, reescrito con C(p∘U) = j (I). |
| 36 | Parte lineal (s − ½)j₀/k | (1+2v)j₀/(2(k−1)) con v = s − 1, 1/(k−1) = 1/k + O(k⁻²) y j₀ ≤ C (S, M). |
| 37 | −4 + (3−s) + (s−½) = −3/2 | (S). |
| 37–38 | Términos libres → −1/(12k) | 1/(12k) + M_z/2 + Z/4 − s/(2k) − 2l/3 − ¾‖t‖² + ½tᵀHt + ⅔ΣB³ + (v+v²)/(2k) = −1/(12k) exactamente (I, S). Usa M_z = Z − s²/k − zᵀHz y tᵀHt = zᵀHz. |
| 38 | Lo que queda es (eq:xi) | (S); ensamblaje en §2.3. |
| 39 | Signos de los cubos, incluidos sitios prohibidos | Correcto: las sumas de V y de Ξ recorren las k² posiciones (E01:6), y los ejemplos con ceros lo confirman (I). |

**Precisiones.**
- **PX2.1.** E03:37–38 llama «libres de j, T_s, U» a un grupo que, para cerrar, necesita una cancelación: −zᵀHz/2 (de M_z/2, por E03:24) más ½tᵀHt (de V) es 0 porque H𝟙 = 0. Esos dos términos sí contienen T_s y U a través de H. Conviene escribirlo.
- **PX2.2.** En E03:32–34 conviene decir que (Γz)ᵀj es ⟨U, p∘λ⟩ de E02:70, por C(p∘U) = j, y que se evalúa con Γz = z − Hz − (s/(2k))𝟙.
- **PX2.3.** En E03:21 el resto de las diagonales omitidas es exactamente (5/6)Σ(t+j)³; puede escribirse así.

**Veredicto: correcta con precisión.**

### 2.3 Punto 3 · La conclusión

**(a) Fórmula (eq:xi).** Los restos son símbolos propios, cada uno acotado a mano en §2.1–2.2:

| Resto | Origen | Cota |
|---|---|---|
| e_R1 | Desarrollo del permanente en E02:22 (R1/permanente:20–21) | O(k⁻²), condicional a D1 |
| e_stir, e_loc | Stirling y suma local (E02:67) | O(k⁻³) y O(Σp⁴) |
| e_trGD, e_trGDGD, e_cub | E02:56, E02:57 y la cola del logaritmo (E02:53) | O(k⁻²) |
| e_dD, e_b | E02:47 y E02:39 | O(k⁻²) |
| e_VD, e_Vdiag | V(D) − V(P) (E03:5) y diagonales omitidas (E03:21) | O(k⁻²) |
| e_dpp, e_km1 | d_D″/d_D − d_P″/d_P (E03:11) y 1/(k−1) − 1/k | O(k⁻¹)·(1/k) y O(k⁻²) |

- **Simbólico.** g_T − (−1/(12k) + Ξ) = e_R1 + e_stir + e_dD − e_b + e_loc + ½e_trGD − ¼e_trGDGD + e_cub + e_Vdiag + e_VD + e_dpp/(2k) + e_km1, sin ningún otro símbolo (`resultados/simbolico.txt`, §5).
- **Control de sensibilidad.** Cambiar −3j₀/2 por −j₀, 2ΣBU² por ΣBU², o −¾‖j‖² por −½‖j‖² deja un residuo ajeno a los restos: las tres alteraciones se detectan.
- **Exacto.** [E02:69–70] + V(P) + (d″/d)_P/(2k) = −1/(12k) + Ξ(P) + (5/6)Σ(t+j)³ se cumple como igualdad de racionales en los 6 ejemplos.

**Cuantificadores y alcance** (E01:2–5).
- Las constantes dependen sólo de (M, r), también las heredadas de las entradas de R1 a través de D.
- k ≥ k₀(M, r) se usa para p < 1/2, ‖D − J‖_op < 1 y para absorber restos.
- La deducción no usa soporte lleno: P puede tener ceros y grados desiguales, como dice E01:28. Los ejemplos E2, E3, E4 y E6 tienen ceros.
- Es un enunciado determinista para una máscara fija; no interviene ninguna ley de probabilidad. El tamaño k es el de la máscara: j en el uso puntual y m en los menores.

**(b) Cota (eq:q)** (E03:40–48; ya comprobada en W2T:85). La rehice por cálculo espectral:
- j₀ = Σσ⁴/(1−σ²) ≤ q₄/(1−r²), tr T_R² ≤ q₄/(1−r²)², ‖U‖²_HS = Σσ⁶/(1−σ²)² ≤ r²q₄/(1−r²)², y q₄ ≤ r²(M−1);
- las entradas son O(1/k) por las normas de fila ‖b_i‖² = t_i ≤ M/k;
- j ≥ 0, porque T − G = G²(I−G)⁻¹ ⪰ 0; de ahí ‖j‖² ≤ 2j₀‖j‖_∞, y además jᵀHj ≤ ‖H‖‖j‖²;
- cada suma de cubos está acotada por la máxima entrada por la suma de cuadrados.

En exacto, j ≥ 0 y ‖j‖² ≤ 2j₀‖j‖_∞ se cumplen en los 6 ejemplos. En la familia de restos, kΞ/q₄ es estable (−0,4703 … −0,4204). **Correcta.**

**(c) Γ_z′(0) = 0 en K08:8–9.** La lógica es válida:
- K07:51–57 da R = Γ_z(1/k) + O(k⁻³) uniformemente.
- La replicación (K08:2–7) conserva Γ_z y mantiene la máscara en la clase. Según K06:32–36, P = sv con v holomorfa y acotada en un disco fijo, en cualquier replicación; con la brecha de K08:6–7, las constantes (M′, r′) no dependen de b.
- E01 da entonces R(A_b) = O(s_b²), con constante independiente de b.
- Como Γ_z es holomorfa en un disco fijo, Γ_z(s_b) = O(s_b²) con s_b → 0 implica Γ_z(0) = Γ_z′(0) = 0.

Lo que K08 necesita de E01 es exactamente (eq:xi) con resto uniforme O(k⁻²). Un coeficiente erróneo de orden 1/k en Ξ daría Γ_z′(0) ≠ 0, y el control de sensibilidad muestra que mi verificación simbólica lo habría detectado. Condicional a:
- D1: R1/permanente en E01, y R1/torres_fila o U04 para el O(k⁻³) de K07;
- la replicación y la holomorfía de K06–K08, que revisó W2T (§2.3–2.4, :153) y no reexamino.

**Veredicto: correcta con precisión** (condicional a D1).

### 2.4 Punto 4 · Pasos no verificables y ruta alternativa

**Ningún paso de E02:30–71 ni de E03:1–21 y 30–39 queda sin verificar.** El punto no se activa. Para el registro, la ruta alternativa de WG:150 no daría por sí sola Γ_z′(0) = 0:
- **Equivalencia.** G03 define G_q a partir de Γ_z: conserva log H_q, quita −uφ y cambia u/6 por el desarrollo de Stirling que empieza en u/12 (G03:218–220). Con q = 2 y H₂ = H_* (W2T:119), G₂(u) = Γ_z(u) + uφ(v_u) − u/12. Como v = z en u = 0 (K06:27–28), G₂′(0) = Γ_z′(0) + φ(z) − 1/12. «Identificar G₂′(0) con φ − 1/12» equivale, pues, a Γ_z′(0) = 0: es una reformulación, no una prueba.
- **Lo que está escrito.** Ni K07 ni el atajo calculan G₂′(0). K07:10–12 sólo da kΞ = φ, y K07:58–60 sólo da cocientes removibles y H_*(0) = d(1). El atajo prueba G₂(0) = 0 y la holomorfía (G03:226–234; U05:23–36; GUIA:5). La propia GUIA:7 advierte que una cota puntual no da ese orden.
- **Lo que faltaría.** Calcular G₂′(0) exige derivar en u = 0 los términos de márgenes, grados, cofactor, local y log H₂. Es la versión en núcleos de E02:30–71 y E03, y no está escrita. El corrector de D1 (WG:139–141) sólo aporta log H₂ a primer orden; el resto seguiría pidiendo ese cálculo.

**Veredicto: no aplica.** La ruta alternativa no es necesaria ahora que E02–E03 están verificadas.

### 2.5 Cálculos (código en `codigo/`, salidas en `resultados/`)

| Id | Archivo | Qué comprueba | Resultado | Tiempo |
|---|---|---|---|---|
| S | `simbolico.py` (+ `poli.py`) | Series de Taylor (c(p), p²/(1−2p), p(1−p)e^ξ, derivadas de log d); contabilidad de E02:30–71 y de E03 como identidades polinómicas sobre ℚ; ensamblaje completo; control de sensibilidad | 22/22 OK; la diferencia es combinación lineal de 12 restos; 3/3 alteraciones detectadas | 0,06 s |
| I | `identidades.py` (+ `matq.py`) | 45 identidades exactas por ejemplo en 6 matrices bistocásticas racionales (k = 3…7, max p < 1/2, con ceros, grados desiguales y no simétricas), con Γ independiente | 270/270 OK, ninguna falla | 0,73 s |
| R | `restos.py` | Orden de los restos racionales de E02:53, 56 y 57 y E03:21, y kΞ, en la familia ½Circ + ½·inversión·Circ, k = 8…40 (M = 3) | k²·resto acotado y decreciente: E02:56 de 269,6 a 89,1; E02:57 de 541,2 a 90,2; cola cúbica de 225,9 a 8,9; diagonales de 28,6 a 20,9. kΞ → −0,1586 | 22,0 s |
| A | `busca_ejemplo.py` | Elección determinista del ejemplo E6, por búsqueda exhaustiva entre 42 permutaciones afines | 4i+2 da p = 11/20 en (5,1); 16 candidatos válidos; elegido 4i+1 | 0,04 s |

**Incidencias** (todas con `nice -n 10` y un proceso cada vez, salvo donde se indica).
1. `simbolico.py`, 1.ª ejecución: TypeError, porque faltaba la división por escalares en `poli.py` (0,05 s).
2. `simbolico.py`, 2.ª ejecución: 2 FALLAS por un error de mi guion. No había sustituido ⟨U, p∘λ⟩ = (Γz)ᵀj en el ensamblaje, y el residuo era exactamente Upl − (Γz)ᵀj (0,04 s). Corregido.
3. `identidades.py`, 1.ª ejecución: ZeroDivisionError. El ejemplo E2 original tenía p = 1/2, fuera de la hipótesis p < 1/2 de E02 (k > 2M), y el E1 original tenía p = 2/3. Rehice los ejemplos y añadí una aserción (0,07 s).
4. `identidades.py`, 2.ª ejecución: AssertionError en E6, por un solapamiento triple con p = 11/20 (0,5 s). Hice dos búsquedas auxiliares de menos de 0,1 s sin `nice` y las repetí con `nice` como `busca_ejemplo.py`.
5. Pruebas breves: interpolación y redondeo (0,02 s) y cronometraje de `restos.py` en k = 8 y 16 (0,56 s).

**Huellas SHA256 de lo entregado** (primeros 16 hexadecimales):

| Archivo | Huella |
|---|---|
| `codigo/poli.py` | 92d9fe764d6eb2aa |
| `codigo/matq.py` | 2311b4bb16b95ade |
| `codigo/simbolico.py` | 639dc82488207d3c |
| `codigo/identidades.py` | adfdf292254f4039 |
| `codigo/restos.py` | f3bff393a883ed48 |
| `codigo/busca_ejemplo.py` | fb020d5887ed0f04 |
| `resultados/simbolico.txt` | 1f690c9f5cb8ea62 |
| `resultados/identidades.txt` | 3dcc03f9dabe70c6 |
| `resultados/restos.txt` | 6e1053086cb19e2c |
| `resultados/busca_ejemplo.txt` | 87f13f8d5b7161b3 |

**Lectura.** S es prueba de la contabilidad, dadas las relaciones estructurales demostradas a mano. I y R son evidencia: I, de las identidades matriciales en ejemplos, y R, del orden de los restos en una familia. No miden la uniformidad de las constantes en toda la clase; esa uniformidad la dan las cotas a mano.

## 3. Dictamen global

**Parte W3_xi (D2): certificada con precisiones.**
- La deducción de Ξ en E01 es correcta paso a paso en todo el alcance: E02:30–71 y E03:1–21 y 30–39. Junto con lo que ya comprobó W2_torres (E02:5–6, E03:22–29 y 40–48), la deducción de E01 a partir de sus entradas queda verificada completa.
- No hay huecos de prueba ni enunciados falsos.
- (eq:xi) y (eq:q) salen tal como están enunciadas, con constantes C(M, r), k ≥ k₀(M, r) y ceros permitidos.
- K08:8–9 obtiene correctamente Γ_z(0) = Γ_z′(0) = 0, y con ello el orden s³ que necesita M01.

**D2 queda descargado.** La reparación por la ruta alternativa (G₂′(0) = φ − 1/12) no es necesaria. Además, esa ruta no es independiente: equivale a Γ_z′(0) = 0 y exigiría el mismo cálculo de primer orden.

**Sigue condicional a:**
- D1: el desarrollo O(K⁻²) de R1/permanente, extraído de Divoux–Wang (E01:29–30; WG:130–142);
- las entradas de clase y de escalado de R1/mascara:5–7 y de C;
- la replicación y la holomorfía de K06–K08, revisadas por W2_torres (sus puntos 2–3, correctos con precisión).

**Precisiones para la próxima entrega.**
- **PX1.1.** Citar R1/mascara:5–7 en E02:31.
- **PX1.2.** Justificar Σp(λ−p) = 0 en E02:44 por Cp = 𝟙 y Γ𝟙 = ½𝟙.
- **PX1.3.** Escribir pdet S = pdet S₀·det(I+ΓΔ) y la cota simetrizada de la cola en E02:51–53.
- **PX2.1.** Hacer explícita en E03:37–38 la cancelación −zᵀHz/2 + ½tᵀHt = 0.
- **PX2.2.** Decir en E03:32–34 que (Γz)ᵀj = ⟨U, p∘λ⟩ y escribir Γz = z − Hz − (s/(2k))𝟙.
- **PX2.3.** Escribir en E03:21 el resto exacto (5/6)Σ(t+j)³.

## 4. Resumen final

```
W3_xi · D2: verificación exacta de la deducción de Xi en E01 (ronda 8)
Integridad: r19 116/116; R8 30/30; R9 98/98; r21 03_torres 4/4; R1 17/17
presentes (copia parcial) y mascara/permanente/traza = FUENTES R9:10-12;
E01 y K07 transcritos literalmente.
Punto                                                   Veredicto
1 E02:30-71 (escalado y operador de líneas)             Correcta con precisión
2 E03:1-21 y 30-39 (V, d'', cancelaciones)              Correcta con precisión
3 Conclusión: (eq:xi), (eq:q), Gamma_z'(0)=0 en K08     Correcta con precisión
4 Pasos no verificables / ruta alternativa G2           No aplica
Dictamen global: CERTIFICADA CON PRECISIONES. Sin huecos ni enunciados falsos.
D2 queda descargado; E01 sigue condicional a D1 (R1/permanente, Divoux-Wang).
Verificado:
- E02: sum p xi=b, sum p^2 lambda=sum p lambda^2=M_z, sum p lambda=s,
  <B,p(lambda-p)>=M_z-l, d log d=<B+U,.>, c_e'(Gamma-I)c_e, pdet S0=2det(I-B'B),
  pdet S=pdet S0 det(I+Gamma Delta), tr(Gamma Delta), tr(Gamma Delta)^2: exactas;
  restos O(k^-2) acotados a mano; E02:69-70 sale simbólicamente.
- E03: resolvente, V(D)=V(P)+O(k^-2), d''/d exacta para P, V(P) con resto exacto
  (5/6)sum(t+j)^3; cancelaciones -4j0/k, (3-s)j0/k, (s-1/2)j0/k, -1/(12k).
- Ensamblaje simbólico: g_T-(-1/(12k)+Xi) = combinación lineal exacta de 12
  restos O(k^-2); 3 coeficientes alterados de Xi se detectan.
- (eq:q) rehecha; K08:8-9 válida: R=O(s_b^2) uniforme + holomorfía.
- Ruta alternativa: G2'(0)=Gamma_z'(0)+phi(z)-1/12, luego identificar
  G2'(0)=phi-1/12 equivale a lo que se quiere; no es atajo ni está escrita.
Cálculo propio (Fraction, nice -n 10, sin azar ni coma flotante):
- simbólico 22/22 (0,06 s); 270/270 identidades exactas en 6 matrices k=3..7
  con ceros (0,73 s); familia k=8..40: k^2*restos acotados, kXi/q4 estable (22 s).
Precisiones: PX1.1-1.3 (cita de D=p(1+O(1/k)); sum p(lambda-p)=0;
factorización de pdet S); PX2.1-2.3 (cancelación de z'Hz; origen de
(Gamma z)'j; resto exacto de las diagonales). Todas de redacción.
ACTA: rev_exp/W3_xi/ACTA.md (código en codigo/, salidas en resultados/).
```
