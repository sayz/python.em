#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def sayi_icindeki_enbuyuk(sayi):
        """\
            >>> sayi_icindeki_enbuyuk(5376)
            7
        """
        if type(sayi)==int or type(sayi)==float:
                liste=[]
                for i in str(sayi):
                        liste.append(i)
                print max(liste)
        else:
                print 'girdi bir sayı türü olmalı'

doctest.testmod()


