"""Barras continuas de I, xI', V, xV' en los nodos reales de Gauss.

Uso: python -B funcional.py <piloto_nodal.tar.gz> <constantes_iv.json> [--guardar salida.json]
Sólo se reutilizan los certificados p1 del piloto y las constantes B20.
"""
import argparse
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING, localcontext
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import tarfile
import time


def dec(q, arriba):
    with localcontext() as c:
        c.prec = 20
        c.rounding = ROUND_CEILING if arriba else ROUND_FLOOR
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def caja(lo, hi):
    assert lo <= hi
    return [dec(lo, False), dec(hi, True)]


def legendre(n, t):
    antes, actual = F(1), t
    for k in range(2, n + 1):
        antes, actual = actual, ((2*k - 1)*t*actual - (k-1)*antes) / k
    return actual


def escalado(n, x):
    a, b = (F("0.03"), F("0.06")) if n == 6 else (F("0.06"), F(1))
    return legendre(n, (2*x-a-b)/(b-a))


def encierra_gamma(x, umin, norm_b):
    ell = x * (1-umin) / (umin + x*(1-umin))
    izquierda, derecha = F(0), F(1)
    # Cualquier eta es admisible. La bisección sólo selecciona una racional.
    for _ in range(32):
        eta = (izquierda+derecha)/2
        t1 = 1 - ell*(2/eta-1)
        t2 = (1-eta)*(1-norm_b)
        if t1 < t2:
            izquierda = eta
        else:
            derecha = eta
    return min(t1, t2)


def envolvente(p1, n, x, a, b, umin, norm_b, nu):
    assert escalado(n, a) * escalado(n, b) < 0
    filas = p1["filas"]
    fib0, fib1 = filas["fib"]["certificado"]
    th0, th1 = filas["Theta"]["certificado"]
    d0, d1 = 3*fib0 - th1, 3*fib1 - th0
    assert d0 > 0
    rac = (b/a)**8
    dm, dM = d0/rac, d1*rac
    gamma = encierra_gamma(b, umin, norm_b)
    assert gamma > 0
    i0 = dm/4
    i1 = 3*dM/gamma
    dI = 3*dM*(5/gamma + 3/gamma**2)
    t11 = filas["I2"]["certificado"][1]
    pos = (4*t11 + F(3,2)*d1 + F(9,4)*fib1)*rac
    delta = max(x-a,b-x)
    E = 8*pos*delta/a
    Ed = 72*pos*delta/a**2
    deriv = p1["derivadas_de_filas"]
    ve0, ve1 = deriv["V_expl = 4T1 - 1.5Theta + 2.25fib"]
    ved0, ved1 = deriv["V_expl_d"]
    v0, v1 = ve0-E-F(3,2)*i1, ve1+E-F(3,2)*i0
    extremos_der = [xe * de for xe in (a,b) for de in (ved0-Ed, ved1+Ed)]
    xv0, xv1 = min(extremos_der)-F(3,2)*dI, max(extremos_der)+F(3,2)*dI
    return {
        "x_almacenado": float(x).hex(), "x_GL": caja(a,b),
        "D": caja(dm, dM), "gamma_min": dec(gamma, False),
        "I": caja(i0, i1), "xI_prima": caja(-dI, dI),
        "V": caja(v0, v1), "xV_prima": caja(xv0,xv1),
        "V_menos_xV_prima": caja(v0-xv1,v1-xv0),
        "L0_modulo_sup": dec(F(3,2) + 3*nu/gamma, True),
        "Q2_modulo_sup": dec(q2_real(a,b,gamma,umin,nu), True),
    }


