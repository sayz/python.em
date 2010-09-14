#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def kelime_index(dizgi):
        """\
            >>> kelime_index("emineker")
            e » 3
            m » 1
            i » 1
            n » 1
            k » 1
            r » 1
        """
        if type(dizgi) == str:
                k=len(dizgi)
                for i in range(k):
                        if dizgi=="":
                                break
                        ne = dizgi[0] ; sira=0 ; kac_kez=0
                        while ne in dizgi:
                                sira = dizgi.find(ne)
                                dizgi = dizgi[:sira] + dizgi[sira+1:]
                                kac_kez+=1
                        print "%s » %s" %(ne , kac_kez)
        else:
                print 'string yapıda bir yapı giriniz'

doctest.testmod()



