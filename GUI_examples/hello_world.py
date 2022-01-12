# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:09:23 2021

@author: agarc
"""

from tkinter import *

root = Tk()

myLabel1 = Label(root, text = 'Hello World!')
myLabel2 = Label(root, text = "My name is Andrew")

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

root.mainloop()