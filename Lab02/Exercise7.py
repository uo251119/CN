# -*- coding: utf-8 -*-

from functions.secant import newton

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(8, 15, 200)

f = lambda x : np.cosh(x) * np.cos(x) - 1
df = lambda x : np.cos(x) - 0.1

OX = 0*x

plt.plot(x, f(x))
plt.plot(x, OX, 'k-')

tol = 1e-12
maxiter = 100

n1 = secant(f, df, 2, tol, maxiter)
n2 = secant(f, df, 6, tol, maxiter)
n3 = secant(f, df, 8, tol, maxiter)

plt.plot(n1[0], 0,'ro')
plt.plot(n2[0], 0,'ro')
plt.plot(n3[0], 0,'ro')

print n1
print n2
print n3