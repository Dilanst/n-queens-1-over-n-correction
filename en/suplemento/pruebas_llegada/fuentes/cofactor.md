# Acta de revisión externa W2 · Cofactor con exterior común y sustitución de átomos

**Revisor.** Externo e independiente, ajeno al proceso que escribió la prueba. Fecha: 2026-11-17. Trabajé sin web y sin acceso a otros equipos, sólo con la carpeta `rev_exp/`. Los cálculos son propios y exactos (enteros y `Fraction` de Python), deterministas, con `nice -n 10`, un proceso cada vez y tiempos medidos. No hay Monte Carlo ni azar. No reviso E1, E2, el recuento de tipos ni la cota por soporte, salvo lo que esta pieza importa de ellos.

**Objeto.** El enunciado de la pieza [GUIA 3] tiene tres partes:
1. Todas las caras de un soporte usan el mismo exterior RC conexo.
2. En el interior x_i < 1/d_i y con márgenes positivos, el cofactor y el campo afín comunes son los de U07.
3. Para √n ≤ j ≤ n, 5 ≤ v ≤ 8 log n y q = 4v+12, dados U01–U05 en la misma normalización, sustituir los átomos cuesta O(j⁻⁸) en la suma de las proyecciones.

La prueba es B01, U02, U07 y A03 [GUIA 5].

**Integridad** (`codigo/c0_cotejo.py`, `resultados/c0_cotejo.txt`).
- **Originales.** Las huellas SHA256 de B01, U02, U07 y A03 coinciden con las que declara `prueba_fuente.md`. Los manifiestos de sus entregas dan 14/14 (ronda 18), 14/14 (menores uniformes) y 9/9 (márgenes y átomos).
- **Transcripciones.** Los cuatro bloques de `prueba_fuente.md` son idénticos byte a byte a los originales (59, 55, 83 y 50 líneas). También lo son:
  - `r21/fuentes/latex/{B01,U02,U07,A03}.tex`;
  - quitada la cabecera, las copias de `r19/expediente/originales/` (B/01, U/02, U/07, A/03 y B/REVISION_ADVERSARIAL).
- **Revisiones internas.** Las tres de r21 (U, A y B) tienen la huella de sus originales.
- **Otros manifiestos.** r19 da 116/116. Media matriz da 14/14 y ronda 9 da 98/98; son fuentes que consulté para la normalización.
- **r21.** Los 106 archivos presentes coinciden con su manifiesto y no hay archivos sin listar. Las otras 248 entradas son archivos no copiados a `rev_exp/r21/` (archivo_r19, fuentes/privadas…). Durante mi revisión aparecieron en `r21/fuentes/publicas/` 19 archivos nuevos: también coinciden con el manifiesto y no los uso. No hay ninguna huella discordante.

**Convenciones de cita.** Los números son líneas del archivo original.
- [B0n], [U0n] y [A0n] son `rev_exp/fuentes/<entrega>/latex/0n_*.tex` de, respectivamente, ronda 18, menores uniformes y márgenes y átomos.
- [MM0n] es `…media_matriz_20261116T150154Z/latex/0n_*.tex` y [R9-06] es `…ronda9_20261116T082611Z/latex/06_torres.tex`.
- En `prueba_fuente.md`, la línea original n de B01, U02, U07 y A03 está en n+9, n+75, n+137 y n+227.
- [GUIA n] es `r21/piezas_T2/02_cofactor/GUIA.md`; [V n] es `r19/expediente/originales/V/REVISION.md`; [UA n] es el acta de menores uniformes.
- [E1 n] y [W2j n] son `rev_exp/E1/ACTA.md` y `rev_exp/W2_jets/ACTA.md`, con líneas del archivo.

**Notación.**
- j es el tamaño del tablero, m = j−h el del menor y s = σ = 1/j el valor físico del parámetro.
- t_b = 1−y_b es el margen de una fibra RC marcada y q_f la vacancia de una diagonal activa.
- **Dos letras d_i distintas.** En U07, d_i es el número de factores incidentes en el sitio i: las dos incidencias RC y las diagonales activas, luego d_i ≤ 4 [U07 9]. En B02, B03, G02 y U08 la misma letra es la fibra máxima d_i* = máx_f |f∩U| [B02 29; U08 3–4].

## 1. Tabla de veredictos

