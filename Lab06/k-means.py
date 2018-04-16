# -*- coding: utf-8 -*-
"""
k.means
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2))
x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
X = np.concatenate((x1,x2,x3),axis=0)

plt.plot(X[:,0],X[:,1],'k.')
plt.show()

# Initialization
# Drawing the centroids
n = 3
c = np.zeros((n, 2))
for i in range(2):
    c[:, i] = np.random.rand(n)
    ma = max(X[:, i])
    mi = min(X[:, i])
    c[:, i] = c[:, i]*(ma - mi) + mi
    
x1 = np.random.standard_normal((100,2))*0.6+np.ones((100,2))
x2 = np.random.standard_normal((100,2))*0.5-np.ones((100,2))
x3 = np.random.standard_normal((100,2))*0.4-2*np.ones((100,2))+5
X = np.concatenate((x1,x2,x3),axis=0)

plt.plot(X[:, 0], X[:, 1], 'k.')
plt.plot(c[:, 0], c[:, 1], 'mo')
plt.show()

#Assign points to centroids
m = X.shape[0]
labels = np.zeros((m,))
tol = 1

for i in range(7):
    for i in range(300):
        minDist = np.Infinity
        for j in range(3):
            d = np.sqrt(((c[j, 0] - X[i, 0])**2) + ((c[j, 1] - X[i, 1])**2))
            if(d < minDist):
                minDist = d
                l = j
        labels[i] = l
    

plt.plot(X[labels==0,0],X[labels==0,1],'r.', label='cluster 1')
plt.plot(X[labels==1,0],X[labels==1,1],'b.', label='cluster 2')
plt.plot(X[labels==2,0],X[labels==2,1],'g.', label='cluster 3')

plt.plot(c[:,0],c[:,1],'mo',markersize=8, label='centroids')

plt.legend(loc='best')
plt.show()