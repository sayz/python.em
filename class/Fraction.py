def gcd(m,n):
        while m%n !=0:
                m, n = n, m%n
        return n

class Fraction:
        def __init__(self, top, bottom):
                self.num = top
                self.den = bottom

        def show(self):
                print self.num, "/", self.den

        def __str__(self):
                k = gcd(self.num,self.den)
                return str(self.num/k) + "/" + str(self.den/k)

        def __add__(self, other):
                newnum = self.num * other.den + self.den * other.num
                newden = self.den * other.den
                return Fraction(newnum, newden)

        def __sub__(self, other):
                newnum = self.num * other.den - self.den * other.num
                newden = self.den * other.den
                return Fraction(newnum, newden)

        def __mul__(self, other):
                newnum = self.num * other.num
                newden = self.den * other.den
                return Fraction(newnum, newden)

        def __div__(self, other):
                newnum = self.num * other.den
                newden = self.den * other.num
                return Fraction(newnum, newden)

        def __pow__(self, x):
                newnum = self.num ** x
                newden = self.den ** x
                return Fraction(newnum, newden)

        def __abs__(self):
                if self.num<0:
                        newnum=self.num*-1
                else:
                        newnum=self.num
                return Fraction(newnum,self.den)

        def __neg__(self):
                newnum = self.num * -1
                return Fraction(newnum, self.den)

        def __cmp__(self, other):
                num1 = self.num * other.den
                num2 = other.num * self.den
                return num1 - num2
