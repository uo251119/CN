# -*- coding: utf-8 -*-

import numpy as np
import Exercise2

BIAS = 127

def de2bi_a(x):
    sol = "";
    x = int(x)
    while(x > 0):
        sol = str(int(x%2)) + sol
        x = int(np.fix(x/2))
    return str(sol)

def de2bi_b(x):
    sol = "";
    
    i = int(x)
    d = float("0." + str(x).split(".")[1])
    
    while(i > 0):
        sol = str(int(i%2)) + sol
        i = int(np.fix(i/2))
    sol = sol + "."
    while(d < 1):
        d = d*2
        sol = sol + str(int(d))
        if(d > 1):
            d -= 1
    return sol

#x = 105.8125
#x = 120.875
#x = 7.1
x = -1.41

s = str(int(x <= 0))

m = 0
n = str(de2bi_b(x))
aux = float(n)

print aux

while(aux < 1):
    m -= 1
    aux = aux * 10
    
print aux
while(aux > 10):
    m += 1
    aux = aux / 10

n = n.replace('.', '')
n = n[:1] + '.' + n[1:]

exp = de2bi_a(m + BIAS)
while(len(exp) < 8):
    exp = '0' + exp

n = str(n)[2:]

while(len(n) < 23):
    n = n + '0'
if(len(n) > 23):
    n = n[:23]
    
print x, '\t', "---> ", de2bi_b(x)
print "[Sign]:", s, "[Exponent]:", exp, "[Mantissa]:", n