def raiz_sup(q):
    escala = 10**30
    entero = isqrt((q.numerator * escala**2)//q.denominator)
    return F(entero+1, escala)


def q2(p, pk, kap, lam):
    """Recuento del segundo término, parte_05.tex, con parámetros positivos."""
    a1 = 96*kap*p**2 + p
    gk = p*(6*kap+1)
    gu = 6*kap*p
    c0 = 16*p**2 + F(1,2) + a1 + 4*((p+F(1,2))**2 + 6*p**2 + gk*(p+F(1,2)))
    a2 = 2*p**2
    p_k = 8*p + F(1,2) + gu + gk
    t = c0**2 + 4*(2*a2*(2*p+F(1,2))*p_k+a2**2) + pk**2*(256*p**2+8*a2)
    return (6*lam)**2*t/4


def q2_real(a, b, gamma, umin, nu):
    # 0 < a <= x <= b < 1. K <= nu, int K rho <= 3, U <= 1.
    u = umin+a*(1-umin)
    w = nu/u**2
    l0 = F(3,2)+3*nu/gamma
    theta = 3*w+3*nu
    p = l0+nu+w+theta+1
    return q2(p, nu, nu, 1/a)


def circulo(r, umin, norm_b, nu, fila_nu2):
    m = 1-umin
    u = umin - r*m
    sigma_inv = 1 - r*2*m/umin
    assert sigma_inv > 0 and u > 0
    # U+ <= 1 al ser U=u_f + x(1-u_f), u_f en [0,1], |x| < 1.
    s, a, n = 1/(sigma_inv*umin), 1/(1-norm_b), 2*raiz_sup(m)
    alpha = raiz_sup((a+r*a**2*n**2*s)**2+(a*n*s)**2+(r*a*n*s)**2+s**2)
    z = r/u
    k2 = max(fila_nu2*(1+2*z*z), nu*m*(2*z*z+z**4))
    kt2 = max(3*fila_nu2, 3*nu*m*z*z)
    kk = raiz_sup(k2*kt2)
    pk = nu*max(1,z,z*z)
    w = nu/u**2
    phi_f = max(1,r*m/u)
    l0 = F(3,2)+kk*alpha
    theta = 3*w*phi_f+kk
    p = l0 + pk + w + theta + 1
    return {"radio":str(r), "L0_modulo_sup":dec(l0,True),
            "Q2_modulo_sup":dec(q2(p,pk,nu*max(1,z),1/r),True)}


def constantes(ct, exactos):
    # El histórico empleó 4.37e-11 en u. Se proyecta u* a la banda
    # archivada antes de propagar el exceso a nu, B y la integral de nu².
    du = max(F(0), exactos["eps_u"]-ct["eps_u"])
    assert exactos["eps_S"] <= ct["eps_S"]
    dn = ct["S"][1]**2 * du*(2*ct["u"][1]+du)
    u, nb, nu, fila = F(".174"), F(".164"), F("1.405"), F("1.10")
    assert u <= ct["u"][0]-du
    assert nb >= ct["normB_HS_sup"]+dn
    assert nu >= ct["nu"][1]+dn
    assert fila >= ct["sup_r_int_nu2_dq"]+dn*(2*ct["nu"][1]+dn)
    return u, nb, nu, fila, du, dn


def json_binario(datos):
    # Los extremos del piloto se serializaron desde binary64. Recuperarlos
    # con su valor binario exacto, también cuando sólo figuran 15 decimales.
    return json.loads(datos, parse_float=lambda s: F.from_float(float(s)))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("piloto", type=Path)
    p.add_argument("constantes_p5", type=Path)
    p.add_argument("--guardar", type=Path)
    opt = p.parse_args()
    t0 = time.process_time()
    resultados, huellas = {}, {}
    with tarfile.open(opt.piloto, "r:gz") as tar:
        def lee(nombre):
            archivo = tar.extractfile("piloto_nodal/"+nombre)
            datos = archivo.read()
            huellas[nombre] = hashlib.sha256(datos).hexdigest()
            return json_binario(datos)
        raw = opt.constantes_p5.read_bytes()
        huellas["p5/constantes_iv.json"] = hashlib.sha256(raw).hexdigest()
        c = json_binario(raw)
        param = lee("nodo_GLb_n10/p1_explicitas.json")["meta"]["parametros"]
        u, nb, nu, fila_nu2, du, dn = constantes(c,param)
        for n, grupo in ((6, "GL6"), (20, "GLb")):
            ultimo = F(0)
            for j in range(1, n+1):
                tag = f"{grupo}_n{j:02}"
                p1 = lee(f"nodo_{tag}/p1_explicitas.json")
                x = p1["meta"]["parametros"]["x0"]
                a, b = x-F("1e-15"), x+F("1e-15")
                assert ultimo < a < b < 1
                ultimo = b
                resultados[tag] = envolvente(p1, n, x, a, b, u, nb, nu)
    # n intervalos disjuntos con cambio de signo agotan las n raíces.
    assert len(resultados) == 26
    salida = {"entradas_sha256": huellas, "aritmetica": "racional exacta tras leer binary64",
              "constantes_corregidas": {"u_min": str(u), "normB_sup": str(nb),
                "nu_sup": str(nu), "sup_r_integral_nu2": str(fila_nu2),
                "exceso_eps_u_sup": dec(du,True), "delta_nu_sup":dec(dn,True)},
              "circulo_32_muestras_17_por_conjugacion":circulo(F(3,100),u,nb,nu,fila_nu2),
              "nodos": resultados, "cpu_s": time.process_time()-t0}
    assert salida["cpu_s"] < 300
    if opt.guardar:
        with opt.guardar.open("x", encoding="utf-8") as archivo:
            json.dump(salida, archivo, indent=2, ensure_ascii=False)
            archivo.write("\n")
    else:
        print(json.dumps(salida, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
