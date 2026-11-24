# Acta de revisión externa W2 · Entradas analíticas y algebraicas de la cota por soporte

**Revisor.** Externo e independiente, ajeno al proceso que escribió la prueba. Fecha: 2026-11-17. Trabajé sin web y sin acceso a otros equipos, sólo con esta carpeta. Los cálculos son propios, exactos y deterministas, con `nice -n 10`, un proceso cada vez y tiempos medidos. No reviso E1, E2, el recuento de tipos ni el exponente 7 de los pares.

**Objeto.** La cota que el teorema usa para cada soporte U de v casillas, con 5 ≤ v ≤ 8 log n [B03 55–58]:

  |Δ_U(F̂_{U,q} − Λ)| ≤ C^v·(Cv)^{c+1}·∏_i d_i·j^{−p},  con p = v+c+1, v+c o v+c−1 según β = 0, 1 o ≥ 2.

Reviso sus entradas analíticas (holomorfía y gas) y algebraicas (órdenes en s, proyección y ciclo).

**Integridad.**
- Manifiestos comprobados:
  - ciclo_exterior 8/8, cotejo_adenda2 7/7, grados_ponderados 12/12 y grupos_interlinea 12/12;
  - media_matriz 14/14, menores_uniformes 14/14 y patrones_finitos 12/12;
  - `rev_exp/r19/SHA256SUMS` 116/116.
- Cotejé las 21 transcripciones del expediente que corresponden a mis fuentes (U01–U08, Z01, Z02, Z04, X02, G01, G05–G07, P01 y P03–P06). Quitada la cabecera, todas coinciden literalmente con los originales.

**Convenciones de cita.**
- [Gnn], [Pnn], [Unn], [Znn], [Xnn] e [Inn] son `rev_exp/fuentes/<entrega>/latex/nn_*.tex` de, respectivamente:
  - grados_ponderados, patrones_finitos y menores_uniformes;
  - ciclo_exterior, cotejo_adenda2 y grupos_interlinea.

  Los números son líneas del propio archivo.
- [B01], [B02], [B03] y [V] son las transcripciones `rev_exp/r19/expediente/originales/B/0n_*.md` y `V/REVISION.md`. Los números son líneas originales; en el `.md`, súmese 7.
- [06c] es `expediente/latex/06_corte.tex`, [MAPA] es `expediente/MAPA_DEPENDENCIAS.md` y [W2t] es `rev_exp/W2_tipos/ACTA.md`.

**Notación.**
- s es el parámetro de tamaño, con valor físico s = 1/j. ζ_i es la actividad del sitio i, de valor físico O(1/j). Llamo coste al exponente de s.
- c es el número de componentes del grafo de incidencia completo (sitios y líneas de las cuatro familias, incluidas filas y columnas), y β su número ciclomático. Un grupo es una componente.
- El soporte de un término es el número de grupos de los que depende. El déficit de una interacción de coste l y h grupos es η = l+1−h.
- d_i = máx_{f∋i}|f∩U|.
- H(s,ζ) es la diferencia alternada sobre las caras Y ⊆ U de log Ẑ_Y − Λ_Y, centrada. 𝒰 = ∏_{i∈U}(I − ev_{ζ_i=0}).

## 1. Tabla de veredictos

| # | Punto | Veredicto | Naturaleza del resultado |
|---|---|---|---|
| 1 | Holomorfía y gas local en \|ζ_i\| ≤ κ′/d_i, \|s\| ≤ κ/v: silla holomorfa y única, logaritmo O(v), gradiente exterior acotado, constantes uniformes para v ≤ 8 log n [G02–G04, B02] | **Correcta con precisión** | Demostrado como implicación de entradas importadas. Dos precisiones de redacción, sin consecuencias (1.1 y 1.2). |
| 2 | Órdenes por clase: c+1 en bosques, c−1 con un campo repetido en un ciclo, c−1 en varios ciclos; mismo exterior, campo afín y cofactor en todas las caras [P03–P05, U06, U07, Z01–Z02, X02] | **Correcta con precisión** | Demostrado; rehíce la cuenta de incidencias, el desarrollo del bosque, la poda, la raíz y la identidad del cofactor. Comprobado además de forma exacta en un modelo de juguete con esas mismas hipótesis. Precisión 2.1: el paso de v fijo a v ≤ 8 log n queda implícito. |
| 3 | Proyección y Cauchy: (Cv/j)^w desde el coste w; ∏_i(Cd_i/j); Σ_iCd_i/j ≤ Cv²/j para la repetición; la cota final [G05, B03] | **Correcta** | Demostrado. |
| 4 | El ciclo: el término crítico conserva log(1−θ²), con dos potencias de actividad por casilla del ciclo, y el resto empieza en el coste c [Z01–Z03] | **Correcta** | Demostrado. Identidades locales verificadas exactamente en nueve grafos y fórmula de poda verificada exactamente. |
| 5 | Coherencia con el tablero uniforme; en varios ciclos no se supone ninguna cancelación [V, B03, P05] | **Correcta** | Para β ≥ 2 la deducción sólo usa conexidad. Las leyes del hipergrafo no son verificables con este material, pero no son premisa. Mi modelo de juguete muestra que los tres exponentes son nítidos. |
| 6 | Cálculos exactos propios | **Realizados** | Cuatro programas, 29 s de CPU en total. Ninguna discrepancia con lo que afirma la prueba. |

