# Precisiones que acompañan el cierre

No se modifican enunciados ni constantes de las fuentes. Se explicita su lectura conjunta.
Las entradas pendientes de la edición v3 proponen cambios en fuentes, piezas o GUIAs que están
fuera del consolidado; aquí sólo se registran.

1. **Corte y constantes.** j=floor(bn), M=ceil(delta n); b y delta son positivos,
   admisibles y fijos antes de n. No se hace b→0 con n. Fuente: R21 CONSTANTES.md:3–8;
   acta de salidas:243–261.
2. **Ley.** Una sola historia bajo nu original, con fila uniforme. Las probabilidades
   de torres evalúan una máscara fija; no reemplazan la ley de la historia.
3. **Llegada corta.** H_j incluye regularidad del hijo de tamaño j y longitud máxima
   menor que ceil(alpha j). Su definición no exige completabilidad; la positividad se obtiene
   posteriormente de E1, una vez acreditadas difusión, brecha y carga.
4. **Bandas.** La cota de salida con exponente c−2 beta se suma sólo sobre las bandas
   diádicas de C 5.8. No se afirma para todos los intervalos [m,2m) arbitrarios.
5. **Acumulado.** A_tau se define desde el tablero inicial. Su cota es
   C_delta/M+C/j. En la reducción macroscópica d_n≤C_delta/M, como explicita
   ACTA_identidad.md:135; por tanto J_n es exponencialmente pequeño.
6. **Paso al logaritmo.** La propia prueba da Z_n=1+O(1/n) y después Z_n≥1/2.
   El límite cualitativo de C no es necesario para este último paso.
7. **Normalización.** La reserva documental sobre B §B3T01 se resuelve para la definición
   usada con C/02_preliminares.txt:42–67, C/06a_estatico.txt:20–37 y
   B/07a_macro.txt:72, en los commits fijados. No se declara leído B §B3T01.
   pdet S=2k det S_gf convierte exactamente el término con 1/2 log(4 pi k)
   en el cofactor con 1/2 log(2 pi). No se añade otra normalización.
8. **Norma y soporte.** La norma se prueba en clase abstracta; identifica después la rama
   usada por los coeficientes de soporte. La identidad del cofactor es algebraica.
   No se usa la cota final por soporte para demostrar su propia norma o sus radios.
9. **Rango.** L=8 es fijo. No es log n. Las identidades se continúan en actividades
   para cada soporte; las estimaciones uniformes permiten todos los v≤8 log n.
   No se continúa analíticamente el entero v ni el permanente exacto en el tamaño.
10. **Orden bajo.** Sólo se necesitan cotas de orden de los pesos, no los coeficientes
    exactos antiguos de R3. Una línea se trata completa. Los pares sumados están en
    líneas distintas. M01 activa sólo los dos conflictos elegidos, además de RC;
    otras incidencias geométricas permanecen apagadas para ese peso.
    Los pares con una a cuatro coincidencias RC y las cuñas siguen la ruta alternativa que
    certifica rev_exp/W2_r3/ACTA.md, punto 4 (:195–234 y 300–302): una sola componente y los
    casos bosque, ciclo y varios ciclos de P05/GI03–04, que ACTA_pares.md:138–146 certificó
    para tres o más conflictos. Los pesos T05–T08c no se usan (latex/05_lineas_y_grados.tex:59–83).
11. **Positividad.** Los ceros estructurales de los átomos y la positividad real de los
    compatibles no sustituyen la no anulación compleja: ésta tiene sus cotas de E1
    y de la rama canónica. Mantener ambas afirmaciones separadas.
12. **Fuentes externas.** Divoux–Wang ya no es dependencia: W/permanente se demuestra en las
    partes 8 y 9 desde U01 con q=2, con la certificación de rev_exp/W4_rev/ACTA.md (D1
    descargado), y los cuatro elementos que citaba U01 los rehízo E1. No atribuir O(K^-2) al
    enunciado de su Proposición 3.1, que sólo enuncia o(1) y sólo interviene dentro de C 7.4–7.5.
13. **Corolario.** La tasa implica n R_Q/log n→0. Para llamar a esto a(0)=0 se
    requiere además la definición mediante la expansión antigua y sus hipótesis:
    H2/H3 en el suelo raíz, la reducción ponderada y el límite de a.
    Dini proporciona el resto O(1/n); no es necesaria para excluir un límite a(0) no nulo.
