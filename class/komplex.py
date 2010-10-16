class komplex:
        def __init__(self, reel, imaj):
                self.reel, self.imaj = reel, imaj

        def __str__(self):
                if self.imaj==0:
                        return str(self.reel)
                if self.imaj==1 or self.imaj==-1:
                        return str(self.reel) + '+' + 'i'
                if self.reel==0:
                        return str(self.imaj) + 'i'
                return str(self.reel) + '+' + str(self.imaj) + 'i'

        def __add__(self, other):
                return (self.reel + other.reel, self.imaj + other.imaj)

        def __sub__(self, other):
                return (self.reel - other.reel, self.imaj - other.imaj)

        def __mul__(self, other):
                reel = self.reel * other.reel - self.imaj * other.imaj
                imaj = self.reel * other.imaj + self.imaj * other.reel
                return komplex(reel, imaj)

        def __div__(self, other):
                import math
                k = '%.1f' %math.hypot(other.reel, other.imaj)
                k = float(k)

                other.imaj = other.imaj*(-1)
                reel = self.reel * other.reel - self.imaj * other.imaj
                imaj = self.reel * other.imaj + self.imaj * other.reel

                reel = '%.1f' %(reel/k)
                imaj = '%.1f' %(imaj/k)
                if '.0' in reel:        reel = int(reel)
                else:                   reel = float(reel)
                if '.0' in imaj:        imaj = int(imaj)
                else:                   imaj = float(imaj)
                return komplex(reel, imaj)

f1 = komplex(1,2)
f2 = komplex(2,3)

print f1 / f2


