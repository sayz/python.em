#!/usr/bin/python
# -*- coding: utf-8 -*-

def terstten_dosya_karakterleri_sayisi(dosya_yolu):
        dosya  = open( dosya_yolu , "r")
        okunan = dosya.read().decode("utf8")
        dosya.close()    
        k=0
        for i in okunan:
                if not 48 <= ord(i) <= 57:
                        k+=1
        m=0
        for i in okunan:
                if not 65 <= ord(i) <= 91 and not 96 <= ord(i) <= 122:
                        m+=1
        n=0
        for i in okunan:
                if not 48 <= ord(i) <= 57 and not 65 <= ord(i) <= 91 and not 96 <= ord(i) <= 122:
                        n+=1
        print "dosyada %s tane sayı dışında karakter var" %(k)
        print "dosyada %s tane harf dışında karakter var" %(m)
        print "dosyada %s tane sayı ve harf olmayan karakter var" %(n)


