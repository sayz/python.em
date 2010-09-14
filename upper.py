#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def upper(dizgi):
    """\
        >>> upper('emineker')
        EMINEKER
    """
    if type(dizgi)==str:
        son=''
        for harf in dizgi:
            if 97<=ord(harf)<=122:
                son += chr(ord(harf)-32)
            else:
                son += harf
        print son
    else:
        print 'karakter dizgisi girmelisiniz'

doctest.testmod()