| # | Punto | Veredicto | Motivo breve |
|---|---|---|---|
| 1a | El exterior A∖U es el mismo en las 2^v caras y no depende de la cara | **Correcta** | Por construcción [B01 3, 6–7; U07 2–3; A03 2–4]. |
| 1b | Exterior RC conexo; el complemento de (1,−1) quita exactamente una dimensión | **Correcta con precisión** | Núcleo = span(1,−1) ⟺ soporte conexo (c5). B01 no enuncia la conexión; se deduce de su brecha r′ < 1 [B01 5]. |
| 1c | La conexión se conserva al apagar o encender actividades, átomos duros incluidos | **Correcta con precisión** | Con t_b > 0 el soporte no cambia. En un átomo duro la conexión la da la brecha de cada menor [U02 27–38]; no es automática (c5). |
| 2a | La actualización por los sitios da det T·det(−H_B″−R″); con b_i y vacancias, D_loc | **Correcta** | Verificado exactamente en cinco configuraciones (c1). |
| 2b | Al apagar una actividad, la columna tiende a e_i | **Correcta** | Igualdad exacta en x_i = 0, con desviación Θ(x_i) (c1). |
| 2c | Al ocupar una marca, (1/2)·log(m/j) convierte el covolumen del padre en el del menor | **Correcta** | Signo y convención comprobados: j·d̄_j = m·d̄_m y Stirling en J_N (c2). |
| 2d | El denominador basal es común a las caras | **Correcta** | [A03 26–28; B03 26–27]; c3. |
| 2e | El dominio de menores está garantizado en el interior x_i < 1/d_i con márgenes positivos | **Correcta con precisión** | El exterior sólo ve una perturbación TV O(v/j) en todo el rango real. La parte holomorfa vive en la caja ‖x‖_* ≤ a, contenida en el interior. |
| 3a | Cada átomo positivo está entre e^{±η_v} veces su aproximante | **Correcta** (importada) | Es U01 con h ≤ v y m ≥ j/2; C′ = 2C, o 4C con la receta de B03. |
| 3b | Sumar átomos y luego caras da 2^v η_v; a lo sumo j^{2v} soportes | **Correcta** | Positividad en cada cara; C(j², v) ≤ j^{2v}. |
| 3c | Con C′q ≤ j^{1/3} sale 2^v j^{−8−2v/3}; la parte exponencial es exp(O(log² n) − cj) | **Correcta con precisión** | La desigualdad equivale exactamente a C′q ≤ j^{1/3} (c4). Vale en todo el rango desde un n₀ finito. |
| 3d | Se conserva exactamente la masa cero de un átomo imposible | **Correcta con precisión** | Con la receta de B03 exige que todo átomo compatible sea positivo; lo da la clase, no la combinatoria (c3). |
| 4 | Dependencias U01–U05 en la misma normalización | **Correcta con precisión** | Lo importado coincide con el uso. E1 certificó el orden lineal Q*; el descenso a q [U04 37–39] lo verifico aquí. |
| 5 | Cálculos exactos propios | **Realizados** | Seis programas, 0,9 s de CPU en total, ninguna discrepancia. |

**No encontré ningún enunciado falso ni ningún hueco de prueba en mi parte.** Las siete precisiones (P1–P7, §3) son de redacción, de alcance o de notación, y ninguna obliga a cambiar enunciados ni constantes.

## 2. Detalle por punto

### Punto 1 · Exterior común [B01]

**1a. Un solo exterior.**
- **Mismo exterior.** B01 quita U entero de la máscara también al evaluar una cara Y ⊂ U [B01 3]. Las caras sólo cambian qué diagonales de los sitios de Y se activan [B01 6]. U07 [2–3] y A03 [2–4] dicen lo mismo, y B03 fija A₀ = A∖U antes de la cara [B03 2].
- **Nada depende de Y.** El núcleo z = jD₀ y sus ceros son los del exterior escalado [B01 4]. Los grupos g que indexan los parámetros h_g de las copias son las componentes de la incidencia completa de U, antes de desactivar nada [B01 7].
- **Lo que sí cambia con la cara** es el punto de evaluación, es decir las ocupaciones x de la silla local. R, A_* y el campo afín r = ∇R(0) son la misma función en todas las caras [U07 53; B02 23–24].
- c1 (f) comprueba que S_ext es literalmente el mismo en las caras comparadas.
- **Copias.** La silla se resuelve en el espacio con copias antes de identificarlas [B01 23–31]. Así se corrigió la objeción de la primera lectura de R18 (acta de R18, línea 10).

**1b. Conexión y núcleo RC.**
- **Núcleo y conexión.** Sea S = C·diag(τ)·Cᵗ el operador de líneas, con τ > 0 en el soporte. Su forma cuadrática es Σ_rc τ_rc(a_r + b_c)², que se anula exactamente en los vectores constantes con signo opuesto en cada componente del grafo filas–columnas. Por tanto el núcleo es span(1,−1) si y sólo si el soporte es conexo.
- **U_R.** Las columnas e_r + e_c de U_R son ortogonales a (1,−1) [U07 13–14, 21].
- **c5 (a).** Con soporte conexo, el rango es 2j−1. Con dos bloques, el rango es 2j−2 y aparece un segundo vector nulo. Entonces S₀ deja de ser invertible en RC^⊥ y [U07 22] falla.
- **Precisión P1.** B01 no enuncia la conexión del exterior; se deduce de su margen de clase ‖D₀ − J_j‖₂ ≤ r′ < 1 [B01 5]. Si el soporte de una biestocástica tuviera dos bloques, ambos serían cuadrados y biestocásticos. Entonces |R₂|·1_{R₁} − |R₁|·1_{R₂} sería vector singular de valor 1 para D − J (c5 b, exacto). U07 supone la conexión [U07 3] y la atribuye a la brecha de U02 [U07 75–76]. Conviene escribir esa implicación en B01.
- **Operador físico.** Para S = S₀ + UTUᵗ, con sitios y diagonales, el núcleo sigue siendo exactamente (1,−1,0) en las cinco configuraciones de c1. El covolumen √(2j) es, pues, común a las caras [U07 49–50; B01 58–59].
- **En complejo**, (1,−1) sigue en el núcleo por álgebra. Que sea el único equivale a que d̄ y det(I − WᵗW) no se anulen. Eso se obtiene por continuidad desde el centro real con brecha [U02 49–55; B02 47–50; MM05 27–33].
- **Fórmula del pseudodeterminante.** pdet S_ext = (2/d̄)·∏_v(t_v d_v)·det(I − WᵗW) [MM05 16]. c2 (C) la comprueba exactamente con márgenes positivos arbitrarios.

