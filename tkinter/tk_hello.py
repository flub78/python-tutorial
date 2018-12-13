#!/usr/bin/python
# coding=utf-8

"""
Python tutorial: Hello world in Tkinter

"""

# Warning use a lowercase t in python 3
from tkinter import *


# Callback definitions
def print_txt():
    print ("text = ")

# Main program
w = Tk()

logo = PhotoImage(file="resources/smile.gif")
lbl = Label(w, compound=RIGHT, image=logo,
             fg="red",
             text='Hello Frédéric!\nI am a label\nwith an image on my right')
lbl.pack(side="right")

bt = Button(w, text="Exit", command=w.quit)
bt.pack()

txt = StringVar()
ent = Entry(w, textvariable=txt, width=30)
ent.pack()

cr = Button(w, text="Ok", command=print_txt())
cr.pack()

w.mainloop()

print ("bye")

