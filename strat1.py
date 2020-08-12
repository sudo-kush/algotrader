# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:13:43 2020

@author: Remy
"""

import numpy as np 
import matplotlib.pyplot as plt 
import time 

money = 200000

years = 3
n = int(365*years)
owned = 0

x = np.linspace(1,n,n)
y = np.zeros(n)
z = np.zeros(n)
b = []
account = [] 
sma_line =[]
der_line = []

file1 = open('rip.csv','r')
line = file1.readline()

sma = 0
sum_der = 0 
trans = 0

for i in range(n):
    
    line_first = file1.readline()
    a = line_first.split(',')
    b.append(a[0])
    y[i] = a[1]
    
    days = 30 #moving avg for specified day
    
    #Simple 30-Day Moving Average 
    #First Calculation 
    if i > 0:    
        if i < days:
            sma += y[i] 
            avg = sma/i 
            sma_line.append(avg)

        else: 
            sma = sma + y[i] - y[i-days] 
            avg = sma/days
            sma_line.append(avg)
    else:
        sma_line.append(y[i])
    
    interval = 2 #days 
    
    if i > interval:
        
        dy = y[i] - y[i-interval]
        dx = x[i] - x[i-interval]
        der = dy/dx 
        der_line.append(der)
    else:
        der_line.append(0)
     
    
    perc = 15
    
    if der > -perc and der < perc:
        owned = owned
    
    elif der < 2*perc and der > perc:
        
        #10% Buy 
        play = money*.1 
        move = play//y[i] 
        money -= move*y[i]
        
        owned += move
        
    elif der < 3*perc and der > 3*perc:
        
        #20% Buy 
        play = money*.2 
        move = play//y[i] 
        money -= move*y[i]
        
        owned += move 
        
    elif der > 3*perc:
        
        #30% Buy 
        play = money*.3
        move = play//y[i] 
        money -= move*y[i]
        
        owned += move 
        
    elif der > -2*perc and der < -perc and owned > 0:
        
        #10% Sell 
        play = money*.1
        move = play//y[i] 
        money += move*y[i] 
        
        owned -= move 
        
    elif der > -3*perc and der < -2*perc and owned > 0:
        
        #20% Sell 
        play = money*.2 
        move = play//y[i] 
        money += move*y[i] 
        
        owned -= move 

    elif der < -3*perc and owned > 0:
        
        #30% Sell 
        play = money*.3
        move = play//y[i] 
        money += move*y[i] 
        
        owned -= move  
        
    account.append(money+owned*y[i]) 
        

    
              
plt.plot(x, sma_line, x, y)
                 

     
        

