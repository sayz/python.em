#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import MySQLdb , MySQLdb.cursors
assert MySQLdb.apilevel == "2.0"
from MySQLdb.cursors import DictCursor
from MySQLdb.cursors import SSDictCursor
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def tuval_hazirla(pdfdosya, yazitipi="FreeSans", punto=14):
    pdfmetrics.registerFont(
        TTFont(yazitipi, "/usr/share/fonts/truetype/freefont/" + yazitipi  + ".ttf"))
    tuval = canvas.Canvas(pdfdosya)
    tuval.setFont(yazitipi, punto)
    return tuval

def tuval_bas(tuval, kayit):
    baslik = "database bilgileri"
    tuval.drawString(8*cm, 24*cm, baslik)
    x,y = 7,22
    alan  = ["no" , "ad" , "soyad" , "tc"]   #hop#
    for anahtar in alan:
        tuval.drawString(x*cm, y*cm, anahtar)
        deger = "»  " + str(kayit[anahtar])
        tuval.drawString((x+3)*cm, (y)*cm, deger)  ;   y-=1
    tuval.showPage()

class yinekursor:
    def __init__(self, baglanti, sorgu, veri = None):
        self._cursor = baglanti.cursor(SSDictCursor)
        self._cursor.execute(sorgu, veri)
    def __iter__(self):
        while True:
            result = self._cursor.fetchone()
            if not result: return
            yield result

def pdfver(aranan):
    conn = MySQLdb.connect(host="localhost",user="root",
                           passwd="emineker",db = "deneme")
    cursor = conn.cursor()
    cursor.execute("select * from okul")
    result = cursor.fetchall()
    for i in result:
        if aranan in i:
            tuval = tuval_hazirla('data.pdf')
            veri = {'tc': aranan}
            for kayit in yinekursor(conn, "SELECT * FROM okul WHERE tc = %(tc)s", veri):
                tuval_bas(tuval, kayit)
            tuval.save()
            print "pdf dosyanız 'data.pdf' adı altında oluşturuldu"

        else:
            print aranan + ' içerikli bir veri kaydı yok'

pdfver( sys.argv[1] )
