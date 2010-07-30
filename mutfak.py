#!/usr/bin/python
#!-*- coding:utf-8 -*-

import MySQLdb, MySQLdb.cursors , csv , sys


def kucult(dizgi):
    return dizgi.decode('utf-8').lower().encode('utf-8')

def buyult(dizgi):
    return dizgi.decode('utf-8').upper().encode('utf-8')

def ilkbuyult(dizgi):
    return " ".join(s.decode('utf-8').lower().capitalize().encode('utf-8') for s in dizgi.split()   )

def baslik():
    return ["SIRA" , "AD" , "SOYAD" , "TC_NO"]

def cursor_baglan():
    db = MySQLdb.connect(host="localhost",user="root",passwd="emineker",db="deneme")
    return db.cursor()

def baglan( tablo ):
    cursor = cursor_baglan()
    cursor.execute("SELECT * FROM %s" % tablo)
    data  = cursor.fetchall()
    #cursor.rowcount  #tablodaki satır sayısı
    liste=list()
    for i in data:  liste.append(i)
    db.close() ; cursor.close()
    return liste


def db_ara( tablo , ara ):
    liste = list()
    for i in baglan( tablo ):
        if ara in i:
            liste.append(i)
    return liste


def db_bilgicek(tablo , tc):
    data = baglan(tablo)
    tc = str(tc)
    for i in data:
        if i[3] in tc:
            print 'SIRA  : ' + i[0]
            print 'AD    : ' + i[1]
            print 'SOYAD : ' + i[2]
            print 'TC    : ' + i[3]


def db_csv_olustur( tablo ):
    dosya  = open('data.csv' , 'w')
    yazici = csv.writer(dosya)
    yazici.writerow(baslik())    
    for i in baglan( tablo ):   yazici.writerow(i)


def csv_kopyala(eski_dosya , yeni_dosya):
    eski_dosya = open(eski_dosya , "r") ; okunan = csv.reader(eski_dosya)
    yeni_dosya = open(yeni_dosya , "w") ; yazici = csv.writer(yeni_dosya)
    for liste in okunan:                  yazici.writerow(liste)
    eski_dosya.close()                  ; yeni_dosya.close()


def csv_sirala(dosya_yolu):
    data = csv_oku(dosya_yolu)
    k=1
    dosya = open('data.csv' , 'w')
    yazici= csv.writer(dosya)
    yazici.writerow(baslik())
    for i in data:
        yedek=list()
        yedek.append(str(k))
        yedek.append(i[1])
        yedek.append(i[2])
        yedek.append(i[3])
        yazici.writerow(yedek)
        k+=1


def kucult_kopya_csv(eski_dosya , yeni_dosya):
    eski_dosya = open(eski_dosya , "r") ; okunan = csv.reader(eski_dosya)
    yeni_dosya = open(yeni_dosya , "w") ; yazici = csv.writer(yeni_dosya)

    for liste in okunan:
        for j in liste:
            liste.append(kucult(liste[0]))
            del liste[0]
        yazici.writerow(liste)

    eski_dosya.close()  ;  yeni_dosya.close()


def csv_oku(dosya_yolu):
    dosya  = open(dosya_yolu)  ;  okunan = csv.reader(dosya)
    liste  = list()
    for oge in okunan:
        yedek = list()
        for i in oge:      yedek.append(i)
        liste.append(yedek)
    del liste[0]
    return liste


def create_table(tablo):
    cursor = cursor_baglan()
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


def db_veri_gonder(tablo , liste):
    cursor = cursor_baglan()
    s = """insert into """ + tablo + """ (SIRA , AD , SOYAD , TC_NO) values (%s , %s , %s , %s)"""
    try   : cursor.executemany(s , [liste])
    except: print '»» bu kayıt zaten bulunmakta'


def db_csv_gonder(tablo , dosya_yolu):
    cursor = cursor_baglan()
    okunan = csv_oku(dosya_yolu)
    s = """insert into """ + tablo + """ (SIRA , AD , SOYAD , TC_NO) values (%s , %s , %s , %s)"""
    k=0
    for i in okunan:
        try   :  cursor.executemany(s , [i] )
        except:  k+=1  ;  print i[3]

    if k==0:     print "»» csv kayıtları " + tablo + " tablosuna gönderildi"
    else:        print '»» toplam ' + str(k) + ' kayıt çakışmaktadır'