**No encontré ningún enunciado falso ni ningún hueco de prueba en mi parte.** Las tres precisiones (1.1, 1.2 y 2.1) son de redacción y no obligan a cambiar enunciados ni constantes.

## 2. Detalle por punto

### Punto 1 · Holomorfía y gas local [G02–G04; B02 28–60]

**1a. Equilibrio exterior en una bola de variación total** [G02 2–24; B02 28–50; U02 6–26].
- Cada copia RC tiene masa s y peso t_b = 1 − y_b. Identificando copias, la medida M_1 = tμ difiere de la basal en TV a lo sumo (2+a)Σ|h| = O(v|s|) [G02 10–14].
- Las dos masas totales coinciden, porque Σ_filas y_r = Σ_columnas y_c = Σ_i x_i.
- El jacobiano basal en calibre fijo tiene inverso uniforme en supremo:
  - el Schur I − D_0^tD_0 es invertible en norma dos por la brecha;
  - el núcleo acotado convierte norma dos en supremo [B02 33–36; U02 13–17];
  - las copias de masa cero tienen bloque identidad.
- La raíz w = 2Z′/(1+√(1−4σt_rt_cZ′)) es regular si 4|σ|(1+a)²M_0′e^{2r_0} < 1/2 [B02 38–42]. La iteración con el inverso basal es contractiva y da existencia, unicidad y holomorfía uniformes [B02 43–46].
- El número de casillas sólo interviene a través de la TV, que es O(v|s|) ≤ Cκ. Por eso basta |s| ≤ κ/v en la diagonal h_g = σ = s [B02 52].
- Observación: en s = 1/j las filas originales suprimidas tienen masa 0. Sigue siendo una perturbación pequeña, de TV total 2v/j.

**1b. Gradiente de la acción** [G02 25–42].
- Rehíce la cuenta con el teorema de la envolvente, con las restricciones ∫u dμ_C = t_r y ∫u dμ_R = t_c.
- Los multiplicadores valen −log t_r − α_r − 1 y −log t_c − β_c − 1, y la variación de t log t cancela los dos log t y las dos unidades. Sale ∂_i(ℛ/s) = α_{r_i} + β_{c_i}, acotado en la bola de potenciales.
- La cota direccional Σ_l|∂_l∂_iR_c|/d_l ≤ 2B/a, con h_l = e^{iφ_l}/d_l, es correcta y no pierde el número de vecinos. El revisor de tipos ya la comprobó [W2t 81].

**1c. Silla local, determinante y O(v)** [G02 48–66].
- La contracción en ‖x‖_* = máx_i d_i|x_i| es correcta. Usa Σ_{i∈f}1/d_i ≤ 1 y la cota direccional. La silla es única en la caja y holomorfa en (s, ζ).
- Escribí (−H_B″)V_0 = diag(1−d_ix_i) + [Σ_f 1_f1_f^t/q_f]·diag(x(1−x)), y la parte exterior R″V_0 tiene filas ≤ C‖x‖_*. Por tanto ‖Δ‖_∞ ≤ C‖x‖_* y |log det(I+Δ)| ≤ v·Σ_k‖Δ‖_∞^k/k ≤ 2v‖Δ‖_∞.
- Los logaritmos de q_f, 1−x_i y x_i/ζ_i son O(1) por sitio o fibra, y hay a lo sumo 4v fibras. R_c(x) = ∫_0^1∇R_c(tx)·x dt ≤ B·a·v. El prefactor exterior está acotado por 1d. El valor canónico es, pues, O(v) en el polidisco.

