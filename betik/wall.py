#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################
# belirlenen siteden tüm resimlerin indirme
#
# emineker                          group19
###########################################

import mechanize, cookielib, os, sys, re, BeautifulSoup

url   = "http://www.wallbase.net/wallpaper/"    # sitenin ismini belirleyelim
basla = 100106                                  # baslangic resmi numarasi
test  = 3                                       # test icin resim sayisi
dizin = os.getcwd()                             # dizin olarak çalışma dizinini seçelim siz değiştirebilirsiniz

dizin = os.path.join( dizin , "foto" )          # indirilecek dosyalara dizin başlangıcı 
if not os.path.isdir(dizin):
        os.mkdir(dizin)

os.chdir(dizin)                                 # çalışma dizinini değiştirelim

inenler = [os.path.splitext(dosya)[0] for i,j,k in os.walk(dizin) for dosya in os.listdir(i)]       # indirilmis resimler listesi
indir   = list()                                # indirilecek resimler listesi

# indirilecek resimlerin listelenmesi
for dosya in range(basla , basla+test):
        if str(dosya) not in inenler:
                indir.append(str(dosya))
        else:
                print str(dosya) + ' dosyası zaten var'


br = mechanize.Browser()                        # Tarayiciyi baslat
cj = cookielib.LWPCookieJar()                   # Cookieleri aktif et
br.set_cookiejar(cj)

# Handlerlari aktif et
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)


# resmi indirme fonksiyonu
def image_get(resim_no):
        br.open(url+resim_no)                           # sayfayi tarayici ile acmak
        html = br.response().read()                     # sayfayi html olarak okumak
        soup = BeautifulSoup.BeautifulSoup(html)        # html'i beautifulsoup ile derlemek
        resim_div = soup.find('div', {'id':'bigwall','class':'right'})        # resmin icinde bulundugu "div" bulur
        if not resim_div:
                print '\n%s numaralı bulunamadı'%resim_no
                return
        link   = resim_div.find('img').attrs[0][1]          # resmin linki
        uzanti = soup.find("span", {'class':re.compile('right imgtype*')})
        uzanti = uzanti.contents[0].lower()           #resmin uzantisi
        dosya_adi = os.path.join( dizin , resim_no+'.'+uzanti )
    
        try:
                br.retrieve(link , dosya_adi)[0]    # resmin siteden cekilmesi ve kaydedilmesi
        except:
                print "indirme hatası; internet bağlantınızı kontrol ediniz..."
                sys.exit()


if __name__ == "__main__":
        #indirilecek resimleri sırasıyla indirmeye gönderelim
        toplam = len(indir)
        count  = 1
        for image in indir:
                percent = (float(count) / toplam)*100.0
                sys.stdout.write("indiriliyor... %3.2f%% %d. dosya (%d dosyadan)\r" % (percent, count, toplam) )
                sys.stdout.flush()
                image_get(image)
                count += 1
        print "\ntüm indirmeler tamamlandı..."


