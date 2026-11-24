# El menor doble y la primera media de frontera

La proposición «Primera media a corte fijo» del apéndice D identifica dos límites. El incremento
del funcional de torres en el menor, multiplicado por el tamaño y por el peso del par, aporta
`dF₂(b)`. Su signo en la primera media física es negativo. Las dos fórmulas usan el indicador
de llegada regular y completable `F_b`.

[Extractos de las fuentes con su numeración original](FUENTES.txt).

| Paso de la prueba | Archivo en el registro del autor | Líneas |
|---|---|---|
| Definición de la media, del peso de línea y de la derivada | `pt_integrado_punto9_20261122T0920Z/parte_01.tex` | 35–68 |
| Masa de los pares, densidad de sus extremos y autopares en la regla de malla | `pt_integrado_punto9_20261122T0920Z/parte_02.tex` | 7–46, 60–65 |
| Centrado exacto en la malla y en el continuo | `pt_integrado_punto9_20261122T0920Z/parte_03.tex` | 3–35 |
| Hipótesis originales para promediar la máscara y alcance del resto | `pt_integrado_punto9_20261122T0920Z/parte_04.tex` | 8–39 |
| Cociente exacto y dos incrementos de la corrección de torres | `p10_limite_firmado_20261123T100111Z/tex/10_termino_por_par.tex` | 2–34 |
| Número de pares y resto total a escala n | `p10_limite_firmado_20261123T100111Z/tex/03_pares.tex` | 8–31 |
| Motivos bajo la ley física, indicadores repetidos y condicionamiento | `p10_llegada_fisica_20261123T104835Z/tex/07_motivos.tex` | 2–14, 28–61 |
| Escalado y transferencia de las influencias con una raíz | `p10_llegada_fisica_20261123T104835Z/tex/08_punto_torres.tex` | 13–41, 43–92 |
| Primera media física y coste de imponer vacancias en la solución completa | `p10_llegada_fisica_20261123T104835Z/tex/09_medias.tex` | 2–21 |
| Brecha del escalado y control de la excepción ponderada | `p10_llegada_fisica_20261123T104835Z/tex/14_precisiones.tex` | 10–23 |

En la malla del perfil la identidad exacta usa las primeras variaciones y cuenta a mitad de peso
ambas ordenaciones, incluidos los autopares de cada familia. En el tablero físico cada par usa
dos casillas distintas. El desarrollo del incremento del menor deja un error uniforme de orden
`1/j` por par en la escala de la ecuación del apéndice. Tras multiplicar por `n/j⁴` y sumar
hasta `j²(j−1)` pares, cuesta `O(n/j²)`. El paso desde la máscara al perfil tiene su propio
error `o_b(1)`. Primero se toma el límite en n con b fijo y después se hace tender b a cero.
