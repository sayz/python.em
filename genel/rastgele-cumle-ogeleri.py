#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

def rastgele_cumle_ogeleri(cumle):
        if type(cumle)==str:
                liste = cumle.split()
                for i in range(len(liste)):
                        k = random.randint(0,len(liste)-1)
                        print liste[k],
                        del liste[k]
        else:
                print 'girdi string yapıda olmalı'
