#!/usr/bin/python
# -*- coding: utf-8 -*-

import shutil

# dosya kopyalama
shutil.copy(kopyalanacak_dosya_yolu , kopyalanacak_yer)

# dosya ve dizin taşıma
shutil.move(kopyalanacak_dosya_yolu , kopyalanacak_yer)

# dizin silme
shutil.rmtree(dizin_adi)

# ortak dizinin içeriğini 'yedek' dizini altına kopyalar
shutil.copytree("ortak", "yedek/")


