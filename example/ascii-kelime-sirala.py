#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def kelime_sirala(kelime):
        """\
            >>> kelime_sirala("emineker")
            eeeikmnr
        """
        liste = [] ; son = ""
        for i in kelime: liste.append(i)
        for i in range(len(kelime)):
                son += min(liste)
                del liste[liste.index(min(liste))]
        print son

doctest.testmod()