**1d. Representación de los átomos** [G03 10–63].
- G_s(X) depende de X sólo a través de θ = sT_X, con ‖T_i‖ ≤ 3. Todas las interpolaciones quedan en la bola, porque 3v|s| ≤ 3κ.
- La acción, escrita en w y M_1 tras cancelar t log t, admite el valor en el átomo duro t = 0 [G03 23–27].
- Cauchy multilineal da |Δ_iΔ_DG_s| ≤ (l+1)!C^{l+1}|s|^l. Con C(v,l) ≤ v^l/l! sale Σ_{D≠∅}|Δ_DΔ_iG_s| ≤ CΣ_{l≥1}(l+1)(Cv|s|)^l ≤ B_1, uniforme en v. Comprobado.
- La extensión a conjuntos incompatibles [G03 45–47] sólo sirve para acotar. La inversión de Möbius de G04 sólo usa subconjuntos de un conjunto independiente.

**1e. El gas** [G04 1–35]. Rehíce la inducción en |V_0|.
- La eliminación de vecinos cuesta ≤ exp(2K_1·4κ′) ≤ e.
- El último factor es la esperanza compleja de ∏_D(1 + (e^{a_D}−1)1_{D⊆X}). Cada monomio de indicadores tiene módulo ≤ 1, porque se factoriza en cocientes R_l/(1+R_l), con |R_l| ≤ 1/2, en volúmenes estrictamente menores y con pines admisibles. La hipótesis de inducción cubre todos esos casos.
- Se cierran Z ≠ 0 y |R_i| ≤ K_1|ζ_i|, y de ahí |log Z| ≤ Σ_i 2|R_i| = O(v).
- **Precisión 1.1 (constante).** De Σ_D|a_D| ≤ B_1 sólo se sigue ∏_D(1+|e^{a_D}−1|) ≤ exp(B_1e^{B_1}), no e^{B_1} como se escribe [G04 32]. Basta definir K_1 con B_1e^{B_1} en lugar de B_1. No cambia nada más.

**1f. Error físico** [G04 36–44; U05 32–44].
- Se tiene Σ_X|ζ^X||Ŵ_X/W_∅| ≤ e^{(B_0+κ′)v} y |1/Ẑ| ≤ e^{Cv}. El error relativo de la suma es, pues, ≤ e^{C′v}Δ_q.
- Δ_q = (Cq/j)^q + Ce^{−cj} ≤ j^{−(2v+6)} si Cq ≤ √j, y e^{C′v}Δ_q < 1/2 uniformemente en 5 ≤ v ≤ 8 log n.
- La rama del logaritmo exacto en campos complejos queda fijada como log Ẑ + log(1+ε), con |ε| < 1/2. No se usa ninguna continuación en s del conteo exacto.
- El valor de Δ_q es una entrada de Menores uniformes 01–05, del dominio de E1, y no lo reviso.

**1g. Uniformidad.**
- Las condiciones son v/j ≤ κ/2, Cd_i/j ≤ κ′/2, Cq ≤ √j con q = 4v+12, y e^{Cv}Δ_q < 1/2.
- Valen para v ≤ 8 log n y j = ⌊bn⌋ desde un n_0(b).
- Las constantes (M_0′, r′, a, κ, κ′, B_0, B_1, K_1, C) son de clase y no dependen de b, de ρ ni de v. Esto concuerda con [B03 59–60] y [W2t 174–179].

**Precisión 1.2 (fuentes).** [G02 22], [G03 39] y [G05 18] remiten a «Grados intermedios», partes 03–05, que no está en el material. El contenido que se necesita sí está:
- el argumento de función implícita, en [B02 28–50] y [U02 6–26];
- la función de torres holomorfa y acotada en |u| ≤ c_0/q, en [U01 26–28] y [U05 9–31];
- las cancelaciones, en [U06] y [P03–P05].

El expediente cita U06, no Grados intermedios 05 [B03 47–49].

**Entradas importadas, no revisadas aquí:**
- las fórmulas del exterior [B01 34–56], que proceden de Media matriz y R9 y se revisaron en R18;
- Δ_q y la rama holomorfa del aproximante de torres (Menores uniformes 01–05);
- la identificación de la rama física por la norma canónica ‖q_i/P_i − 1‖ ≤ Cη [B02 56–58];
- los márgenes de clase (A01, D04).