**1c. Conexión al cambiar actividades.**
- **Con t_b > 0**, la medida levantada M̃₁ = tμ̃ tiene el mismo soporte en todas las caras, así que la conexión no cambia.
- **En un átomo duro**, t_b = 0 y los índices ocupados desaparecen. Hace falta que el exterior superviviente, un menor con h ≤ v filas y columnas suprimidas, sea conexo. Lo da la brecha común r′ < 1 de todos esos menores [U02 27–38], que E1 rehízo [E1 37], por el argumento de 1b.
- **No es automático.** En un ciclo 7×7, 462 supresiones con h ≤ 2 desconectan el superviviente; en una máscara densa, ninguna (c5 d).
- **Espacio con copias.** Una copia con masa positiva repite la fila original y no añade dirección nula. Un índice de masa cero sí la añade (c5 c): el original cuando h_g = s, o la copia ocupada cuando t = 0. La prueba lo trata aparte:
  - en el balanceo, las ecuaciones auxiliares de masa cero tienen bloque identidad y no añaden dirección nula [B02 35–36; MM03 24–25; U02 25];
  - en el cofactor, los índices de masa cero no entran en las integrales y no se toma el pseudodeterminante con filas nulas [U07 73–74; MM05 32, 53–54].

  La frase «el modo RC sigue siendo el único modo nulo» [U07 49–50] se refiere, pues, a los índices de masa positiva.
- **Masas iguales de M̃₁** [B01 20]. Cada sitio está en una sola fibra fila y una sola fibra columna, del mismo grupo [B01 8]. Por eso ambas masas valen 1 − Σ_i h_{g(i)}x_i. c5 (e) lo comprueba con fibras de dos sitios.
- **Fuera de mis tres preguntas.** Comprobé en lectura, a primer orden en σ, la pieza −(E₁₂+E₂₁)/2 de A_* [B01 51, 55], que la revisión de R18 sólo aceptó en lectura [V 70–72]:
  - d_r = 1 + σt_r∫t_c²Z²dμ_C + O(σ²) [MM05 43–45];
  - la suma −∫(log d_r)/(2σ)dμ_R [MM05 46] da −½∫Z² dM₁^R dM₂^C = −E₁₂/2, y las columnas dan −E₂₁/2.

  La amplitud E₂₂/2 la revisó la ronda 18 [V 29] y W2_jets la dejó fuera [W2j 118]; no la rehago.

**Veredicto:** 1a correcta; 1b y 1c correctas con precisión.

### Punto 2 · Cofactor y campo afín: la parte analítica [U02, U07]

**2a. Actualización por los sitios** [U07 22–27]. La identidad es

  pdet S / (pdet S_ext·∏_D q_f) = det T · det(T⁻¹ + U_RᵗS_ext⁺U_R + U_Dᵗdiag(1/q)U_D).

- **Es el lema del determinante** para S = S₀ + UTUᵗ, con S₀ invertible en RC^⊥ ⊕ diagonales. La invertibilidad es la conexión de 1b, y en el interior T_ii > 0.
- **Hessiana de Bethe.** −H_B″ = T⁻¹ + U_Rᵗdiag(1/t)U_R + U_Dᵗdiag(1/q)U_D [U07 33–39]. Sale de sumar diag(1/x) + 11ᵗ/q_f por factor y restar d_i − 1 términos de Bernoulli: (d_i(1−x_i) − (d_i−1))/(x_i(1−x_i)) = 1/T_ii.
- **Hessiana restringida.** Con R″ = U_Rᵗdiag(1/t)U_R − U_RᵗS_ext⁺U_R [U07 28–30], los términos diag(1/t) se cancelan y el último factor es det(−H_B″−R″) [U07 40].
- **D_loc.** Se tiene b_iT_ii = x_i(1−x_i)^{1−d_i}, y ∏_i(1−x_i)^{d_i} = ∏_f∏_{i∈f}(1−x_i). Por tanto D_loc = ∏b_i·(pdet S/pdet S_ext)·∏_RC t_b. Ese ∏t_b es el que cancela el +½Σlog t_b de A_* [U07 41–51; B01 57–58; MM02 12].
- **c1 lo verifica todo** con racionales exactos en cinco configuraciones (j = 4, 5, 6 y v = 3, 5, 6), más tres casos de apagado (2b) y uno de factor unitario. Incluyen:
  - dos sitios en una fila y dos en una columna, para las multiplicidades [U07 50–51];
  - diagonales dobles y triples;
  - factores unitarios, que resultan redundantes [U07 10];
  - ocupaciones cerca del borde del interior: x_i = 1/5 con d_i = 4, es decir 1 − d_ix_i = 1/5.
- **Lo que acepto sin recalcular.** R″ es la Hessiana del máximo exterior por dualidad convexa, es decir, la respuesta de los multiplicadores de margen [U07 28–33]. Lo acepto como resultado estándar; recalcularlo exigiría resolver el balanceo no lineal.

**2b. La columna tiende al vector coordenado** [U07 53–55].
- **Igualdad en x_i = 0.** Se tiene (−H_B″−R″)V₀ = diag(1 − d_ix_i) + [U_RᵗS⁺U_R + U_Dᵗdiag(1/q)U_D]V₀, que está definida también en x_i = 0. Allí la columna i es exactamente e_i.
- **Velocidad.** Con x_i = ε la desviación es Θ(ε): 6,57·ε, 3,29·ε y 7,32·ε en los tres ejemplos (c1 f).
- **Submatriz complementaria.** Es la del soporte sin el sitio i, con el mismo exterior. Coincide en la cara que activa las diagonales de i y en la que no, y D_loc coincide en las dos [U07 56–58].
- **Fuera de mi encargo.** Que x_i → 0 cuando ζ_i → 0 en la rama pequeña es parte de la silla local [U06 68; B02 52–58].

