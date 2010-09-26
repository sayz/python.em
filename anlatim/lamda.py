#!/usr/bin/python
# -*- coding: utf-8 -*-

def f(x):
    return x*3

print f(2)
# 6

g=(lambda x:x*3)

print g(2)
# 6

print (lambda x:x*3)(2)
# 6

sayilar=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  

print map(lambda x:x**2,sayilar)
# [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]


print map(lambda x:len(x),'suan disarda kar yagiyor'.split())
# [4,7,3,7]


print reduce(lambda x,y:x+y,sayilar)
# 120


aylar=["Ocak","Subat","Mart","Nisan","Mayis","Haziran",
       "Temmuz","Agustos","Eylul","Ekim","Kasim","Aralik"]
print filter(lambda x:x[0]=="M",aylar)
# ['Mart' , 'Mayis']

for i in range(2,8):
	sayilar=filter(lambda x:x==i or x%i,sayilar)  
print sayilar 
# [1,2,3,5,7,11,13]


# '#' ile verdiğimiz kısımlar o an dönen sonuçlardır

# lambda fonksiyonunu ve yardımcılarını sırayla örnekledik
# bu fonksiyonu işleri listeler yardımıyla işte bu kadar kolaylaştırıyor



