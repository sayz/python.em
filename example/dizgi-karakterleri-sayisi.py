#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def dizgi_karakterleri_sayisi(cumle):
        """\
            >>> dizgi_karakterleri_sayisi('Dumansiz hava sahasini %100 DESTEKLIYORUM')
            'Dumansiz hava sahasini %100 DESTEKLIYORUM'
            karakter dizgileri içerisindeki
            41 tane karakterden;
            33 tanesi harf
            3 tanesi sayı,
            5 tanesi de diğer karakterden oluşmaktadır.
        """
        harfler , sayi , karakter , toplam = 0 , 0 , 0 , 0
        if type(cumle) == str :
                for harf in cumle:
                        toplam += 1
                        if 65<=ord(harf)<=90 or 97<=ord(harf)<=122 :
                                harfler += 1
                        elif 48<=ord(harf)<=57 :
                                sayi += 1
                        else:
                                karakter += 1            
        print "'%s'" %(cumle)
        print "karakter dizgileri içerisindeki"
        print "%s tane karakterden;" %(toplam)
        print "%s tanesi harf"       %(harfler)
        print "%s tanesi sayı,"      %(sayi)
        print "%s tanesi de diğer karakterden oluşmaktadır."  %(karakter)

doctest.testmod()