14. **Citas.** Las referencias a A01 con desplazamiento +46 en el acta de norma son
    corregidas por ACTA_difusion.md:307: usar las líneas originales 13–42.

## Edición v3: las precisiones de la tabla de rev_exp/W3_v2/ACTA.md, §2.1(b)

Claves de la tabla de W3_v2 (:98–100): en v2, **A** es ausente y **P** parcial; **N** afecta al
consolidado y **F** a una fuente, una pieza o una GUIA fuera de él. Son 46 ausentes y 19 parciales;
la extensión de K08 cuenta una vez. Las líneas de los destinos del consolidado son las de v3.
«Pendiente» indica el archivo donde debe hacerse el cambio; no se hace aquí.

### W2_pares (rev_exp/W2_pares/ACTA.md:109–112, 167–169, 226–231)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|1|P1.1/PW2a (:110, 228): declarar como entrada la extensión de K06/K08 a menores con cruce ausente y a hasta cuatro supresiones sucesivas; es la PT4 de W2_torres|A|F|Pendiente en la fuente K08. Enunciado propuesto en la sección «Enunciado extendido de K08»; referencia en MAPA.md:18|
|2|P1.2/PW2b (:111, 228): las prolongaciones de φ de K07 a las medidas complejas μ_h (MM07:28–44) y del equilibrio desdoblado (MM03:9–29) están escritas de forma esquemática|A|F|Pendiente en K07, M07 y MM03. Texto propuesto en la fila PT5 de r22/PRECISIONES_PARA_EL_CONSOLIDADO.md:36|
|3|P3.1 (:168): la cota P05 depende de los desarrollos de GI02, que usan las entradas de R9|A|F|Incorporada como dependencia en MAPA.md:16 y 21|
|4|P3.2/PW3 (:169, 229): la segunda justificación de p=7 no es independiente de M01: reorganiza la misma cancelación (PF04:54–63 ≡ MM06:26–36)|A|N|Incorporada en latex/05_lineas_y_grados.tex:73–75|
|5|PW4 (:230): enumerar las 28 clases con coincidencias RC y restar las dos parejas del 4-ciclo|P|F|Incorporada en latex/05_lineas_y_grados.tex:101–106|

### W2_torres (rev_exp/W2_torres/ACTA.md:273–279)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|6|PT1 (:274): en E01:29–30, cambiar «admitido» por el estado real de R1, que se deduce de cotas intermedias de Divoux–Wang|A|F|Anotada, sin reescribir E01, en MAPA.md, sección «Anotaciones de D1 en fuentes selladas», fila A3 (precisión 8a de W4_rev). D1 está descargado|
|7|PT3 (:276): corregir la errata de U05:10–12 y citar U04:34–39 o R1/torres_fila para el resto O(s³) de K07:54–55|A|F|Pendiente en U05 y K07. Texto propuesto en r22/PRECISIONES_PARA_EL_CONSOLIDADO.md:34|
|8|PT6 (:279): declarar en T08b la convención del producto local y pseudodeterminante, que coincide con la J de T05|A|F|Pendiente en T08b. Convención propuesta en r22/PRECISIONES_PARA_EL_CONSOLIDADO.md:48–56|
|9|PT2 (:275): separar los usos (A) y (B) del error puro de torres|P|N|Incorporada en MAPA.md:20–21|
|10|PT5 (:278): definir φ(v; μ_h) por las integrales bilineales, con las cotas de Neumann en supremo|P|F|Pendiente en K07 y M07 (texto en la fila PT5 de r22/PRECISIONES_PARA_EL_CONSOLIDADO.md:36); mencionada en MAPA.md:18|

### W2_norma (rev_exp/W2_norma/ACTA.md:86–89, 124, 155, 171, 181–185)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|11|1a (:86): el «para toda subactivación» de la GUIA 01:3 es todo el cubo de activaciones por sitio|A|F|Pendiente en la GUIA 01 (sección «Correcciones de las GUIAs»)|
|12|2a (:124): N02:39 escribe O_ρ; la dependencia explícita en ρ sólo aparece en N03:18–19|A|F|Pendiente en N02|
|13|3a (:171): las O(ρ²ε_A) y O(ρ²j) de N03:30 y 35 son sobreestimaciones válidas|A|F|Pendiente en N03; es una observación de redacción|
|14|1b (:87–89): P es el punto estacionario de torres, P_e(1−P_e)=a_r b_c|P|F|Ya dicho en latex/04_marginales.tex:2. Pendiente en N01:17 y en la GUIA 01|

