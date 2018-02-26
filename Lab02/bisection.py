# -*- coding: utf-8 -*-

from __future__ import division

import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt

def bisection(f, a, b, tol, maxiter):
    ak = a
    bk = b
    i = 1
    x = a
    while(i <= maxiter):
        xk = ((ak + bk) / 2.)
        if(np.abs(xk - x) < tol):
            return x, i
        else:
            if(f(ak) * f(xk) > 0):
                ak = xk
            elif(f(ak) * f(xk) < 0):
                bk = xk
            else:
                return x, i
        x = xk
        i = i + 1


#%%

f = lambda x : x**3 - 2*x**2 + 1

out1 = bisection(f, -1.0, 0.0, 1e-12, 200)
out2 = bisection(f, 0.0, 1.0, 1e-12, 200)
out3 = bisection(f, 1.0, 1.0, 1e-12, 200)

print out1
print out2
print out3