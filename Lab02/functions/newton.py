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
        