**2c. Covolumen: signo y convención** [U07 59–76; B03 19–28; MM05 53–57].

**Convención.**
- **Covolumen.** El del retículo {(a,b) ∈ Z^N×Z^N : Σa = Σb} es √(2N): el determinante de Gram vale 2N para N ≤ 10 (c2 A). Con el factor √(2π) del modo que falta se obtiene ½log(4πN), que es el «modo RC» de [B01 58; MM02 23].
- **Combinación con la parte global.** La fórmula del pseudodeterminante [MM05 16; R9-06 39–46] da como parte global ½log(d̄/2) − ½log det(I−WᵗW) [B01 46–48]. Así, ½log(4πN) + ½log(d̄/2) = ½log(2π·Nd̄), y Nd̄ es la conductancia total, una cantidad intrínseca.
- **Contraste exacto con Stirling en J_N** (c2 D, series racionales en 1/N). La acción de Bethe más el prefactor más ½log(4πN) reproduce log(N!/N^N) sin término en N ni constante. El resto, −1/(12N) − 1/(4N²) − …, es el error puro de torres. Con ½log(2πN) en su lugar quedaría una constante ½log 2. R9 usa la misma convención [R9-06 99–105].

**El átomo.**
- **Solución en el átomo.** Comparo el padre (σ = 1/j, masas 1/j en los supervivientes y 0 en los índices ocupados) con el menor intrínseco (σ′ = 1/m, masas 1/m). El vector w′ = (m/j)w resuelve las ecuaciones del menor: el núcleo cambia sólo por la constante m/j, que va a los potenciales, y por unicidad es la solución.
- **Consecuencias, exactas** (c2 B, con h = 1, 2 y 3):
  - las probabilidades de casilla p = σw son las mismas, y por tanto también b₂(p) y las conductancias s·ℓ [U07 63];
  - los grados coinciden, y valen exactamente 1 en los índices apagados [U07 61–62];
  - el operador normalizado y det(I − WᵗW) coinciden, y las filas y columnas apagadas desaparecen [U07 66–68];
  - d̄_j = (m/j)·d̄_m, es decir, j·d̄_j = m·d̄_m [U07 69].
- **Signo.** Sin covolumen, la fórmula del padre en el átomo es la del menor más ½log(m/j), que es negativo. Con los covolúmenes, ½log(4πj) + ½log(m/j) = ½log(4πm) [U07 69–72; B03 22–24; UA 12; V 35]. **El signo es el correcto**; el cociente contrario, j/m, es falso (c2 B).
- **Por qué importa.** Sin ese cambio quedaría un error ½log(j/m) = h/(2j) + O(h²/j²) en cada átomo. Ese error depende de |I|, no se cancela en Δ_U y es de orden v/j, no (Cq/j)^q. Con el cambio, el error del átomo es el error puro de torres del menor, sin rastro de j; en J_m vale −1/(12m) + … (c2 D).
- **Acción.** En el átomo, la acción del padre es la de Bethe del menor más Σp·log(D₀/D′). Ese término son exactamente los logaritmos de los factores de escala de filas y columnas, que U05 conserva [U05 3–6]. Además, t log t vale cero en t = 0 y t = 1 [B03 24–25].

**2d. Denominador basal común.**
- F(Y) = log(Q_Y/per A), con el mismo per A en todas las caras; al aproximar se conserva el denominador exacto [A03 26–28]. En la receta de B03, la única constante es log(W_∅/per A) [B03 26–27].
- c3 (b) comprueba que per A es el conteo de la cara vacía y que un factor común a todos los átomos se cancela exactamente en Δ_U.

**2e. Dominio de menores** (la pregunta del encargo y el aviso de [GUIA 7]).
- **Exterior.** El balanceo, el cofactor y el campo afín dependen de x sólo a través de la medida levantada tμ̃. Para cualquier vector real de ocupaciones con márgenes en [0, 1], incluidos los átomos duros, esa medida está a distancia TV a lo sumo 3v/j de μ⁰ por lado. Ese es justamente el dominio de U02:
  - balanceo con perturbación TV pequeña y v/j pequeño [U02 6–26];
  - brecha común r′ [U02 27–38];
  - rama compleja por continuación [U02 39–55].

  También es el de Media matriz, que admite |x_i| ≤ 2 [MM03 9–10]. Con v ≤ 8 log n y j ≥ √n, v/j → 0 uniformemente. **Así que el dominio está garantizado para la parte exterior en todo el interior con márgenes positivos, y también en el camino x = λ1_I hasta el átomo duro** [U07 62–66].
- **Comprobaciones de lectura.** El término de Fredholm de grado l es ≤ C^l l^{l/2}/l! por Hadamard [U02 49–50]. La cota inferior real es exp(−C/(1−r′²)) [MM05 27–29]. La continuidad sale de telescopar factores de medida y filas [U02 51–52].
- **Parte local.** La identidad algebraica vale en todo el interior: allí T_ii, b_i y q_f son positivos, y c1 la comprueba con x hasta 1/5. La descomposición holomorfa con cotas uniformes, que es la que usa Cauchy, sólo se establece en la caja compleja ‖x‖_* ≤ a, |ζ_i| ≤ κ′/d_i*, |s| ≤ κ/v [B02 29–31, 52–60], que W2_jets certificó [W2j 51–93].
  - Como d_i ≤ 4 y Σ_{i∈f} 1/d_i* ≤ 1 [B02 30], en la caja |x_i| ≤ a, |1−t_b| ≤ a y |1−q_f| ≤ a.
  - Si a < 1/4, la caja queda dentro del interior con márgenes positivos y 1 − d_ix_i no se anula en ella.
  - El punto físico x_i = O(1/j) está dentro de la caja.
