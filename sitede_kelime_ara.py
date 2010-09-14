#!/usr/bin/python
#-*-coding:utf-8-*-

def sitede_kelime_ara(ne,adress):
    import urllib
    try:
        print 'bağlantı kuruluyor...'
        net_adres = urllib.urlopen(adress)
        text = net_adres.read().decode('utf8')
        print 'bağlantı kuruldu.'
        kac_kez = text.count(ne)
        print 'site içerisinde %s kez "%s" dizgisi geçmektedir.' %(kac_kez , ne)
    except:
        print 'girdiğiniz değerleri veya internet bağlantınızı kontrol ediniz.'
