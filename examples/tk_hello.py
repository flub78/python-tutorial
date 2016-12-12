#!/usr/bin/python
# -*- coding:utf8 -*

"""
Python tutorial: Hello world in Tkinter

"""

from Tkinter import *

w = Tk()

lbl = Label(w, text='Hello Frédéric!')
lbl.pack()

w.mainloop()

print "bye"

