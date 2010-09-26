#!/usr/bin/python
#-*-coding:utf-8-*-

from __future__ import division
from Tkinter import *

pencere = Tk()
pencere.title("doğru mu? yanlış mı?")
pencere.geometry("350x150+400+200")
pencere.resizable(width=FALSE,height=FALSE)
Label(pencere , text="\noyunumuzun kuralları basit\ncümleyi okuyun ve\ndoğru yanlış seçeneklerinden birini işaretleyin\n" , fg="#660000" ).pack() 

a="Dünyanın yaşayan\nen büyük hayvanları balinalardır."
b="Bir insan bir günde\nyaklaşık33 bin kez nefes alır."
c="Türkiye şu an\n60. hükümet\ntarafından yönetilmektedir."
d="Bir arı günde 2 bin çiçekten bal alır."
e="Örümcekler 8 ayaklıdır."
f="Her 100 liralık harcamanın\n25 lirası\nİstanbul'da yapılmaktadır."
g="Beşiktaş'ın\n2008/2009 sezonunda\naldığı şampiyonluk\n13. şampiyonluğudur."
h="Robert De Niro\n'Kadın kokusu' filminde\nmüthiş tango sahnesiyle\nmüthiş bir seyir ziyafeti çektirmiştir."
m="'Bir kadına bağlanmak\ndiğerlerini aldatmaktır'\nsözü\nalman yazar Goethe'ye aittir."
n="Yediveren kirazı\nsahip olduğu\nenzimlerden dolayı\nher mevsim yaz çiçek açar."


global x,y,k
x=0
y=0

def basla():
        pencere.destroy()
        soru = Tk()
        soru.title("sorular")
        soru.geometry("350x150+400+200")
        soru.resizable(width=FALSE,height=FALSE)
        bil=Label(soru , text=a , fg="#660000")
        bil.place(relx=0.23 , rely=0.1)

        def ogren():
                sonuc.destroy()
                ogren = Tk()
                ogren.title("öğrenin")
                ogren.geometry("500x250+400+150")
                ogren.resizable(width=FALSE,height=FALSE)
                Label(ogren , text="\nDünyanın yaşayan en büyük hayvanları balinalardır."                           , fg="#660000").pack()
                Label(ogren , text="Bir insan bir günde yaklaşık 23 bin kez nefes alır."                  , fg="#660000").pack()
                Label(ogren , text="Türkiye şu an 60. hükümet tarafından yönetilmektedir."                        , fg="#660000").pack()
                Label(ogren , text="Bir arı günde 4 bin çiçekten bal alır."           , fg="#660000").pack()
                Label(ogren , text="Örümcekler 8 ayaklıdır."                                                       , fg="#660000").pack()
                Label(ogren , text="Her 100 liralık harcamanın\25 lirası İstanbul'da yapılmaktadır."              , fg="#660000").pack()
                Label(ogren , text="Beşiktaş'ın 2008/2009 sezonunda aldığı şampiyonluk 13. şampiyonluğudur."     , fg="#660000").pack()
                Label(ogren , text="Al Pacino 'Kadın kokusu' filminde müthiş tango sahnesiyle\nmüthiş bir seyir ziyafeti çektirmiştir." ,
                                fg="#660000").pack()
                Label(ogren , text="'Bir kadına bağlanmak diğerlerini aldatmaktır' sözü Descartes'a aittir." , fg="#660000").pack()
                Label(ogren , text="Yediveren kirazı sahip olduğu enzimlerden dolayı her mevsim yaz çiçek açar."  , fg="#660000").pack()

        def dogru():
                global x,y,sonuc
                if y==0:
                        bil["text"]=b
                        x+=10
                elif y==1:
                        bil["text"]=c
                elif y==2:
                        bil["text"]=d
                        x+=10
                elif y==3:
                        bil["text"]=e
                elif y==4:
                        bil["text"]=f
                        x+=10
                elif y==5:
                        bil["text"]=g
                        x+=10
                elif y==6:
                        bil["text"]=h
                        x+=10
                elif y==7:
                        bil["text"]=m
                elif y==8:
                        bil["text"]=n
                elif y==9:
                        x+=10
                        soru.destroy()
                        sonuc = Tk()
                        sonuc.title("sonuç")
                        sonuc.geometry("200x150+400+200")
                        sonuc.resizable(width=FALSE,height=FALSE)    
                        Label(text=("\nteprikler\npuanınız\n",x,"\n\n") , fg="#660000").pack()
                        Button(sonuc , text="öğrenin" , fg="#660000" , command=ogren).pack()
                y+=1
        def yanlis():
                global x,y,sonuc
                if y==0:
                        bil["text"]=b
                elif y==1:
                        bil["text"]=c
                        x+=10
                elif y==2:
                        bil["text"]=d
                elif y==3:
                        bil["text"]=e
                        x+=10
                elif y==4:
                        bil["text"]=f
                elif y==5:
                        bil["text"]=g
                elif y==6:
                        bil["text"]=h
                elif y==7:
                        bil["text"]=m
                        x+=10
                elif y==8:
                        bil["text"]=n
                        x+=10
                elif y==9:
                        soru.destroy()
                        sonuc = Tk()
                        sonuc.title("sonuç")
                        sonuc.geometry("200x150+400+200")
                        sonuc.resizable(width=FALSE,height=FALSE)    
                        Label(text=("\nteprikler\npuanınız\n",x,"\n\n") , fg="#660000").pack()
                        Button(sonuc , text="öğrenin" , fg="#660000" , command=ogren).pack()
                y+=1

        dogru=Button(soru , text="doğru" ,fg="#660000" , command=dogru)
        dogru.place(relx=0.2 , rely=0.6)
        yanlis=Button(soru , text="yanlış" , fg="#660000" , command=yanlis)
        yanlis.place(relx=0.6 , rely=0.6)

Button(pencere , text="BAŞLA" , fg="white" , bg="black", width=8 ,
       command=basla).pack()

mainloop()



