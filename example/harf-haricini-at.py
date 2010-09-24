#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def harf_haricini_at(dizgi):
        """\
            >>> harf_haricini_at('emin22^4eker05#ed')
            emin****eker***ed
        """
        if type(dizgi)==str:
                son=''
                for harf in dizgi:
                        if 65 <= ord(harf)<=90 or 97<=ord(harf)<=122:
                                son += harf
                        else:
                                son += '*'
                print son
        else:
                print 'karakter dizgisi girmelisiniz'

doctest.testmod()



