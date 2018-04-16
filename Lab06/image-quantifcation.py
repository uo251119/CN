# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits

I = Image.open("holi.jpg")

I1 = np.asarray(I,dtype=np.float32)/255
plt.figure(figsize=(12,12))
plt.imshow(I1)
plt.axis('off')
plt.show()

w, h = I.size
colors = I.getcolors(w * h)
num_colors = len(colors) 
num_pixels = w*h 

print ('Number of pixels = ', num_pixels)
print ('Number of colors = ', num_colors)

R = I1[:,:,0]
G = I1[:,:,1]
B = I1[:,:,2]

XR = R.reshape((-1, 1))  
XG = G.reshape((-1, 1)) 
XB = B.reshape((-1, 1)) 

X = np.concatenate((XR,XG,XB),axis=1)

n = 10
k_means = KMeans(n_clusters=n)
k_means.fit(X)

centroids = k_means.cluster_centers_
labels = k_means.labels_

m = XR.shape
for i in range(m[0]):
    XR[i] = centroids[labels[i]][0] 
    XG[i] = centroids[labels[i]][1] 
    XB[i] = centroids[labels[i]][2] 
XR.shape = R.shape 
XG.shape = G.shape
XB.shape = B.shape 
XR = XR[:, :, np.newaxis]  
XG = XG[:, :, np.newaxis]
XB = XB[:, :, np.newaxis]

Y = np.concatenate((XR,XG,XB),axis=2)

plt.figure(figsize=(12,12))
plt.imshow(Y)
plt.axis('off')
plt.show()

print ('Number of pixels = ', num_pixels)
print ('Number of colors = ', n)

Y1 = np.floor(Y*255)
Image.fromarray(Y1.astype(np.uint8)).save("holi2.jpg")