- **Precisión P2.** El interior x_i < 1/d_i no es por sí solo el dominio analítico: cerca de x_i = 1/d_i, T_ii → ∞ y no hay control uniforme. Pero nada usa la descomposición holomorfa fuera de la caja, y en el átomo duro sólo se evalúa el exterior [U07 76].
  - La condición literal de B02, ‖x‖_* ≤ a [B02 30], excluye los átomos. Lo que el exterior necesita allí (|t| ≤ 1 y TV pequeña) sí se cumple, y lo cubren U02 y MM03.
  - Convendría decirlo así en la GUIA.
- **Precisión P3 (notación).** La d_i de U07 (≤ 4) no es la de B02, B03 y G02, que es la fibra máxima. U08 ya las distingue [U08 3–4].
- **Precisión P4.** El párrafo «Alcance» de U07 [77–83] habla de radios c/v⁸ y de un coste (Cv)^{A₁v} procedentes de «Grados intermedios». Lo han superado los radios κ/v y κ′/d_i* de B02 y G02–G04 [B02 52–55; U08 9–14], que W2_jets certificó. Debería actualizarse para que no sugiera un coste no sumable.

**Veredicto:** 2a, 2b, 2c y 2d correctas; 2e correcta con precisión.

### Punto 3 · Sustitución de átomos [A03], con √n ≤ j ≤ n, 5 ≤ v ≤ 8 log n y q = 4v+12

**3a. Emparedado.**
- **Origen.** La hipótesis del lema [A03 16–21] es la precisión de U01 para cada menor positivo [A03 22–23], con h = |I| ≤ v. Como m ≥ j/2, (Cq/m)^q ≤ (2Cq/j)^q.
- **Requisitos de U01** [U01 12–13, 18–22], todos válidos desde un n₀ [A03 24–25; U01 25–26]:
  - v/j ≤ 8 log n/√n → 0;
  - h ≤ v ≤ aj;
  - q ≤ 4⌊8 log n⌋ + 12 ≤ εj;
  - 1/m ≤ c₀/q.
- **Receta directa.** Con Ŵ_I = factores exactos × (m!/m^m)·H_q(1/m; D′_I) basta una evaluación, y C′ = 2C.
- **Receta de B03** [B03 10–17]. Ŵ_∅ = per(A₀) es exacto, y log(Ŵ_I/W_I) = [d̃_T(I) − G_*(I)] − [d̃_T(∅) − G_*(∅)]. Esto vale por la normalización de 2c y por la cota del error puro de torres [U05 9–15]. Son dos evaluaciones, así que C′ = 4C [B03 31].
- **Cambio de receta.** Pasar de una a otra cuesta O(j⁻⁸), por el mismo lema aplicado dos veces [B03 32–35].

**3b. 2^v·η_v y j^{2v}.**
- **En cada cara**, los pesos son reales positivos y la familia 𝓘_Y es la misma en los dos lados [A03 5–8]. Por tanto e^{−η}Q_Y ≤ Q̂_Y ≤ e^{η}Q_Y y |F̂ − F| ≤ η [A03 29–31]. La alternancia sobre las 2^v caras da 2^v η [A03 32–34].
- **Sin cancelaciones.** No hace falta ninguna cancelación entre caras, como ya observó W2_jets [W2j 198].
- **Soportes.** C(j², v) ≤ j^{2v}, de hecho ≤ j^{2v}/v! [A03 36]; c4 (C).
- **Comprobación en tableros reales** (c3, exacta, en cuatro tableros de reinas):
  - en todas las caras (32 en tres tableros y 16 en el cuarto), el conteo directo coincide con la suma de permanentes de los menores del exterior sobre los I compatibles;
  - el emparedado se cumple con perturbaciones ±1 en la escala 101/100.

**3c. Umbral y sumas.**
- **Equivalencia.** Con q = 4v+12, la desigualdad 2^v j^{2v}(C′q/j)^q ≤ 2^v j^{−8−2v/3} de [A03 39], elevada al cubo, equivale a (C′q)^{3q} ≤ j^{3q−8v−24} = j^q. Es decir, equivale a C′q ≤ j^{1/3}. c4 (A) lo confirma en 192 casos alrededor del umbral.
- **Todo el rango.** El peor caso es j = ⌈√n⌉ con v = ⌊8 ln n⌋, y basta √n ≥ (C′(32 ln n + 12))³. Si vale en algún n ≥ 278, vale ya para todo n mayor, porque f(n) = √n − (C′(32 ln n+12))³ crece donde f ≥ 0 (c4 B).
  - Con una cota racional certificada de ln 2, vale desde n = 2^63 para C′ = 1, desde 2^86 para C′ = 10 y desde 2^108 para C′ = 100.
  - Es un n₀ finito, coherente con un enunciado existencial. Con j = ⌊bn⌋ el umbral es menor.
- **Suma en v.** Para j ≥ 8, j^{2/3} ≥ 4, luego Σ_{v≥5} 2^v j^{−8−2v/3} ≤ j⁻⁸/16 [A03 41].
- **Parte exponencial.** Σ_v 2^v j^{2v}·C′e^{−cj} ≤ (8 ln n + 1)(2n²)^{8 ln n}·C′e^{−cj} = exp(O(log² n) − cj). Como cj ≥ c√n, esto es o(j⁻⁸) [A03 41–43].
- **Precisión P5.** Conviene escribir:
  - que C′ incluye el factor 2 de m ≥ j/2 y, con la receta de B03, las dos evaluaciones;
  - que C′ y c son constantes de clase, fijadas antes de n;
  - que la condición C′q ≤ j^{1/3} es equivalente, no sólo suficiente.

