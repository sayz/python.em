#!/usr/bin/python
# -*- coding: utf-8 -*-

# 'append' => listenin en sonuna yeni bir eleman eklemede kullanılır
t = ['a', 'b', 'c']
t.append('d')
print t
# ['a', 'b', 'c', 'd']


# 'extend' => bir listenin sonuna diğer bir listeyi eklemek için kullanılır
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print t1
# ['a', 'b', 'c', 'd', 'e']


# 'sort' => listenin elemanlarını küçükten büyüğe doğru sıralamak için kullanılır
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print t
# ['a', 'b', 'c', 'd', 'e']
u = ['d', 4, 'c', -1, 7, 'e', 0, 'b', 1.7, 'a']
u.sort()
print u
# [-1, 0, 1.7, 4, 7, 'a', 'b', 'c', 'd', 'e']


# 'pop' => listenin herhangi bir indeksindeki elemanı çıkartıp bir değişkene atmak için kullanılır
t = ['a', 'b', 'c']
x = t.pop(1)
print t
# ['a', 'c']
print x
# b


# 'del' => listeden eleman çıkarmak için kullanılır
t = ['a', 'b', 'c']
del t[1]
print t
# ['a', 'c']


# 'remove' => listeden değeri bilinen elemanı çıkarmak için kullanılır
t = ['a', 'b', 'c']
t.remove('b')
print t
# ['a', 'c']



###################################
# listeleme özelliklerine birkaç ek


s = 'Python2.4.2-Python2.6.4-Python3.1.1'
print s.split('-')
# ['Python2.4.2', 'Python2.6.4', 'Python3.1.1']


t = ['Python2.4.2', 'Python2.6.4', 'Python3.1.1']
print '+'.join(t)
# 'Python2.4.2+Python2.6.4+Python3.1.1'


# koşullu yapılar ile tekrar tekrar liste tanımlamak yerine
print [i for i in 'emineker' if 'e' in i]
# ['e','e','e']

# tekrar tekrar döngü ile
print [ [i for i in oge] for oge in 'emin']
# [['e'],['m'],['i'],['n']]








