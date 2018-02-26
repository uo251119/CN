# -*- coding: utf-8 -*-

import numpy as np

def de2bi_a(x):
    sol = "";
    x = int(x)
    while(x > 0):
        sol = str(int(x%2)) + sol
        x = int(np.fix(x/2))
    return [str(d) for d in sol]
