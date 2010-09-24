#!/usr/bin/python
#-*- coding: utf-8 -*-

import os, sys, warnings
warnings.simplefilter("ignore", DeprecationWarning)

from pyPdf import PdfFileWriter , PdfFileReader


def pdf_birlestir(liste):
        """aldığı argümanların pdf olup olmadığına bakarak bunları birleştirir"""
        try:
                islem   = PdfFileWriter()
                hedef   = open("data.pdf", "wb")
                for dosya in liste:
                        dosya =  os.path.abspath(dosya)
                        if os.path.splitext(dosya)[1]=='.pdf':
                                kaynak  = PdfFileReader(open(dosya , "rb"))
                                for i in range(kaynak.getNumPages()):
                                        islem.addPage(kaynak.getPage(i))
                        else:
                                pass
                islem.write(hedef)
                hedef.close()
                print "»» pdf oluşturuldu"
        except:
                print "»» pdf oluşturulamadı"


if __name__ == "__main__":
        pdf_birlestir(sys.argv[1:])


