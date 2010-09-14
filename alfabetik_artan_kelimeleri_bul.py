#!/usr/bin/python
#-*-coding:utf-8-*-

def alfabetik_artan_kelimeleri_bul(dosya_yolu):
    dosya = open(dosya_yolu , "r").read()
    liste = dosya.split()
    son = 0
    for kelime in liste:
        a = 0
        for i in range(len(kelime)-1):
            if kelime[a] <= kelime[a+1]:    a += 1
            else:                           pass
        if a==len(kelime)-1:                son += 1
    print "Alfabetik artan sozcuk sayisi: %s" %(son)
