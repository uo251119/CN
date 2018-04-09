# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 19:00:17 2018

@author: UO251119
"""

from __future__ import division
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

I = Image.open('lena_gray_512.tif')
I1 = I.convert('L')
I2 = np.asarray(I1, dtype = np.double)

m = np.zeros((512, 512), dtype = np.double)

for i in range (0, 512):
    for j in range (0, 512):
        if((j - 256)**2 + (i - 256)**2 < 150**2):
            m[i][j] = 1

s1 = np.multiply(I2, m)

for i in range (0, 511):
    for j in range (0, 511):
        if((j - 256)**2 + (i - 256)**2 < 150**2):
            m[i][j] = 1
        else:
            m[i][j] = 0.5

s2 = np.multiply(I2, m)

plt.subplot(121)
plt.imshow(s1, cmap = 'gray')

plt.subplot(122)
plt.imshow(s2, cmap = 'gray')
