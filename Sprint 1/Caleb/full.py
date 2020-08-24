# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:08:01 2020

@author: Remy
"""

from strat1 import strat1
import numpy as np
from scipy.optimize import minimize 

def objective(x) :
    return -strat1.finisher(x) 

days_guess = 20
interval_guess = 4
perc_guess = 3

x0 = np.array([days_guess, interval_guess, perc_guess]) 
res = minimize(objective, x0, method='SLQSP') 

print(res.x) 