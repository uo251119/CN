# -*- coding: utf-8 -*-

from __future__ import division

import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt

def secant(f,x0,x1,tol,maxiter):
    