### W2_cofactor (rev_exp/W2_cofactor/ACTA.md:266–272)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|15|P1: escribir en B01 que la brecha r′<1 implica la conexión RC del exterior y de cada superviviente|A|F|Pendiente en B01|
|16|P2: el dominio analítico es la caja ‖x‖_*≤a, dentro del interior si a<1/4|A|F|Pendiente en B01 y U07|
|17|P4: actualizar el párrafo «Alcance» de U07 [77–83], obsoleto|A|F|Pendiente en U07|
|18|P5: C′ absorbe el factor 2 de m≥j/2 y las dos evaluaciones; C′q≤j^{1/3} equivale a la desigualdad de A03; n₀ es finito pero enorme|A|F|Pendiente en A03. La falta de efectividad de n₀ se dice en CONSTANTES.md:18|
|19|P7: el descenso Q→q de U04 está comprimido, pero es correcto|A|F|Pendiente en U04|
|20|P6: con la receta de B03, la masa cero exacta requiere que todo átomo compatible sea positivo, y eso lo da la clase|P|F|Pendiente en B03; el punto 11 de la lista inicial trata un asunto afín|

### W2_difusion (rev_exp/W2_difusion/ACTA.md:307–312)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|21|PD2: «max_f» recorre las diagonales de las dos familias; γ≤1, así que min(1, γ) es cosmético|A|F|Pendiente en A01 y D04|
|22|PD3: citar la unicidad del escalado de Sinkhorn al identificar D_A con el escalado exacto; la cota relativa sale de los potenciales en supremo; en la GUIA 04:5, «aplicado a P», no «a P(1−P)»|A|F|Pendiente en A01 y en la GUIA 04|
|23|PD5: explicitar γ′ y C′ en D04:43|A|F|Pendiente en D04|
|24|PD4: márgenes por objeto, (2C, 1−γ_T) para P y (4C, 1−γ_T/2) para D_A, y ‖·‖₂ espectral|P|N|Incorporada en NOTACION.md:24–25 y CONSTANTES.md:4|

### W2_salidas (rev_exp/W2_salidas/ACTA.md:79–85, 117–123, 208–210)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|25|1c (:85): O(e^{−2j}) significa una constante 1+e^{C₀}, para n≥n₀(α, b, δ, β, C_pres)|A|F|Pendiente en H02 y H03|
|26|2b (:119): la transición por hijo es resultado de la prueba de B 8.1 (B/08e_meso:80–88)|A|N|Incorporada en CONSTANTES.md:3 y MAPA.md:47|
|27|2c (:120–122): la presuposición de H02:10 no se usa en H02:12–49 y debe leerse referida a las llegadas cortas|A|F|Pendiente en H02|
|28|2d (:123): la GUIA 05:5 omite la condición s, t≤j/2 de H02:17|A|F|Pendiente en la GUIA 05|
|29|1a (:80): la j de la pieza es el suelo de C, y C 5.8 se aplica con K=⌊bn⌋, admisible para n≥n₀|P|F|Reflejada en latex/06_corte.tex:71 y NOTACION.md:29; pendiente en H03|
|30|4a (:209): la llegada larga es regular, luego interior y exterior; se usan las hipótesis de coste-estatico (C/06a:42–45) y (hyp) para la tabla p|P|F|Reflejada en MAPA.md:29 y 59; pendiente en A01|

