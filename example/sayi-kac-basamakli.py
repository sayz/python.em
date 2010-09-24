#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def sayi_kac_basamakli(sayi):
        """\
            >>> sayi_kac_basamakli(3268.0)
            4
            >>> sayi_kac_basamakli(-538.20)
            3
        """
        if type(sayi)==int or type(sayi)==float:
                sayi = abs(sayi)
                sayi = int(sayi)
                sayi = str(sayi)
                sayi = len(sayi)
                sayi = int(sayi)
                print sayi
        else:
                print 'girdi sayı türlerinde olmalıdır'

doctest.testmod()


