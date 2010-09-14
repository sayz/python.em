#!/usr/bin/python
#-*- coding: utf-8 -*-

import doctest

def obeb(sayi1 , sayi2):
        """\
            >>> obeb(28 , 42)
            14
        """
        if type(sayi1)==int and type(sayi2)==int :
                for i in range((sayi1+sayi2)/2 , 0 , -1):
                        if sayi1%i==0 and sayi2%i==0:
                                print i
                                break
                        else:
                                pass
        else:
                print 'girdiler integer türünde olmalı'
        

def okek(sayi1 , sayi2):
        """\
            >>> okek(12,8)
            24
        """
        if type(sayi1)==int and type(sayi2)==int :
                for i in range (1 , sayi1*sayi2 + 1) :
                        if i%sayi1 == 0 and i%sayi2 == 0 :
                                print i
                                break
                        else:
                                pass
        else:
                print 'girdiler integer türünde olmalı'


doctest.testmod()



