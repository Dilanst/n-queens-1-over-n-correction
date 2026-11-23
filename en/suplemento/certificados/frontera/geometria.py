"""Partición poliédrica racional de un octavo del dominio de cuadrados."""
from fractions import Fraction as F
from itertools import combinations


def linear(p, form):
    return sum(x * y for x, y in zip(p, form)) + form[3]


def determinant(a, b, c, d):
    u, v, w = [[t - s for t, s in zip(row, a)] for row in (b, c, d)]
    return sum(u[i] * (v[(i+1)%3] * w[(i+2)%3] - v[(i+2)%3] * w[(i+1)%3])
               for i in range(3))


def hull(points):
    """Ciclo de vértices extremos de un polígono plano, en orden de borde."""
    if len(points) < 3:
        return []
    for i, j in combinations(range(3), 2):
        ordered = sorted(points, key=lambda p: (p[i], p[j]))
        def cross(a, b, c):
            return (b[i]-a[i])*(c[j]-a[j]) - (b[j]-a[j])*(c[i]-a[i])
        if all(cross(ordered[0], ordered[-1], p) == 0 for p in ordered):
            continue
        def half(seq):
            out = []
            for p in seq:
                while len(out) > 1 and cross(out[-2], out[-1], p) <= 0:
                    out.pop()
                out.append(p)
            return out
        return half(ordered)[:-1] + half(reversed(ordered))[:-1]
    return []


def split(faces, form):
    vals = {p: linear(p, form) for face in faces for p in face}
    if min(vals.values()) >= 0 or max(vals.values()) <= 0:
        return [faces]
    out = [[], []]
    section = {p for p, val in vals.items() if val == 0}
    for face in faces:
        on = [{p for p in face if sign * vals[p] >= 0} for sign in (-1, 1)]
        for a, b in zip(face, face[1:] + face[:1]):
            va, vb = vals[a], vals[b]
            if va * vb < 0:
                p = tuple((va*t-vb*s)/(va-vb) for s, t in zip(a, b))
                section.add(p)
                for side in on:
                    side.add(p)
        for part, side in zip(out, on):
            clipped = hull(side)
            if clipped:
                part.append(clipped)
    face = hull(section)
    assert len(face) >= 3
    for part in out:
        part.append(face)
    return out


# Argumentos de los cuatro perfiles de filas al cuadrado y las seis vacancias.
ROWS = ((1,0,0,0), (0,1,0,0), (1,0,1,0), (0,1,1,0))
VAC = ((1,-1,0,0), (1,-1,1,0), (1,-1,-1,0), (1,1,0,-1),
       (1,1,1,-1), (1,1,2,-1))


def panels(tet):
    """(panel G6, argumentos en [0,1] en los 4 vértices, multiplicidad)."""
    out = []
    for i, form in enumerate(ROWS + VAC):
        y = [linear(v, form) for v in tet]
        if i < 4:
            if max(y) <= F(1,2):
                y = [2*x for x in y]
            else:
                assert min(y) >= F(1,2)
                y = [2*(1-x) for x in y]
            key, power = 'cS', 2
        else:
            if min(y) < 0:
                assert max(y) <= 0
                y = [-x for x in y]
            if max(y) <= F(1,2):
                key, y = 'cu0', [2*x for x in y]
            else:
                assert min(y) >= F(1,2)
                key, y = 'cu1', [2*x-1 for x in y]
            power = 1
        assert min(y) >= 0 and max(y) <= 1
        out.append((key, y, power))
    return out


def tetrahedra():
    half = F(1,2)
    verts = [tuple(map(F, row)) for row in [(0,0,0), (0,half,0),
                                                (half,half,0), (0,0,1)]]
    pieces = [[list(f) for f in combinations(verts, 3)]]
    for forms, offsets in ((ROWS, (half,)), (VAC, (-half, F(0), half))):
        for a, b, c, d in forms:
            for offset in offsets:
                pieces = [q for piece in pieces for q in split(piece, (a,b,c,d-offset))]
    tets = []
    for faces in pieces:
        v = min({p for face in faces for p in face})
        for face in faces:
            if v in face:
                continue
            for b,c in zip(face[1:],face[2:]):
                t = (v,face[0],b,c)
                vol6 = abs(determinant(*t))
                if vol6:
                    tets.append((t,vol6,panels(t)))
    assert sum(x[1] for x in tets) == F(1,4)
    return len(pieces), tets
