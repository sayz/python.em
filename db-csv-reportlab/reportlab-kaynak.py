#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import *

def faktar():
        import os
        for yazitipi in os.listdir('/usr/share/fonts/truetype/freefont'):
                'türkçe karakter destekli fontlarımızı içe aktaralım'
                'FreeSans, FreeSansBold, FreeSansOblique, FreeSansBoldOblique'
                yazitipi = yazitipi[:-4]
                registerFont(TTFont(yazitipi,'/usr/share/fonts/truetype/freefont/' + yazitipi + '.ttf'))

c = canvas.Canvas('test.pdf')
c.drawString(400,800, 'selam millet')
c.save()



"""
A4=(595.27559055118104, 841.88976377952747)     # standart  A4 kağıdı
A4[::-1]                                        # yatay A4 sayfası için kullan
cm  =28.3464566929                              # cm'nin boyutu
inch=72.0                                       # inch boyutu
dik =(21*cm , 30*cm)                            # bir sayfanın cm türünden boyutu

c = canvas.Canvas('test.pdf' , pagesize=A4)     # pdf oluştur
c.setTitle('hooooooooop')                       # pdf'ye başlık ver
c.setAuthor('emin')                             # pdf'yi yazan kişi
c.setSubject('deneme')                          # pdf özelliklerinden konu kısmı
c.showPage()                                    # bir sonraki sayfaya geçirir
c.setFont('Helvetica', 12)                      # kendi fontunu belirle
c.drawString(100,800,"merhaba")                 # yazı yaz
c.drawCentredString(21*cm/2.0,27*cm,'center')   # sayfayı ortala yaz

c.saveState()                                   # yazıtipini kaydeder
c.translate(2.4*inch, 1.5*inch)                 # (0,0) noktasını yer değştirir
c.restoreState()                                # başlangıcı (0,0) noktasına çeker
c.getPageNumber()                               # sayfa numarasını verir
c.line(480,747,580,747)                         # çizgi çizer
c.rect(100,100,20,20)                           # kutu çizer
c.circle(30, 50, 50, stroke=1, fill=1)          # çember çizer
c.setStrokeColor(pink)                          # ızgaranın rengini belirle
c.grid([30,60,90], [30,60,90])                  # ızgara çiz

c.scale(0.5, 0.5)           # sayfayı verilen oranlarda küçültüp (0,0)'dan basar
c.setFillColor(yellow)      # yazı rengini belirler
c.setFillColorRGB(1,0,1)    # yazı rengini RGB cinsinden verir
c.setLineWidth(cm/4)        # çizginin kalınlığını belirler
c.setLineWidth(.4)          # noktalı verirsek çizgiyi belirginleştirir 1 ile 9 arası bir değer
c.setStrokeColor(green)     # şekilerin renklerini belirler içlerini de doldurur

c.drawInlineImage('top.jpg', 10,200, width=None,height=None)    # resim bas
"""


