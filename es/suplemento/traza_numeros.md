# Trazabilidad del cálculo y sus afirmaciones

Las rutas parten de la raíz del archivo de investigación. Los valores de la tabla de contornos de la edición española se documentan punto por punto en [Datos de los contornos](contornos/LEEME.md). ORIGEN_NUMERICO.tsv identifica con una huella SHA256 cada una de las 50 copias de datos y programas incluidas. [O] para enteros o aritmética de intervalos conserva los supuestos aritméticos descritos por el archivo correspondiente. Un cálculo reproducible en doble precisión conserva su etiqueta [N].

| Texto y afirmación | Estado | Comprobación y fuente |
|---|---|---|
| calculo, malla cerrada, dos paridades y traza de recorridos | Identidad de sumas finitas; límites extrapolados [N] | `traspaso_b16_estado_20261122T0352Z/B16_EXPLICACION.md` §§2–7 y `B16_API_motor.md` §§Malla, Nivel. |
| calculo, ejemplo de la fila f6 con hasta cuatro vértices | Reordenación exacta, controles flotantes [N] | `traspaso_b16_estado_20261122T0352Z/B16_ejemplo_f6.md` §§1–3 y `malla_local_v3_20261122T0915Z/v/rect/f6/f6_malla.py`. |
| calculo, dieciséis aportes, f2F doble, separación de f4 explícito y de L0 | [D] para su identificación en media en el interior | `p10_cotejo_de_las_dos_medias_20261123T114324Z/03_interior.tex`, apartado de correspondencia; `programas_J_y_16_filas_20261123T1138Z/filas_jet.py`, líneas 10–13 y sumas ejecutables. |
| calculo, clases mod 24, pesos de lado cero, sesgo por centros, cambios de receta | [N] para magnitud del error y extrapolación | `traspaso_b16_estado_20261122T0352Z/B16_EXPLICACION.md` §§1,6–8; `resultados_c_v3b_20261122T1401Z/codigo/analiza_v3b.py` y `resumen_v3_20261122T140025.txt`, tabla final. |
| calculo y cuadratura_ap, fórmula de extremos de $k_F/x^2$ | [D] | Véase la nota al pie de la tabla. |
| cuadratura_ap, error de Gauss en Chebyshev, truncación y término adicional de la derivada | [D] para las fórmulas con sus hipótesis analíticas | `p5_cuadratura_rigurosa_20261122T0836Z/parte_03.tex`, lema de línea 13, teorema de línea 35 y proposición de línea 66. |
| cuadratura_ap, serie y Gauss para $k_6/x^2$ | [D si C] | Véase la nota al pie de la tabla. |
| calculo, valor 0,40550038 ± 3·10⁻⁸, cifra conservadora y errores por partida | [N] | `resultados_c_v3b_20261122T1401Z/RESULTADO.md` §§1 y 3. Réplica desde tres agregados y las mismas recetas por el programa adjunto. |
| calculo, valores numéricos de J y P₀ | [N] | `resultados_c_final_20261122T0701Z/LEEME.md` §Resultado y `ens_final/r2_J.json` (ajustes por clases de malla). S, P_T históricos y definición firmada en `traspaso_b16_estado_20261122T0352Z/etapa_final_P0_S_J.md`. |
| certificado, radio ≤2,1·10⁻¹⁵ del perfil físico | [O] | `p6_certificacion_20261123T124757Z/perfil/PERFIL.md`, cierre por coercividad, y `perfil/log_M16d14.json`. Comprobación independiente en ACTA.md, línea 7. |
| certificado, G_cof, f4_expl, f2F y T1 en 43 nodos y cuadrado C3 | [O] | `p6_certificacion_20261123T124757Z/NODOS.md` líneas 3–11; ACTA.md línea 9; `reales/reales26.json`, `circulo/nodos48/j00.json` a `j16.json` y `cubos/c3_combinado.json`. Los mayorantes de las coincidencias están en `cubos/deltas43.json`. |
| certificado, intervalo de S con perfil autónomo | [O] | `p6_certificacion_20261123T124757Z/frontera/LEEME.md` para geometría e integración; `RESULTADO.json:S_autonomo` para el valor ensanchado y redondeado hacia fuera; ACTA.md líneas 8 y 15. |
| certificado, encierro de P_T con 2048 celdas por semieje | [O] | `p6_viabilidad_Q2_20261123T132743Z/pt/TORRES_2048.md`, `pt/pt_n2048.json` y revisión, LECTURA.md línea 11. |
| certificado, Q₂ completo, GL20 n.º 10 y tiempo | [O] | `p6_viabilidad_Q2_20261123T132743Z/q2_completo.json`, `EVALUADOR_Q2.md`, `GEOMETRIA.md`, LECTURA.md líneas 3–7. |
| certificado, límite del método de cajas independientes para S13 | [D] para el argumento con [O] para el mínimo de la tabla | `p6_viabilidad_Q2_20261123T132743Z/POR_QUE_PARAR.md` §Límite; `anchura_rc.json` y LECTURA.md línea 9. Alcance limitado a la tabla archivada y a esa separación de S13. |
| certificado, intervalo global grueso y obstáculo con J | [O] para los extremos globales y abierto para decimales | `p6_certificacion_20261123T124757Z/RESULTADO.json`, `global_jet/directo.json`, ACTA.md líneas 11 y 15; `p6_viabilidad_Q2_20261123T132743Z/pt/B16_Y_J.md`. |
| numeros_ap, Q(n) y comparación finita | Q entero exacto; columna nR y ajuste [N] | `traspaso_b16_estado_20261122T0352Z/datos/c_n.json`; `resultados_c_final_20261122T0701Z/ens_final/r7_cn.py`, `r7_cn.json`, y LEEME.md §Ajuste. El análisis usa n=16…27 para el ajuste. |

**Fórmula exacta y comprobación numérica.** La integral de \(k_F/x^2\) vale \(F(0)+F'(0)-F(1)\) [D].
La identidad se demuestra en `p5_cuadratura_rigurosa_20261122T0836Z/parte_01.tex`, lema de la línea 18.
La réplica forma la serie con \(\mathcal V+F\) y aplica GL6 y GL20 a \(k/x^2\).
En `replica/analizador/analiza_v3b.py`, `metodo_nuevo` coteja por separado el aporte de \(F\).
La diferencia entre la fórmula de los extremos evaluada con los datos y la integral numérica es
\(-3{,}77\cdot10^{-13}\) [N]. Figura en `datos/analisis_v3b.json`, campo `nuevo.parte_F`.

**Precisión de redondeo.** Las cotas de serie y cuadratura corresponden a \(k_6/x^2\)
bajo las tolerancias de las muestras [D si C]. Proceden de los teoremas de las líneas 14 y 38 de
`p5_cuadratura_rigurosa_20261122T0836Z/parte_04.tex` y de `resultados_c_v3b_20261122T1401Z/RESULTADO.md`,
§2. La suma de la serie y GL6 vale 8,561112159144814·10⁻¹⁰. El presupuesto añade 1,7·10⁻¹¹ por GL20.
El redondeo a dos cifras significativas da 8,7·10⁻¹⁰. La cota redondeada hacia arriba es 8,74·10⁻¹⁰.

**EN.** The analytic bound of \(8.74\cdot10^{-10}\) applies to the series and quadrature for
\(k_6/x^2\) under the sampling tolerances [D if C]. The implementation integrates \(k/x^2\).
For \(k_F/x^2\), the endpoint formula evaluated with the data minus the numerical integral is
\(-3.77\cdot10^{-13}\) [N].
