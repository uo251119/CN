# -*- coding: utf-8 -*-

from functions.newton import newton

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 15, 200)

f = lambda x : np.sin(x) - 0.1 * x
df = lambda x : np.cos(x) - 0.1

OX = 0*x

plt.plot(x, f(x))
plt.plot(x, OX, 'k-')

tol = 1e-12
maxiter = 100

n1 = newton(f, df, 2, tol, maxiter)
n2 = newton(f, df, 6, tol, maxiter)
n3 = newton(f, df, 8, tol, maxiter)

plt.plot(n1[0], 0,'ro')
plt.plot(n2[0], 0,'ro')
plt.plot(n3[0], 0,'ro')

print n1
print n2
print n3