### W2_identidad (rev_exp/W2_identidad/ACTA.md:326–333)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|31|P1.1 (:124, 327): enunciar la parada admisible con sus cinco condiciones (§2.1(d), :102–109) y corregir la paráfrasis de la GUIA 06:3|A|F|Pendiente en W/identidad y en la GUIA 06|
|32|P1.3 (:83, 328): para la identidad basta que los hijos incluyan todos los de Q>0|A|F|Pendiente en W/identidad|
|33|P1.4 (:127): en id:15 la letra j es un índice de paso y choca con j=⌊bn⌋|A|F|Pendiente en W/identidad; separación registrada en NOTACION.md:30|
|34|P2.2 (:155, 330): la GUIA 06:5 debe citar la inclusión de C §8 junto a C 4.12 y C 5.7|A|F|Pendiente en la GUIA 06; la inclusión figura en MAPA.md:63|
|35|P2.4 (:157): las constantes dependen de δ y de las clases (co:14), no de b ni de n|A|F|Pendiente en W/corte|
|36|«B §5.1 ausente» (:121, 338): está en BP/08a_meso.md:8–26 (WG:306)|A|F|Incorporada en MAPA.md:46 y 66–67|
|37|P2.3 (:156): τ_M (co:21) y J_n (co:34) se usan sin definición explícita|P|F|J_n está escrito en latex/06_corte.tex:91–97; pendiente en W/corte|
|38|P4.2 (:239, 333): en H03:13–15, m es el borde de la banda, no el orden j−h|P|F|Ya en NOTACION.md:6; pendiente en H03|

### W2_t4 (rev_exp/W2_t4/ACTA.md:264–270)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|39|1.2 (:137–141): colisiones de notación de H_q y de d_i|P|N|Incorporada en NOTACION.md:8, 12, 22–23 y 27|
|40|1.3 (:143): las referencias a documentos de r22 que no estaban en el material|P|N|Incorporada en latex/07_alcance_logaritmico.tex:88–93|
|41|2.3 (:195, 270): Pr(S_M∖G)=O(1/K) es un supuesto, no un resultado de R10|P|F|Pendiente en r22/latex/01_corolario.tex:72, donde «usa» debe decir «supone». El corolario no forma parte del consolidado|

### W2_r3 (rev_exp/W2_r3/ACTA.md:310–317)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|42|PR1 (:312): el argumento c=1 de PF05/GI03–04 se aplica a dos conflictos unidos por fibras RC y a las cuñas; citar el acta; GI01:22–28 sólo enuncia soportes diagonalmente conexos|A|N|Incorporada en latex/05_lineas_y_grados.tex:59–60, 76 y 80–83|
|43|PR5 (:316): citar PF05:1–5 en lugar de «P04–05»|A|N|Incorporada en latex/05_lineas_y_grados.tex:78|
|44|La cita de W2_r3 en el MAPA y en esta lista|A|N|Incorporada en MAPA.md:7–8 y 17, en el punto 10 de la lista inicial y en esta tabla|
|45|PR2 (:313): la cota puntual de w_bd en colocaciones con otras relaciones diagonales es la de PF05 para la activación restringida a b y d|P|N|Incorporada en latex/05_lineas_y_grados.tex:66–69, porque EMP no está en el consolidado. EMP:37–39 sigue sin esa frase|
|46|PR3 (:314): decir qué ruta usa la prueba|P|N|Incorporada en latex/05_lineas_y_grados.tex:59–61|

PR4 y PR6 no aplican: no se mantiene la ruta de la ronda 3 y T07 no se cita.