### Punto 2 · Órdenes por clase de soporte [P03–P05; U06; U07; Z01–Z02; X02]

**2a. Hipótesis estructurales** [B02 2–22; P03 15–30; U06 7–12].
- R_0(θ)/s y A_0(θ), con θ lineal en s·y, tienen grados ≤ l+1 y ≤ l en y.
- Desarrollé E_ab = ∫Z(θ)²dM_a^RdM_b^C con M_a = μ^0 + Σ_b h f_a(y_b)δ_b:
  - una inserción da s·f_2·K/2 en la acción y s(f_2 − f_1 − f_2)K/2 = −s f_1K/2 en el prefactor (c2, §5);
  - dos inserciones dan s²(Z_rc²/2)(P, B);
  - los grados cumplen las cotas, salvo la pareja, que se trata aparte por su soporte ≤ l.
- Restos sΨ. Con h_g = 0, las copias de g tienen masa cero y desaparecen de las integrales, del determinante de Fredholm (son nulas en L²) y de los grados, que van pesados por su masa. Todo término que depende de y_g lleva, pues, h_g. Hay además un σ inicial: R = V/s y V = R_0 + σE_22/2 + σ²Ψ̃. Por tanto el soporte es ≤ l−1.
- d̃_T sólo depende de los datos a través de h_g y lleva el factor s_m [G03 38–43; U05 9–31], así que cumple lo mismo.
- La amplitud común está fuera de mi encargo (revisión de R18, [V 22]). Aquí sólo compruebo su uso.

**2b. Cuenta de incidencias y clase de varios ciclos** [P03 32–48; U06 41–42; Z02 16; X02 44].
- Para un coeficiente conexo, d = 1 + Σ_a(h_a−1) − L_I = w + 1 − Σ_aη_a − L_I es una identidad del grafo bipartito interacciones–grupos.
- Un término que no toca un grupo no depende de sus activaciones: los coeficientes exteriores están congelados, y una diagonal con dos sitios de U une sus grupos. La alternancia lo anula.
- Como η_a ≥ 0, sale w ≥ c−1. **Esto prueba la clase de varios ciclos** [P05 1–6]. No usa la exactitud de Bethe, sino sólo que el exacto y el canónico se separan para interacciones sobre grupos disjuntos: la partición se factoriza, la silla se descompone y el determinante es diagonal por bloques.

**2c. Bosque: términos ordinarios** [P04 1–24; U06 13–39]. Rehíce el argumento.
- Por exactitud de Bethe, con m la silla (igual a la media inclinada exacta), el exacto menos el canónico vale log E_m exp{R(m+Z) − R(m) − R′(m)Z + A(m+Z) − A(m)} + ½ log det(I − V_mR″(m)).
- Esto usa que D_loc = det[(−H_B″−R″)V_0]·∏q_f/∏(1−x_i) es igual a det(I − VR″), porque en un bosque el factor sin reacción vale 1. Lo verifiqué exactamente (c1).
- En un diagrama conexo, d ≤ q + b ≤ w + 1 − N_A − L.
- Los casos (N_A, L) = (0,0) y (1,0) son imposibles: un árbol tiene dos hojas y sólo un vértice de prefactor puede tener grado 1.
- En el caso (0,1) todos los grados valen 2. Son anillos que suman −½ log det(I − VR″) y cancelan.
- La reposición de la silla añade a lo sumo t grupos a coste t. Queda d ≤ w−1.

**2d. Raíz excepcional** [P04 26–64; U06 40–56; X02 1–45; U05 45–54].
- Con un solo excepcional de déficit 1, árbol y vértices de soporte máximo (multilineales), la poda deja la raíz.
- Verifiqué exactamente, como identidades polinómicas (c2):
  - P + B = uv′[2(1−u)(1−v′) + (1−u) + (1−v′)], que se anula en {0,1}²;
  - (P+B)(m) + ½tr(ΣP″(m)) = 4(1−m_1)(1−m_2)Σ_12, que vale 0 para fibras de grupos distintos;
  - la expresión que figura en [P04 59].
- El predictor lleva P″ y no (P+B)″, porque B es prefactor y se evalúa en la silla. Es correcto.
- Con amplitud λ ≠ 1 delante de B, el exacto ve 1−λ en el átomo (1,1), y el residuo del predictor es (λ−1)·m_1m_2(m_1m_2 − m_1 − m_2) ≠ 0. La amplitud común es, pues, necesaria.
- Si las dos fibras están en un mismo grupo, el déficit es ≥ 2.
- **Conclusión: el primer coste en bosques es c+1** [P04 64; B03 49].

