#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# kullanılan işletim sistemini gösterir
>>> os.name

# konsol işlemlerinin yürütüldüğü fonksiyon
>>> os.system()

#çalışma dizinini verir
>>> os.getcwd()

# çalışma dizinini değiştir
>>> os.chdir('/home/emin/Masaüstü')

# verilen dizinin içerisindekileri gösterir
>>> os.listdir('/home/emin/Masaüstü')

# bulunulan dizin içeriğini döker
>>> os.listdir(os.curdir)

# bir üst dizinin içeriğini döker
>>> os.listdir(os.pardir)

# boş satır ekler
>>> os.linesep

# '/' koyar (sistemine göre değişir)
>>> os.sep

# bulunduğun dizine resimler dizini ekler
>>> os.path.join(os.getcwd()+os.sep, 'resimler')

# sistemin kullandığı dil bilgisini verir
>>> os.getenv('LANG')

# 0 dönüyorsa kullanıcı root 1000 dönüyorsa değil
>>> os.getuid()

# dizin oluştur
>>> os.mkdir( dizin_adi )

# dizinler oluştur
>>> os.makedirs( dizin1/dizin2 )

# dizin sil
>>> os.rmdir('/home/emin/HOP'

# dizinleri sil boş olmak şartıyla
>>> os.removedirs("test1/test2")

# bulunduğun dizinden dosyayı silme
>>> os.remove("deneme.txt")

# isim değiştir test'i deneme yap
>>> os.rename("test.txt","deneme.txt")

# bir üst dizini gösterir dosyanın var olup olmadığına bakmaz
>>> os.path.dirname('/home/emin/Masaüstü')
'/home/emin'

# bulunduğu dizini verir dosyanın var olup olmadığına bakmaz
>>> os.path.basename('/home/emin/Masaüstü')
'Masaüstü'

# dosyanın bulunduğu tüm dizini verir dosyanın var olup olmadığına bakmaz
>>> os.path.abspath("python.pdf")
'/home/emin/python.pdf'

# bir dosyanın veya dizinin var olup olmadığını gösterir
>>> os.path.exists('/home/emin/Masaüstü/python.pdf')

# yolun dizin olup olmadığını kontrol eder
>>> os.path.isdir('/home/emin/Masaüstü/falanca.pdf')

# yolun dosya olup olmadığını kontrol eder
>>> os.path.file('/home/emin/Masaüstü/deneme.txt')

# dosya ve dizin adını birbirinden ayırır
>>> os.path.split("/home/emin/Masaüstü/python.pdf")
(’/home/emin/Masaüstü’, ’python.pdf’)

# bir dosyanın adıyla uzantısını tuple olarakbirbirinden ayırır
>>> os.path.splitext("python.pdf")
(’python’, ’.pdf’)

# bir dosyanın boyutunu verir bayt cinsiznden
>>> os.path.getsize('Masaüstü') 

# oturum kullanıcı adını verir
>>> os.getlogin()
'emin'

# dosyanın tamyolunu verir
>>> os.path.expanduser("~/.pythonrc")
'/home/effbot/.pythonrc'

# tüm sistem bilgilerini öğrenebiliriz 
for i in os.environ.keys():
        print i  , '»»' , os.environ[i]


# bir dosyanın oluşturulma ve erişim zamanlarını verir
import time    
stat_info = os.stat('os_modul') 
print 'Mode    :', stat_info.st_mode
print 'Created :', time.ctime(stat_info.st_ctime)
print 'Accessed:', time.ctime(stat_info.st_atime)
print 'Modified:', time.ctime(stat_info.st_mtime)





