# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:09:23 2021

@author: agarc
"""

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = 'I clicked the Button!')
    myLabel.pack()

myButton = Button(root, text = 'Click Me', 
                  padx = 50, pady = 50, 
                  command = myClick, 
                  fg = 'blue', bg = 'green'
                  )
myButton.pack()

root.mainloop()