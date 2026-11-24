# Supplement to "The order-1/n correction to the canonical n-queens predictor"

Data, programs, certificates and documentary sources accompanying the paper by Dilan Steven Mejia.
Keep `paper/` and `suplemento/` as sibling folders.

| Folder or file | Contents |
|---|---|
| `datos/` | Data: exact counts and predictor values (`c_n.json`), finite-size fit, nodes, samples and intervals |
| `replica/` | Calculations: aggregated grids, analysis programs and `reproducir_valor.py`, which replays the numerical estimate |
| `certificados/`, `contornos/` | Evidence: programs that generate the intervals for the profile, S, P_T and Q₂, with their inputs and certificates |
| `cuadrado/` | Evidence: rational computations of the computer-assisted steps (one line and square) |
| `pruebas_llegada/`, `prueba_linea/`, `prueba_pt/`, `cota_previa.md`, `f6.md` | Evidence: developments and sources of the proof steps |
| `ESTADO.md`, `TRAZABILIDAD.md`, `traza_*.md`, `TRAZA_AMPLIACIONES_ES.md` | Evidence: status of each claim and traceability of the proof, the rooks and the calculation |
| `CATALOGO.md`, `metodos_historicos.md`, `FUENTES_EMPALMES.md`, `ORIGEN_*.tsv`, `NOTACION_V14.md` | Evidence: catalogue of techniques, development of the methods, source extracts, file provenance and notation equivalences |
| `articulos_citados/`, `REFERENCIAS.md` | The four earlier papers cited and the provenance of the bibliography |
| `REPRODUCIR.md` | Reproduction guide |
| `LICENSE` | MIT License |
| `SHA256SUMS` | SHA256 digests of all the supplement files |

## Reproducing the numerical value

From `suplemento/`, with Python 3 and NumPy, run:

```
python -B replica/reproducir_valor.py replay
```

The command repeats the analysis in the new directory `replay` and should give 0.4055003786 to ten decimal
places [N]. From `certificados/`, `python -B verificar_insumos.py` checks the inputs of the interval
certificates. `REPRODUCIR.md` also explains how to regenerate the primary grids.

Folder and file names are in Spanish, as in the paper, and several documents are in Spanish. The labels
[D], [O], [N] and [D if C] have the same meaning as in the paper. The license is MIT; citation data are in
`CITATION.cff`.
