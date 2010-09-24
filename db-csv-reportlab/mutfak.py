#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb, MySQLdb.cursors, csv, sys

def kucult(dizgi):
        return dizgi.decode('utf-8').lower().encode('utf-8')

def buyult(dizgi):
        return dizgi.decode('utf-8').upper().encode('utf-8')

def ilkbuyult(dizgi):
        return " ".join(s.decode('utf-8').lower().capitalize().encode('utf-8') for s in dizgi.split()   )

def baglan():
        return MySQLdb.connect(host = "localhost",
                               user = 'root',
                               passwd = "emineker",
                               db = 'deneme' ) #,cursorclass = MySQLdb.cursors.DictCursor,) # veritabanının sözlük halinde gelmesi için

def csvyukle(tablo, filename):
        try:
                con = baglan()
        except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit (1)

        cursor = con.cursor()
        dosya  = csv.reader(open(filename))
        sutun  = len(dosya.next())

        assert(sutun > 0)
        toplam = (sutun-1) * "%s, " + "%s"
        query = ("insert into %s" % tablo) + (" values (%s)" % toplam)
        def f(x):
                if(x == ""):
                        return None
                else:
                        return x
        for line in dosya:
                veri = [f(x) for x in line]
                try:
                        cursor.execute(query, veri)
                except: 
                        print 'bu kayıt bulunmakta'
        cursor.close()
        conn.close()


def db_baglan( tablo ):
        cursor = baglan().cursor()
        cursor.execute("SELECT * FROM %s" % tablo)
        #cursor.rowcount  #tablodaki satır sayısı
        return cursor.fetchall()


def db_ara( tablo , ara ):
        return [satir for satir in db_baglan( tablo ) if ara in satir]


def db_csv_olustur( tablo ):
        dosya = open('data.csv' , 'w')
        yazici = csv.writer( dosya )
        for i in db_baglan( tablo ):
                yazici.writerow(i)
        dosya.close()


def csv_kopyala(dosya_yolu):
        dosya = open('data.csv' , 'w')
        yazici = csv.writer(dosya)
        for liste in csv_oku(dosya_yolu):
                yazici.writerow(liste)


def kucult_csv(dosya_yolu ):
        yazici = csv.writer( open('data.csv' , 'w') )
        [yazici.writerow( [kucult(i) for i in liste] ) for liste in csv_oku(dosya_yolu)]


def csv_oku(dosya):
        okunan = csv.reader( open(dosya) )
        return [ [i for i in oge] for oge in okunan][1:]


def csv_yaz(liste):
        dosya= open('data.csv' , 'w') 
        yazici = csv.writer(dosya)
        for i in liste:
                yazici.writerow(i)        
        dosya.close()  


def create_table(tablo):
        con    = baglan()
        cursor = con.cursor()
        sql = """CREATE TABLE %s (
                 SIRA  INT(100) NOT NULL AUTO_INCREMENT ,
                 AD    VARCHAR(30) NOT NULL default '' ,
                 SOYAD VARCHAR(30) NOT NULL default '' ,
                 TC_NO VARCHAR(30) NOT NULL default '' ,
                 PRIMARY KEY (SIRA , TC_NO))""" %( tablo )
        try:
                cursor.execute(sql)
                print "»» veritabanında " + tablo + " tablosu oluşturuldu"
        except:
                print "»» böyle bir tablo var veya bağlantı hatası"



