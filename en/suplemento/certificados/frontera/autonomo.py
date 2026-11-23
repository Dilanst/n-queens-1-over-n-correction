"""Convert S from the cubic integration to the autonomous profile enclosure."""
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as F
import json
import sys
from pathlib import Path


def main():
    source, destination = map(Path, sys.argv[1:])
    sample = json.loads(source.read_bytes())
    floor = F("0.17")
    eps = F("3.751e-14")
    change = eps - F(sample["eps_vacancia"])
    assert F(sample["minimos_candidato"][1]) - eps > floor and change > 0
    low, high = map(F, sample["S"])
    bounds = (low * (1 - change / floor)**6, high * (1 + change / floor)**6)
    with localcontext() as ctx:
        ctx.prec = 38
        result = []
        for value, rounding in zip(bounds, (ROUND_FLOOR, ROUND_CEILING)):
            ctx.rounding = rounding
            result.append(str(Decimal(value.numerator) / Decimal(value.denominator)))
    with destination.open("x", encoding="utf8") as handle:
        json.dump({"S_autonomo": result}, handle, indent=2)


if __name__ == "__main__":
    main()