### W_global (rev_exp/W_global/ACTA.md:82, 130–151, 229–244, 271–277, 349–354)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|47|D1 (:130–142): el primer corrector del permanente descansa en cotas intermedias de un preprint ajeno a B y C; ni reparado ni declarado|A|N|Reparado y descargado: la prueba de rev_exp/W4_d1/, certificada por rev_exp/W4_rev/ACTA.md, se integra como latex/08_corrector_sin_dw.tex, 08b_corrector_prueba.tex y 09_uniformidad_y_usos.tex, y se cita en latex/04_marginales.tex:16–18 y 72–75. Estado en TEOREMA.md:3–8, latex/00_alcance.tex:2–9, latex/06_corte.tex:6–10 y 17–18, MAPA.md:22 y 92–95, DIVOUX_WANG.md y el punto 12 de la lista inicial|
|48|D2 (:144–151): verificación externa incompleta de E01; no registrado|A|N|Registrado como descargado por W3_xi en TEOREMA.md:6 y MAPA.md:21|
|49|4a (:229): objeto de la brecha de CONSTANTES.md:4|A|N|Incorporada en CONSTANTES.md:4|
|50|4b (:230): C_pres no depende de b gracias a B 8.1|A|N|Incorporada en CONSTANTES.md:3|
|51|4d (:232): los dos sentidos de C₀|A|N|Incorporada en CONSTANTES.md:19 y NOTACION.md:28|
|52|El tercer d_i, d_i=x_i⁰−p_i en 05:4 (:240)|A|N|Incorporada en latex/00_alcance.tex:30–31 y NOTACION.md:12 y 23|
|53|q=2 en NOTACION.md:14 (:242)|A|N|Incorporada en NOTACION.md:14 y 26|
|54|Escribir «op» en N01:18 y B01:5 (:238)|A|F|Pendiente en N01 y B01; el sentido se fija en NOTACION.md:25|
|55|La lista de §2.7 de resultados de B y C con su uso|A|N|Incorporada en MAPA.md:35–69|
|56|1a (:82): actualizar los estados; en v2 se actualizan pero se sobredeclaran|P|N|Incorporada, con el estado final tras integrar D1, en TEOREMA.md:3–8, MAPA.md, latex/00_alcance.tex:2–9, latex/06_corte.tex:1, 6–10 y 17–18, DIVOUX_WANG.md, ../LEEME.md:8 y ../ACTA_ADVERSARIAL.md:37|
|57|4c (:231): b y n₀ no son efectivos; TEOREMA.md:13 de v2 sólo decía que no se calculan|P|N|Incorporada en TEOREMA.md:20 y CONSTANTES.md:18|
|58|Las colisiones de letras (:244): H_q, K, j, β y m|P|N|Incorporada en NOTACION.md:8, 12, 27, 29 y 30; m ya estaba en NOTACION.md:6|
|59|La integración en esta lista de las precisiones de las actas posteriores|P|N|Incorporada: esta tabla|

### W3_xi (rev_exp/W3_xi/ACTA.md:223–229)

|#|Precisión|v2|Alcance|Estado en v3|
|---|---|---|---|---|
|60|PX1.1: citar R1/mascara:5–7, por el Lema 7.3 de C, en E02:31|A|F|Pendiente en E02|
|61|PX1.2: justificar Σp(λ−p)=0 en E02:44 por Cp=𝟙 y Γ𝟙=½𝟙|A|F|Pendiente en E02|
|62|PX1.3: escribir pdet S=pdet S₀·det(I+ΓΔ) y la cota simetrizada de la cola en E02:51–53|A|F|Pendiente en E02|
|63|PX2.1: hacer explícita en E03:37–38 la cancelación −zᵀHz/2+½tᵀHt=0|A|F|Pendiente en E03|
|64|PX2.2: decir en E03:32–34 que (Γz)ᵀj=⟨U, p∘λ⟩ y escribir Γz=z−Hz−(s/(2k))𝟙|A|F|Pendiente en E03|
|65|PX2.3: escribir en E03:21 el resto exacto (5/6)Σ(t+j)³|A|F|Pendiente en E03|

E1, E2, W2_tipos, ola1 y W2_jets no añaden entradas: sus precisiones ya estaban en R21
(WG:252–254), salvo E2 P4, que era D1 (ya descargado), y W2_jets 1.1, innecesaria (WG:268).

## Enunciado extendido de K08 (PT4 de W2_torres; P1.1/PW2a de W2_pares), pendiente en la fuente

Destino: K08, líneas 11–17 y 46–52 (fuentes/latex/K08.tex de R21; en rev_exp,
fuentes/velocidad_via2_ronda9_20261116T082611Z/latex/08_estabilidad.tex); uso en M07:2–14.
Texto propuesto por el equipo en r22/PRECISIONES_PARA_EL_CONSOLIDADO.md:39–46 (huella
3d98568d…), que es la propuesta de rev_exp/W2_torres/ACTA.md:166 desarrollada; el dictamen
global lo encuentra coherente con las actas de pares, jets y torres (WG:161). Se transcribe sin
cambios. Las letras h y C_4 son las de K08 y M07: no son la h de supresiones ni la C₄ de 00.

**Estabilidad al suprimir una fila y una columna arbitrarias.** Fijados \(M_0\) y \(0\le r<1\), existen \(k_0,C\) de clase con la siguiente propiedad. Sea \(A\) una máscara de tamaño \(k\ge k_0\) de la clase difusa de K06, cuyo punto de torres \(P\) es interior en su soporte, bistocástico, con \(k\max P\le M_0\) y \(\|P-J_k\|_{\rm op}\le r\), donde \(J_k=\mathbf1\mathbf1^t/k\). Escribamos \(R_T(A)=\log\operatorname{per}A-L_T(A)-u_T(A)\), con \(u_T(A)=-1/(12k)+\Xi(P)\). Para cualquier fila \(i\) y cualquier columna \(h\), esté o no \((i,h)\) en el soporte, su eliminación pura satisface
\[
  |R_T(A)-R_T(A_{-i,-h})|\le C/k^3 .
\]

