#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:15:06 2022

@author: XBTJames
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Hashprice Data.csv',sep='\t', encoding='utf-16')
df['Time'] = pd.to_datetime(df['Time'])

"""
Bring in Hashprice data, this data from coinmetrics.io, BTC Miner Revenue Per Hash Per Sec (USD), which is the USD earnings of 1 TH/s per day. make sure you select ALL data (not just 1YR) before downlaoding data'

"""

beginDate = pd.to_datetime('2016-05-31')
df = df.set_index('Time')

'''  Set the start to May 31 2016, when Bitmain released the Antminer S9, the start of the modern ASIC era, and the index of the dataframe equal to the Time, which is actually just the date, but that's how it coems from CM.

'''

def breakevenPower(eff, startDate=beginDate):
    THperMW = (1000000)/eff #The efficiency is how many W produce 1TH, so by taking 1,000,000 watts and dividing by eff, we get the terrahashes per MW
    df3 = df[startDate:] #by default, the function will start at May 31 2016. If you want a custom start date, provide an optional agument in a datetime format
    rev = []
    i=0
    while i < len(df3):
        rev.append(THperMW * (df3['BTC / Miner Revenue per Hash per Sec (USD)'].iloc[i])/24) #this appends hourly revenues per megawatt for a megawatt of miners with the efficiency specified
        i+=1
    plt.suptitle('Breakeven MWH Price for ' + str(eff) + 'J/TH Efficinecy Machines') #now we plot
    plt.xlabel('Date')
    plt.ylabel('USD per MWH')
    plt.plot(df3.index, rev, c = 'blue')
    plt.show()
    minRev = "${:.4g}".format(min(rev))
    print('the minimum breakeven power cost for this efficiency is',minRev,'per MWH')
    return