#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def cumleden_tekrarlari_at(cumle):
        """\
            >>> cumleden_tekrarlari_at("emin de 20 yaşında can da 20 yaşında")
            emin de 20 yaşında can da
        """
        if type(cumle)==str:
                liste = cumle.split()
                yeni_liste= []
                for oge in liste:
                        if oge not in yeni_liste:
                                yeni_liste.append(oge)
                        else:
                                pass
                print " ".join(yeni_liste)
        else:
                print 'girdi string yapıda olmalı'
       
doctest.testmod()



