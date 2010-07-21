#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb , MySQLdb.cursors , csv

def send_csv_to_mysql(dosya_yolu):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="emineker",
                         db="deneme")  
    cursor = db.cursor()

    dosya = open( dosya_yolu , "r")
    okunan = csv.reader(dosya)
    for i in okunan:
        no    = i[0]
        ad    = i[1]
        soyad = i[2]
        tc    = i[3]
        s = """insert into okul (no , ad , soyad , tc) values (%s , %s , %s , %s)"""
        cursor.executemany(s , [(no , ad , soyad , tc)])

    cursor.close()
    db.close()

send_csv_to_mysql("/home/emin/Masaüstü/kull.csv")
