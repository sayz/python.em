#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

for i in range(4):
    # 0 ile 1 arasında bir seçim yapalım sayının türü doğal olarak float gelecek
    print random.random(),
    # 10 ile 20 arasında float sayı türünde seçim yapıyoruz
    print random.uniform(10, 20),
    # 10 ile 100 arasında tamsayı türünden seçim yapalım
    print random.randint(100, 1000),
    # 100 ile 1000 arasında 3'er 3'er giden sayılar arasından interger türünden sayı seçelim
    print random.randrange(100, 1000 , 3)



