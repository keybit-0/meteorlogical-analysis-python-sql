import pickle
import numpy as np
import mysql.connector
import pandas as pd
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
X = matplotlib.dates.num2date(55400)
print(X)
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="key",
#     password="123",
#     database="Project"
# )
# mycursoreast = mydb.cursor() 
# mycursorwest = mydb.cursor() 
# mycursornorth = mydb.cursor() 
# mycursorsouth = mydb.cursor() 
# sqleast = 'SELECT avg(temp) AS totaltemp FROM Project.AllData WHERE  location = "E" ORDER BY id;'
# sqlwest = 'SELECT avg(temp) AS totaltemp FROM Project.AllData WHERE  location = "W" ORDER BY id;'
# sqlsouth= 'SELECT avg(temp) AS totaltemp FROM Project.AllData WHERE  location = "S" ORDER BY id;'
# sqlnorth = 'SELECT avg(temp) AS totaltemp FROM Project.AllData WHERE  location = "N" ORDER BY id;'

# mycursoreast.execute(sqleast)
# east = (np.average(mycursoreast.fetchall()) - 273.15)

# mycursorwest.execute(sqlwest)
# west = (np.average(mycursorwest.fetchall()) - 273.15)

# mycursorsouth.execute(sqlsouth)
# south = (np.average(mycursorsouth.fetchall()) - 273.15)

# mycursornorth.execute(sqlnorth)
# north = (np.average(mycursornorth.fetchall()) - 273.15)

# print(east)
# print(south)
# print(north)
# print(west)


data_east = pd.read_pickle("EastTempanomYear+bestfit.pkl") 
data_west = pd.read_pickle("WestTempanomYear+bestfit.pkl") 
data_south = pd.read_pickle("SouthTempanomYear+bestfit.pkl") 
data_north = pd.read_pickle("NorthTempanomYear+bestfit.pkl") 
east = np.std(data_east['anomaly'])
west = np.std(data_west['anomaly'])
south = np.std(data_south['anomaly'])
north = np.std(data_north['anomaly'])

# print(east)
# print(south)
# print(north)
# print(west)