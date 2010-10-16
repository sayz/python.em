
class Poly:
        def __init__(self, liste):
                self.liste = liste

        def __str__(self):
                liste = []
                us = 0
                for i in self.liste[::-1]:
                        if us==0:
                                liste.append(str(i))
                                us+=1
                                continue

                        if type(i)==int:
                                liste.append(str(i)+'*'+'x^'+str(us))
                        else:
                                liste.append('('+str(i)+')'+'*'+'x^'+str(us))
                        us+=1 
                return (' + '.join(liste[::-1]))

        def __add__(self, other):
                ters1, ters2 = self.liste[::-1], other.liste[::-1]

                if len(ters1)>=len(ters2):
                        liste, ekle = ters1, ters2
                else:
                        liste, ekle = ters2, ters1

                for i in range(len(ekle)):
                        liste[i] = liste[i] + ekle[i]
                return Poly(liste[::-1])

        def __sub__(self, other):
                liste, cikar = self.liste, other.liste

                if len(liste)<len(cikar):
                        k = len(cikar)-len(liste)
                        for i in range(k):
                                liste.insert(0,0)

                for i in range(len(liste)):
                        liste[i] = liste[i] - cikar[i]
                return Poly(liste)

        def __mul__(self, other):
                carp0, carp1 = self.liste, other.liste
                liste, yeni = list(), list()

                for i in range(len(carp1)):
                        for j in range(len(carp0)):
                                yeni.append(carp1[i]*carp0[j])
                        
                        a = len(carp1)-i-1
                        
                        for m in range(a):
                                yeni.append(0)
                        for n in range(i):
                                yeni.insert(0,0)
                        liste.append(yeni)
                        yeni = list()

                k = 0
                hop = list()
                for j in range(len(liste[0])):
                        for i in liste:
                                k += i[j]
                        hop.append(k)
                        k = 0

                return Poly(hop)

        def __div__(self, other):
                bolunen, bolen = self.liste, other.liste
                if len(bolunen)==len(bolen):
                        return Poly([bolunen[0]/float(bolen[0])])
                if len(bolunen)<len(bolen):
                        return Poly([0])
 
                kalan = list()
                k = 0
                while len(bolunen)!=len(bolen)-1:# or len(bolunen)!=0:
                        k = bolunen[0]/float(bolen[0])
                        kalan.append(k)
                        cikar = list()
                        for i in range(len(bolen)):
                                cikar.append(bolen[i]*k)
                        
                        z = len(bolunen) - len(bolen)
                        while z!=0:
                                cikar.append(0)
                                z-=1

                        for i in range(len(bolunen)):
                                bolunen[i] = bolunen[i] - cikar[i]

                        for i in bolunen:
                                if i==0.0:      del bolunen[0]
                                else:           break

                for i in range(len(kalan)):
                        if '.0' in str(kalan[i]):
                                kalan[i] = int(kalan[i])

                return Poly(kalan)


liste1 = [6,2,4,2]
liste2 = [2,4,6]

f1 = Poly(liste1)
f2 = Poly(liste2)

print f1 * f2

