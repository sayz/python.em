#!/usr/bin/python
# -*- coding: utf-8 -*-

import anydbm

# database adında bir veritabanı oluşturalım
db = anydbm.open("database", "c")
db["1"] = "one"
db["2"] = "two"
db["3"] = "three"
db.close()
# veritabına eklemeler yaptıktan sonra kapatıyoruz

# şimdi de veritabanı bigilerine ulaşalım
db = anydbm.open("database", "r")
# db artık bir sözlük
for key in db.keys():
        print repr(key), repr(db[key])



