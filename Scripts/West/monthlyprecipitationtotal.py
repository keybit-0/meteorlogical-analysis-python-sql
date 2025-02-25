import mysql.connector
import numpy as np
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle
X = matplotlib.dates.num2date(34222.46843)
print(X)

with open('baselineprecipW.pickle', 'rb') as handle:
    baseline = pickle.load(handle)


# set empty lists
monthavgtemp=[]
time=[]
dates=[]
totalprecip=[]

# Mysql connection + cursor
mydb = mysql.connector.connect(
    host="localhost",
    user="key",
    password="123",
    database="Project"
)
mycursor = mydb.cursor() 

start = datetime.datetime.now()

# get data
for y in range(1981, 2021):
   
    for m in range(1,13):
            
        # Append month and year from loop to time list
        z = datetime.datetime(y, m, 1 ,0 ,0 )
        time.append(z)

        # Sql query for montly temp and average it.
        sql = 'SELECT SUM(precip) as avgtemp FROM Project.AllData where month(date_time) =' + str(m) + ' and year(date_time) =' + str(y) + ' and hour(date_time) = 23 and location = "W" order by id;'

            ## quicker to average inside the sql query, time saved.
                ##result = np.average(mycursortemp.fetchall())
                ##anomaly.append(float(result - baseline[m])

        # Subtract the monthly average temp from baseline average for that month and append to anomaly.
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        totalprecip.append(float(result[0][0]) - baseline[m] )
        print(baseline[m])
        print(z)
        
#Print time taken for loop.
end = datetime.datetime.now()  
print(end - start)
#Combine lists into a pandas dataframe for easy graphing.
data = pd.DataFrame({'time': time, 
                   'precip': totalprecip})
data = data.set_index('time')
print(data)
data.to_pickle("Westmonthlyprecipanom.pkl")