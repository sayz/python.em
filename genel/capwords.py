#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def capwords(cumle):
    """\
        >>> capwords("emin ata bak")
        Emin Ata Bak
    """
    if type(cumle)==int:
         print 'girdi string yapıda olmalı'
    elif type(cumle)==str:
        liste = cumle.split()
        for kelime in liste:
            if 97<=ord(kelime[0])<=122:
                k=ord(kelime[0]) - 32
                print chr(k) + kelime[1:] ,
            else:
                print kelime ,
    else:
        print cumle

doctest.testmod()
