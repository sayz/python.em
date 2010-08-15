#!/usr/bin/python
# -*- coding: utf-8 -*-

from pdf import *
from mutfak import *

liste = [['3' , 'EMİN' , 'eker'  , '68'] ,
         ['3' , 'emin' , 'soyad' , '69'] ,
         ['3' , 'emin' , 'soyaD' , '70']]

[[kucult(i) for i in oge] for oge in liste]



#kucult_csv('okul.csv')

#print [ oge for oge in liste][1:]

#print [kucult(j) for i in liste for j in i]

#kucult_kopya_csv('okul.csv')
#print csv_oku('okul.csv')

#create_table('yenil')
#db_csv_gonder('yenil' , 'okul.csv')

#tuval_bas('-csv' , 'okul.csv')
#tuval_bas('-ex' , liste)
#tuval_bas('-db' , 'hop')
#tuval_bas('-ara'  , 'hop' , '22949558510')


#csv_sirala('okul.csv')
#print csv_oku('okul.csv')


