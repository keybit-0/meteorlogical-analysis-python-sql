import mysql.connector
import numpy as np
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle
from scipy import stats
import pymannkendall as mk
X = (34222.46843)
print(X)

data = pd.read_pickle("Westannualprecip.pkl") 

#Get X and y values
X = data.index.values
Y = data['precip'].values
#convert datetime to number for calculations
X1 = matplotlib.dates.date2num(X)

res = stats.theilslopes(Y, X1, 0.95)
lsq_res = stats.linregress(X1, Y)
print(res) #stats.theilslopes.medintercept(Y, X1, 0.90)
print(lsq_res)

# result = mk.original_test(data['precip']) #   hamed_rao_modification
# print(result)

# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.plot(X, data['precip'])
# ax.plot(X, (res[1] + res[0] * X1), 'r-')
# # ax.plot(X, (res[1] + res[2] * X1), 'r--')
# # ax.plot(X, (res[1] + res[3] * X1), 'r--')
# ax.plot(X, (lsq_res[1] + lsq_res[0] * X1), 'g-')


# plt.gcf().autofmt_xdate()
# ax.grid()
# ax.set_axisbelow(True)

# # yabs_max = abs(max(ax.get_ylim(), key=abs))
# # ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)

# plt.show()


#INCREASED VARIANCE????

start_date = '1981-01-01'
end_date = '2000-01-01'
start_date1 = '2000-01-01'
end_date1 = '2020-12-31'
mask = (data.index >= start_date) & (data.index < end_date)
mask1 = (data.index >= start_date1) & (data.index < end_date1)
# print(data.loc[mask]) # 
# print(data.loc[mask1])
# mktest = mk.original_test(data['wetdays']) #  .loc[mask]
print('1981 - 2000')
print(data['precip'].loc[mask].std())
print(data['precip'].loc[mask].mean())

print('2000-2020')
print(data['precip'].loc[mask1].std())
print(data['precip'].loc[mask1].mean())



##Heavy rainfall events
## consecutive dry days

##MAx min temperatures
##days above 20 deg, below 0
