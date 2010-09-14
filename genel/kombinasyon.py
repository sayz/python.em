#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def fakt(sayi):
    """\
        >>> fakt(6)
        720
    """
    if type(sayi)==int and sayi>=0 :
        if sayi==0 or sayi==1:
            return 1
        else:
            for i in range(2,sayi):
                sayi=sayi*i
            return sayi
    else:
        print 'integer türünde pozitif değerler giriniz'

def kombinasyon(sayi):
    """\
        >>> kombinasyon(4)
        [1, 4, 6, 4, 1]
    """
    if type(sayi)==int:
        liste = []
        for i in range(0 , sayi+1):
            liste.append(  fakt(sayi) / ( fakt(i)*fakt(sayi-i) )  )
        print liste
    else:
        print 'girdi integer yapıda olmalı'

doctest.testmod()
