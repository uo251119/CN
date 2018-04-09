# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 19:44:07 2018

@author: UO251119
"""

from __future__ import division
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


m = np.zeros((500, 500))


def swap_color(color):
    if color == 0:
        return  1
    else:
        return 0

radius = 249
color = 1
while(radius > 1):
    for i in range (0, 499):
        for j in range (0, 499):
            if((j - 250)**2 + (i - 250)**2 < radius**2):
                m[i][j] = color
    radius -= 10
    color = swap_color(color)
    
 
plt.imshow(m, cmap = 'gray')