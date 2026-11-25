# Datos y reproducción / Data and reproduction

## Réplica portátil de la estimación / English quick start

Desde `suplemento/`, con Python 3 y NumPy, ejecutar en un directorio de salida que todavía no exista. Los datos de las tres tandas y los programas de análisis están incluidos. El programa recompone las extrapolaciones espaciales, la serie de radio 0,03, GL6, GL20 y los errores por partida. Verifica el valor y las dos nuevas cotas de muestreo frente al análisis archivado. La ejecución de preparación de esta entrega reprodujo **0,4055003786 [N]** al redondear a diez decimales, a partir de los agregados originales. No requiere acceso a otras carpetas.

From `suplemento/`, run the following with Python 3 and NumPy. Supply a new, empty output path that does not yet exist. The three grid datasets and the original analysis modules are included. This replays the paper’s numerical recipe from finite grid data. It fits the spatial sequences, integrates the panels and the circle, recomputes the error budget and compares with the archived analysis. The expected output is **0.4055003786 [N]** to ten decimal places. The Richardson errors remain empirical.

~~~sh
python -B replica/reproducir_valor.py resultados_reproducidos
~~~

El archivo `analisis_v3_replica.json` contiene el campo `nuevo.c` y sus integrales parciales. Los directorios de réplicas sucesivas deben tener nombres diferentes. El resumen muestra las comprobaciones y las sensibilidades. La ejecución original de las mallas usó Windows, Python 3.14, NumPy y SciPy. El análisis pequeño necesita NumPy. La última combinación se contrastó contra `datos/analisis_v3b.json`. El análisis no vuelve a enumerar soluciones.

**Alcance de la cota / Scope of the bound.** La cota de \(8{,}74\cdot10^{-10}\) para serie y cuadratura
corresponde a \(k_6/x^2\) bajo las tolerancias de muestreo [D si C]. La réplica integra
\(k/x^2=(k_6+k_F)/x^2\). En el círculo usa \(\mathcal V+F\) y en ambos paneles usa \(k\).
Para \(k_F=F-F(0)-xF'\), coteja su integral numérica con \(F(0)+F'(0)-F(1)\).
La diferencia entre la fórmula de los extremos evaluada con los datos y la integral numérica es
\(-3{,}77\cdot10^{-13}\) [N]. La variable `k6` de `metodo_nuevo` guarda los seis valores de \(k\) del
panel corto.