**3d. Masa cero.**
- **Átomos incompatibles.** Un átomo incompatible con RC o con las diagonales activas de Y está fuera de 𝓘_Y en las dos sumas y nunca se logaritma [A03 11; U05 8]. Su masa cero se conserva exactamente.
- **Precisión P6.** La receta de B03 asigna peso positivo a todo átomo compatible. Por eso la masa cero sólo se conserva exactamente si todo átomo compatible tiene permanente positivo y el exterior tiene emparejamiento.
  - En la clase se cumple: cada menor con h ≤ v admite escalado controlado [U02 27–38], luego su permanente es positivo. A03 lo exige expresamente [A03 10–13].
  - Fuera de la clase falla. En tableros pequeños de reinas hay átomos compatibles con permanente cero (c3, casos 1, 2 y 4), y en el caso 4 ni siquiera el exterior tiene emparejamiento.
  - Son máscaras fuera de toda clase difusa, así que no contradicen la pieza. Muestran que la hipótesis de clase es esencial también en este punto.

**Veredicto:** 3a y 3b correctas; 3c y 3d correctas con precisión.

### Punto 4 · Dependencias: U01–U05 en la misma normalización

**Qué se importa exactamente.**
1. **Teorema de los menores, U01** [U01 11–28].
   - Para M₀ y r fijos hay a, ε, c y C uniformes. Si v/j es pequeño y j grande, la cota vale para todo menor obtenido quitando v casillas marcadas y h ≤ aj filas y columnas, con su escalado exacto D′ y m = j−h, y para todo q ∈ [1, ⌊εj⌋].
   - La cota es |log(m^m per D′/m!) − log H_q(1/m; D′)| ≤ (Cq/m)^q + Ce^{−cj}.
   - Se usa el mismo índice en el padre y en las caras [U01 23–24], en particular q = 4v+12 con j ≥ ⌈√n⌉ [U01 25–26].
2. **U02.** Difusión mD′ ≤ C y brecha r′ < 1 comunes a esos menores [U02 27–38]. Dan la positividad y el escalado controlado que pide [A03 12–13], y la conexión del superviviente [U07 75–76].
3. **U03 y U04.** Truncamiento, mezcla, descenso a q [U04 37–39] y paso al logaritmo [U04 40–49]. Son la prueba del punto 1 a orden q.
4. **U05.**
   - Identidad exacta de los átomos [U05 2–8]. Se conservan los factores de filas y columnas, el factorial y las potencias de tamaño. El error de un cociente es la suma de dos errores logarítmicos, y la cota no depende de lo pequeña que sea la masa. Los átomos imposibles no se logaritman.
   - Sólo para la receta de B03: el error puro de torres G_q con Stirling truncado [U05 9–15].
5. **U07, sólo para la receta de B03.** La normalización del átomo (2c) [U07 59–76].

**¿Coincide con el uso que se hace aquí?** Sí.
- A03 usa el punto 1 para todos los átomos positivos de todas las caras, con h ≤ v ≤ aj, m ≥ j/2, q ≤ εj y v/j → 0 (3a). Usa el punto 2 para la positividad y el punto 4 para que los factores exactos sean los mismos en los dos lados.
- **«En la misma normalización».** Con la receta directa lo es por construcción. Con la de B03 lo es por U07, comprobado exactamente en c2.
- **Fuera de esta pieza.** Los márgenes de clase con los que U01 se aplica a la máscara del corte (A01, D04) son una entrada importada que no reviso.

**Estado de la certificación.**
- **Lo que certificó E1.** U01 a orden lineal Q* y la maquinaria de U02–U04 [E1 19, 31–55, 81–99, 287]. Su acta no examina el descenso del orden Q al orden q [U04 37–39], que es lo que usa A03.
- **Comprobé ese descenso:**
  - los mayorantes (Cl/m)^l [U03 40] tienen razón ≤ Ce(l+1)/m ≤ 1/2 para l ≤ Q, si ε es pequeño [U03 44–45];
  - por tanto sup_I |S_Q − S_q| ≤ 2C(C(q+1)/m)^{q+1};
  - el mismo Taylor a orden q, con momentos E|X−1|^{2q+2} ≤ (C(q+1)/m)^{q+1} [U04 24–27], cuesta otro tanto;
  - H_q = d(1) + O(1/m) está separado de cero, y el error pasa al logaritmo [U04 46–49].

  Queda (Cq/m)^q + Ce^{−cj}, con C independiente de q.
- **Precisión P7.** El paso está comprimido en tres líneas. Es correcto y no usa nada que no esté ya en U03–U04.

**Veredicto:** correcta con precisión.

### Punto 5 · Cálculos (código en `codigo/`, salidas en `resultados/`)

Todo es aritmética racional exacta, con coeficientes «genéricos» dados por fórmulas fijas. Cada programa se ejecutó con `nice -n 10 python3 -I`, de uno en uno.

