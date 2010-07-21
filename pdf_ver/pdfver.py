#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb, MySQLdb.cursors

from util import *

def pdfver(aranacak):
    conn = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="emineker",
        db = "deneme"
    )

    tuval = tuval_hazirla('son.pdf')

    SABLON = {
        "no"    : [8, 17],
        "ad"    : [8, 18],
        "soyad" : [8, 19],
        "tc"    : [8, 20],
    }

    veri = {'tc': aranacak}

    for kayit in yinekursor(conn, "SELECT * FROM okul WHERE tc = %(tc)s", veri):
        tuval_bas(tuval, kayit, SABLON)

    tuval.save()

pdfver('32977301484')
