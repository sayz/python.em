#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def capitalize(dizgi):
        """\
            >>> capitalize("emineker")
            Emineker
        """
        if type(dizgi)==int:
                print 'girdi string yapıda olmalı'
        elif 97<=ord(dizgi[0])<=122:
                k=ord(dizgi[0]) - 32
                print chr(k) + dizgi[1:]
        else:
                print dizgi

doctest.testmod()

