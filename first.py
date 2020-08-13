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
owned = 10
inverse_owned = 10

x = np.linspace(1,n,n)
y = np.zeros(n)
z = np.zeros(n)
b = []
account = [] 

file1 = open('rip.csv','r')
file2 = open('sqqq.csv', 'r')
line = file1.readline()
lineb = file2.readline()

gain = 0
loss = 0

for i in range(n):
    
    line2 = file1.readline()
    a = line2.split(',')
    b.append(a[0])
    y[i] = a[1]
    
# =============================================================================
#     line2 = file2.readline()
#     c = line2.split(',')
#     z[i] = c[1]
# =============================================================================
    
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
        
        #Stuff to set up for actual trading 
        leverage = 30 #percent 
        maxmove = money*leverage/100   
        
        #Actual Trading 
        if RSI < 30 and RSI > 0 and money > 0:
            #move = maxmove//y[i]
            multiple = 1
            money = money - y[i]*multiple
            account.append(money)
            owned += multiple 
            
                 
# =============================================================================
#             if inverse_owned > 0:
#                 inverse_shares = y[i]//z[i]
#                 money = money + z[i]*inverse_shares
#                 inverse_owned -= inverse_shares
# =============================================================================
     
        
            print('\n****** Bought',1.0,' Share ******\n')            
            print('\nCurrent Money:',money,'\n')
            
        if RSI > 60 and owned > 0:
            #move = maxmove//y[i]
            multiple = 1
            money = money + y[i]*multiple 
            account.append(money)
            owned -= multiple 
            
# =============================================================================
#             inverse_shares = y[i]//z[i]
#             money = money - z[i]*inverse_shares
#             inverse_owned += inverse_shares
# =============================================================================
            
            print('\n****** Sold',1.0,' Share ******\n')
            print('\nCurrent Money:',money,'\n')
            
    
        print('Date:',b[i],'\nStock Price',y[i],'\nRSI',RSI,'\n')
        #time.sleep(0.5) 
    
trans = np.linspace(1,len(account),len(account))
    
plt.plot(trans, account)
