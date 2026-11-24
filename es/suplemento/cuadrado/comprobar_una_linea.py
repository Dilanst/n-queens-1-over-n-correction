"""Comprueba el Taylor local de H.3 con coeficientes racionales y grado total cuatro."""

from fractions import Fraction

from orden4 import simbolico


def main():
    # Orden de los exponentes en el modelo: p, q, a, b, g, x, y.
    expresiones = simbolico(4)
    calculado = (expresiones["lam"] - expresiones["prim"]).c
    esperado = {
        (2, 2, 0, 0, 0, 0, 0): Fraction(-1, 2),
        (2, 1, 0, 0, 1, 0, 0): Fraction(1),
        (1, 2, 0, 0, 1, 0, 0): Fraction(1),
    }
    if calculado != esperado:
        diferencias = {exp: calculado.get(exp, 0) - esperado.get(exp, 0)
                       for exp in calculado.keys() | esperado.keys()
                       if calculado.get(exp, 0) != esperado.get(exp, 0)}
        raise SystemExit(f"Discrepancia racional en H.3: {diferencias}")
    print("Grados 0 a 3 nulos. Grado 4: -p^2*q^2/2 + p*q*(p+q)*g.")


if __name__ == "__main__":
    main()
