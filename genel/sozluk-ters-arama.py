#!/usr/bin/python
# -*- coding: utf-8 -*-

import doctest

def sozluk_ters_arama(sehirler , ilce):
    """\
        >>> sozluk_ters_arama(sehirler , "terme")
        samsun
        istanbul
    """
    anahtar = sehirler.keys()
    deger   = sehirler.values()
    if ilce in sehirler.values():
        for i in range(len(sehirler)-2):
            cc = deger.index(ilce)
            print anahtar[cc]
            del anahtar[cc] , deger[cc]
    else: print "ilçeye ait şehir bulunamadı"

sehirler={"samsun": "terme" , "çorum": "iskilip" ,
          "ankara": "elmadağ" , "istanbul":"terme"}

sozluk_ters_arama(sehirler , "terme")