| Programa | Qué comprueba | Resultado | CPU |
|---|---|---|---|
| `c0_cotejo.py` | Huellas, transcripciones de `prueba_fuente.md`, copias de r19 y r21, manifiestos | Todo coincide | 0,04 s |
| `c1_determinante.py` | U07: núcleo RC, lema del determinante, −H_B″, R″, b_iT_ii, D_loc, columna e_i, caras con y sin las diagonales del sitio apagado, factores unitarios | 5 configuraciones + 3 apagados + 1 unitario, 0 fallos | 0,25 s |
| `c2_covolumen.py` | Covolumen √(2N); átomo (w′ = (m/j)w, grados, W, d̄_j = (m/j)d̄_m, operador de líneas); pdet = (2/d̄)∏(td)det(I−WᵗW); Stirling en J_N | 0 fallos | 0,08 s |
| `c3_atomos.py` | A03 en tableros de reinas: descomposición en átomos de todas las caras, denominador común, átomos de masa cero, emparedado | 4 tableros, 0 fallos | 0,46 s |
| `c4_umbral.py` | Equivalencia con C′q ≤ j^{1/3}, umbrales n₀(C′), C(j², v) ≤ j^{2v}, suma en v | 0 fallos | 0,04 s |
| `c5_conexion.py` | Núcleo ⟺ conexión, brecha ⇒ conexión, copias de masa cero, conexión en átomos duros, masas iguales de M̃₁ | 0 fallos | 0,04 s |

`exacto.py` es el módulo auxiliar de álgebra lineal racional. Los tiempos están en `resultados/c*_tiempo.txt`. Son comprobaciones exactas de identidades en casos pequeños: no prueban las cotas asintóticas, que se establecen en el §2.

## 3. Cuantificadores, ley, tamaño y estados

**Cuantificadores, ley y tamaño.**
- Todo es determinista, en una máscara fija de la clase (M₀′, r′) de tamaño j, con exterior común y q = 4v+12.
- Las constantes son de clase y se eligen antes que b y ρ; n₀ depende de C′ y, en el corte, de b.
- No interviene ninguna ley: la integración contra ν con el indicador H_j es posterior [A03 48–49].
- Los átomos son menores de tamaño m = j−|I|, con su propio escalado, y s vale 1/j.

**Estados.**
- **Demostrado** (cada paso rehecho): 1a–1c, 2a–2e, 3b–3d y el descenso a q de U04.
- **Demostrado con ordenador** (identidades exactas en casos finitos): c1–c5.
- **Condicional**, por ser entradas importadas fuera de mi parte:
  - U01 a orden lineal y U02–U04 (E1);
  - los márgenes de clase (A01, D04);
  - R″ por dualidad convexa;
  - la amplitud E₂₂/2 y las fórmulas de la acción de B01 (ronda 18, [V]);
  - la silla local, la rama física y los radios κ/v, κ′/d_i* (B02; W2_jets).
- **Heurístico:** nada.

**Precisiones** (ninguna cambia enunciados ni constantes).
- **P1.** Escribir en B01 que la brecha r′ < 1 implica la conexión RC del exterior y de cada superviviente.
- **P2.** El dominio analítico es la caja ‖x‖_* ≤ a, dentro del interior si a < 1/4. El interior es el dominio de la identidad algebraica, y el exterior vale en todo el rango real hasta el átomo duro.
- **P3.** Separar las dos letras d_i: número de factores (U07) y fibra máxima (B02, B03, G02).
- **P4.** Actualizar el párrafo «Alcance» de U07 [77–83], que ha quedado obsoleto.
- **P5.** C′ absorbe el factor 2 de m ≥ j/2 y las dos evaluaciones. C′q ≤ j^{1/3} es equivalente a la desigualdad de A03. n₀ es finito pero enorme.
- **P6.** Con la receta de B03, la masa cero exacta requiere que todo átomo compatible sea positivo, y eso lo da la clase.
- **P7.** El descenso Q → q de U04 está comprimido; es correcto.

## 4. Dictamen global sobre mi parte

**Certificada con precisiones.** La pieza establece, como implicación de las entradas importadas:
- un exterior común e independiente de la cara, RC-conexo por la brecha de clase, con exactamente una dirección nula;
- la identidad del cofactor de U07 y la columna e_i al apagar un sitio;
- la conversión exacta del covolumen del padre en el del menor, ½log(4πj) + ½log(m/j) = ½log(4πm), con el signo correcto y la convención que reproduce Stirling;
- un dominio de menores garantizado donde se usa;
- la sustitución de átomos con error total O(j⁻⁸) en todo el rango √n ≤ j ≤ n, 5 ≤ v ≤ 8 log n, q = 4v+12.

No hay enunciados falsos ni huecos. Las precisiones P1–P7 piden redacción y notación más explícitas.

## 5. Resumen final

