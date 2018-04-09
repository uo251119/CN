# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 19:18:28 2018

@author: UO251119
"""

from __future__ import division
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

I = Image.open('lena_gray_512.tif')
I1 = I.convert('L')
I2 = np.asarray(I1, dtype = np.float32)

line = np.linspace(0, 1, 512)
m = np.tile(line, (512, 1))

m = np.transpose(m)


sol = np.multiply(m, I2)

plt.subplot(121)
plt.imshow(I2, cmap = 'gray')

plt.subplot(122)
plt.imshow(sol, cmap = 'gray')
