import mysql.connector
import numpy as np
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle


#open files
North = pd.read_pickle("NorthPrecipanomYear+bestfit.pkl")
East = pd.read_pickle("EastPrecipanomYear+bestfit.pkl")
South = pd.read_pickle("SouthPrecipanomYear+bestfit.pkl")
West = pd.read_pickle("WestPrecipanomYear+bestfit.pkl")

#set figure axis
fig, ax = plt.subplots()

#plot line of bestfit data for each location on same graph
North.plot(y = 'bestfit', use_index=True, ax = ax, label = 'North')
South.plot(y = 'bestfit', use_index=True, ax = ax, label = 'South')
East.plot(y = 'bestfit', use_index=True, ax = ax, label = 'East')
West.plot(y = 'bestfit', use_index=True, ax = ax, label = 'West')
#labels
plt.title('Annual Precipitation Anomaly Trendlines')
plt.xlabel('Year')
plt.ylabel('Anomaly in mm')
#format axis and grid
plt.gcf().autofmt_xdate()
ax.grid()
ax.set_axisbelow(True)

plt.show()

