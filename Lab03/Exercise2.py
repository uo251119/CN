# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from functions.lagrange import *

#x = np.array([2., 3., 4., 5., 6.])
#y = np.array([2., 6., 5., 5., 6.])

x = np.array([0.,1.,2.,3.,4.,5.,6.])
y = np.array([3.,5.,6.,5.,4.,4.,5.])

z = np.linspace(min(x), max(x))

#plt.plot(z, lagrange_fundamental(2, z, x))
plt.plot(z, lagrange_polynomial(z, x, y), x, y, 'o')
