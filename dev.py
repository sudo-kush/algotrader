# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:34:33 2020

@author: Remy
"""
'''
Notes for next proj 

- Check Market Posture 
    Reel in reports from the Dow and NASDAQ as well as VIX and VXN 
    
    If statements to see if it is bear or bull 
    
    Create algo that decides the posture of the market 
    
''' 
from datetime import date, datetime, timedelta 
import yahoo_fin.stock_info as si 
import matplotlib.pyplot as plt
import numpy as np 

b = (date.today() - timedelta(days=14)).strftime("%m-%d-%y")
c = datetime.now().strftime("%m-%d-%y")

DJI = si.get_data('dia', start_date=b, end_date=c)
COMP = si.get_data('qqq', start_date=b, end_date=c)
VIX = si.get_data('vixm', start_date=b, end_date=c)
VXN = si.get_data('vixy', start_date=b, end_date=c)

x = np.linspace(0,len(DJI.index),1)

fig, axes = plt.subplots(nrows=2, ncols=2)

DJI.plot(ax=axes[0,0],y='open',title='DJI',xticks=[])
COMP.plot(ax=axes[0,1],y='open',title='NASDAQ',xticks=[])
VIX.plot(ax=axes[1,0],y='open',title='VIX',xticks=[])
VXN.plot(ax=axes[1,1],y='open',title='VXN',xticks=[])





