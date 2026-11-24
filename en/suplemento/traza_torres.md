# Trazabilidad de torres y de las configuraciones locales / Rook and local-pattern sources

Raíz del archivo del autor: `output/`. Cada prefijo de la tabla designa una carpeta exacta. Los números de línea corresponden a los originales del archivo, no a su composición bilingüe. Las pruebas son comunes a ambos idiomas. [D] se entiende en el sentido editorial del artículo. [O] identifica por separado las operaciones aritméticas que también se comprobaron mediante código.

| Prefijo | Carpeta |
|---|---|
| G | `L_y_G1_corregidos_20261122T1521Z/` |
| G-rev | `revision_L_y_G1_20261122T1521Z/` |
| L+ | `prueba_Lmas_v2_20261122T1637Z/` |
| L+-rev | `revision_Lmas_20261122T1637Z/` |
| Def | `torres_puntos_9_10_20261122T0822Z/` |
| TL | `torres_lemas_G3_G4_v2_20261122T1123Z/` |
| Est | `estabilidad_menores_S_Phi_clase_20261122T1625Z/` |
| V8 | `punto10_texto_v8_revisado_20261122T1629Z/tex/` |
| T10 | `p10_T10_limite_y_marginales_20261123T092723Z/` |
| Fm | `p10_limite_firmado_20261123T100111Z/tex/` |
| Ll | `p10_llegada_fisica_20261123T104835Z/tex/` |
| Rev-global | `p10_revision_global_20261123T121934Z/` |
| Rev-local | `revision_partes14_18_20261122T1601Z/` |

