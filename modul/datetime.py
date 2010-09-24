#!/usr/bin/python
# -*- coding: utf-8 -*-

###################################
# www.istihza.com
#
# tüm zaman dilimi işlemlerinizi
# bu modül ile gerçekleyebilirsiniz
#
# emineker                  gruop19
###################################


import datetime


# Bugünün Tarihini Bulmak

bugun = datetime.date.today()                                   # bugünün tarihini alalım
print bugun                                                     # çıktı: 2010-07-08
print "%s yılındayız!" %bugun.year                              # çıktı: 2010 yılındayız!
print "%s yılının %s. ayındayız!" %(bugun.year, bugun.month)    # çıktı: 2010 yılının 7. ayındayız!
print "%s. ayın %s. günündeyiz!" %(bugun.month, bugun.day)      # çıktı: 7. ayın 8. günündeyiz!


# Bir Tarihin Hangi Güne Geldigini Bulmak

bugun = datetime.date.today()
print bugun.weekday()                   # çıktı: 3

"""
Sayı    Gün
0       Pazartesi
1       Salı
2       Çarşamba
3       Perşembe
4       Cuma
5       Cumartesi
6       Pazar
"""

tarih = datetime.date(2010, 5, 30)      # Burada, 30 Mayıs 2010 tarihini belirttik » 'yıl-ay-gün'
print tarih                             # çıktı: 2010-05-30


# Tarihlerle Aritmetik işlem Yapmak

bugun = datetime.date.today()   # bugünün tarihini aldık
fark = datetime.timedelta(1)    # kaç gün öncesini bulmak istiyorsak
dun = bugun - fark              # farkı bulalım
print dun                       # 2010-07-08
print dun.strftime("%A")        # strftime() fonksiyonunu kullanarak doğrudan gün adını da alalım
'Perşembe'


# NOT: tarih dilimlerini daha istediğiniz karakter düzenine uygun alabilmek için strftime() fonksiyonu var
# strftime() fonksiyonu daha ayrıntılı kullanımı için time modülü içerisindeki anlatımını inceleyebilirsiniz

