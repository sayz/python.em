#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def ters_cumle_ogeleri(cumle):
        """\
            >>> ters_cumle_ogeleri("super position")
            repus noitisop
        """
        liste = cumle.split()
        for eleman in liste:
                print eleman[::-1] ,
        
doctest.testmod()


