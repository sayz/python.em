#!/usr/bin/python
#-*- coding: utf-8 -*-

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

from pyPdf import PdfFileWriter , PdfFileReader
import os, sys


def kesit(dosya_yolu , sayfa1 , sayfa2=0):
        """pdf dosyasının sayfa1'den sayfa2'ye kadar olan kısmını alır
           sayfa2 verilmesse sayfa1'den sonuna kadar alır        
        """
        try:
                kaynak = PdfFileReader(open(dosya_yolu, "rb"))
                islem  = PdfFileWriter()
                if sayfa1<0:
                        (-1)*sayfa1
                if sayfa2==0:
                        sayfa2=kaynak.getNumPages()
                if sayfa2<=sayfa1:
                        sayfa2=sayfa1+1
                hedef = open("data.pdf", "wb")
                for i in range(int(sayfa1),int(sayfa2)):
                        islem.addPage(kaynak.getPage(i))
                islem.write(hedef)
                hedef.close()
                print "»» pdf oluşturuldu"
        except:
                print "»» pdf oluşturulamadı"


def ayir(dosya_yolu , sayfa1):
        """pdf dosyasının başından sayfa1'e,
           sayfa1'den sonuna kadar iki tabe pdf dosyası oluşturur
        """
        try:
                kaynak = PdfFileReader(open(dosya_yolu, "rb"))
                islem0 = PdfFileWriter()
                islem1 = PdfFileWriter()
                hedef0 = open("data0.pdf", "wb")
                hedef1 = open("data1.pdf", "wb")
                if sayfa1<0:
                        sayfa1 *=(-1)
                for i in range(int(sayfa1)):
                        islem0.addPage(kaynak.getPage(i))
                for i in range(int(sayfa1),kaynak.getNumPages()):
                        islem1.addPage(kaynak.getPage(i))
                islem0.write(hedef0)
                islem1.write(hedef1)
                hedef0.close()
                hedef1.close()
                print "»» pdf oluşturuldu"
        except:
                print "»» pdf oluşturulamadı"


def birlestir(dosya_yolu1 , dosya_yolu2):
        """ilk pdf başta, ikinci pdf sonda olmak üzere
           iki pdf dosyasını birleştirir
        """
        try:
                kaynak0 = PdfFileReader(open(dosya_yolu1, "rb"))
                kaynak1 = PdfFileReader(open(dosya_yolu2, "rb"))
                islem   = PdfFileWriter()
                hedef   = open("data.pdf", "wb")
                for i in range(kaynak0.getNumPages()):
                        islem.addPage(kaynak0.getPage(i))
                for i in range(kaynak1.getNumPages()):
                        islem.addPage(kaynak1.getPage(i))
                islem.write(hedef)
                hedef.close()
                print "»» pdf oluşturuldu"
        except:
                print "»» pdf oluşturulamadı"

def toplu_birlestir(dizin):
        """verilen dizinin içerisindeki tüm pdf dosyalarını birleştirir"""
        try:
                islem   = PdfFileWriter()
                hedef   = open("data.pdf", "wb")
                for dosya in os.listdir(dizin):
                        if os.path.splitext(i)[1]=='.pdf':
                                dosya = dizin + os.sep + dosya
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

def parcala(dosya_yolu):
        """pdf dosyasının herbir sayfasından ayrı bir pdf oluşturur
           data0.pdf, data1.pdf, data2.pdf, ...
        """
        try:
                kaynak = PdfFileReader(open(dosya_yolu, "rb"))
                for i in range(kaynak.getNumPages()):
                        islem = PdfFileWriter()
                        yol   = "data" + str(i) + ".pdf"
                        hedef = open(yol, "wb")
                        islem.addPage(kaynak.getPage(i))
                        islem.write(hedef)
                        hedef.close()
                print "»» pdf oluşturuldu"
        except:
                print "»» pdf oluşturulamadı"



