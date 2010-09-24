#!/usr/bin/python
# -*- coding: utf-8 -*-

import commands

# tüm komut işlemlerinizi yürütebileceğiniz bir fonksiyon
commands.getoutput('sudo apt-get install ruby')

# tüm komut işlemlerini yürütüp sonucu bir tuple olarak döndüren bir fonksiyo
commands.getstatusoutput('ls')

# konsoldaki ls -ld çıktısı ile aynı çıktıyı verir
# verilen dosyanın yazılabilirlik, yazım tarihi boyutu gibi bilgilerini verir
commands.getstatus('top')


# diğer bir şekliyle
outtext = commands.getoutput( komut )
(status , outtext) = commands.getstatusoutput( komut )
commands.getstatus( dosya )


