# Suplemento de «La corrección de orden 1/n al predictor canónico de las n reinas»

Datos, programas, certificados y fuentes documentales que acompañan el artículo de Dilan Steven Mejia.
Conserve `articulo/` y `suplemento/` como carpetas hermanas.

| Carpeta o archivo | Contenido |
|---|---|
| `datos/` | Datos: conteos exactos y valores del predictor (`c_n.json`), ajuste de tamaño finito, nodos, muestras e intervalos |
| `replica/` | Cálculos: mallas agregadas, programas de análisis y `reproducir_valor.py`, que rehace la estimación numérica |
| `certificados/`, `contornos/` | Evidencias: programas que generan los intervalos del perfil, de S, de P_T y de Q₂, con sus insumos y certificados |
| `cuadrado/` | Evidencias: cálculos racionales de la prueba asistida por ordenador (una línea y cuadrado) |
| `pruebas_llegada/`, `prueba_linea/`, `prueba_pt/`, `cota_previa.md`, `f6.md` | Evidencias: desarrollos y fuentes de los pasos de la demostración |
| `ESTADO.md`, `TRAZABILIDAD.md`, `traza_*.md`, `TRAZA_AMPLIACIONES_ES.md` | Evidencias: estado de cada afirmación y trazabilidad de la prueba, de las torres y del cálculo |
| `CATALOGO.md`, `metodos_historicos.md`, `FUENTES_EMPALMES.md`, `ORIGEN_*.tsv`, `NOTACION_V14.md` | Evidencias: catálogo de técnicas, desarrollo de los métodos, pasajes de origen, procedencia de los archivos y equivalencias de notación |
| `articulos_citados/`, `REFERENCIAS.md` | Los cuatro artículos previos citados y la procedencia de la bibliografía |
| `REPRODUCIR.md` | Guía de reproducción |
| `LICENSE` | Licencia MIT |
| `SHA256SUMS` | Huellas SHA256 de todos los archivos del suplemento |

## Reproducción del valor numérico

Desde `suplemento/`, con Python 3 y NumPy, ejecute:

```
python -B replica/reproducir_valor.py replay
```

La orden rehace el análisis en el directorio nuevo `replay` y debe dar 0,4055003786 a diez decimales [N].
Desde `certificados/`, `python -B verificar_insumos.py` comprueba las entradas de los certificados por
intervalos. `REPRODUCIR.md` explica también cómo regenerar las mallas primarias.

Las etiquetas [D], [O], [N] y [D si C] tienen el mismo sentido que en el artículo. La licencia es MIT;
los datos de citación se encuentran en `CITATION.cff`.
