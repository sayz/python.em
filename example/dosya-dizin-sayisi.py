#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def dosya_dizin_sayisi(path):
        try:
                dizin , dosya = 0 , 0
                for oge in os.walk(path):
                        print oge
                        dizin += 1
                        dosya += len(oge[2])        
        except:
                print 'girdiğiniz yol bir dizin olmalı'

        print 'dizin sayısı: %d' % dizin
        print 'dosya sayısı: %d' % dosya

