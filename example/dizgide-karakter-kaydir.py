#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def dizgide_sekil_kaydir(dizgi , n):
        """\
            >>> dizgide_sekil_kaydir('selam', '_')
            _elam
            s_lam
            se_am
            sel_m
            sela_
        """
        if type(dizgi)==str:
                for i in range(len(dizgi)):
                        print dizgi[:i] + str(n) + dizgi[i+1:]
        else:
                print 'karakter dizgisi girmelisiniz'

doctest.testmod()


