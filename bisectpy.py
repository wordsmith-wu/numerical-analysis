# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 07:54:17 2017

@author: Wordsmith
"""


import numpy as np

def bisect(f,a,b,tol):
    """Bisection Method
    
    Compute approximate solution of f(x)=0
    
    Input: function f, a, b such that f(a)*f(b)<0, 
        and tolerance tol
    Output: Approximate solution xc
    """
    assert np.sign(a)*np.sign(b) <= 0 
    fa = f(a)
    fb = f(b)
    k = 0
    while (b-a)/2 > tol:
        c = (a+b)/2
        fc = f(c)
        if fc == 0:
            return fc
        if np.sign(fc)*np.sign(fa) < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    xc = (a+b)/2
    return xc

f = lambda x: x**3+x-1
xc = bisect(f,0,1,0.0000001)
print(xc)