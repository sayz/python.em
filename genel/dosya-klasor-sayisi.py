#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def dosya_klasor_sayisi(ana_dizin):
    try:
        dizin , dosya = 0 , 0
        for oge in os.walk(ana_dizin):
            dizin += 1 ; dosya += len(oge[2])        
    except:
        print 'girdiğiniz bir dizin yolu olmalı'

    print 'dizin sayısı: %s' %(dizin)
    print 'dosya sayısı: %s' %(dosya)
