# -*- coding: utf-8 -*-

from __future__ import division
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

I = Image.open('cameraman.tif')
I1 = I.convert('L')
cameraman = np.asarray(I1, dtype = np.float32)

cameraman_head = cameraman[70 : 160, 190 : 280]


plt.subplot(121)
plt.imshow(cameraman, cmap = 'gray')
plt.title('Cameraman'), plt.axis('off')

plt.subplot(122)
plt.imshow(cameraman_head, cmap = 'gray')
plt.title('Cameramans head'), plt.axis('off')