Para el uso en M01, sea \(A_0=A\) y sea \(A_{t+1}\) el menor obtenido de \(A_t\) suprimiendo una fila y una columna vivas, con \(0\le t<\ell\le4\). Cada menor se evalúa con su propio escalado, punto y normalizador, en su tamaño real. Tomando \(k_0\) suficientemente grande y los márgenes heredados de D04/K02/U02, existe \(C_4=C_4(M_0,r)\) tal que \(|R_T(A_{t+1})-R_T(A_t)|\le C_4/(k-t)^3\). Por suma, \(|R_T(A_\ell)-R_T(A)|\le C_4\sum_{t<\ell}(k-t)^{-3}=O_{M_0,r}(k^{-3})\). Son supresiones puras en el exterior basal de M07; sus ceros preexistentes se conservan. Para un número fijo distinto de cuatro la formulación iterada usa los márgenes y el umbral correspondientes a ese número.

## Correcciones de las GUIAs, pendientes

Las GUIAs son r21/piezas_T2/*/GUIA.md (en la entrega R21, piezas_T2/). No forman parte del
consolidado; las correcciones se registran para la entrega que las reemita.

- **GUIA 01 (01_norma/GUIA.md:3).**
  - 1a de W2_norma (:86): sustituir «y toda subactivación de sus dos familias» por «Λ está
    definido en todo el cubo de activaciones por sitio, que activa las dos familias, y».
  - 1b de W2_norma (:87–89): «ε_A se mide en el punto de torres» debe decir «en el punto
    estacionario de torres P, con P_e(1−P_e)=a_r b_c».
- **GUIA 04 (04_difusion/GUIA.md:3 y 5).**
  - PD1 de W2_difusion (:308): enunciar el umbral de tamaño j≥j_T(C, γ) de D04, o tomar
    K_T≥4j_T, y explicitar K_T, ε_T y j_T. Ya figura en CONSTANTES.md:15.
  - PD3 de W2_difusion (:310): en la línea 5, «El Lema 7.3 de C aplicado a P(1−P)» debe decir
    «aplicado a P», y debe citarse la unicidad del escalado de Sinkhorn.
- **GUIA 05 (05_salidas/GUIA.md:5).** 2d de W2_salidas (:123): añadir la condición s, t≤j/2
  de H02:17 al paso de prescripciones.
- **GUIA 06 (06_identidad/GUIA.md:3 y 5).**
  - P1.1 de W2_identidad (:109, 124): «pesos exp L finitos en todos los hijos anteriores a
    parar» debe enunciarse como las cinco condiciones de la parada admisible: τ≤n; τ adaptada a
    (σ, inserciones reveladas), con el orden completo fijado al principio; L(B₀)<∞; en {t<τ}, L
    finito en el padre y en todos los hijos disponibles de la fila siguiente; y la convención de
    fila vacía.
  - P2.1 de W2_identidad (:154): «Para δ fijo» debe decir «Para δ admisible, en el orden de
    C §5.4 (C/05e:71–75)». Ya figura en TEOREMA.md:12.
  - P2.2 de W2_identidad (:155): en la línea 5, añadir la inclusión de C §8 a «El Corolario 4.12
    y el Lema 5.7 de C».
  - P3.1 de W2_identidad (:177), que la tabla de W3_v2 no cuenta: el consolidado no usa C 1.1
    (latex/06_corte.tex:101–102), pero la GUIA sí. «Por el Teorema 1.1 de C, X(B₀)→1» debe
    citar g(B₀)→0 de C §8 (C/08_cierre:63–67).

## Precisiones de las actas que la tabla no cuenta

- Innecesarias según el dictamen global (WG:267–269): W2_jets 1.1, porque e^{B₁} basta, y
  W2_salidas 1b y 5a, porque C 5.8 con K=m cubre toda banda [m,2m). El consolidado conserva la
  suma diádica, que es válida (latex/06_corte.tex:71; punto 4 de la lista inicial).
- Refuerzos opcionales: W2_norma 3b (‖Λ‖_ρ≤Cρ²j) y W2_identidad P1.2 (la identidad vale
  para cada orden fijo).
- Sin efecto en el consolidado: W2_identidad P3.2 (C 1.1 es prescindible: latex/06_corte.tex:101–102),
  W2_salidas 2a (promedio sobre la fila uniforme en H02:15–16; pendiente en H02) y 4b
  (bastaría β(ε)), y W2_t4 2.1–2.2, que ya recoge el punto 13 de la lista inicial.

## Integración de D1: precisiones de rev_exp/W4_rev/ACTA.md (§5, :390–398)

|Precisión|Qué pide|Estado en v3|
|---|---|---|
|2a (:108, 391)|Declarar que el Teorema para D general usa U01 con h=v=0 leído según 01m:4|Incorporada: declaración expresa de alcance en latex/08_corrector_sin_dw.tex:61–66, con la cita de W4_rev, punto 2|
|2b (:110, 392)|La cota de núcleo de 01m:48 se necesita en \|yw\|≤r₁(1+d₀), no en Ω; el Lema 1(a) la da con 1−r₁(1+d₀)r en lugar de ρ|Incorporada en latex/08_corrector_sin_dw.tex:57–59|
|7a (:261, 393)|El rango de tamaños del telescopio es [j−d−2, j−d], no [j−2d−2, j]|Incorporada en latex/09_uniformidad_y_usos.tex:50–51|
|7b (:263, 394)|Añadir E1, que certifica U02, a las actas de pertenencia a la clase|Incorporada en latex/09_uniformidad_y_usos.tex:35–36, 45, 67 y 73. ESTADO.md de W4_d1 no se copia|
|8a (:291–297, 395)|A3–A5 de INTEGRACION.md: no reescribir originales sellados|Incorporada: anotaciones A3–A5 y C1–C9 en MAPA.md, sección «Anotaciones de D1 en fuentes selladas»; las fuentes no se tocan|
|8b (:299, 396)|Listar [V2]LEEME.md:7, [V2]ACTA_ADVERSARIAL.md:35 y 06:6–7|Incorporada con el estado nuevo en ../LEEME.md:8, ../ACTA_ADVERSARIAL.md:37 y latex/06_corte.tex:6–10 (y 17–18)|
|8c (:301, 397)|B1 sin «allí indicados», con la lista de B y C|Incorporada: TEOREMA.md:3–4 remite a la lista de MAPA.md|
|8d (:303, 398)|A4: citar 01m:23–32 y 59–66 junto a U02–U04|Incorporada en MAPA.md, anotación A4|

## Integración de D1: los cambios de rev_exp/W4_d1/INTEGRACION.md

|Cambio|Estado en v3|
|---|---|
|A1, A2 (04:72 y 04:16–18)|Aplicados en latex/04_marginales.tex:72–75 y 16–18, con las partes nuevas como referencia|
|A3–A5 (E01, U01, U03, U04 y FUENTES.md de menores uniformes)|Anotados en MAPA.md (8a; A4 con 8d); las fuentes selladas no se modifican|
|A6 (DIVOUX_WANG.md)|Aplicado: nota histórica con el texto del apartado D, adaptado, y el registro de v2 debajo|
|A7, B14, B15 (r21)|No aplican: r21 es una entrega cerrada fuera de esta edición|
|B1–B4, B16 (TEOREMA, MAPA, 00 y 06)|Aplicados con el estado final (8b, 8c): TEOREMA.md:3–8, MAPA.md:22 y 92–95, latex/00_alcance.tex:2–9, latex/06_corte.tex:6–10 y 17–18|
|B5 (registro)|Aplicado en consolidado/CAMBIOS.md|
|B6 (CONSTANTES.md)|Aplicado en CONSTANTES.md:3|
|B7 (NOTACION.md, fila H)|Aplicado en NOTACION.md:8|
|B8 (CONTINUAR.md de v2), B10 (coeficiente/), B11–B13 (entrega de cierre)|No aplican: esos archivos no forman parte de esta edición (../PENDIENTE.md)|
|B9 (punto 12 de esta lista)|Aplicado: punto 12|
|C1–C9 (fuentes que citan W/permanente o la ronda 1)|Anotados en MAPA.md, sin reescribir las fuentes|
