#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
assert MySQLdb.apilevel == "2.0"

from MySQLdb.cursors import DictCursor
from MySQLdb.cursors import SSDictCursor

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def tuval_hazirla(pdfdosya, yazitipi="FreeSans", punto=9):
    # yazıtipini doğru seçmez isek Türkçe karakterler sorunlu çıkar
    # öntanımlı "FreeSans" gayet yeterli.  şimdi bu yazıtipinin nerede
    # bulacağını söyleyelim (bir ttf dosya)
    pdfmetrics.registerFont(
        TTFont(yazitipi, "/usr/share/fonts/truetype/freefont/" + yazitipi  + ".ttf")
    )
    # verilen dosyayı tuval yapıyoruz
    tuval = canvas.Canvas(pdfdosya)
    # yazıtipi şu olmalı diyoruz
    tuval.setFont(yazitipi, punto)

    return tuval

def tuval_bas(tuval, kayit, sablon):
    """verilen kaydı şablona uygun şekilde tuvale bas"""
    """burada şablon alan: (x, y) koordinat bilgisini taşıyor"""

    # boş bir sözlük alalım, bunu dolduracağız
    kart = {}
    # sablon'da olup verilen kayıtta olmayan alanları takip lazım
    eksikler = []

    # sablondaki her alan için
    for alan in sablon:
        # eksik bir alanı boş dizgi yapıyoruz
        deger = ""
        # alan verilen kayıtta var mı?
        if alan in kayit:
            # var.  dizgiye çevir (tamsayı değerler olabilir)
            deger = str(kayit[alan])
        else:
            # hmm, yok.  eksiklere ekle bunu, raporlama için
            eksikler.append(alan)

        kart[alan] = deger

    # eksikleri raporla bakayım
    for eksik in eksikler:
        print "%(eksik) alanı kayıtta bulunamadı" % eksik

    # artık kartımızdaki her değeri tuvale basacağız
    for alan in kart:
        # tuvalde nereye?  şablon bunun için var.  x ve y koordinatları.
        (x, y) = sablon[alan]
        # boyama yap
        tuval.drawString(x*cm, y*cm, kart[alan])

    # bu sayfa bitti
    tuval.showPage()

    # eksikler bilgisini de dönelim, çağıran için değerli olabilir
    return len(eksikler) == 0

class yinekursor:
    """yinelenebilir kursör sonuçları dön"""
    def __init__(self, baglanti, sorgu, veri = None):
        self._cursor = baglanti.cursor(SSDictCursor)
        self._cursor.execute(sorgu, veri)

    def __iter__(self):
        while True:
            result = self._cursor.fetchone()
            if not result: return
            yield result