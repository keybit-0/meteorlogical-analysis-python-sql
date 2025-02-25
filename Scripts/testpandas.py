import mysql.connector
import numpy as np
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle


data = pd.read_pickle("BestfitWestTempanomYear.pkl")
data2 = pd.read_pickle("BestfitWestTempanomMonth.pkl")
print(data)
temp = pd.read_pickle('WestTempanomYear.pkl')


fig, ax = plt.subplots()

North.plot(y = 'bestfit', use_index=True, ax = ax, label = 'North')
South.plot(y = 'bestfit', use_index=True, ax = ax, label = 'South')
East.plot(y = 'bestfit', use_index=True, ax = ax, label = 'East')
West.plot(y = 'bestfit', use_index=True, ax = ax, label = 'West')



plt.show()