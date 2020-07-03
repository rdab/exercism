from __future__ import division


class Rational:
    def __init__(self, numer, denom):
        self.numer = int(numer) if denom > 0 else int(-numer)
        self.denom = int(denom) if denom > 0 else int(-denom)

    def __eq__(self, other):
        left = self.reduce()
        right = other.reduce()
        return left.numer == right.numer and left.denom == right.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other):
        n = self.numer * other.denom + other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d).reduce()

    def __sub__(self, other):
        n = self.numer * other.denom - other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d).reduce()

    def __mul__(self, other):
        n = self.numer * other.numer
        d = self.denom * other.denom
        return Rational(n, d).reduce()

    def __truediv__(self, other):
        n = self.numer * other.denom
        d = other.numer * self.denom
        return Rational(n, d).reduce()

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** abs(power), self.denom ** abs(power))

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)

    def reduce(self):
        g = int(gcd(self.numer, self.denom))
        return Rational(self.numer / g, self.denom / g)


def gcd(a, b, d=0):
    if a == 0:
        return b
    a, b = abs(a), abs(b)

    while a != b:
        if a % 2 != 0 and b % 2 != 0:
            a, b = (b, a) if a < b else (a, b)
            a = (a - b) / 2
            continue
        d = d + 1 if a % 2 == 0 and b % 2 == 0 else d
        a = a / 2 if a % 2 == 0 else a
        b = b / 2 if b % 2 == 0 else b
    return a * (2 ** d)
