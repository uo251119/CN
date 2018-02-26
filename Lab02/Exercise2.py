# -*- coding: utf-8 -*-

from functions.bisection import bisection

f = lambda x : x**3 - 2*x**2 + 1

out1 = bisection(f, -1.0, 0.0, 1e-12, 200)
out2 = bisection(f, 0.0, 1.0, 1e-12, 200)
out3 = bisection(f, 1.0, 1.0, 1e-12, 200)

print out1
print out2
print out3