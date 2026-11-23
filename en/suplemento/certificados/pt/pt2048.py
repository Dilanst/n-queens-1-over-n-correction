"""P_T únicamente. Ejecutar en Windows: python -B pt2048.py salida_nueva.json"""
import ctypes
from ctypes import wintypes as wt
from fractions import Fraction as Q
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "BLIS_NUM_THREADS"):
    os.environ[key] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"


def supervise(dest):
    if dest.exists():
        raise FileExistsError(dest)
    get_times = ctypes.windll.kernel32.GetProcessTimes
    get_times.argtypes = [wt.HANDLE] + [ctypes.POINTER(wt.FILETIME)] * 4
    with subprocess.Popen([sys.executable, "-B", __file__, "--worker", str(dest)]) as proc:
        while proc.poll() is None:
            stamps = [wt.FILETIME() for _ in range(4)]
            if not get_times(proc._handle, *(ctypes.byref(t) for t in stamps)):
                proc.kill()
                raise ctypes.WinError()
            cpu = sum(t.dwLowDateTime + (t.dwHighDateTime << 32) for t in stamps[2:]) / 1e7
            if cpu >= 355:
                proc.kill()
                raise TimeoutError("Tope de CPU con margen de cinco segundos")
            time.sleep(0.25)
        return proc.returncode


if __name__ == "__main__" and sys.argv[1] != "--worker":
    raise SystemExit(supervise(Path(sys.argv[1])))

sys.path.insert(0,str(BASE / "torres"))
import cajas as c
import numpy as np
from threadpoolctl import threadpool_info

I, Dual, rat = c.I, c.Dual, c.rat
MAX_PARTIAL = 0
MAX_SUM = 0


def quantize(interval):
    peak = float(np.max(interval.cap()))
    exponent = 20 - math.frexp(max(peak, 2.0**-100))[1]
    scale = 2.0**exponent
    center = np.rint((interval.l * .5 + interval.h * .5) * scale)
    radius = np.ceil(c.up(np.maximum(center - interval.l * scale, interval.h * scale - center)))
    cap = int(np.max(abs(center) + radius))
    assert cap <= 2**21
    return center, radius, exponent, cap


def conv(a, b):
    global MAX_PARTIAL, MAX_SUM
    n = a.l.shape[-1]
    assert n == b.l.shape[0] and n > 0 and n & (n-1) == 0
    ac, ar, ea, ca = quantize(a)
    bc, br, eb, cb = quantize(b)
    total_bound = n * ca * cb
    assert total_bound <= 2**53
    MAX_SUM = max(MAX_SUM, total_bound)
    blo = bhi = None
    for i in range(0, n, 1024):
        sl = slice(i, min(i + 1024, n))
        partial_bound = (sl.stop-sl.start) * ca * cb
        assert partial_bound <= 2**52
        MAX_PARTIAL = max(MAX_PARTIAL, partial_bound)
        left, left_rad = ac[..., sl], ar[..., sl]
        right, right_rad = bc[sl], br[sl]
        center = left @ right
        rad = abs(left) @ right_rad + left_rad @ (abs(right) + right_rad)
        lo, hi = center - rad, center + rad
        if blo is None:
            blo, bhi = lo, hi
        else:
            blo += lo
            bhi += hi
    factor = 2.0**(-ea-eb) / n
    assert 2.0**-1022 <= factor <= 2.0**960
    return I(blo * factor, bhi * factor)


def control():
    # Contra los extremos racionales de una reducción con n=2048 y signos mixtos.
    n = 2048
    i = np.arange(n)
    left = I(np.array([i % 7 - 3, i % 11 - 5.]) / 8,
             np.array([i % 7 - 2, i % 11 - 3.]) / 8)
    right = I(np.array([i % 5 - 5, i % 13 - 6.]).T / 16,
              np.array([i % 5 - 3, i % 13 - 5.]).T / 16)
    prod = conv(left, right)
    for a in range(2):
        for b in range(2):
            low = high = 0
            for k in range(n):
                products = [int(x[a,k]*8)*int(y[k,b]*16)
                            for x in (left.l,left.h) for y in (right.l,right.h)]
                low += min(products)
                high += max(products)
            assert Q(float(prod.l[a,b])) <= Q(low, 128*n) <= Q(high,128*n) <= Q(float(prod.h[a,b]))


