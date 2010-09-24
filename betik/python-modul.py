#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, commands

def ara():
        top = commands.getoutput('apt-cache search python')
        top = top.split()
        return [i for i in top.split() if 'python-' in i]


def yukle (liste):
        for i in liste:
                os.system('sudo apt-get install %s' %i)
        print 'tüm modüller yüklendi \niyi günler...'


def main():
        print 'python modülleri aranıyor...'
        modul = ara()
        print 'toplam %s modul bulundu' %len(modul)
        son = raw_input('yüklensin mi (E/H): ')

        if son in  ['E' , 'e' , 'Evet' , 'EVET' , 'evet']:
                print 'moduller yükleniyor...'
                yukle(modul)
                print 'modüller yüklendi... \nprogramdan çıkılıyor...'
        elif son in ['H' , 'h' , 'Hayır' , 'HAYIR' , 'hayır']:
                print 'programdan çıkılıyor...'
                sys.exit()
        else:
                main()


if __name__ == "__main__":
        main()


