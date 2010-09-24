#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, os

# bulunduğunuz dizinedki pdf dosyalarını bulur ve bunları listeler
pdfdosya = glob.glob(os.getcwd() + '/*.pdf')

# bütün modülleri aynı anda import et
os.chdir('/usr/lib/python2.6')
for modul in glob.glob("*.py*"): 
    ('import %s' % modul)


