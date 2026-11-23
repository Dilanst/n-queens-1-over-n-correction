"""Regla de Gauss en [0,1] por aislamiento racional de todas las raíces."""
from fractions import Fraction as F
from math import comb


def horner_scaled(coef, a, b):
    """b**deg p(a/b), calculado en enteros."""
    val, den = coef[-1], 1
    for c in reversed(coef[:-1]):
        den *= b
        val = val*a + c*den
    return val


def rule(n):
    cf = [(-1)**(n-k)*comb(n,k)*comb(n+k,k) for k in range(n+1)]
    dcf = [k*cf[k] for k in range(1,n+1)]
    den = 4*n*n
    starts = []
    old = cf[0]
    for a in range(1,den+1):
        new = horner_scaled(cf,a,den)
        assert new != 0, "usar orden par"
        if old*new < 0:
            starts.append((a-1,old>0))
        old = new
    assert len(starts) == n
    out = []
    for a, pos in starts:
        b = den
        while b < 2**80:
            a, b = 2*a, 2*b
            val = horner_scaled(cf,a+1,b)
            assert val != 0
            if (val > 0) == pos:
                a += 1
        x0, x1 = F(a,b), F(a+1,b)
        s = F(horner_scaled(dcf,a,b), b**(n-1))
        err = F((n-1)*n*(n+1)*(n+2),2*b)
        assert abs(s) > err
        wl = 1/(x1*(1-x0)*(abs(s)+err)**2)
        wu = 1/(x0*(1-x1)*(abs(s)-err)**2)
        out.append((x0,x1,wl,wu))
    assert sum(q[2] for q in out) <= 1 <= sum(q[3] for q in out)
    return out
