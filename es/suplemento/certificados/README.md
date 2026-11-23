# Continuous interval calculations / Cálculos continuos con intervalos

This directory contains the generators for the certified profile, the boundary terms S and P_T, and the complete Q₂ interval at real GL20 node 10. Starting inputs are supplied here. The 26 archived files total 14,736,050 bytes. The largest file (14,579,631 bytes) is the signed integer bivariate enclosure for this single node. There are no external project paths. Python 3, NumPy and threadpoolctl are required. Use Windows for the archived P_T supervisor. The certified runs used IEEE binary64 arithmetic and a single BLAS thread. Do not invoke Python with `-O` because the checks use assertions.

Los mandatos siguientes se ejecutan desde este directorio. Los nombres de salida deben ser nuevos. El paquete importa los coeficientes y los certificados de base archivados. Reconstruye las cuatro cantidades a partir de esos insumos. En el modelo bivariante incluye tanto el NPZ firmado como su generador.

~~~sh
python -B verificar_insumos.py
~~~

The lightweight test above verifies the SHA256 values in `ORIGEN.tsv`, recomputes the two radius fields of the coercivity argument, checks the inputs to S and P_T, exercises the integer product test for P_T, and reads the Q₂ RC widths from the distributed integer matrix. It was run during preparation. The full integration runs below are the source algorithms; their historical timings are in the record. The long runs were not repeated during editing.

## Profile / Perfil

~~~sh
python -B perfil/paneles.py verificar base 16 14 residuo_nuevo.json --candidato perfil/candidato_M16d14.json
python -B perfil/coercividad.py residuo_nuevo.json perfil/candidato_M16d14.json radio_nuevo.json
~~~

Use the distributed candidate to reproduce its verification with exact fractions. To search for a new candidate, run `python -B perfil/paneles.py generar base 16 14 candidato_nuevo.json` before the two steps above, using the new candidate path in both. Repeated runs may carry different timing fields and hashes even when the mathematics agrees. The downstream generators are pinned to the archived verified inputs.

## S, P_T and Q₂

~~~sh
python -B frontera/certifica_S_perfil.py 64 1048576 base S_malla.json
python -B frontera/autonomo.py S_malla.json S_autonomo.json
python -B pt/pt2048.py PT_nuevo.json
python -B nodo/medir.py completo 16 Q2_nuevo.json
python -B nodo/leer_anchura_rc.py RC_nuevo.json
~~~

The second command applies the six vacancy-factor widening of the assembly proof using rational arithmetic and outward decimal rounding. The P_T supervisor uses the Windows process CPU clock and sets a time limit of 355 seconds. The Q₂ generator verifies both the SHA256 of the finite integer matrix and those of the coefficient and node certificates. Its 17 signed integrand terms are in `intervalos`. `RC_nuevo.json` provides the independent floor for the S13 uncertainty. Historical CPU times were 25.13 s for the S cubature, 111.75 s for P_T and 51.27 s for Q₂.

## Signed model / Modelo firmado

~~~sh
python -B modelo_bivariado/modelo.py 256 base/resultados/candidato_coeficientes.json resolvente/funcional_validado.json GLb_n10 modelo_nuevo.json --modelo modelo_nuevo.npz
~~~

Use fresh paths for both outputs. The stored encoder uses NumPy NPZ and integer endpoints with scale 2⁻²⁰. For cross-platform comparisons, inspect endpoints and metadata rather than ZIP-level byte identity. The original model-generation record reports 21.47 s of CPU. Full historical validation included an independent one-line cross-check; the optional `--linea` comparison is omitted in this replay. The archived primary bounds in `base/resultados/res_nk_4096.json` and `resolvente/funcional_validado.json` are supplied as inputs; this package does not rebuild their earlier proofs.

`ORIGEN.tsv` gives the source and distributed hash of every archived input. Python sources with changed hashes received path-only edits so that their imports and inputs are local. The rational widening script and the quick verification script are new. Scope and output comparisons are documented in the surrounding `REPRODUCIR.md`. The numerical estimate of c remains uncertified.