The \(8.74\cdot10^{-10}\) series and quadrature bound applies to \(k_6/x^2\) under the stated
sampling tolerances [D if C]. The implementation integrates \(k/x^2=(k_6+k_F)/x^2\), reconstructing
the series with \(\mathcal V+F\) and using \(k\) on both Gauss panels. For \(k_F=F-F(0)-xF'\), the
endpoint formula \(F(0)+F'(0)-F(1)\), evaluated with the numerical data, minus the numerical integral
is \(-3.77\cdot10^{-13}\) [N]. The archived difference is in `nuevo.parte_F.exacta_menos_cuadratura`.
In `metodo_nuevo`, the variable `k6` holds the six values of \(k\) on the short panel.

## Certificados continuos ejecutables / Standalone interval calculations

La carpeta [certificados](certificados/README.md) incluye los generadores del perfil, S, P_T y Q₂ en GL20 n.º 10, sus insumos, el modelo entero de 256 paneles y el código que lo construye. From `certificados/`, run `python -B verificar_insumos.py` as a quick check. Its README gives complete commands for the longer procedures. The distributed inputs suffice; the original research directories are unnecessary for these four runs.

## Datos compactos que acompañan al artículo

| Ficheros relativos | Contenido | Interpretación |
|---|---|---|
| `datos/c_n.json`, `datos/ajuste_finito.json` | Q, predictor, nR y ajuste | Véase el diccionario. |
| `replica/datos_malla/`, `replica/pc_resultados/` | Valores por malla de las tres tandas y configuración de la tanda adicional | Entradas de la réplica portable [N]. |
| `datos/analisis_v3b.json`, `datos/balance_GL20.json` | Análisis y GL20 | Cota para \(k_6/x^2\). |
| `datos/muestras*.jsonl` | Muestras auxiliares de la elipse del panel largo, de la elipse corta y del círculo de radio 0,055 | Fourier y condiciones explícitas de muestreo. |
| `datos/candidato_perfil.json`, `datos/residuo_perfil.json`, `datos/perfil_M16d14.json` | Candidato racional, verificación del residuo y cierre autónomo por coercividad | Radios [O] del perfil físico. |
| `datos/nodos_reales.json`, `datos/circulo/`, `datos/cuadrados43.json`, `datos/coincidencias43.json` | 26 reales y 17 complejos, C3 y las cotas de las coincidencias | Distinguir cajas de integración de cotas de módulo. El alcance por fila se detalla en el artículo. |
| `datos/intervalo_global.json`, `datos/pt_n2048.json` | Extremos exactos o exteriores de S y del ensamblaje grueso, más el refinamiento de P_T | El ensamblaje histórico contiene su propio P_T a 1024 celdas. El valor vigente usa el fichero 2048 separado. |
| `datos/q2_completo.json`, `datos/anchura_rc.json` | Evaluación intervalar de las 17 partidas y suelo de precisión de S13 | Los tiempos y el tamaño de panel están registrados junto a los extremos. |

`ORIGEN_NUMERICO.tsv` registra nombre local, nombre original y SHA256 de las 50 copias. Los datos se copiaron byte a byte y se contrastaron ambas huellas. El SHA256SUMS de la entrega incluye además el nuevo programa portátil. Los objetos [O] conservan las condiciones de aritmética exacta o exterior del certificado. No son intervalos estadísticos.

**Errores relativos históricos / Historical relative errors.** En `datos/c_n.json`, el error del
predictor respecto de \(Q(n)\), en porcentaje, se calculó como \(100(\exp(c/n-R_Q(n))-1)\).
Cada campo corresponde a un valor fijo de \(c\). / In `datos/c_n.json`, each field uses a fixed \(c\)
in the formula \(100(\exp(c/n-R_Q(n))-1)\) for the percentage error of the predictor relative to \(Q(n)\).

| Campo / Field | \(c\) |
|---|---:|
| `err_sin_c` | 0 |
| `err_con_c` | 0.637 |
| `err_c_menos` | 0.570 |
| `err_c_mas` | 0.704 |

Para el predictor del artículo se sustituye \(c=0{,}40550038\) [N] en la misma fórmula. En \(n=27\)
resulta \(0{,}30876915\,\%\), frente al \(1{,}17252019\,\%\) de `err_con_c`. Las columnas `Q` y `nR`
dan el conteo exacto y el residuo numérico \(nR_Q(n)\) para \(10\le n\le27\). `logQpred` es el
logaritmo numérico del predictor. El ajuste usa \(16\le n\le27\) con \(c\) prefijado.

For the paper's corrected predictor, substitute \(c=0.40550038\) [N] in the same formula. At \(n=27\)
this gives \(0.30876915\%\), compared with the historical \(1.17252019\%\) in `err_con_c`. The paper
uses `Q` for the exact count and `nR` for the numerical residual \(nR_Q(n)\) at \(10\le n\le27\).
`logQpred` is the numerical logarithm of the predictor. The fit uses \(16\le n\le27\) with \(c\) fixed.

## Cómo repetir las etapas anteriores desde el archivo de investigación

Para regenerar los datos primarios se necesitan los programas y los insumos de las carpetas originales indicadas abajo. Estos paquetes grandes no se redistribuyen íntegros en este suplemento. Cada orden se ejecuta en una **copia nueva** de su carpeta de cálculo, pues algunos programas antiguos crean los JSON directamente en el directorio de trabajo. No ejecutar esos programas en los originales. En los ejemplos, `$BASE` designa `perfil_certificado_20261121T112347Z` del archivo, y todos los archivos de salida deben ser nuevos.

1. **Q y diagnóstico de tamaño finito.** Los enteros de `datos/c_n.json` son datos de entrada. La columna nR se reconstruye como `n*(log(Q)-logQpred)`. Para el ajuste de periodo cuatro usar `ens_final/r7_cn.py` en una copia de `resultados_c_final_20261122T0701Z`, con Python, NumPy y SciPy. `python -B r7_cn.py` usa el valor de la receta anterior en r6_presupuesto.json; el JSON archivado de ese ajuste se incluye. No se atribuye aquí una nueva enumeración de Q al proyecto de este artículo.
2. **Generación de mallas.** En las copias de `malla_local_v3_20261122T0915Z` y `malla_local_v3b_muestrasV_20261122T1247Z`, `PRUEBA_RAPIDA.bat` verifica la instalación local y `EJECUTAR.bat` inicia los casos pendientes de cada configuración. La malla de cada caso está definida en config.json; el lanzador reanuda por archivo de tarea. v3 registró 955 tareas, 16 procesos y 168,3 minutos de pared. La tanda adicional registró 132 tareas y 30,1 minutos con el mismo paralelismo. El agregado precedente está en `resultados_c_final_20261122T0701Z/pc_resultados/`; los scripts de su reproducción y el ajuste de J se describen en su LEEME §Cómo reproducir. El programa portátil de arriba sustituye las rutas de la sesión histórica para la etapa de análisis v3+v3b.
3. **Cuadratura condicional de \(k_6/x^2\).** En una copia de `p5_cuadratura_rigurosa_20261122T0836Z`,
   `python -B balance.py` utiliza el muestreo GL20 archivado. Para el panel de seis puntos y el círculo de
   32 puntos, la réplica reproduce `certificacion.panel` y `certificacion.serie` con los radios de muestreo
   declarados. Los datos nodales y de frontera intervienen además en la incertidumbre numérica de \(c\).
4. **Perfil.** En `p6_certificacion_20261123T124757Z/perfil/`, ejecutar por orden `python -B paneles.py generar $BASE 16 14 nuevo_candidato.json`, `python -B paneles.py verificar $BASE 16 14 nuevo_certificado.json --candidato nuevo_candidato.json` y `python -B coercividad.py nuevo_certificado.json nuevo_candidato.json nuevo_log.json`. PERFIL.md explica la validación racional y el traslado del candidato anterior.
5. **Frontera y filas explícitas.** En la subcarpeta `frontera/` de esa copia, `python -B certifica_S_perfil.py 64 1048576 $BASE nuevo_S.json` rehace la cubatura del cuadrado. El extremo autónomo final incorpora el ensanchamiento descrito en `ensamblar.py`. En `reales/`, `python -B estrechar.py replica26.json` produce las partes reales. En `circulo/`, `python -B refinar.py replica48 --orden 48` escribe un JSON por punto. En `cubos/`, `cuadrados.py`, `ajustar.py` y `deltas.py` producen las 43 cajas de cuadrados y mayorantes de las dos coincidencias. En la raíz, `python -B ensamblar.py replica_global.json` usa los certificados archivados. En `global_jet/`, `python -B directo.py replica_J.json` reconstruye el mayorante por estados de J. El ajuste numérico por clases de la etapa 2 conserva su propia incertidumbre [N].
6. **P_T y Q₂.** En `p6_viabilidad_Q2_20261123T132743Z/pt/`, `python -B pt2048.py replica_pt.json` reproduce P_T a 2048 celdas con un hilo y los insumos de la carpeta del punto 6. La ejecución archivada consumió 111,75 s de CPU. En la raíz de la misma entrega, `python -B medir.py completo 16 replica_q2.json` y `python -B leer_anchura_rc.py replica_rc.json` reproducen el único nodo GL20 n.º 10 y el mínimo del bloque RC. Requieren el NPZ de 256 paneles de la carpeta original del punto 6. El nodo completo consumió 51,27 s de CPU y la cubatura final de S, 25,13 s de CPU. La referencia de B16 en ese nodo se reconstruye con el analizador de mallas y conserva su estado [N].

**For readers using only the supplement.** The portable replay covers the fitted value, the two-panel decomposition, the short-panel and circle bounds, and the error budget. The interval package regenerates the refined profile, S, P_T and the full single-node Q₂ using its included inputs. Regeneration of the original large B16 grids, the global coarse box for J and every certified explicit row still requires the historical packages identified above. The guide distinguishes archived bounds taken as inputs from the quantities recomputed by each script.
