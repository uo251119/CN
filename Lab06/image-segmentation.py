# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans

I = Image.open("VictoriaLake.jpg")

plt.figure(figsize=(8,8))
plt.imshow(I)
plt.axis('off')
plt.show()

I1 = I.convert('L')
I2 = np.asarray(I1,dtype=np.float)

plt.figure(figsize=(8,8))
plt.imshow(I2,cmap='gray')
plt.axis('off')
plt.show()

X = I2.reshape((-1, 1))

k_means = KMeans(n_clusters=3)
k_means.fit(X) 

centroids = k_means.cluster_centers_
labels = k_means.labels_

I2_compressed = np.choose(labels, centroids)
I2_compressed.shape = I2.shape

plt.figure(figsize=(8,8))
plt.imshow(I2_compressed,cmap='gray')
plt.axis('off')
plt.show()

I2 = (I2_compressed-np.min(I2_compressed))/(np.max(I2_compressed)-np.min(I2_compressed))*255
I2 = Image.fromarray(I2.astype(np.uint8))
w, h =I2.size
colors = I2.getcolors(w * h)
print (colors)

print ('Area = ',  float(210000)*float(colors[0][0])/float(w*h), 'km2')