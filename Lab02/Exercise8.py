# -*- coding: utf-8 -*-

from functions.bisection import bisection

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 200)

f = lambda x : x ** 3 - 75
df = lambda x : 1 / (3 * x ** (2/3))

OX = 0*x

plt.plot(x, f(x))
plt.plot(x, OX, 'k-')

tol = 1e-12
maxiter = 100

n1 = bisection(f, df, 2, tol, maxiter)
n2 = bisection(f, df, 6, tol, maxiter)
n3 = bisection(f, df, 8, tol, maxiter)

plt.plot(n1[0], 0,'ro')
plt.plot(n2[0], 0,'ro')
plt.plot(n3[0], 0,'ro')

print n1
print n2
print n3