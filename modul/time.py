#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################
# www.istihza.com
#
# tüm zaman saat dilimi işlemlerinizi
# bu modul ile gerçekleyebilirsiniz
#
# emineker                    gruop19
#####################################


import time


# sleep() Fonksiyonu

time.sleep(3) # kodu ile işlemlerinizi 3 saniye bekletebilirsiniz

# fonksiyonu daha iyi anlamak için şu öğreği kullanın
for i in range(10):
        time.sleep(1)
        print i



# strftime() Fonksiyonu

print time.strftime("%m")       # '09' ay
print time.strftime("%d")       # '23' gün
print time.strftime("%x")       # '23/09/10' Ay, gün ve yılı birlikte görmek için
print time.strftime("%d.%m.%Y") # '23.09.2010' ay gün ve yılı verilen şekilde görmek için

# türkçe localleri etkin hale getirelim ve türkiyede kullandığımız gün-ay-yıl sıralamasını elde edebilim
import locale
locale.setlocale(locale.LC_ALL, "tr_TR")
print time.strftime("%x")

# strftime() fonksiyonu ile daha ayrıntılı zaman dilimi değerleri elde edelim
%a      Kısaltılmış gün adı
%A      Tam gün adı
%b      Kısaltılmış ay adı
%B      Tam ay adı
%c      Tam tarih ve saat
%d      Ondalık sayı cinsinden gün (aya göre)
%H      Ondalık sayı cinsiden saat (24 saat hesabına göre)
%I      Ondalık sayı cinsinden saat (12 saat hesabına göre)
%j      Ondalık sayı cinsinden gün (yıla göre)
%m      Ondalık sayı cinsinden ay
%M      Ondalık sayı cinsinden dakika
%S      Ondalık sayı cinsinden saniye
%U      Yıla göre hafta numarası. Pazar haftanın ilk günü olarak alınır
%x      Tam tarih
%X      Tam saat
%y      Yılın son iki hanesi
%Y      Tam yıl gösterimi



# localtime() Fonksiyonu

zaman = time.localtime()
print zaman
# çıktı: time.struct_time(tm_year=2010, tm_mon=8, tm_mday=16, tm_hour=16, tm_min=49, tm_sec=42, tm_wday=0, tm_yday=228, tm_isdst=1)
# Bu demette toplam 9 adet değer bulunur ve bu değerlerin anlamı sudur:

Sıra    Deger           Anlamı
0       tm_year         yıl
1       tm_mon          ay
2       tm_mday         gün
3       tm_hour         saat
4       tm_min          dakika
5       tm_sec          saniye
6       tm_wday         haftanın günü (Pazartesi 0)
7       tm_yday         yıla göre gün
8       tm_isdst        gün ışığından yararlanma uygulamasının olup olmadığını denetler

# bu şekilde de kullanılır
print zaman.tm_year     # çıktı: '2010'



# gmtime(), time() ve ctime() Fonksiyonları

# zamanın başlangıcının ne olduğunu bulmak için gmtime() fonksiyonunu kullanabiliriz
print time.gmtime(0).tm_year    # çıktı: '1970'

# time() adlı başka bir fonksiyonu kullanarak zamanın başlangıcından bu yana kaç saniye geçtiğini bulabiliriz
print time.time()       # çıktı: '1285025564.984'

#i ctime() fonksiyonu ise bize tam tarih ve saat bilgisini gösterir
print time.ctime()      # çıktı : 'Thu Sep 23 23:13:47 2010'

# time() ve ctime() fonksiyonlarını birlikte kullanarak sonraki bir zamanı hesaplayabiliriz.
# Mesela su andan 1 saat sonrasını hesaplamak için şöyle bir sey yazabiliriz
sonraki_tarih = time.time() + 60*60
print time.ctime(sonraki_tarih)         # çıktı: 'Fre Sep 23 00:13:47 2010'

