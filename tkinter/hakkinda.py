#!/usr/bin/python
#-*-coding:utf-8-*-

from Tkinter import *
import webbrowser

def hakkinda():
        hakkinda= Tk()
        hakkinda.title("Hakkında")
        hakkinda.geometry("160x180+260+195")
        hakkinda.resizable(width=FALSE,height=FALSE)
        Label(hakkinda,text="*SIRADIŞI*\ncorporation\n\nhesapcık\nV1 0.0,1.0\n\nLisans:\ntabiki özgür\n" , fg="#660000" ).pack()
        url=Label(hakkinda,text="websites\nbil.omu.edu.tr",fg="#660000")
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

Button( text="hakkında", fg="#660000", width=6, height=1, command = hakkinda).grid(row=7, column=1, columnspan=2)