**2e. Un ciclo** [P05 8–30; U06 57–69; Z02 13–63].
- A coste c−1 con d = c sólo caben árboles de interacciones de acción de soporte máximo, que se enraízan en el grupo con ciclo.
- Las hojas son forestales: sus medias son las verdaderas y su determinante vale 1 en todo campo. Así ∂_tΔ|_{t=0} = (∏m_a)·D_0Δ_núcleo, con D_0 = Σα_iζ_i∂_{ζ_i}. La derivada es logarítmica porque un campo lineal multiplica las actividades [B02 25–26].
- En la raíz queda log(1−θ²) ∈ (∏_{i∈𝒞}ζ_i²). Los operadores ζ∂_ζ y los factores holomorfos de las hojas conservan ese ideal, y las caras que rompen el ciclo son bosques.
- 𝒰 lleva (∏_𝒞ζ²) a (∏_Uζ·∏_𝒞ζ). Desde el coste c basta la proyección ordinaria [B03 49–50].

**2f. Mismo exterior, campo afín y cofactor** [U07 11–58; I03 26–44; B01 3, 57–59].
- El exterior A∖U es común a las 2^v caras y los coeficientes exteriores no dependen de las activaciones. El campo afín r = ∇R(0) sólo depende del exterior [B02 23–24].
- Rehíce la identidad del cofactor con el lema del determinante: pdet S/(pdet S_ext·∏_Dq_f) = det T·det(T^{−1} + U_R^tS_ext^+U_R + U_D^t diag(1/q)U_D).
- Con −H_B″ = T^{−1} + U_R^t diag(1/t)U_R + U_D^t diag(1/q)U_D y R″ = U_R^t diag(1/t)U_R − U_R^tS_ext^+U_R, el último factor es det(−H_B″−R″).
- Con b_iT_ii = x_i(1−x_i)^{1−d_i}, el cociente con D_loc es ∏_bt_b, que cancela +½Σlog t_b.
- En x_i = 0, la columna i de (−H_B″−R″)V_0 es e_i: su término diagonal es 1 − d_ix_i y los demás llevan el factor x_i.
- Los escalares se restringen igual. Los factores unitarios son redundantes, porque la entropía categórica de un sitio solo es la de Bernoulli.
- Las dos caras de un sitio coinciden, pues, en ζ_i = 0, también en el normalizador. Verificado.

**2g. Paso a v ≤ 8 log n.**
- Las anulaciones [s^l]H ≡ 0 para l < w, y la pertenencia a los ideales, son identidades entre coeficientes de Taylor en s = 0. Si se prueban en un polidisco pequeño (radios ρ_v que dependen de v [P05 33]), se extienden por continuación analítica en ζ al polidisco |ζ_i| ≤ κ′/d_i, donde H es holomorfa y acotada (punto 1).
- Hace falta que el aproximante sea el mismo:
  - las propiedades de soporte valen con q = 4v+12, por el argumento de marcadores de 2a;
  - cambiar q conserva los coeficientes de grado w ≤ v [X03 9–31], y basta porque w ≤ c+1 ≤ v/2+1.
- **Precisión 2.1.** [B03 47–49] y [G05 18–19] usan este paso sin enunciarlo. Es válido, pero conviene escribirlo.

**2h. Comprobación exacta en un modelo de juguete** (c3a y c3b).
- **Construcción.** Con coeficientes racionales fijados por una fórmula determinista, construí interacciones que cumplen exactamente las hipótesis de [U06 7–12]:
  - acción de grado ≤ l+1 y prefactor de grado ≤ l, en todos los patrones de grupos;
  - la pareja con amplitud común;
  - restos de soporte ≤ l−1 en los dos lados, y un error de torres sólo en el exacto.

  Calculé el exacto y el predictor (silla, A(x*) y −½ log D_loc con R″) como series exactas en s.
- **Nivel de grupos (c3a).**
  - Bosques con c = 1, 2 y 3: [s^w]H = 0 para w ≤ c y ≠ 0 en w = c+1.
  - Un ciclo con c = 2 y c = 3: H se anula hasta el coste c−2.
  - Con c = 2, [s^1]H coincide exactamente con la fórmula de poda de [Z02 26–29].
  - Si se escala por ε un sitio del ciclo, h/ε → 0 y h/ε² se estabiliza en 5,85·10⁻⁵ (4,83·10⁻⁵ en ε = 10⁻¹; 5,848·10⁻⁵ en ε = 10⁻⁴): divisibilidad por ζ². Lo mismo ocurre a coste 2 con c = 3. Si se escala un sitio de rama, h tiende a una constante no nula (2,14·10⁻⁶).
