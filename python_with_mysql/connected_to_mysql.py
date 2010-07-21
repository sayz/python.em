#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb , MySQLdb.cursors

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="emineker",
                     db="deneme")  
cursor = db.cursor()  

cursor.execute("select * from okul")  
result = cursor.fetchall()
 
print result           # tüm bilgileri ekrana döker
print cursor.rowcount  #tablodaki satır sayısı

cursor.close()
db.close()  

