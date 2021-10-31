#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:16:53 2021

@author: andrewgarcia
"""

import numpy as np

class myClass:
    def __init__(self, path, num):
        self.path = path
        self.num = num
        
    def get_cmd(self):
        txt = 'python example.py --parm1="{}" --parm2="{}"'
        print(txt.format(self.path,self.num))




p1 = myClass('/Users/andrewgarcia/Documents',5)
p1.get_cmd()
    

p2 = myClass('/some_path','2')
p2.get_cmd()



a = "str"
b = 5
t = 'Output: ' + a+ str(b)
