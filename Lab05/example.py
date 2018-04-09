# -*- coding: utf-8 -*-

from __future__ import division
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

I = Image.open('lena_gray.tif')
I1 = I.convert('L')
a = np.asarray(I1, dtype = np.float64)

lena_eye = a [251 : 283, 317 : 349]


plt.subplot(121)
plt.imshow(a, cmap = 'gray')
plt.title('Lena'), plt.axis('off')

plt.subplot(122)
plt.imshow(lena_eye, cmap = 'gray')
plt.title('Lena eye'), plt.axis('off')
