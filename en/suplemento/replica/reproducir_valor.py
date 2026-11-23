"""Reejecuta el análisis archivado sobre sus datos finitos. El directorio de salida debe ser nuevo."""
import argparse
import json
import math
import sys
from pathlib import Path

sys.dont_write_bytecode = True
base = Path(__file__).resolve().parent
sys.path.insert(0, str(base / "analizador"))
import analiza_v3b as motor


def leer(ruta):
    return json.loads(ruta.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("salida", type=Path)
    args = parser.parse_args()
    args.salida.mkdir(parents=False, exist_ok=False)
    config = leer(base / "analizador/malla_local_v3/config.json")
    extra = leer(base / "datos_malla/config_v3b.json")
    grupo_extra = next(g for g in extra["grupos"] if g["nombre"] == "muestras_c")
    grupo = next(g for g in config["grupos"] if g["nombre"] == "muestras_c")
    if grupo_extra["puntos"] != grupo["puntos"]:
        raise ValueError("Los puntos de las dos configuraciones difieren")
    grupo["mallas"] = grupo_extra["mallas"]
    lineas, resultado = motor.analizar(str(base / "datos_malla/v3.json"), config,
                                      str(args.salida), extra=[str(base / "datos_malla/v3b.json")])
    motor.guardar(lineas, resultado, str(args.salida), "replica")
    archivo = leer(base.parent / "datos/analisis_v3b.json")
    # El orden de redondeo de los mínimos cuadrados y la FFT puede variar entre bibliotecas BLAS.
    actual = resultado["nuevo"]["c"]
    objetivo = archivo["nuevo"]["c"]
    for valor, referencia, tolerancia in (
        (actual, objetivo, 1e-10),
        (resultado["certificacion"]["serie"]["total"], archivo["certificacion"]["serie"]["total"], 2e-12),
        (resultado["certificacion"]["panel"]["total"], archivo["certificacion"]["panel"]["total"], 2e-12),
    ):
        if not math.isclose(valor, referencia, abs_tol=tolerancia, rel_tol=0.):
            raise ArithmeticError((valor, referencia, tolerancia))
    print(f"c [N] = {actual:.10f}; referencia = {objetivo:.10f}")
    print("El control mide reproducibilidad del análisis [N]. Las tolerancias nodales siguen abiertas.")


if __name__ == "__main__":
    main()
