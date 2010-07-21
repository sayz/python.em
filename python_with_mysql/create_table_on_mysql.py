#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb , MySQLdb.cursors

def create_table_on_mysql():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="emineker",
                         db="deneme")  
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS yeni")

    sql = """CREATE TABLE yeni (
             deneme1  CHAR(20) NOT NULL,
             deneme2  CHAR(20),
             deneme3 INT(18),  
             deneme4 CHAR(1),
             INCOME FLOAT )"""

    cursor.execute(sql)
    db.close()

