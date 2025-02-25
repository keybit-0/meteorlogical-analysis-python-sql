import mysql.connector
import numpy as np
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle



North = pd.read_pickle("NorthTempanomYear+bestfit.pkl")
East = pd.read_pickle("EastTempanomYear+bestfit.pkl")
South = pd.read_pickle("SouthTempanomYear+bestfit.pkl")
West = pd.read_pickle("WestTempanomYear+bestfit.pkl")

print(North)
fig, ax = plt.subplots()

North.plot(y = 'bestfit', use_index=True, ax = ax, label = 'North')
South.plot(y = 'bestfit', use_index=True, ax = ax, label = 'South')
East.plot(y = 'bestfit', use_index=True, ax = ax, label = 'East')
West.plot(y = 'bestfit', use_index=True, ax = ax, label = 'West')

plt.title('Annual Temperature Anomaly Trendlines')
plt.xlabel('Year')
plt.ylabel('Anomaly in deg Celcius')

plt.gcf().autofmt_xdate()
ax.grid()
ax.set_axisbelow(True)

plt.show()