| Parte de la edición / section | Afirmación, alcance y estado | Fuente de enunciado y prueba | Lectura o control |
|---|---|---|---|
| `torres.tex` | [D] Clase de escalado, paso a la clase estacionaria, umbral del tamaño y clase de los menores sucesivos. | TL/`parte_01.tex:9–18,27–40,51–71`; Est/`parte_01.tex:26–34`; T10/`tex/07_estabilidad.tex:2–16`. | Rev-global/`ACTA_GLOBAL.md`, §2, «Qué clase entra», «Estabilidad de la clase». |
| `torres_ap.tex` | [D] Normalización de torres, invariancia y separación exacta G1. | Def/`parte_01.tex:6–42`; G/`torres_G1_v2/parte_01.tex:18–56` y `parte_02.tex:3–54`. | G-rev/`REVISION_L.md`; Rev-global, §2. |
| `torres_ap.tex` | [D] Estimación estática (L*), mezcla gamma, contracciones de exceso uno, índices distintos y colas. | G/`prueba_L_v2/parte_01.tex:32–67`, `parte_02.tex:4–30,44–57`, `parte_03.tex`, `parte_04.tex:21–54`, `parte_05.tex:34–66` y `parte_06.tex:24–65`; G/`torres_G1_v2/parte_04.tex`. | G-rev/`REVISION_L.md`, controles `indep_wick_L`, `indep_rango1_L`, `indep_puntual_L`. El estado abierto en el enunciado preliminar de G1 queda resuelto por la prueba posterior. |
| `torres_estabilidad.tex` | [D] Expresión de la corrección de perfil, de la parte determinista y de (T); parámetros uniformes por encima del máximo de los dos umbrales. | Def/`parte_01.tex`; G/`torres_G1_v2/parte_01.tex:8–56`, `parte_02.tex`, `parte_03.tex`, `parte_04.tex`, `parte_05.tex`. | G-rev/`REVISION_L.md`, controles `indep_det_G1` e `indep_identidad_G1`; Rev-global, §2. |
| `torres_estabilidad.tex` | [D] (L*+) para la parte estática, diferencia de menor de orden tres y de borrado de sitio de orden cuatro. | L+/`parte_01.tex:24–47`, `parte_02.tex:50–72`, `parte_03.tex`, `parte_04.tex`, `parte_05.tex`, `parte_06.tex:1–25`. | L+-rev/`REVISION_LMAS.md`; Rev-global, §2. |
| `torres_incrementos.tex` | [D] Teorema A, identidad exacta que fija el signo de la corrección y equivalencia para el menor. | TL/`parte_01.tex` y `parte_03.tex`–`parte_05.tex`; V8/`operador_lineas_parte_19.tex:34–74`. | Rev-global, §2. En V8/19 se establece la identidad; la ganancia uniforme se demuestra después. |
| `torres_incrementos.tex` | [D] (A+),(D+),(T+), incluidos el cambio de tamaño, las caras de masa cero y el camino de pesos. [O] Los 27 coeficientes racionales son controles adicionales. | Fm/`04_masas_de_tipos.tex:18–63`, `05_determinantes.tex:26–50`, `06_incrementos_uniformes.tex:18–63`, `09_extremo_de_masas.tex:1–18`; Ll/`06_correcciones.tex:5–22`. | Est/`serie_S.json`; lectura global en Rev-global, §2 «Ley puntual e incrementos». |
| `torres_pares.tex` | [D] Corolario C de torres, variación de Φ, (R0) para la marginal exacta y alcance del Corolario 7. | TL/`parte_01.tex`; Est/`parte_03.tex:13–20,51–69`; T10/`tex/07_estabilidad.tex:18–45`; V8/`operador_lineas_parte_18.tex:25–57,60–89`; Fm/`10_termino_por_par.tex:2–20`. | T10/`ACTA.md:5–16`; Rev-global, §2. El uso posterior exige que haya completaciones al tomar logaritmos. |
| `torres_pares.tex` | [D] (S), variación del resto del Corolario C, (R1) y (R2) con peso. (R1) se usa sólo en el menor binario lejano que conserva el par. | Est/`parte_01.tex:42–53`, `parte_07.tex:3–36`, `parte_08.tex:73–80`; T10/`tex/03_incrementos.tex:2–35` y `tex/08_variaciones.tex:9–93`; Fm/`07_marginal.tex:9–59`. | T10/`ACTA.md`; Rev-global, §2, filas (S), ΔRπ y (R1), (R2). |
| `torres_pares.tex` | [D] Minoración del peso para uno o dos pares binarios; alcance de M2. [O] El banco degenerado de M1 no mide constantes. | T10/`tex/01_masas.tex:2–48`; Rev-local/`REVISION.md:99–116,232–249`. | Rev-global, §2 «M1 y M2». |
| `torres_pares.tex` | [D] Teoremas locales 1 y 2, Corolario 5, para una línea con dos sitios. [O] Taylor racional de grado cuatro. | V8/`operador_lineas_parte_08.tex:13–18,40–57`; partes `09`–`11`, `14:22–34`, `15:136–149` y `16:22–49` del mismo prefijo. | Rev-local/`REVISION.md:25–41`; Rev-global, §2 «Teoremas 1–3 y signos». |
| `torres_pares.tex` | [D] Teorema local 3 y Corolario 6; exceso del predictor de signo positivo y exceso final de signo negativo. [O] Polinomio de Taylor en 18 argumentos. | V8/`operador_lineas_parte_17.tex:7–51` y `operador_lineas_parte_17d.tex:108–122`. | Rev-local/`REVISION.md:159–166`; Rev-global, §2. |
| `torres_insercion.tex`, `torres_insercion_prueba.tex` (H.4) | [D] Teorema H.7, inserción de torres: cotas de la matriz de Green, identidades de Ward y expresión de la corrección de una casilla, estabilidad de la clase al pasar al hijo, descomposición exacta del resto de inserción, cancelación de primer orden y cotas. | TL/`parte_01.tex` (objetos, hipótesis y enunciado), `parte_02.tex` (cotas elementales, norma del supremo, función dual, Newton–Kantorovich y estabilidad), `parte_03.tex` (Ward, acción, determinante y desplazamiento) y `parte_04.tex` (pasos 1–3 y tabla de restos). | Rev-global, §2. |
| `torres_dos_casillas.tex` (H.4) | [D] Corolario H.8, dos casillas, con el peso del par; matriz de Green, marginal y corrección del hijo. | TL/`parte_01.tex` (enunciado) y `parte_05.tex` (lemas del hijo y prueba); Est/`parte_07.tex:25–34`; T10/`tex/03_incrementos.tex:2–13`. | Rev-global, §2. |
| `torres_menor_lejano.tex`, `torres_menor_variacion.tex` (H.4) | [D] Proposición H.9, menor lejano y estabilidad (S), y Corolario H.10, incremento del resto de dos casillas. Se demuestran los órdenes uniformes; no se evalúan las constantes literales de las tablas de origen. | Est/`parte_01.tex:42–53`, `parte_05.tex`, `parte_07.tex:3–36` y `parte_08.tex:73–80`; T10/`tex/02_torres.tex`, `tex/03_incrementos.tex:2–35` y `tex/08_variaciones.tex:9–93`; Fm/`07_marginal.tex:9–59`. | T10/`ACTA.md`; Rev-global, §2, filas (S), ΔRπ y (R1), (R2). |

El control del extremo inferior que sustituye la reserva de la primera lectura global pertenece a la prueba por dos cortes del texto principal. No altera las estimaciones de menores de esta tabla.

Correspondencia de nombres desde la v15.1. En las fuentes y en las filas anteriores, «Teorema A» es el Teorema H.7 del artículo, «Corolario C» es el Corolario H.8, la cota de un menor lejano y (S) son la Proposición H.9, y el incremento ΔRπ es el Corolario H.10. La numeración H.1–H.6 de la v14.1 no cambia. En el artículo (R1) sólo se aplica al menor binario lejano que conserva el par, y (S) y (R2) sólo intervienen en el promedio por filas de la marginal del par (H.3).
