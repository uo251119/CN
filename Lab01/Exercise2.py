# -*- coding: utf-8 -*-

import numpy as np

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

