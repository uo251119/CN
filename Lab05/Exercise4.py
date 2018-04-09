# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 19:29:02 2018

@author: UO251119
"""

from __future__ import division
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

m = np.zeros((2000, 2000))


color = 1

def swap_color(color):
    if color == 0:
        return  1
    else:
        return 0

for i in range (0, 1999):
    for j in range (0, 1999):
        m[i][j] = color
        if ((j) % 250) == 0:
            color = swap_color(color)
    if ((i) % 250) == 0:
        color = swap_color(color)
    

plt.imshow(m, cmap = 'gray')