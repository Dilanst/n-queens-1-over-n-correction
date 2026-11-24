# Datos de la tabla de contornos del apéndice J.2

[datos.json](datos.json) conserva las muestras usadas para la estimación condicional del error de
integración de h₆ = k₆/x². Cada lista almacena los puntos desde el ángulo cero hasta π. El semicírculo
restante se obtiene por conjugación. Al calcular la media cuadrática, los dos extremos tienen
multiplicidad uno y los puntos interiores, dos.

| Clave | Datos | Procedencia |
|---|---|---|
| circulo | 33 representantes. Por punto se dan k₆, 𝒱 y sus tolerancias | resultados_c_v3b_20261122T1401Z/analisis_v3_20261122T140025.json, muestras.muestras_c.filas |
| GL6 | 24 representantes. Para la elipse se usa delta_h | Mismo archivo, muestras.muestras_e.filas |
| GL20 | 117 representantes. Para la elipse se usa delta | p5_cuadratura_rigurosa_20261122T0836Z/balance.json, muestras |
| certificacion_circulo y certificacion_GL6 | Radios, mayorantes, datos, resto y suma de cada tramo | Archivo del primer renglón, certificacion.serie y certificacion.panel |
| certificacion_GL20 | Datos, solapamiento, ruido y cola para la elipse exterior de parámetro 2,2 | balance.json, cotas["2.2"] |

Las tolerancias se obtuvieron por refinamiento. La desigualdad de integración se aplica si cada error
complejo está dentro de su tolerancia nodal. Estos contornos auxiliares son distintos de los 43 nodos
independientes de evaluación cuya incertidumbre figura en la sección 5.
