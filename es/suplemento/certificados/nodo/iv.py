"""Intervalos binarios cerrados. Los productos matriciales se encierran en enteros diádicos."""
import math
import numpy as np


def down(x):
    return np.nextafter(x, -np.inf)


def up(x):
    return np.nextafter(x, np.inf)


def iv(a):
    return a if isinstance(a, I) else I(a)


def bounds(lo, hi, exact_zero=False):
    return I(np.where(exact_zero, 0., down(lo)), np.where(exact_zero, 0., up(hi)))


def dyadic(a, bits):
    magnitude = float(np.maximum(np.abs(a.lo), np.abs(a.hi)).max(initial=0.))
    if not np.isfinite(magnitude):
        raise ArithmeticError("Extremos no finitos en el producto matricial")
    if magnitude == 0:
        return a.lo, a.hi, 0
    exponent = math.frexp(magnitude)[1] - bits
    low = np.floor(down(np.ldexp(a.lo, -exponent)))
    high = np.ceil(up(np.ldexp(a.hi, -exponent)))
    # Los ceros estructurales son representables exactamente.
    low = np.where(a.lo == 0, 0., low)
    high = np.where(a.hi == 0, 0., high)
    center = np.floor((low + high) / 2.)
    radius = np.maximum(center-low, high-center)
    return center, radius, exponent


class I:
    __array_priority__ = 10000

    def __init__(self, lo, hi=None):
        if isinstance(lo, I) and hi is None:
            self.lo, self.hi = lo.lo, lo.hi
            return
        low = np.asarray(lo, dtype=np.float64)
        high = low if hi is None else np.asarray(hi, dtype=np.float64)
        self.lo, self.hi = np.broadcast_arrays(low, high)

    @property
    def shape(self):
        return self.lo.shape

    @property
    def T(self):
        return I(self.lo.T, self.hi.T)

    def transpose(self, *axes):
        return I(self.lo.transpose(*axes), self.hi.transpose(*axes))

    def reshape(self, *shape):
        return I(self.lo.reshape(*shape), self.hi.reshape(*shape))

    def __getitem__(self, key):
        return I(self.lo[key], self.hi[key])

    def __len__(self):
        return len(self.lo)

    def tolist(self):
        return [self.lo.tolist(), self.hi.tolist()]

    @staticmethod
    def hull(a,b):
        a,b = iv(a),iv(b)
        return I(np.minimum(a.lo,b.lo),np.maximum(a.hi,b.hi))

    def __neg__(self):
        return I(-self.hi,-self.lo)

    def __add__(self,b):
        b=iv(b)
        return bounds(self.lo+b.lo,self.hi+b.hi,
                      (self.lo==0)&(self.hi==0)&(b.lo==0)&(b.hi==0))

    __radd__ = __add__

    def __sub__(self,b):
        return self+(-iv(b))

    def __rsub__(self,b):
        return iv(b)+(-self)

    def __mul__(self,b):
        b=iv(b)
        ll,lh,hl,hh=self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi
        minimum=np.minimum(np.minimum(ll,lh),np.minimum(hl,hh))
        maximum=np.maximum(np.maximum(ll,lh),np.maximum(hl,hh))
        return bounds(minimum,maximum,((self.lo==0)&(self.hi==0))|((b.lo==0)&(b.hi==0)))

    __rmul__ = __mul__

    def sq(self):
        zero=(self.lo<=0)&(self.hi>=0)
        a,b=self.lo*self.lo,self.hi*self.hi
        return I(np.where(zero,0.,down(np.minimum(a,b))),
                 np.where((self.lo==0)&(self.hi==0),0.,up(np.maximum(a,b))))

    def __truediv__(self,b):
        b=iv(b)
        if np.any((b.lo<=0)&(b.hi>=0)):
            raise ZeroDivisionError("Intervalo divisor contiene cero")
        return self*I(down(1./b.hi),up(1./b.lo))

    def __rtruediv__(self,b):
        return iv(b)/self

    def sum(self,axis=None):
        if axis is None:
            a=self.reshape(-1)
            return a.sum(axis=0)
        if isinstance(axis,tuple):
            a=self
            for i in sorted((x%self.lo.ndim for x in axis),reverse=True):
                a=a.sum(axis=i)
            return a
        l,h=np.moveaxis(self.lo,axis,0),np.moveaxis(self.hi,axis,0)
        if len(l)==0:
            return I(np.zeros(l.shape[1:]))
        while len(l)>1:
            end=2*(len(l)//2)
            left,right=l[:end:2],l[1:end:2]
            lows=np.where((left==0)&(right==0),0.,down(left+right))
            left,right=h[:end:2],h[1:end:2]
            highs=np.where((left==0)&(right==0),0.,up(left+right))
            if len(l)%2:
                lows=np.concatenate((lows,l[-1:]),axis=0)
                highs=np.concatenate((highs,h[-1:]),axis=0)
            l,h=lows,highs
        return I(l[0],h[0])

    def __matmul__(self,b):
        b=iv(b)
        n=self.shape[-1]
        bits=min(22,(50-max(1,n).bit_length())//2)
        ac,ar,ea=dyadic(self,bits)
        bc,br,eb=dyadic(b,bits)
        max_a=int((np.abs(ac)+ar).max(initial=0.))
        max_b=int((np.abs(bc)+br).max(initial=0.))
        if n*max_a*max_b>=2**52:
            raise ArithmeticError("Producto entero fuera de la escala exacta")
        center=ac@bc
        radius=np.abs(ac)@br+ar@(np.abs(bc)+br)
        low,high=center-radius,center+radius
        return I(np.where(low==0,0.,down(np.ldexp(low,ea+eb))),
                 np.where(high==0,0.,up(np.ldexp(high,ea+eb))))

    def __rmatmul__(self,b):
        return iv(b)@self

