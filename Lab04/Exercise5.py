# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 19:15:02 2018

@author: UO251119
"""
from scipy.special import legendre
import numpy as np
import matplotlib as plt

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