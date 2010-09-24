#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


text = "emin eker!"
print re.match(".", text).group()       # ilk karakteri alıyo
print  re.match(".*", text).group()     # tümünü yazıyor 
print re.match("\w+", text).group()     # boşluğa kadar olan kısmı alıyo
#print re.match("\d+", text).group()    # hata veriyor

text ="10/15/99"
print re.match("(\d{2})/(\d{2})/(\d{2,4})", text).group(1,2,3) # ('10' , '15' , '99') çıktısını veriyor

text = "Example 3: There is 1 date 10/25/95 in here!"
print  re.search("(\d{1,2})/(\d{1,2})/(\d{2,4})", text).group(0)

text = "you're no fun anymore..."
print re.sub("fun", "entertaining", text)             # fun yerine entertanaining'i yerleştirir
print re.sub("[^\w]+", "-", text)                     # boşluklara - karakterini yerleştirir
print re.sub("\S+", "-BEEP-", text)                   # tüm karakter kümelerini -BEEP- ile değiştirir




