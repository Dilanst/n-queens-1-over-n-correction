# Estado de las afirmaciones / Claim ledger

Las claves aparecen en ambas versiones. Las entradas de fuente identifican carpetas relativas a `output/`. Las tablas `traza_prueba.md`, `traza_torres.md` y `traza_numeros.md` precisan los pasajes de cada deducción. [D] identifica los resultados demostrados en el artículo.

| Etiqueta | Afirmación | Cómo se comprobó | Carpeta y archivo de origen |
|---|---|---|---|
| [D] | Existencia y valor del límite (1) | Comparación de dos cortes del mismo tablero inicial | A · `p10_cierre_por_dos_cortes_20261123T123435Z/07_cierre.tex`<br>B · `p10_revision_global_20261123T121934Z/ACTA_GLOBAL.md` |
| [D] | Derivadas nulas en el extremo físico | Finitud de la integral truncada y analiticidad. La edición española v12 deduce también el orden cero. | A · `p10_cierre_por_dos_cortes_20261123T123435Z/07_cierre.tex`<br>H · `demostraciones_7_8_revisadas_20261122T0646Z/paso_limite/parte_04.tex` |
| [D] | Identidad con signo y salidas a corte fijo | Historias detenidas, diferencia firmada y momentos | C · `p10_limite_firmado_20261123T100111Z/tex/03_pares.tex`<br>D · `p10_llegada_fisica_20261123T104835Z/tex/12_ensamblaje.tex`<br>W · `p10_T10_limite_y_marginales_20261123T092723Z/ACTA.md` |
| [D] | Resto de llegada en media, uniforme en el corte | Ley física, suma por tamaño y error de orden $b$ | D · `p10_llegada_fisica_20261123T104835Z/tex/12_ensamblaje.tex` |
| [D] | Densidad interior | Dieciséis términos y límite de Riemann a corte fijo | E · `p10_cotejo_de_las_dos_medias_20261123T114324Z/03_interior.tex`<br>Z · `programas_J_y_16_filas_20261123T1138Z/filas_jet.py` |
| [D] | Torres en la frontera y cuadrado | Supervivencia de dos filas y dos columnas y multiplicidad del cuadrado | D · `p10_llegada_fisica_20261123T104835Z/tex/12_ensamblaje.tex`<br>G · `pt_integrado_punto9_20261122T0920Z/parte_04.tex` |
| [D] | Respuesta del par $J=-B_2+L_2$ | Ocho submedidas y reinserción de rango dos | F · `p10_F2_camino_del_par_20261123T115914Z/06_F2_y_limite.tex`<br>X · `p10_frontera_por_estado_20261123T113157Z/02_enunciado.tex` |
| [D] | Desarrollo de torres y estabilidad | Resto uniforme, menores y borrado con pesos | I · `revision_L_y_G1_20261122T1521Z/REVISION_L.md`<br>K · `revision_Lmas_20261122T1637Z/REVISION_LMAS.md`<br>Y · `torres_lemas_G3_G4_v2_20261122T1123Z/INFORME.md` |
| [D] | Incremento restringido de la marginal | Punto estacionario, determinante y pesos físicos | B · `p10_revision_global_20261123T121934Z/ACTA_GLOBAL.md`<br>C · `p10_limite_firmado_20261123T100111Z/tex/03_pares.tex`<br>L · `punto10_texto_v8_revisado_20261122T1629Z/tex/operador_lineas_parte_19.tex` |
| [O] | Identidades racionales de la demostración asistida | Desarrollo del par en siete variables y no aditividad del cuadrado en dieciocho. Los restos uniformes se prueban en el artículo. | [Procedimiento y salidas](cuadrado/README.md) |
| [O] | Controles algebraicos | 27 coeficientes de marginal y control del extremo transcrito | M · `estabilidad_menores_S_Phi_clase_20261122T1625Z/serie_S.json`<br>H · `demostraciones_7_8_revisadas_20261122T0646Z/paso_limite/parte_04.tex` |
| [N] | Estimación decimal y banda conservadora | Extrapolación de mallas y presupuesto empírico | P · `resultados_c_v3b_20261122T1401Z/RESULTADO.md` |
| [N] | Integral de $k_F/x^2$ | Cotejo con los extremos | P (véase abajo) |
| [D si C] | Serie y cuadratura de $k_6/x^2$ | Tolerancias de muestreo | P, Q (véase abajo) |
| [O] | Perfil físico y términos nodales explícitos | Intervalos exteriores y cobertura por fila | R · `p6_certificacion_20261123T124757Z/RESULTADO.json` |
| [O] | Integrales de frontera $S$ y $P_T$ | Cubatura certificada y recurrencia intervalar | R · `p6_certificacion_20261123T124757Z/RESULTADO.json`<br>T · `p6_viabilidad_Q2_20261123T132743Z/q2_completo.json` |
| [O] | $Q_2$ completo en un nodo real | Encierros del núcleo y trazas con signo | T · `p6_viabilidad_Q2_20261123T132743Z/q2_completo.json` |
| [O] | Mayorantes globales | El ancho de la integral impide certificar el signo | R · `p6_certificacion_20261123T124757Z/RESULTADO.json` |
| [O] | Conteos enteros $Q(n)$ | Enumeraciones citadas hasta 27 | N · `traspaso_b16_estado_20261122T0352Z/datos/c_n.json` |
| [N] | Residuos $nR_Q(n)$ | Evaluación del predictor, oscilación y deriva ajustadas | N · `traspaso_b16_estado_20261122T0352Z/datos/c_n.json` |
| Abierto | Encierro fino de $c$ | Errores nodales, integración del par y resto de malla | P · `resultados_c_v3b_20261122T1401Z/RESULTADO.md`<br>R · `p6_certificacion_20261123T124757Z/RESULTADO.json`<br>T · `p6_viabilidad_Q2_20261123T132743Z/q2_completo.json` |
| Fuera del teorema | Llegada puntual y vetos arbitrarios | Bastan las versiones restringidas | A · `p10_cierre_por_dos_cortes_20261123T123435Z/07_cierre.tex`<br>B · `p10_revision_global_20261123T121934Z/ACTA_GLOBAL.md` |

Para la serie y cuadratura de \(k_6/x^2\) el error es a lo sumo \(8{,}74\cdot10^{-10}\) [D si C].
La réplica integra \(k/x^2\) y coteja \(k_F/x^2\) con la fórmula de los extremos [N].
The bound \(8.74\cdot10^{-10}\) applies to \(k_6/x^2\) under the sampling tolerances [D if C].
The implementation integrates \(k/x^2\) and checks \(k_F/x^2\) against the endpoint formula [N].

- P · `resultados_c_v3b_20261122T1401Z/RESULTADO.md`, `datos/analisis_v3b.json`.
- Q · `p5_cuadratura_rigurosa_20261122T0836Z/INFORME.md`.
