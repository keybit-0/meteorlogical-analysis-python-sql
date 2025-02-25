##This script will test the yearly and monthly temp anomalies datasets and determine which is more statistically significant, usinf r squared values.
import mysql.connector
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle
from scipy.stats import ttest_ind
from scipy import stats
import seaborn
#open datasets, stored in pickle files
data_year = pd.read_pickle("WestTempanomYear.pkl")
data_month = pd.read_pickle("WestTempanomMonth.pkl")


#Null Hypothesis - data is not statistically significant
#p value test
# mean_year = np.mean(data_year["anomaly"].values)
# mean_month = np.mean(data_month["anomaly"].values)

# N_year = len(data_year['anomaly'].values)
# N_month = len(data_month['anomaly'].values)

# print(mean_year)
# print(N_year)
# print(mean_month)
# print(N_month)

# pvalyear = stats.ttest_1samp(data_year['anomaly'], 0).pvalue  
# pvalmonth = stats.ttest_1samp(data_month['anomaly'], 0).pvalue 

# res1 = describe()
# print(pvalyear)
# print(pvalmonth)
#import seaborn library

def r2calc(data): 
    r2 = 0  #r squared value
    X = []
    Y = []
    mean_x = 0
    mean_y = 0
    St = 0  # total sum of squares
    Sr = 0  # total sum of squares of residuals

    #Get X and y values
    X = data.index.values
    Y = data['anomaly'].values
    #convert datetime to number for calculations
    X = matplotlib.dates.date2num(X)
    # Averages
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    # Total number of values
    n = len(X)
    # Calculate 'm' and 'c', use y = mx+c to find y values. 
    numerator = 0
    denomenator = 0
    m = 0
    c = 0
    # Forumla for slope given n, x and y values
    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denomenator += (X[i] - mean_x) ** 2
    m = numerator / denomenator
    c = mean_y - (m * mean_x)

# Printing c
    for i in range(n):
        y_pred = c + m * X[i]
        St += (Y[i] - mean_y)**2
        Sr += (Y[i] - y_pred)**2
    r2 = 1 - (Sr/St)
    print(r2)


r2calc(data_year)
r2calc(data_month)

r2_year = 0.12692154052664884
r2_month = 0.01837668228625733

#year data better to use.