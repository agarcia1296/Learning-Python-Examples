# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:09:23 2021

@author: agarc
"""

from tkinter import *

root = Tk()

entry = Entry(root, width = 50, borderwidth = 5)
entry.pack()


def myClick():
    hello = "Hello " + entry.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

myButton = Button(root, text = 'Click Me', 
                  padx = 50, pady = 50, 
                  command = myClick, 
                  fg = 'blue', bg = 'green'
                  )
myButton.pack()

root.mainloop()