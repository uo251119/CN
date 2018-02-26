# -*- coding: utf-8 -*-

from __future__ import division

import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt

def newton(f,df,x0,tol,maxiter):
    i = 1
    x = x0
    while(i < maxiter):
        xk = x - (f(x)/df(x))
        if(np.abs(xk - x) < tol):
            return x, i
        x = xk
        i = i + 1
        
#%%

f = lambda x : x**3 - 2*x**2 + 1
df = lambda x : 3*x**2 - 4*x


out1 = newton(f, df, -1, 1e-12, 200)
out2 = newton(f, df, 0.1, 1e-12, 200)
out3 = newton(f, df, 1, 1e-12, 200)

print out1
print out2
print out3