- **Pruebas de sensibilidad.** Con amplitud distinta, con un término de acción de grado l+2, o sin R″ en el determinante, el bosque falla en w = c. Las hipótesis son necesarias y la comprobación no es vacía.
- **Nivel de sitios (c3b).** Trabajo módulo ζ_i² = 0, donde el coeficiente de ∏ζ_i a coste w da el orden físico j^{−v−w}. El primer coste con coeficiente no nulo es exactamente:
  - c+1 en bosques (c = 1, 2, 3);
  - c en un ciclo (c = 1, 2, 3);
  - c−1 en varios ciclos (c = 1, 2).

  Los tres exponentes son a la vez cotas correctas y nítidos.
- Es evidencia algebraica exacta en casos pequeños, no una prueba para v creciente. La prueba es la de 2b–2g.

### Punto 3 · Proyección y Cauchy [G05 6–28; B03 47–58]

- **Campos.** La diferencia alternada cuesta ≤ 2^v y se anula en cada cara ζ_i = 0 (2f). Por el lema de Schwarz iterado, |H/∏ζ_i| ≤ M/∏R_i con R_i = κ′/d_i. En |ζ_i| ≤ C/j queda M·∏(Cd_i/(κ′j)). La versión con suma geométrica [G05 9–13] es equivalente si Cd_i/j ≤ 1/2.
- **Repetición.** Σ_{α≥1, algún α_i≥2}∏ρ_i^{α_i} = ∏ρ_i·[∏(1−ρ_i)^{−1} − 1] ≤ 4·∏ρ_i·Σρ_i. Aquí Σρ_i ≤ CΣd_i/j ≤ Cv²/j [G05 14–15].
- **Tamaño.** Cauchy en |s| = κ/v da |Σ_{l≥w}[s^l]H·s^l| ≤ 2M(v/(κj))^w si v/(κj) ≤ 1/2. El resto sigue siendo holomorfo en ζ y se anula en las caras, porque 𝒰 conmuta con [s^l]. Sustituir el campo físico tras extraer el coeficiente es legítimo, porque es una identidad puntual en el dominio [Z03 21].
- **Las tres clases.**
  - Bosque: (Cv/j)^{c+1}.
  - Un ciclo: (Cv/j)^{c−1}·Cv²/j + (Cv/j)^c.
  - Varios ciclos: (Cv/j)^{c−1}.

  Con M ≤ 2^v·Cv ≤ C^v, las tres caben en C^v(Cv)^{c+1}∏d_i·j^{−p}.
- **Error físico.** 2^v·e^{Cv}Δ_q ≤ C^v·j^{−(2v+6)} ≤ C^v·j^{−p}, porque p ≤ v+c+1 ≤ 3v/2+1. Ni siquiera hace falta proyectar en campos [U08 35–38].

### Punto 4 · El ciclo [Z01–Z03; I04]

- **Identidad local** (c1, exacta). Probé nueve grafos: cuatro bosques y cinco con un ciclo de 3, 4 o 5 sitios, con ramas y con factores ternarios sobre el ciclo. En todos:
  - Z/Z_B = 1+θ, con θ = (−1)^b∏x_i/(1−x_i);
  - D_loc = (1−θ)², que coincide con la forma de Sylvester [Z01 45–55];
  - en los bosques, Z = Z_B y D_loc = 1.

  El argumento de [Z01 50–55] es correcto: las caminatas cerradas no retroceden, y las dos orientaciones usan estados de incidencia disjuntos, cada una con producto θ.
- **Transporte al coste crítico** [Z02]. Es correcto (2e), y la fórmula de poda queda verificada exactamente (c3a, T5).
- **Dos potencias por casilla del ciclo.** El coeficiente crítico proyectado es divisible por ∏_Uζ_i·∏_𝒞ζ_i [Z02 61–63]. Con b ≥ 3 [Z03 4–6], pues dos casillas comparten como mucho una línea, sale T_U ≤ C_2^v(C_2v)^{c+2}∏d_i·j^{−(v+c+2)} [Z03 26–35].
- **Resto desde el coste c** [Z03 36–38]. La cota mejorada del sector [Z03 55–59] no la usa el expediente, que se queda con p = v+c [B03 49–50].

