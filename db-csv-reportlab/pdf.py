#!/usr/bin/python
# -*- coding: utf-8 -*-

from mutfak import *
import MySQLdb, csv, sys
assert MySQLdb.apilevel == "2.0"

from MySQLdb.cursors import DictCursor
from MySQLdb.cursors import SSDictCursor

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def tuval_hazirla(pdfdosya, yazitipi="FreeSans", punto=12):
    pdfmetrics.registerFont(
        TTFont(yazitipi, "/usr/share/fonts/truetype/freefont/" + yazitipi  + ".ttf") )
    tuval = canvas.Canvas(pdfdosya)
    tuval.setFont(yazitipi, punto)
    return tuval


def tuval_bas(arguman , tablo , ara=0 ):
        try:
                if arguman=='-csv':
                        data = csv_oku( tablo )
                elif arguman=='-db':
                        data = db_baglan( tablo )
                elif arguman=='-ara':
                        data = db_ara(tablo , ara)
                elif arguman=='-ex':
                        data=tablo
                else:
                        print 'hop dur orda'            
                        sys.exit()
        
                tuval = tuval_hazirla('data.pdf')

                x,y = 3,27
                for liste in data:
                        if y==27:
                                for i in baslik():
                                        tuval.drawString(x*cm, y*cm, i)
                                        x+=4
                                        y-=1
                        x=3
                        y-=1
                        for i in liste:
                                tuval.drawString(x*cm, y*cm, str(i)) ; x+=4
                                if y==3:
                                        tuval.showPage()
                                tuval.setFont("FreeSans", 12)
                                x,y = 3,27
                tuval.save()
                print '»» pdf oluşturuldu'
        except:
                print '»» yanlış argüman kullanımı'



