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

# set empty lists
monthavgtemp=[]
time=[]
dates=[]
winterprecip=[]

# Mysql connection + cursor
mydb = mysql.connector.connect(
    host="localhost",
    user="key",
    password="123",
    database="Project"
)
mycursor = mydb.cursor() 
mycursor2 = mydb.cursor() 
start = datetime.datetime.now()

# get data
for y in range(1982, 2021):

    sql = 'SELECT SUM(precip) as avgtemp FROM Project.AllData where month(date_time) IN (1,2) \
              and year(date_time) =' + str(y) + ' and hour(date_time) = 23 and location = "W" order by id;'   
   
    sql2 = 'SELECT SUM(precip) as avgtemp FROM Project.AllData where month(date_time) = 12 \
            and year(date_time) =' + str(y-1) + ' and hour(date_time) = 23 and location = "W" order by id;'  

    z = datetime.datetime(y, 1, 1 ,0 ,0 )
    time.append(z)

    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    mycursor2.execute(sql2)
    result2 = mycursor2.fetchall()
    winterprecip.append(float(result[0][0]) + float(result2[0][0]))
       
    print(z)
   
#Print time taken for loop.
end = datetime.datetime.now()  
print(end - start)

#Combine lists into a pandas dataframe for easy graphing.
data = pd.DataFrame({'time': time, 
                   'precip': winterprecip})
data = data.set_index('time')
print(data)
data.to_pickle("Westwinterprecip.pkl")