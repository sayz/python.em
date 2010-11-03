#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys

def sade(okunan):
        liste = re.findall(r'<[/]*\w+[^>]*>', okunan)
        liste = [i for i in liste if i[-2]!='/']

        tag, kapa = list(), list()

        for i in liste:
                if ' ' in i:
                        tag.append(i[1:i.find(' ')])
                elif ' ' not in i and '/' not in i:
                        tag.append(i[1:i.find('>')])
                else:
                        kapa.append(i[2:i.find('>')])
        return (tag, kapa)


if __name__ == "__main__":
        with open(sys.argv[1]) as dosya:
                okunan = dosya.read().decode("utf8")

        (tag, kapa) = sade(okunan)
        for i in tag:
                if i not in kapa:
                        print 'açılan bir', i, 'tagı kapanmamış'
                elif okunan.find('<'+i) > okunan.find('</%s>' %i):
                        print i, "tagı önce kapanmış sonra açılmış"
                        kapa.remove(i)
                else:
                        kapa.remove(i)

        for i in kapa:
                print 'daha önce açılmayan bir', i, 'tagı kapanmış'