```
ACTA W2_cofactor · revisor externo · 2026-11-17
Ruta: rev_exp/W2_cofactor/ACTA.md (código en codigo/, salidas en resultados/)
Integridad: huellas de B01, U02, U07 y A03 = declaradas = manifiestos (14/14, 14/14, 9/9).
  Las 4 transcripciones de prueba_fuente.md son idénticas byte a byte; r19 116/116.
Veredictos:
 1a Mismo exterior en todas las caras ........................ correcta
 1b Exterior RC conexo; (1,-1) quita una sola dimensión ....... correcta con precisión
 1c Conexión al cambiar actividades y en átomos duros ......... correcta con precisión
 2a det T·det(-H_B''-R'') y D_loc ............................. correcta
 2b Columna -> e_i al apagar una actividad .................... correcta
 2c ½log(m/j): signo y convención del covolumen ............... correcta
 2d Denominador basal común ................................... correcta
 2e Dominio de menores en el interior ......................... correcta con precisión
 3a Emparedado e^{±η_v} (desde U01) ........................... correcta
 3b 2^v·η_v y j^{2v} soportes ................................. correcta
 3c C'q ≤ j^{1/3}, j^{-8-2v/3}, parte exponencial ............. correcta con precisión
 3d Masa cero de los átomos imposibles ........................ correcta con precisión
 4  Dependencias U01–U05 ...................................... correcta con precisión
 5  Cálculos: 6 programas exactos, 0,9 s de CPU, 0 fallos ..... realizados
Hallazgos:
- Núcleo RC = span(1,-1) ⟺ soporte conexo. B01 no enuncia la conexión; sale de la
  brecha r'<1. En átomos duros no es automática (contraejemplo ralo): la da U02.
- Identidad de U07 exacta en 5 configuraciones y 3 apagados (multiplicidades,
  diagonal triple, unitarios redundantes, x_i = 1/5 con d_i = 4).
- Átomo: w'=(m/j)w; mismos grados y mismo W; j·d̄_j = m·d̄_m. El cambio es +½log(m/j)
  y con covolúmenes da ½log(4πm): signo correcto. La convención ½log(4πN)+½log(d̄/2)
  reproduce Stirling en J_N sin constante residual.
- Dominio: el exterior sólo ve TV O(v/j) en todo el rango real, átomos incluidos; la
  parte holomorfa vive en la caja ‖x‖_*≤a, dentro del interior si a<1/4.
- A03: su desigualdad equivale a C'q ≤ j^{1/3}; n₀ finito pero enorme (2^63 si C'=1).
  Las sumas O(j^-8) son correctas en todo el rango.
- La masa cero exacta exige átomos compatibles positivos: lo da la clase. Fuera de
  ella falla (tableros pequeños con átomos compatibles de permanente cero).
- E1 no examinó el descenso Q→q de U04 37-39; lo verifiqué y es correcto.
Precisiones P1–P7 de redacción, alcance y notación; ninguna cambia enunciados.
No encontré enunciados falsos ni huecos de prueba.
Dictamen global: CERTIFICADA CON PRECISIONES, condicional a las entradas importadas
  (U01–U04 de E1, márgenes de clase, acción de B01 revisada en R18, silla local y
  radios de W2_jets).
```

## Anexo · Huellas de los archivos de esta revisión (SHA256)

```
76868eebb683a1096e1086bcd46589047c3f0bfff5074de6dee0d077ecc0e4ee  codigo/c0_cotejo.py
2ff92d80ebf893a41dc725c4ad3643735aa4832b2dbabb5cc0beb621c9a2513a  codigo/c1_determinante.py
99dee845e213bc9bfad5cb09e7775d98cb4da6ac5e06c6991750c8b2890528d4  codigo/c2_covolumen.py
dfe11eead6a09bf085a7d6526f047f7c919d5d764d3f32efca5d3fe9695ab847  codigo/c3_atomos.py
b8382bc4266ececcccfd80319f112f517a5bea31f7b0ca219ae5ca272af93408  codigo/c4_umbral.py
0fa65b76dd0f4554fc7af5337edbf43bc12496d9b4c45c67c2866b7519d34003  codigo/c5_conexion.py
88b78a5eed0e9d0e1aaafbc8c3b89ad9c347027b84c84f8bb98005b6cc878283  codigo/exacto.py
24d09cb6f2ecd19d26f7b53db7100f50e97eede801052165c26060190a321fa8  resultados/c0_cotejo.txt
a8195e1720dd6c8b9bf1b0c1e5c5146f1ad1d6df3045e94f4fac763457530c7c  resultados/c0_tiempo.txt
178e94643ad6cf10664564efc9c3b519ecad988f9a076afddd115247f0d1b668  resultados/c1_determinante.txt
687cb18039d04a61dbc53ab784dfbaab060a6ed47b3915a10f800fa91a5d74af  resultados/c1_tiempo.txt
548f72a38baf43f70584169b777ecde5d4c9b7eed02c1a1965cafdbe043c05c6  resultados/c2_covolumen.txt
5d6f9828b1e9c6893eb94c0c3af2a50529251272870c07aef76c00e39c3d4e78  resultados/c2_tiempo.txt
dd207c18372835a0a213e00c89c732f81e83292d204293fd9015cccf7908637e  resultados/c3_atomos.txt
59e0599cb563eb327361ef487cd1e4ec220e63b8035a12f2df8c4b2536b6eb25  resultados/c3_tiempo.txt
eee6d133f51dee501603d3036959b24535c1de97ac6e3d5fa5227260e71a05ec  resultados/c4_tiempo.txt
edbd3c13e3426a487d6e6c0ac8eef01c85dde75e97fa58c8bfdae57c8bac5a95  resultados/c4_umbral.txt
685ed8250129e5c43771f04ceae65e48d1c546a64cee6ab1220f63563e01751f  resultados/c5_conexion.txt
eb8b8cb8accb4bd48b4991e00feb304b4c2495b8d4bd3e94526ed096ab5eaf9c  resultados/c5_tiempo.txt
```

Para reproducir, desde `rev_exp/W2_cofactor/`: `nice -n 10 python3 -I -B codigo/<programa>.py`; `c0_cotejo.py` recibe como argumento la ruta de `rev_exp/`. Los tiempos de cada ejecución están en `resultados/*_tiempo.txt`.

Nota de procedimiento: durante el trabajo creé tres archivos auxiliares temporales en la raíz del directorio de trabajo, fuera de `rev_exp/` (un visor de máscaras y dos listados del manifiesto de r21). Los borré antes de cerrar el acta; no se modificó ningún archivo ajeno a esta carpeta.