def endpoints(iv):
    scale = 10**15
    out = []
    for x, rounding in ((iv.l, math.floor), (iv.h, math.ceil)):
        t = rounding(Q(float(x)) * scale)
        out.append(("-" if t < 0 else "") + f"{abs(t)//scale}.{abs(t)%scale:015d}")
    return out


def run(n=2048, order=14):
    s, u, W, hashes = c.perfil(n)
    assert hashes["cajas.py"] == "1b3c5ba63a6594ffbd6dbd5740fab3a56b43360d1d193269667d0545917404b3"
    i, j = np.ogrid[:n, :n]
    q = np.abs(i-j)
    d = c.span(u, np.maximum(q-1, 0), q)
    a = c.span(u, 2*n-i-j-2, 2*n-i-j-1)
    p = s[:,None] * s[None,:] * d * a
    z = p-1
    gamma = d.reciprocal() + a.reciprocal() - 2
    eta = 2*W - (p*gamma).avg(1)
    del q, d, a, gamma
    rho = Q(float(np.max(I(z.cap()).avg(1).h)))
    b = Q(float(np.max(z.cap())))
    assert rho < 1
    term = eta
    v = I(np.zeros(n))
    for k in range(1, order+1):
        term = -conv(z, term)
        v += term
    v = v.widen(rat(Q(float(np.max(eta.cap())))*rho**(order+1)/(1-rho)).h)
    zd = p*(v[:,None]+v[None,:])
    del p
    density = (eta[:,None]+eta[None,:])*.5
    D = zd + z*density
    Cpow, Dpow = z, D
    zero = I(np.zeros((n,n)))
    T = [zero, zero]
    U = [zero, zero]
    J = [I(np.zeros(n))]*2
    for k in range(2, order+1):
        old = Cpow
        Cpow = conv(z, old)
        Dpow = conv(D, old) + conv(z, Dpow)
        for ix, val in enumerate([Cpow, Dpow]):
            if k % 2:
                U[ix] += val
            else:
                T[ix] += val
                if k >= 4:
                    J[ix] += val.diag()
    tails = [b*rho**order/(1-rho),
             Q(float(np.max(D.cap())))*rho**order*(order+1-order*rho)/(1-rho)**2]
    del D, old, Cpow, Dpow, val, zero
    for ix, err in enumerate(tails):
        for arr in (T,U,J):
            arr[ix] = arr[ix].widen(rat(err).h)
    tt = Dual(T[0], T[1]-T[0]*density)
    uu = Dual(U[0], U[1]-U[0]*density)
    jj = Dual(J[0], J[1]-J[0]*eta)
    del T, U, J, density
    fd = c.F(Dual(z, zd), tt, uu, jj, Dual(I(np.ones(n)),eta))
    pt = (rat(Q(1,6))-2*fd.v)*W-fd.d
    bounds = endpoints(pt)
    return dict(n=n, orden=order, P_T=bounds, semiancho=str((Q(bounds[1])-Q(bounds[0]))/2),
                W=endpoints(W), F0=endpoints(fd.v), delta_F=endpoints(fd.d),
                contraccion=endpoints(rat(rho)), colas_superiores=[endpoints(rat(e))[1] for e in tails],
                sha256=hashes)


if __name__ == "__main__":
    start = time.perf_counter()
    pools = threadpool_info()
    assert pools and all(pool["num_threads"] == 1 for pool in pools)
    ctl = time.process_time()
    control()
    ctl = time.process_time() - ctl
    result = run()
    result.update(control_2x2048x2_cpu_s=ctl, max_cota_parcial_entera=MAX_PARTIAL,
                  max_cota_total_entera=MAX_SUM, hilos=1, numpy=np.__version__, python=sys.version,
                  script_sha256=c.sha(Path(__file__)), cpu_s=time.process_time(),
                  pared_desde_control_s=time.perf_counter()-start)
    assert result["cpu_s"] < 355
    with Path(sys.argv[2]).open("x",encoding="utf-8") as fp:
        json.dump(result,fp,indent=2,ensure_ascii=False)
    print(json.dumps(result))
