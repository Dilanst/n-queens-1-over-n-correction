# Series de potencias truncadas en varias variables, con coeficientes racionales exactos (biblioteca estandar).
# Sirve para desarrollar expresiones cerradas en los datos locales del par hasta un grado total dado.
# Sin Monte Carlo.
from fractions import Fraction
class Ser:
    NV = 7; N = 4                                  # numero de variables y grado total maximo que se conserva
    __slots__ = ('c',)
    def __init__(self, c=None): self.c = {} if c is None else {k: v for k, v in c.items() if v != 0 and sum(k) <= Ser.N}
    @staticmethod
    def cte(x): return Ser({(0,)*Ser.NV: Fraction(x)})
    @staticmethod
    def var(i): return Ser({tuple(1 if j == i else 0 for j in range(Ser.NV)): Fraction(1)})
    @staticmethod
    def de(x): return x if isinstance(x, Ser) else Ser.cte(x)
    def c0(self): return self.c.get((0,)*Ser.NV, Fraction(0))
    def __add__(self, o):
        o = Ser.de(o); r = dict(self.c)
        for k, v in o.c.items(): r[k] = r.get(k, 0) + v
        return Ser(r)
    __radd__ = __add__
    def __neg__(self): return Ser({k: -v for k, v in self.c.items()})
    def __sub__(self, o): return self + (-Ser.de(o))
    def __rsub__(self, o): return Ser.de(o) - self
    def __mul__(self, o):
        o = Ser.de(o); r = {}
        for k1, v1 in self.c.items():
            s1 = sum(k1)
            for k2, v2 in o.c.items():
                if s1 + sum(k2) > Ser.N: continue
                k = tuple(a + b for a, b in zip(k1, k2)); r[k] = r.get(k, 0) + v1*v2
        return Ser(r)
    __rmul__ = __mul__
    def inv(self):
        a = self.c0(); assert a != 0; u = self*(Fraction(1)/a) - 1; r = Ser.cte(1); t = Ser.cte(1)
        for _ in range(Ser.N): t = -(t*u); r = r + t
        return r*(Fraction(1)/a)
    def __truediv__(self, o): return self*Ser.de(o).inv()
    def __rtruediv__(self, o): return Ser.de(o)*self.inv()
    def __pow__(self, n):
        r = Ser.cte(1)
        for _ in range(n): r = r*self
        return r
    def log(self):
        assert self.c0() == 1; u = self - 1; r = Ser(); t = Ser.cte(1)
        for j in range(1, Ser.N + 1): t = t*u; r = r + t*Fraction((-1)**(j + 1), j)
        return r
    def grado(self, d): return Ser({k: v for k, v in self.c.items() if sum(k) == d})
    def hasta(self, d): return Ser({k: v for k, v in self.c.items() if sum(k) <= d})
    def es_cero(self): return not self.c
    def valor(self, xs):                           # evaluacion numerica en numeros cualesquiera (Decimal, float...)
        tot = 0
        for k, v in self.c.items():
            t = xs[0]**0*v.numerator/type(xs[0])(v.denominator) if not isinstance(xs[0], float) else float(v)
            for x, e in zip(xs, k):
                if e: t = t*x**e
            tot = tot + t
        return tot
    def texto(self, nombres):
        def mon(k): return '*'.join(n if e == 1 else f'{n}^{e}' for n, e in zip(nombres, k) if e) or '1'
        ts = sorted(self.c.items(), key=lambda kv: (sum(kv[0]), tuple(-x for x in kv[0])))
        return ' '.join(f"{'+' if v > 0 else '-'} {abs(v)}*{mon(k)}" if abs(v) != 1 or not any(k) else f"{'+' if v > 0 else '-'} {mon(k)}"
                        for k, v in ts) or '0'
