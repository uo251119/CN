# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib as plt

#%% Divided differences
def div_dif(x, y):
    n = len(x)
    d = np.zeros((n,n))
    d[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            num = d[i + 1, j - 1] - d[i, j - 1]
            den = x[i + j] - x[i]
            d[i, j] = num / den
    return d

#%% Polynomial
def newton_polynomial(z, x ,y):
    d = div_dif(x, y)
    n = len(x)
    p = 0.
    f = 1.
    for i in range(n):
        p += d[0, 1] * f
        f *= z - x[i]
    return p

#%% data
x = np.array([2., 3., 4., 5., 6.])
y = np.array([2., 6., 5., 5., 6.])

#%%
z = np.linspace(min(x), max(x))
p = newton_polynomial(z, x, y)
plt.plot(z, p, label = 'Polynomial')
plt.plot(x, y, 'o', label = 'Nodes')
plt.legend()
plt.show()