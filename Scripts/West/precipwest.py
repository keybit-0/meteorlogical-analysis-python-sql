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
        # Append year from loop to time list
        z = datetime.datetime(y, 1, 1 ,0 ,0 )
        time.append(z)

        # Sql query for annual temp and average it.
        sql = 'SELECT sum(precip) AS totalprecip FROM Project.AllData WHERE YEAR(date_time) =' + str(y) + ' and hour(date_time) = 23 and location = "W" ORDER BY id;'

        # Subtract the annual average temp from baseline average annual temp and append to anomaly.
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        totalprecip.append(result[0][0])
        
        print(z)
   
#Print time taken for loop.
end = datetime.datetime.now()  
print(end - start)
print(np.average(totalprecip))
#Combine lists into a pandas dataframe for easy graphing.
data = pd.DataFrame({'time': time, 
                   'totalprecip': totalprecip})
data = data.set_index('time')

ax = data.plot( kind = 'bar', width=0.95, alpha = 1, edgecolor = 'k', legend=False)

x_labels = data.index.strftime('%Y')
ax.set_xticklabels(x_labels, rotation = 'horizontal')
ax.set_xticks(ax.get_xticks()[::3])


plt.title('Annual Precipitation in West Ireland')
plt.xlabel('Year')
plt.ylabel('Total precipitation (mm)')

plt.show()
