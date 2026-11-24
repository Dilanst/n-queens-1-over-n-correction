# Termino de orden k^-4 de lambda para un par aislado {e, e'}: modelo cerrado en los datos locales
#   p, q = p0_e, p0_e';  a = G(e,e) - 2;  b = G(e',e') - 2;  g = G(e,e');  x = c_e + 1;  y = c_e' + 1
# (c_e = a_e^T G0 grad Lambda_T(z0)).  El modelo es lambda con error O(k^-5):
#   lambda = E0(p,q) - ee + [Lambda(y0) - Lambda_T(z0)] + delta_e chat^_e + delta_e' chat^_e' + 2 p^2 q^2 + O(k^-5),
# con todas las piezas exactas en los datos locales, salvo las sumas cubicas en las casillas, que entran a orden
# principal.  La misma funcion corre con series truncadas (racionales exactos) y con numeros de precision alta.
# Sin Monte Carlo.
from series import Ser
def modelo(p, q, a, b, g, x, y, log, ptilde):
    tau = lambda d, t: t*(1 - t)/(1 - d*t)
    ell = lambda d, t: (d*log(1 - t) - log(1 - d*t))/2
    ellp = lambda d, t: d*(d - 1)*t/(2*(1 - d*t)*(1 - t))
    kap = lambda d, t: (1 - 2*t + d*t*t)/((1 - d*t)*(1 - d*t))
    pe = ptilde(p, q); pf = ptilde(q, p); de = p - pe; df = q - pf
    te = tau(3, pe); tf = tau(3, pf); t0e = tau(2, p); t0f = tau(2, q); De = te - t0e; Df = tf - t0f
    G11 = 2 + a; G22 = 2 + b; G12 = g
    m11 = 1 + De*G11; m12 = De*G12; m21 = Df*G12; m22 = 1 + Df*G22; det = m11*m22 - m12*m21
    i11 = m22/det; i12 = -m12/det; i21 = -m21/det; i22 = m11/det                  # (I + D G)^-1
    Gt11 = G11*i11 + G12*i21; Gt12 = G11*i12 + G12*i22; Gt22 = G12*i12 + G22*i22   # G (I + D G)^-1 (simetrica)
    h = 1 - p - q
    S = h + te + tf - (te*te*Gt11 + 2*te*tf*Gt12 + tf*tf*Gt22)
    se = (1 - (Gt11*te + Gt12*tf))/S; sf = (1 - (Gt12*te + Gt22*tf))/S
    Ghee = Gt11 + se*se*S; Ghef = Gt12 + se*sf*S; Ghff = Gt22 + sf*sf*S
    E0 = (3*pe + 2*log(1 - pe) - 2*p - log(1 - p)) + (3*pf + 2*log(1 - pf) - 2*q - log(1 - q)) - (p + q) - log(1 - p - q)
    ee = (de*de*Ghee + 2*de*df*Ghef + df*df*Ghff)/2
    II = (ell(3, pe) - ell(2, p)) + (ell(3, pf) - ell(2, q)) - log(det)/2 - log(S)/2
    ge = te*(ellp(3, pe) - kap(3, pe)*Ghee/2); gf = tf*(ellp(3, pf) - kap(3, pf)*Ghff/2)
    g0e = t0e*(ellp(2, p) - kap(2, p)*G11/2); g0f = t0f*(ellp(2, q) - kap(2, q)*G22/2)
    gw = -h/(2*S)
    n1 = i11*te + i12*tf; n2 = i21*te + i22*tf
    Q11 = -i11*De + n1*n1/S; Q22 = -i22*Df + n2*n2/S
    me1 = i11*(1 - se*te) - i12*se*tf; me2 = i21*(1 - se*te) - i22*se*tf
    mf1 = -i11*sf*te + i12*(1 - sf*tf); mf2 = -i21*sf*te + i22*(1 - sf*tf)
    v1 = (x - 1) + G11*(ge - g0e) + G12*(gf - g0f) - Q11
    v2 = (y - 1) + G12*(ge - g0e) + G22*(gf - g0f) - Q22
    che = me1*v1 + me2*v2 + se*(ge + gf + gw); chf = mf1*v1 + mf2*v2 + sf*(ge + gf + gw)
    III = de*che + df*chf + 2*p*p*q*q
    lam = E0 - ee + II + III
    chat_e = ((1 - p)/(1 - 2*p))*(ellp(2, p) - kap(2, p)*G11/2 - (x - 1))
    chat_f = ((1 - q)/(1 - 2*q))*(ellp(2, q) - kap(2, q)*G22/2 - (y - 1))
    prim = -p*q*(1 - g + chat_e + chat_f)
    return dict(lam=lam, prim=prim, E0=E0, ee=ee, II=II, III=III, de=de, df=df, che=che, chf=chf, S=S, chat_e=chat_e, chat_f=chat_f)
NOM = ('p', 'q', 'a', 'b', 'g', 'x', 'y')
def simbolico(N=4):
    Ser.N = N; Ser.NV = 7
    p, q, a, b, g, x, y = [Ser.var(i) for i in range(7)]
    def ptilde(p, q):
        rhs = p*(1 - p)*(1 - p - q); t = rhs
        for _ in range(N + 1): t = rhs/((1 - t)*(1 - t))
        return t
    return modelo(p, q, a, b, g, x, y, lambda s: Ser.de(s).log(), ptilde)
if __name__ == '__main__':
    m = simbolico(4); R = m['lam'] - m['prim']
    for d in range(0, 4): print(f'grado {d} de lambda - primer orden:', R.grado(d).texto(NOM))
    print('Lambda_4 =', R.grado(4).texto(NOM))
    print('lambda hasta grado 3 =', m['lam'].hasta(3).texto(NOM))
    for k in ('E0', 'ee', 'II', 'III'): print(k, 'grado 4:', m[k].grado(4).texto(NOM))
    print('chat^_e hasta grado 2 =', m['che'].hasta(2).texto(NOM))
    print('delta_e hasta grado 4 =', m['de'].hasta(4).texto(NOM))
    print('S hasta grado 3 =', m['S'].hasta(3).texto(NOM))
    print('lambda_H = E0 - ee hasta grado 4 =', (m['E0'] - m['ee']).hasta(4).texto(NOM))
    print('II hasta grado 4 =', m['II'].hasta(4).texto(NOM))
    print('III hasta grado 4 =', m['III'].hasta(4).texto(NOM))
    # Control independiente del desarrollo: el modelo evaluado con 60 cifras en puntos t*v, t -> 0.
    from decimal import Decimal, getcontext
    getcontext().prec = 60
    def ptil(p, q):
        la = (p*(1 - p)*(1 - p - q)).ln(); t = p
        for _ in range(200):
            dt = -(t.ln() + 2*(1 - t).ln() - la)*t*(1 - t)/(1 - 3*t); t += dt
            if abs(dt) < Decimal(10)**-55: break
        return t
    L4 = R.grado(4)
    for v in ((1, 1, -3, -3, -1, 2, 2), (2, 1, 1, -2, 3, -1, 4), (1, 3, 2, 5, -2, 3, -1)):
        fila = []
        for j in range(3, 8):
            t = Decimal(1)/Decimal(10*2**j); xs = [Decimal(c)*t for c in v]
            mm = modelo(*xs, lambda z: Decimal(z).ln(), ptil)
            fila.append((mm['lam'] - mm['prim'] - L4.valor(xs))/t**5)
        print('control numerico, direccion', v, ': [modelo - primer orden - Lambda_4]/t^5 =', ', '.join(format(float(z), '+.5f') for z in fila))
