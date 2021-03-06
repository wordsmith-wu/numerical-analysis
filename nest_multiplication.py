# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 07:54:17 2017

@author: Wordsmith
"""
import numpy as np

def nest(degree, coefficients, x, base_points=None):
    if not base_points:
        base_points = np.zeros(degree)
    for i in range(degree):
        coefficients[-i-2] = (x-base_points[i])*coefficients[-i-1]+coefficients[-i-2]
    return coefficients[0]

ans = nest(4,[-1,5,-3,3,2],1/2,[0,0,0,0])
print(ans)
x=1.00001
ans2 = nest(50,np.ones(51),x)
print(ans2)
ans22 = (x**51-1)/(x-1)
print(ans22)
print('error = %g' % (ans22-ans2))