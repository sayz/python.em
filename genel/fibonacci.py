#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def fibonacci(sayi):
        """\
            >>> fibonacci(28)
            1 1 2 3 5 8 13 21
        """
        if type(sayi)==int and sayi>=0:
                ilk , son = 0 , 1
                while son <= sayi :
                        print son ,
                        ilk , son = son , ilk+son
        else:
                print 'integer türünde pozitif değerler giriniz'

doctest.testmod()


