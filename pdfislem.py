#!/usr/bin/python
#-*- coding: utf-8 -*-

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

from pyPdf import PdfFileWriter , PdfFileReader

def kesit(dosya_yolu , sayfa1 , sayfa2=0):
    try:
        kaynak = PdfFileReader(open(dosya_yolu, "rb"))
        islem = PdfFileWriter()
        if sayfa1<0:         (-1)*sayfa1
        if sayfa2==0:        sayfa2=kaynak.getNumPages()
        if sayfa2<=sayfa1:   sayfa2=sayfa1+1
        hedef = open("data.pdf", "wb")
        [islem.addPage(kaynak.getPage(i)) for i in range(sayfa1,sayfa2)]
        islem.write(hedef)
        hedef.close()
    except:         print "»» pdf oluşturulamadı"


def ayir(dosya_yolu , sayfa1):
    try:
        kaynak = PdfFileReader(open(dosya_yolu, "rb"))
        islem0 = PdfFileWriter()
        islem1 = PdfFileWriter()
        hedef0 = open("data0.pdf", "wb")
        hedef1 = open("data1.pdf", "wb")
        if sayfa1<0:    (-1)*sayfa1
        [islem0.addPage(kaynak.getPage(i)) for i in range(sayfa1)]
        [islem1.addPage(kaynak.getPage(i)) for i in range(sayfa1,kaynak.getNumPages())]
        islem0.write(hedef0)
        islem1.write(hedef1)
        hedef0.close()
        hedef1.close()
    except:         print "»» pdf oluşturulamadı"

    
def birlestir(dosya_yolu1 , dosya_yolu2):
    try:
        kaynak0 = PdfFileReader(open(dosya_yolu1, "rb"))
        kaynak1 = PdfFileReader(open(dosya_yolu2, "rb"))
        islem = PdfFileWriter()
        hedef = open("data.pdf", "wb")
        [islem.addPage(kaynak0.getPage(i)) for i in range(kaynak0.getNumPages())]
        [islem.addPage(kaynak1.getPage(i)) for i in range(kaynak1.getNumPages())]
        islem.write(hedef)
        hedef.close()
    except:         print "»» pdf oluşturulamadı"


def parcala(dosya_yolu):
    try:
        kaynak = PdfFileReader(open(dosya_yolu, "rb"))
        for i in range(kaynak.getNumPages()):
            islem = PdfFileWriter()
            yol = "data" + str(i) + ".pdf"
            hedef = open(yol, "wb")
            islem.addPage(kaynak.getPage(i))
            islem.write(hedef)
            hedef.close()
    except:         print "»» pdf oluşturulamadı"














