#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import *
import os, sys


def bas(yol, isim, yeni, bilgi):
        pdf = canvas.Canvas(yeni)
        pdf.setTitle(isim)
        pdf.setAuthor('emineker')
        pdf.setSubject(isim)

        # sayfanın düzenini ayarlayalım
        registerFont(TTFont('FreeSans', "/usr/share/fonts/truetype/freefont/FreeSans.ttf"))
        pdf.setFont('FreeSans', 15)
        cm = 28.3464566929

        # ilk sayfa ders bilgileri
        x = 21*cm/2.0
        y = 22.0*cm
        for i in bilgi:
                pdf.drawCentredString(x, y, i)
                y-=0.65*cm
        pdf.showPage()

        # resim dosyaları sırası ile pdf'e basalım 
        for i in dosya:
                pdf.drawInlineImage(yol+os.sep+i, 0,0, width=595,height=842)
                pdf.showPage()

        # pdf'e son darbeyi vurmak istiyorum
        pdf.save()

if __name__ == "__main__":
        yol = sys.argv[1]
        isim = yol.split('/')[-2]
        dosya = os.listdir(yol)
        dosya.sort()
        yeni = isim + '.pdf'
        bilgi = [
                        'ONDOKUZ MAYIS ÜNİVERSİTESİ',
                        'MÜHENDİSLİK FAKÜLTESİ',
                        'BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ',
                        '2009-2010 » 1. SINIF 2. DÖNEM',
                        'İNGİLİZCE II',
                        'DERS NOTLARI', ' ',
                        'EMİN EKER', ' ',
                        'DERS ÖĞRETİCİSİ',
                        'EVRİM KEŞMER'
                ]

        bas(yol, isim, yeni, bilgi)

        # daha önce çalıştırılabilir hale getirilen betik sayesinde dosya boyutunu küçültelim
        os.system('tighten-pdf ' + yeni)

        print "\n\n»» %s dosyası oluşturuldu" %yeni


