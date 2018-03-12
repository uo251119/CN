# -*- coding: utf-8 -*-

def lagrange_fundamental(k, z, x):
    l = 1
    for i in range(len(x)):
        if i != k:
            l *= (z - x[i]) / (x[k]-x[i])
    return l

def lagrange_polynomial(z, x, y):
    p = 0;
    for i in range(len(x)):
        p += y[i] * lagrange_fundamental(i, z, x)
    return p