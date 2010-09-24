#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def sayilari_sirala(sayi):
        """\
            >>> sayilari_sirala(47856)
            87654
        """
        if type(sayi)==int and sayi>=0:
                liste=[]
                son_sayi=""
                for i in str(sayi):
                        liste.append(int(i))
                for i in range(len(liste)):
                        son_sayi+=str(max(liste))
                        del liste[liste.index(max(liste))]
                print son_sayi
        else:
                print 'integer türünde ve pozitif değerler giriniz'

doctest.testmod()



