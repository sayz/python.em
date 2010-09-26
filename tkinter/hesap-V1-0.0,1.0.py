#!/usr/bin/python
#-*-coding:utf-8-*-

from __future__ import division
from Tkinter import *
import math, webbrowser

pencere = Tk()
pencere.title("hesap makinası")
pencere.geometry("250x280+500+150")
pencere.resizable(width=FALSE,height=FALSE)

liste = list()
def giris_0():
        ekran.insert(END,0)
def giris(i):
        if i in "123456789":
                ekran.insert(END,i)
def giris_C():
        ekran.delete(0,END)
def giris_carpi():
        liste.append( ekran.get() )
        liste.append("*")
        ekran.delete(0,END)
def giris_bolu():
        liste.append( ekran.get() )
        liste.append("/")   
        ekran.delete(0,END)
def giris_arti():
        liste.append( ekran.get() )
        liste.append("+")
        ekran.delete(0,END)
def giris_eksi():
        liste.append( ekran.get() )
        liste.append("-")
        ekran.delete(0,END)
def giris_sin():
        ekran.delete(0,END)
        ekran.insert(END , math.sin(math.radians( float( ekran.get() ) ) ) )
def giris_cos():
        ekran.delete(0,END)
        ekran.insert(END , math.cos(math.radians( float( ekran.get() ) ) ) )
def giris_tan():
        ekran.delete(0,END)
        ekran.insert(END , math.tan( float( ekran.get() ) ) )
def giris_cot():
        ekran.delete(0,END)
        ekran.insert(END , 1/(math.cos( float( ekran.get() ) )) )    
def giris_kok():
        ekran.delete(0,END)
        ekran.insert(END , math.sqrt( float( ekran.get() ) ) )
def giris_x():
        i=float( ekran.get() )
        j=i
        while i >= 2:
                i-=1
                j=j*i
        ekran.delete(0,END)
        ekran.insert(END,j)    
def giris_log():
        ekran.delete(0,END)
        ekran.insert(END , math.log10( float( ekran.get() ) ) )    
def giris_ln():
        ekran.delete(0,END)
        ekran.insert(END, math.log(math.e , float( ekran.get() ) ) )
def giris_MS():
        if ekran.get()!="":
                ekran.delete(0,END)
                ekran2.delete(0,END)
                ekran2.insert(END, ekran.get() )
def giris_DEL():
        ekran.delete( len( ekran.get() )-1 , END)    
def giris_nokta():
        ekran.insert(END,".")
def giris_esittir():
        j = float( ekran.get() )
        if j == 0:
                ekran.insert(0,"ERROR")
        i=float( liste.pop(0) )
        sonuc = {"*":i*j , "/":i/j,"+":i+j,"-":i-j}
        ekran.delete(0 , END )    
        ekran.insert(0 , sonuc[liste.pop(0)] )

#fonksiyonlar    
def giris_fonksiyon():
        fonksiyon = Tk()
        fonksiyon.title("Fonksiyonlar")
        fonksiyon.geometry("250x90+500+455")
        fonksiyon.resizable(width=FALSE,height=FALSE)    
        Button(fonksiyon, text="sin", fg="#660000", width=4, height=2, command = giris_sin).grid(row=0, column=0)
        Button(fonksiyon, text="cos", fg="#660000", width=4, height=2, command = giris_cos).grid(row=0, column=1)
        Button(fonksiyon, text="tan", fg="#660000", width=4, height=2, command = giris_tan).grid(row=0, column=2)
        Button(fonksiyon, text="cot", fg="#660000", width=4, height=2, command = giris_cot).grid(row=0, column=3)
        Button(fonksiyon, text="^x" , fg="#660000", width=4, height=2, command = giris_kok).grid(row=1, column=0)
        Button(fonksiyon, text="x!" , fg="#660000", width=4, height=2, command = giris_x  ).grid(row=1, column=1)
        Button(fonksiyon, text="log", fg="#660000", width=4, height=2, command = giris_log).grid(row=1, column=2)
        Button(fonksiyon, text="ln" , fg="#660000", width=4, height=2, command = giris_ln ).grid(row=1, column=3)

#hakkında
def hakkinda():
        hakkinda = Tk()
        hakkinda.title("Hakkında")
        hakkinda.geometry("160x180+550+200")
        hakkinda.resizable(width=FALSE,height=FALSE)
        Label(hakkinda,text="*SIRADIŞI*\ncorporation\n\nhesapcık\nV1 0.0,1.0\n\nLisans:\ntabiki özgür\n", fg="#660000" ).pack()
        url = Label(hakkinda,text="websites\nbil.omu.edu.tr",fg="#660000")
        url.pack()
        def tikla(env=None):
                webbrowser.open('http://bil.omu.edu.tr')
        def ust(env=None):
                url["fg"] = "darkblue"
        def terket(env=None):
                url["fg"]="#660000"
        url.bind("<Button-1>",tikla)
        url.bind("<Enter>",ust)
        url.bind("<Leave>",terket)

Button( text="hakkında", fg="#660000", width=6, height=1, command = hakkinda).grid(row=7,column=1,columnspan=2,ipady=2)


#ekranlar
ekran = Entry(width=22)
ekran.grid(row=1, column=0,  columnspan=3, ipady=3)
ekran2 = Entry(width=7)
ekran2.grid(row=1, column=3, columnspan=1, ipady=1)

#butonlar
numara_liste = ["7","8","9",
                "4","5","6",
                "1","2","3", ]

satir, sutun = 3, 0
for i in numara_liste:
        komut=lambda x=i:giris(x)
        etiket=Button(text=i, fg="#660000",width=4,height=2,command=komut)
        etiket.grid(row=satir,column=sutun)
        sutun+=1
        if sutun>2:
                satir+=1
                sutun=0

Button( text="FONKS", fg="#660000", width=4, height=2, command = giris_fonksiyon).grid(row=2, column=0)
Button( text="MS"   , fg="#660000", width=4, height=2, command = giris_MS       ).grid(row=2, column=1)
Button( text="DEL"  , fg="#660000", width=4, height=2, command = giris_DEL      ).grid(row=2, column=2)
Button( text="C"    , fg="#660000", width=4, height=2, command = giris_C        ).grid(row=2, column=3)
Button( text="."    , fg="#660000", width=4, height=2, command = giris_nokta    ).grid(row=6, column=1)
Button( text="0"    , fg="#660000", width=4, height=2, command = giris_0        ).grid(row=6, column=0)
Button( text="+"    , fg="#660000", width=4, height=2, command = giris_arti     ).grid(row=5, column=3)
Button( text="="    , fg="#660000", width=4, height=2, command = giris_esittir  ).grid(row=6, column=2)
Button( text="*"    , fg="#660000", width=4, height=2, command = giris_carpi    ).grid(row=3, column=3)
Button( text="/"    , fg="#660000", width=4, height=2, command = giris_bolu     ).grid(row=4, column=3)
Button( text="-"    , fg="#660000", width=4, height=2, command = giris_eksi     ).grid(row=6, column=3)


mainloop()

