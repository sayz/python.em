#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def satir_ortala(cumle , uzunluk):
        """\
            >>> satir_ortala("cümbür cemaat gedik" , 35)
            cümbür        cemaat        gedik
        """
        if type(cumle)==str and type(uzunluk)==int:
                toplam , oge = 0 , 0
                liste = cumle.split()
                for i in liste:
                        oge+=1
                        for j in i:
                                toplam +=1
                for i in liste:
                        print i ,
                        if liste.index(i) == len(liste)-1:
                                break
                print " "*((uzunluk-toplam-oge)/(oge-1)) ,
        else:
                print 'yok'

doctest.testmod()



