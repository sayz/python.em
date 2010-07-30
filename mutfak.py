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

def db_baglan( tablo ):
    cursor = cursor_baglan()
    cursor.execute("SELECT * FROM %s" % tablo)
    #cursor.rowcount  #tablodaki satır sayısı
    return cursor.fetchall()


def db_ara( tablo , ara ):
    return [i for i in db_baglan( tablo ) if ara in i]

def db_bilgicek(tablo , tc):
    data = db_baglan(tablo)
    tc = str(tc)
    for i in data:
        if i[3] in tc:
            print 'SIRA  : ' + str( i[0] )
            print 'AD    : ' + str( i[1] )
            print 'SOYAD : ' + str( i[2] )
            print 'TC    : ' + str( i[3] )


def db_csv_olustur( tablo ):
    yazici = csv.writer( open('data.csv' , 'w') )
    yazici.writerow(baslik())    
    for i in db_baglan( tablo ):   yazici.writerow(i)


def csv_kopyala(dosya_yolu):
    yazici = csv.writer( open('data.csv' , 'w') )
    yazici.writerow(baslik())
    for liste in csv_oku(dosya_yolu):   yazici.writerow(liste)


def csv_sirala(dosya_yolu):
    yazici= csv.writer( open('data.csv' , 'w') )
    data = csv_oku(dosya_yolu)
    yazici.writerow(baslik())
    SIRA=1
    for i in data:
        i[0]=str(SIRA) ; yazici.writerow(i) ; SIRA+=1


def kucult_csv(dosya_yolu ):
    yazici = csv.writer( open('data.csv' , 'w') )
    yazici.writerow(baslik())
    [yazici.writerow( [kucult(i) for i in liste] ) for liste in csv_oku(dosya_yolu)]


def csv_oku(dosya_yolu):
    okunan = csv.reader( open(dosya_yolu) )
    return [ [i for i in oge] for oge in okunan][1:]


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
        try   :  cursor.execute(s , i )
        except:  k+=1

    if k==0:     print "»» csv kayıtları " + tablo + " tablosuna gönderildi"
    else:        print '»» toplam ' + str(k) + ' kayıt çakışmaktadır'


