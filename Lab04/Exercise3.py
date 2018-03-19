# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib as plt

x = np.linspace(-1, 1, 5)
f = lambda x : np.cos(x)
y = f(x)
g = 2 #degree of the polynomial

#%%
A = np.random.rand(3,5)
At = A.T
a = np.dot(A.T, A)

#%% Another method
#M = np.zeros(3,3)
#for i in range(3):
#    for j in range(3):
#        M[i, j]...

#%%
print (sum(x ** 4))
print (sum(x ** 2 * y))

#%% Data
f = lambda x : np.cos(x)
a = -1
b = 1
g = 2

#%%
from scipy.integrate import quad
e = 3
inte = lambda x : x ** e
a = 0
b = 3
I = quad(inte, a, b)[0]

#%% Error
xx = np.linspace(a, b)
yy = np.polyval(a,  xx)

Error = np.linalg.norm(f(xx) - yy) / np.linalg.norm(f(xx))


from scipy.special import legendre

def L(x,n):
    Leg = legendre(n)
    y = Leg(x)
    return y

xx = np.linspace(-1,1,100)
plt.plot(xx,0*xx,'k-')
for i in range(6):
    plt.plot(xx,L(xx,i),label=r'$L_'+str(i)+'$') 
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)  
plt.title('Legendre polynomials')
plt.show()