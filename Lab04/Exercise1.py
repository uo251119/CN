# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#%% Data
x = np.linspace(-1, 1, 5)
f = lambda x : np.cos(x)
y = f(x)
g = 2 #degree of the polynomial

#%%
n = len(x)
A = np.ones((n, g + 1))
for j in range(1, g + 1):
    A[:, j] = A[:, j - 1] * x
     
#%% 
M = np.dot(A.T, A) # Coefficient matrix of the linear system
b = np.dot(A.T, y) # Independent term
a = np.linalg.solve(M, b)
a = a[::-1]

#%%
xx = np.linspace(min(x), max(x))
yy = np.polyval(a, xx)

plt.plot(xx, yy, label = 'Fitting polynomial')
plt.plot(x, y, 'o', label = 'Point')
plt.show()