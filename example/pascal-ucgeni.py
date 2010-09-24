#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def fakt(sayi):
        if type(sayi)==int and sayi>=0 :
                if sayi==0 or sayi==1:
                        return 1
                else:
                        for i in range(2,sayi):
                                sayi=sayi*i
                        return sayi
        else:
                print 'integer türünde pozitif değerler giriniz'

def komb(sayi):
        if type(sayi)==int:
                liste = []
                for i in range(0 , sayi+1):
                        liste.append(  fakt(sayi) / ( fakt(i)*fakt(sayi-i) )  )
                return liste
        else:
                print 'girdi integer yapıda olmalı'

def pascal(sayi):
        """\
            >>> pascal(4)
                [1]
               [1, 1]
              [1, 2, 1]
             [1, 3, 3, 1]
            [1, 4, 6, 4, 1]
        """
        if type(sayi)==int:
                for i in range(0 , sayi+1):
                        print ' '*(sayi-i) + str(komb(i))
        else:
                print 'olmadı hacı'
        
doctest.testmod()



