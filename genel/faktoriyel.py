#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def faktoriyel(sayi):
    """\
        >>> faktoriyel(6)
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

doctest.testmod()

