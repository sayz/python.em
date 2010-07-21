#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb , MySQLdb.cursors

def send_data_to_mysql(no , ad , soyad , tc):
    db = MySQLdb.connect(host="localhost",user="root",passwd="emineker",db="deneme")  
    cursor = db.cursor()

    s = """insert into okul (no , ad , soyad , tc) values (%s , %s , %s , %s)"""
    cursor.executemany(s , [(no , ad , soyad , tc)])

    cursor.close()
    db.close()
