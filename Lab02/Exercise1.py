# -*- coding: utf-8 -*-

from __future__ import division

from functions.newton import newton

f = lambda x : x**3 - 2*x**2 + 1
df = lambda x : 3*x**2 - 4*x

out1 = newton(f, df, -1, 1e-12, 200)
out2 = newton(f, df, 0.1, 1e-12, 200)
out3 = newton(f, df, 1, 1e-12, 200)

print out1
print out2
print out3