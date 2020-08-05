# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:13:43 2020

@author: Remy
"""

import numpy as np 
import matplotlib.pyplot as plt 
import time 

money = 20000

years = 3
n = int(365*years)


x = np.linspace(1,n,n)
y = np.zeros(n)
b = []
account = [] 

file1 = open('rip.csv','r')
line = file1.readline()

gain = 0
loss = 0

for i in range(n):
    
    line2 = file1.readline()
    a = line2.split(',')
    b.append(a[0])
    y[i] = a[1]
    
    #RSI
    #First Calculation 
    if i > 0:    
        if i < 15:
            if y[i-1] < y[i]:
                currgain = y[i] - y[i-1]
                gain += y[i] - y[i-1]
            else:
                currloss = y[i-1] - y[i]
                loss += y[i-1] - y[i]
            
        
            avggain = gain / i
            avgloss = loss / i
            
        
        #Second Calculation 
        else: 
            prevgain = currgain
            prevloss = currloss 
            if y[i-1] < y[i]:
                currgain = y[i] - y[i-1]
                gain += y[i] - y[i-1]
            else:
                loss += y[i-1] - y[i] 
                currloss = y[i-1] - y[i]
                
            avggain = (prevgain *13 + currgain) / 14
            avgloss = (prevloss *13 + currloss) / 14            
            
    RS = avggain / avgloss
    RSI = 100 - 100 / (1+RS)       
    
    if RSI < 30 and RSI > 0:
        print('\n****** Bought Share ******\n')
        money = money - y[i]
        account.append(money)
        print('\nCurrent Money:',money,'\n')
    if RSI > 60:
        print('\n****** Sold Share ******\n')
        money = money + y[i] 
        account.append(money)
        print('\nCurrent Money:',money,'\n')
    
    print('Date:',b[i],'\nStock Price',y[i],'\nRSI',RSI,'\n')
    #time.sleep(0.1) 
    
trans = np.linspace(1,len(account),len(account))
    
plt.plot(trans, account)
