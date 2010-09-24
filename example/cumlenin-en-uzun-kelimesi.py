#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def cumlenin_uzun_kelimesi(cumle):
        """\
            >>> cumlenin_uzun_kelimesi('güzel günler')
            günler
        """
        if type(cumle) == int:
                print 'girdi string yapıda olmalı'
        else:
                liste = cumle.split()
                uzunluk = []
                for kelime in liste:
                        uzunluk.append(len(kelime))
                m= uzunluk.index(max(uzunluk))
                print liste[m]

doctest.testmod()
