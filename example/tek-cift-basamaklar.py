#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def tek_cift_basamaklar(sayi):
        """\
            >>> tek_cift_basamaklar(1234568)
            cift: 4 adet, toplami = 20
            tek : 3 adet, toplami = 9
        """
        if type(sayi)==int:
                tek , cift, teksayi , ciftsayi = 0 , 0 , 0 , 0
                while sayi>0:
                        if (sayi%10)%2==0:
                                cift +=sayi%10 ; ciftsayi+=1
                        else:
                                tek+=sayi%10   ; teksayi+=1 
                        sayi /= 10
            
        print "cift: %s adet, toplami = %s" % (ciftsayi , cift)
        print "tek : %s adet, toplami = %s" % (teksayi  , tek )

doctest.testmod()



