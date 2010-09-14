#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def asal_sayilar(girilen):
    """\
        >>> asal_sayilar(12)
        2 3 5 7 11
    """
    if type(girilen)==int and girilen>=0:
        for denek in range(2,girilen+1):
            for i in range(2,denek+1):
                if denek%i==0 and denek==i:
                    print denek , 
                elif denek%i==0 and denek!=i:
                    break
                else:
                    pass
    else: print 'integer türünde pozitif değerler giriniz'

doctest.testmod()
