#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def sesli_harfleri_at(dizgi):
        """\
            >>> sesli_harfleri_at('emineker')
            *m*n*k*r
        """
        sesli_harfler= "aeıioöuüAEIİOÖUÜ"
        son=''
        if type(dizgi)==str:
                for harf in dizgi:
                        if harf in sesli_harfler:
                                son += '*'
                        else:
                                son += harf
                print son
        else:
                print 'karakter dizgisi girmelisiniz'

doctest.testmod()

