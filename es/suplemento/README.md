# Suplemento de «El término de orden 1/n del problema de las n reinas»

Datos, programas y certificados que acompañan el artículo de Dilan Steven Mejia. Conserve `articulo/` y
`suplemento/` como carpetas hermanas.

| Carpeta o archivo | Contenido |
|---|---|
| `datos/` | Datos: conteos exactos y valores del predictor (`c_n.json`), ajuste de tamaño finito, nodos, muestras e intervalos |
| `replica/` | Cálculos: mallas finales, programas de análisis y `reproducir_valor.py`, que rehace la estimación numérica |
| `certificados/` | Evidencias: programas que generan los intervalos del perfil, de S, de P_T y de Q₂, con sus insumos y certificados |
| `ESTADO.md`, `TRAZABILIDAD.md`, `traza_prueba.md`, `traza_torres.md`, `traza_numeros.md` | Evidencias: estado de cada afirmación y trazabilidad de la prueba, de las torres y del cálculo |
| `CATALOGO.md`, `FUENTES_EMPALMES.md`, `ORIGEN_ESTADO.tsv`, `ORIGEN_NUMERICO.tsv` | Evidencias: catálogo de técnicas, pasajes de origen y procedencia de los archivos, con huellas SHA256 |
| `REPRODUCIR.md` | Guía de reproducción, en español y en inglés |
| `LICENSE` | Licencia MIT |
| `SHA256SUMS` | Huellas SHA256 de todos los archivos del suplemento |

## Reproducción del valor numérico

Desde `suplemento/`, con Python 3 y NumPy, ejecute:

```
python -B replica/reproducir_valor.py replay
```

La orden rehace el análisis en el directorio nuevo `replay` y debe dar 0,4055003786 a diez decimales [N].
Desde `certificados/`, `python -B verificar_insumos.py` comprueba las entradas de los certificados por
intervalos; su README da las órdenes completas. `REPRODUCIR.md` explica también cómo regenerar las mallas a
partir del archivo de investigación.

En los archivos del suplemento, la constante c_err del artículo aparece como `c`. Las etiquetas [D], [O],
[N] y [D si C] tienen el mismo sentido que en el artículo.

La licencia es MIT. Los datos de citación se encuentran en `CITATION.cff`.
