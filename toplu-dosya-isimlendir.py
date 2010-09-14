#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def yenile( yol , ad='' ):
        if os.path.isdir(yol)==True:
                os.chdir(yol)
                sira=0
                for i in os.listdir(yol):
                        if os.path.isdir(i) == True:
                                continue
                        os.rename( i , ad + str(sira).zfill(4) + os.path.splitext(i)[1])
                        sira+=1
                print 'toplam %s dosya ismi değiştirildi' %sira
        else:
                print 'böyle bir dizin yok'


