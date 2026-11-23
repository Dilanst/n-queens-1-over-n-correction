# Supplement to "The order-1/n term of the n-queens problem"

Data, programs and certificates accompanying the paper by Dilan Steven Mejia. Keep `paper/` and
`suplemento/` as sibling folders.

| Folder or file | Contents |
|---|---|
| `datos/` | Data: exact counts and predictor values (`c_n.json`), finite-size fit, nodes, samples and intervals |
| `replica/` | Calculations: final grids, analysis programs and `reproducir_valor.py`, which replays the numerical estimate |
| `certificados/` | Evidence: programs that generate the intervals for the profile, S, P_T and Q₂, with their inputs and certificates |
| `ESTADO.md`, `TRAZABILIDAD.md`, `traza_prueba.md`, `traza_torres.md`, `traza_numeros.md` | Evidence: status of each claim and traceability of the proof, the rooks and the calculation |
| `CATALOGO.md`, `FUENTES_EMPALMES.md`, `ORIGEN_ESTADO.tsv`, `ORIGEN_NUMERICO.tsv` | Evidence: catalogue of techniques, source extracts and file provenance with SHA256 digests |
| `REPRODUCIR.md` | Reproduction guide, in Spanish and English |
| `LICENSE` | MIT License |
| `SHA256SUMS` | SHA256 digests of all the supplement files |

## Reproducing the numerical value

From `suplemento/`, with Python 3 and NumPy, run:

```
python -B replica/reproducir_valor.py replay
```

The command repeats the analysis in the new directory `replay` and should give 0.4055003786 to ten decimal
places [N]. From `certificados/`, `python -B verificar_insumos.py` checks the inputs of the interval
certificates; its README gives the complete commands. `REPRODUCIR.md` also explains how to regenerate the
grids from the research archive.

Folder and file names are in Spanish, as in the paper. The reproduction guides and the traceability index
are bilingual; the catalogue and some trace tables are in Spanish. In the supplement files, the constant
c_err of the paper appears as `c`. The labels [D], [O], [N] and [D if C] have the same meaning as in the
paper.

The license is MIT. Citation data are in `CITATION.cff`.