### Punto 5 · Coherencia con el tablero uniforme [V 39–50]

- **Órdenes.** Las ocho filas de la tabla de [V] coinciden con p:
  - árbol v+2, dos árboles v+3, tres pares v+4;
  - un ciclo v+1; fila o columna común v+1;
  - ciclo con árbol v+2 (ley conjetural M7);
  - dos componentes con ciclo v+1; conexo con varios ciclos v.
- **Varios ciclos.** La deducción para β ≥ 2 usa sólo conexidad: [B03 51], [P05 1–6], [G05 20], [U08 31] y la línea 3 del CONTINUAR de ciclo exterior. No importa la serie del hipergrafo [B03 60–61; MAPA 14].
- **No supone ninguna cancelación en ese sector.** El lado e del hipergrafo sin potencia adicional (W_{≥2}x^v y λ₁λ₂ab·x^{v+1}) es compatible con la cota.
- Las leyes del hipergrafo proceden de entregas que no están en el material, y por eso no son verificables aquí. No son premisa, y una cota superior no depende de la fila conjetural.
- **Evidencia independiente** (c3b, B7–B9). En varios ciclos, el coeficiente multilineal a coste c−1 es no nulo (−1/2, 1 y −4/9). No hay ningún mecanismo algebraico general de cancelación.

### Punto 6 · Cálculos (código en `codigo/`, salidas en `resultados/`)

| Programa | Qué comprueba | CPU medida |
|---|---|---|
| `c1_ciclo_local.py` | Z/Z_B = 1+θ y D_loc = (1−θ)² en un ciclo; 1 y 1 en bosques; forma de Sylvester (Z01) | 0,04 s |
| `c2_raiz_dos_fibras.py` | Factorización de P+B, anulación booleana, identidad con covarianza y sensibilidad a la amplitud (X02, P04, U05) | 0,03 s |
| `c3a_juguete_grupos.py` | Órdenes por grupos, fórmula de poda, escala ε² y tres pruebas de sensibilidad | 7,2 s |
| `c3b_juguete_sitios.py` | Primer coste con coeficiente multilineal no nulo en las tres clases | 21,8 s |

Todo es aritmética racional exacta, sin azar: los coeficientes «genéricos» salen de una fórmula fija.

## 3. Cuantificadores, ley y tamaño

- La cota por soporte es determinista. Vale en una máscara fija de la clase de referencia (márgenes M_0′ y r′), de tamaño j, con el exterior A∖U común a las 2^v caras.
- Los átomos usan menores de tamaño m = j−|I|, con su escalado propio y el mismo q = 4v+12.
- s es complejo sólo en el aproximante; el conteo exacto sólo se evalúa en s = 1/j. Los campos varían en el polidisco κ′/d_i; los físicos son O(1/j).
- Las constantes son de clase y se fijan antes que b y ρ; sólo n_0 depende de b. Aquí no interviene ninguna ley: la integración contra ν con el indicador H_j es posterior y pertenece a [W2t].

## 4. Estados

- **Demostrado** (lectura con cada paso rehecho):
  - la holomorfía uniforme y la cota O(v) del gas y del canónico;
  - la cuenta de incidencias y la clase de varios ciclos;
  - el desarrollo del bosque y la raíz;
  - la poda y el ciclo;
  - la identidad del cofactor por caras;
  - la proyección y Cauchy;
  - la uniformidad para v ≤ 8 log n.
- **Demostrado con ordenador:**
  - las identidades polinómicas de c2, que son pruebas completas;
  - las identidades locales de c1 en los nueve grafos probados; la identidad general está probada en Z01.
- **Evidencia exacta en un modelo de juguete:** c3a y c3b.
- **Condicional** (entradas importadas, fuera de mi parte):
  - las fórmulas del exterior [B01] y la amplitud común (revisión de R18);
  - Δ_q y la rama del aproximante de torres (Menores uniformes 01–05, dominio de E1);
  - la norma canónica para identificar la rama física;
  - los márgenes de clase.
- **Heurístico:** nada.

## 5. Dictamen global sobre mi parte

**Certificada con precisiones.** Las entradas analíticas y algebraicas de la cota por soporte son correctas como implicación de las entradas citadas:
- la holomorfía y el gas en el polidisco;
- los órdenes c+1, c−1 con campo repetido y c−1;
- el mismo exterior, el mismo campo afín y el mismo cofactor en todas las caras;
- la proyección y Cauchy;
- el término crítico del ciclo.

