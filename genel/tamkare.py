#!/usr/bin/python
#-*- coding: utf-8 -*-

import doctest

def tam_kare(sayi):
        """\
            >>> tam_kare(28)
            1 4 9 16 25
        """
        if type(sayi)==int:
                for i in range(1 , sayi+1):
                        if i**2<=sayi:
                                print i**2 ,
                        else:
                                pass
        else:
                print 'girdi integer türde olmalı'

doctest.testmod()



