#!/usr/bin/python
# -*- coding:utf8 -*

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

lbl = Label(w, text='Hello Frédéric!\nI am a label')
lbl.pack()

bt = Button(w, text="Exit", command=w.quit)
bt.pack()

txt = StringVar()
ent = Entry(w, textvariable=txt, width=30)
ent.pack()

cr = Button(w, text="Ok", command=print_txt())
cr.pack()

w.mainloop()

print ("bye")

