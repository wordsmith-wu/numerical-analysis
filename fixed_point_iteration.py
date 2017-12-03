# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:26:17 2017

@author: Wordsmith
"""
import numpy as np
def fpi(g,x0,k):
    x = x0
    for i in range(k):
        x = g(x)
        print("step: %d     value: %g" % (i,x))

g1 = lambda x: 1 - x**3
g2 = lambda x: (1-x)**(1/3)
g3 = lambda x: (1+2*x**3)/(1+3*x**2)
g4 = lambda x: x+np.cos(x)-np.sin(x)
fpi(g4,0.5,20)
