#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def basamaklarin_kareleri_toplami(sayi):
    """\
        >>> basamaklarin_kareleri_toplami(429)
        101
    """
    if type(sayi)==int: 
        kare = 0
        while sayi>0:
            kare += (sayi%10)**2
            sayi /=10
        print kare
    else:
        print 'integer türünde veri girmelisiniz'

doctest.testmod()
