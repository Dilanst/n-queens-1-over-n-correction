# Cuadrado: cuatro casillas 0 = e = (r1,c1), 1 = e' = (r2,c2), 2 = c = (r1,c2), 3 = d = (r2,c1); lineas f0 = {0,1}, f1 = {2,3}.
# Modelo cerrado de lambda (error O(k^-5)) en los datos locales del punto de torres de la mascara:
#   p_i;  G(i,j) = a_i^T G0 a_j  (G_ii = 2 + ga_i;  G_01, G_23 = O(1/k);  G_02, G_03, G_12, G_13 = 1 + n_ij);  x_i = c_i + 1.
# Misma estructura que orden4.py (un par), con matrices 4x4 (casillas) y 2x2 (lineas).  La funcion corre con series
# truncadas (racionales exactos) y con numeros de precision alta.  Sin Monte Carlo.
from series import Ser
PAR = (1, 0, 3, 2); LIN = ((0, 1), (2, 3)); CHI = ((1, 0, 1, 0), (0, 1, 0, 1), (1, 0, 0, 1), (0, 1, 1, 0))   # r1, r2, c1, c2
def inversa(A):
    n = len(A); M = [list(f) + [1 if i == j else 0 for j in range(n)] for i, f in enumerate(A)]; det = 1
    for i in range(n):                                   # Gauss-Jordan sin pivoteo (matrices cercanas a la identidad)
        piv = M[i][i]; det = det*piv; M[i] = [v/piv for v in M[i]]
        for t in range(n):
            if t != i:
                f = M[t][i]; M[t] = [a - f*b for a, b in zip(M[t], M[i])]
    return [f[n:] for f in M], det
def mm(A, B): return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def modelo_cuadrado(p, G, x, log, ptilde):
    tau = lambda d, t: t*(1 - t)/(1 - d*t)
    ell = lambda d, t: (d*log(1 - t) - log(1 - d*t))/2
    ellp = lambda d, t: d*(d - 1)*t/(2*(1 - d*t)*(1 - t))
    kap = lambda d, t: (1 - 2*t + d*t*t)/((1 - d*t)*(1 - d*t))
    pt = [ptilde(p[i], p[PAR[i]]) for i in range(4)]; de = [p[i] - pt[i] for i in range(4)]
    tt = [tau(3, pt[i]) for i in range(4)]; t0 = [tau(2, p[i]) for i in range(4)]; D = [tt[i] - t0[i] for i in range(4)]
    IDG = [[(1 if i == j else 0) + D[i]*G[i][j] for j in range(4)] for i in range(4)]
    W, detW = inversa(IDG); GW = mm(G, W)
    TB = [[tt[i] if i in LIN[f] else 0 for f in range(2)] for i in range(4)]
    h = [1 - p[a] - p[b] for (a, b) in LIN]
    S = [[(h[f] + tt[LIN[f][0]] + tt[LIN[f][1]] if f == g else 0) - sum(TB[i][f]*GW[i][j]*TB[j][g] for i in range(4) for j in range(4))
          for g in range(2)] for f in range(2)]
    Si, detS = inversa(S)
    bv = lambda i: [(1 if i in LIN[f] else 0) - sum(TB[j][f]*GW[j][i] for j in range(4)) for f in range(2)]      # b_i - V^T Gt a_i
    B = [bv(i) for i in range(4)]; sg = [[sum(Si[f][g]*B[i][g] for g in range(2)) for f in range(2)] for i in range(4)]
    Gh = [[GW[j][i] + sum(B[j][f]*sg[i][f] for f in range(2)) for j in range(4)] for i in range(4)]
    E0 = sum(3*pt[i] + 2*log(1 - pt[i]) - 2*p[i] - log(1 - p[i]) for i in range(4)) - sum((1 - h[f]) + log(h[f]) for f in range(2))
    ee = sum(de[i]*de[j]*Gh[i][j] for i in range(4) for j in range(4))/2
    II = sum(ell(3, pt[i]) - ell(2, p[i]) for i in range(4)) - log(detW)/2 - log(detS)/2
    g = [tt[i]*(ellp(3, pt[i]) - kap(3, pt[i])*Gh[i][i]/2) for i in range(4)]
    g0 = [t0[i]*(ellp(2, p[i]) - kap(2, p[i])*G[i][i]/2) for i in range(4)]
    gw = [-h[f]*Si[f][f]/2 for f in range(2)]
    WTB = mm(W, TB)
    Q = [[-W[i][j]*D[j] + sum(WTB[i][f]*Si[f][g_]*WTB[j][g_] for f in range(2) for g_ in range(2)) for j in range(4)] for i in range(4)]
    TT = [sum(sum(c[i]*Q[i][j]*c[j] for i in range(4) for j in range(4))*c[t] for c in CHI) for t in range(4)]
    vec = [(x[j] - 1) + sum(G[j][t]*(g[t] - g0[t]) for t in range(4)) - TT[j]/2 for j in range(4)]
    lin = [g[LIN[f][0]] + g[LIN[f][1]] + gw[f] for f in range(2)]
    ch = []
    for i in range(4):
        r = [(1 if t == i else 0) - sum(TB[t][f]*sg[i][f] for f in range(2)) for t in range(4)]
        m = [sum(W[t][u]*r[u] for u in range(4)) for t in range(4)]
        ch.append(sum(m[t]*vec[t] for t in range(4)) + sum(sg[i][f]*lin[f] for f in range(2)))
    A = p[0]*p[1]; Bp = p[2]*p[3]
    III = sum(de[i]*ch[i] for i in range(4)) + 2*A*A + 2*Bp*Bp + 2*A*Bp
    return dict(lam=E0 - ee + II + III, E0=E0, ee=ee, II=II, III=III)
NOM = ('p0', 'p1', 'p2', 'p3', 'a0', 'a1', 'a2', 'a3', 'n02', 'n03', 'n12', 'n13', 'g01', 'g23', 'x0', 'x1', 'x2', 'x3')
def variables():
    Ser.NV = 18; v = [Ser.var(i) for i in range(18)]; p = v[0:4]; a = v[4:8]; n02, n03, n12, n13, g01, g23 = v[8:14]; x = v[14:18]
    G = [[2 + a[0], g01, 1 + n02, 1 + n03], [g01, 2 + a[1], 1 + n12, 1 + n13], [1 + n02, 1 + n12, 2 + a[2], g23], [1 + n03, 1 + n13, g23, 2 + a[3]]]
    return p, a, G, x, g01, g23
def ptilde_ser(p, q):
    rhs = p*(1 - p)*(1 - p - q); t = rhs
    for _ in range(Ser.N + 1): t = rhs/((1 - t)*(1 - t))
    return t
if __name__ == '__main__':
    import time
    from orden4 import modelo
    Ser.N = 4; p, a, G, x, g01, g23 = variables(); t0 = time.time()
    lg = lambda s: Ser.de(s).log()
    S = modelo_cuadrado(p, G, x, lg, ptilde_ser)
    P0 = modelo(p[0], p[1], a[0], a[1], g01, x[0], x[1], lg, ptilde_ser); P1 = modelo(p[2], p[3], a[2], a[3], g23, x[2], x[3], lg, ptilde_ser)
    N = S['lam'] - P0['lam'] - P1['lam']
    for d in range(5): print(f'no aditividad del predictor, N_lambda = lambda(cuadrado) - lambda(par 01) - lambda(par 23), grado {d}:', N.grado(d).texto(NOM))
    print(f'[{time.time() - t0:.0f} s]')
