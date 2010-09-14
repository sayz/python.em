#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def dizgiden_parca_sil(dizgi , parca):
        """\
            >>> dizgiden_parca_sil('karakter' , 'ak')
            karter
        """
        if type(dizgi)==str and type(parca)==str:
                m = dizgi.find(parca)
                n = len(parca)
                print dizgi[:m] + dizgi[m+n:]
        else:
                print 'karakter dizgisi girmelisiniz'
    
doctest.testmod()
