# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:13:43 2020

@author: Remy
"""

import numpy as np 
import matplotlib.pyplot as plt 
import time 




file = 'rip.csv' 
    

days = 30
interval = 3
    
money = 40000

weeks = 52*2

n = int(5*weeks)
owned = 0

x = np.linspace(1,n,n)
y = np.zeros(n)
sma_line = np.zeros(n)
der_line = np.zeros(n)
dder_line = np.zeros(n)

b = []
account = [] 

file1 = open(file,'r')
line = file1.readline()

sma = 0


for i in range(n):
    
    line_first = file1.readline()
    a = line_first.split(',')
    b.append(a[0])
    y[i] = a[1]
    
    #days = days #moving avg for specified day
    
    #Simple 30-Day Moving Average 
    #First Calculation 
    if i > 0:    
        if i < days:
            sma += y[i] 
            avg = sma/i 
            sma_line[i] = avg

        else: 
            sma = sma + y[i] - y[i-days] 
            avg = sma/days
            sma_line[i] = avg
    else:
        sma_line[i] = y[i]
        
    #interval = interval #days 
    
    if i > interval:
        
        dy = sma_line[i] - sma_line[i-interval]
        dx = x[i] - x[i-interval]
        der = dy/dx 
        der_line[i] = der
        
    else:
        der_line[i] = 0
   
        
    if i > interval:
        
        ddy = der_line[i] - der_line[i-interval]
        dder = ddy/dx 
        dder_line[i] = dder
          
    else:
        dder_line[i] = 0
        
    
    multiple = 10
    band = 0
    
    if der_line[i] > band and der_line[i-1] < -band and money > y[i]*multiple:
        #print('fpoound', x[i],'bought')
        money -= y[i]*multiple
        owned += multiple
        
        
    elif der_line[i] < band and der_line[i-1] > -band and owned > 0:
        #print('found', x[i],'sell')
        money += y[i]*multiple 
        owned -= multiple
      
    account.append(money+owned*y[i]) 
    
plt.plot(x, sma_line,x,y)
          

             

 
    