La cota final C^v(Cv)^{c+1}∏d_i·j^{−p} se sigue con constantes uniformes para 5 ≤ v ≤ 8 log n. Las precisiones son tres, y ninguna obliga a cambiar enunciados ni constantes:
1. La constante e^{B_1} de [G04 32] debe ser exp(B_1e^{B_1}).
2. Las referencias a «Grados intermedios», que no está en el material, quedan cubiertas por B02, U01–U06 y P03–P05.
3. Conviene escribir el paso de v fijo a v ≤ 8 log n por continuación analítica de identidades.

## 6. Resumen final

- Comprobé todas las huellas. Leí completas, contra las fuentes, G01–G07, P01–P07, U01–U08, Z01–Z04, X01–X03, I01–I04, B01–B03, V y 06c.
- **Punto 1, holomorfía y gas: correcta con precisión.**
  - La silla exterior y la local son holomorfas y únicas en |s| ≤ κ/v, |ζ_i| ≤ κ′/d_i, porque v sólo entra a través de la TV, que es O(v|s|).
  - La inducción del gas da Z ≠ 0 y |log Z| = O(v); el canónico también es O(v).
  - El error físico es e^{Cv}Δ_q < 1/2.
  - Precisiones: la constante de G04 32 y unas fuentes ausentes, cubiertas por B02 y U01–U05.
- **Punto 2, órdenes: correcta con precisión.**
  - La identidad d = w+1−Ση−L_I da c−1 en varios ciclos.
  - En el bosque, la cancelación diagramática con ½ log det(I−VR″) y la raíz P+B dan c+1.
  - En un ciclo, la poda deja log(1−θ²) ∈ (∏_𝒞ζ²).
  - La identidad del cofactor (U07) hace coincidir las caras en ζ_i = 0.
  - Precisión: el paso de v fijo a v ≤ 8 log n es por continuación analítica.
- **Punto 3, proyección y Cauchy: correcta.** Schwarz en campos da ∏(Cd_i/j), con Cv²/j por repetición; Cauchy en s da 2(Cv/j)^w. Así sale la cota de B03.
- **Punto 4, ciclo: correcta.** Z/Z_B = 1+θ y D_loc = (1−θ)² se verificaron exactamente en nueve grafos; la fórmula de poda coincide exactamente.
- **Punto 5, coherencia: correcta.** Varios ciclos sólo usa conexidad y no supone ninguna cancelación; los órdenes de [V] coinciden con p.
- **Cálculos (29 s de CPU, exactos).** En un modelo de juguete con exactamente las hipótesis de U06, los primeros costes con coeficiente no nulo son c+1, c y c−1. Las tres pruebas de sensibilidad fallan, como deben.
- **Dictamen global: certificada con precisiones.** No hay hueco ni enunciado falso en mi parte. Es condicional a las entradas importadas.

## Anexo · Huellas de los archivos de esta revisión (SHA256)

```
3f89ef201e1c0db0f30cf8c16a7e4d072df5eb55fdaa7a0860d4bb793dcc75a3  codigo/c1_ciclo_local.py
b432691692a00a191b97f658d74bc941a386f1c804282e68655960946dd00b9f  codigo/c2_raiz_dos_fibras.py
a5da87088fd390261f9c096e3f96a70c9f75aaade5dadf1c984c971341bcf6c4  codigo/c3a_juguete_grupos.py
8e65e2c832e0849030cb81330a3e236922ce191ac00695e6a9d3491dbb469e7c  codigo/c3b_juguete_sitios.py
e8b879bd008c66a9dd7b570cc9f449884687537d20f1c71f06421b69d447f958  resultados/c1_ciclo_local.txt
e02573aee9e1b8c06b7cdb5b086ea786acb902f5257414f32dd47db4dd8e6af5  resultados/c2_raiz_dos_fibras.txt
75c0388e7164e7d05f1ceabaa02743f75030e98467f659f1afee30d54baa03a7  resultados/c3a_juguete_grupos.txt
21b5f0f84ffac267daff7b3a4872a1f343210d9d8556705cd81361766fa29042  resultados/c3b_juguete_sitios.txt
```

Para reproducir: desde `rev_exp/W2_jets/`, `nice -n 10 python3 codigo/<programa>.py`. Los tiempos de cada ejecución están en `resultados/*_tiempo.txt`.
