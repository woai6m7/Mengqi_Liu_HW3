#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 23:28:28 2020

@author: liumengqi
"""

import pylab
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels as stat
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data= pd.read_csv('/Users/liumengqi/Desktop/HY_Universe_corporate bond.csv')
print(data.head())
print(data.tail())

ncol=len(data)
nrow=len(data.iloc[0])
    
nrow = data.shape[0]
ncol = data.shape[1]
print("Number of Rows of Data = ", nrow) 
print("Number of Columns of Data = ", ncol)

print(data.dtypes)

#qqplot
stats.probplot(data['n_trades'], dist = 'norm', plot = pylab)
pylab.show()
stats.probplot(data['n_days_trade'], dist = 'norm', plot = pylab)
pylab.show()

#heatmap
x = pd.DataFrame(data.iloc[0:60, [20, 21, 26, 31, 36]].corr())
sns.heatmap(x)
plt.show()

# Scatter plot
plt.scatter(data['Coupon'], data['Issued Amount'])
plt.xlabel('Coupon')
plt.ylabel('Issued Amount')
plt.title('Coupon Vs Issued Amount')
plt.show()

#histogram
plt.hist(data['volume_trades'],bins=10)
plt.xlabel('volume_trades')
plt.ylabel('amcounts')
plt.title('volume_trades histogram')
plt.show()

#box plot
boxplot = data.boxplot(column=[ 'total_mean_size','total_median_size'])
plt.xlabel('Attibutes')
plt.ylabel('Quartile Ranges')
plt.show()

print("My name is {Mengqi Liu}")
print("My NetID is: {mengqi3}")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")