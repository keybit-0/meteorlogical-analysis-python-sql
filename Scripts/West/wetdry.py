import mysql.connector
import datetime
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from scipy.stats import norm
from scipy import stats
import seaborn as sns
import numpy as np
import pymannkendall as mk

maxprecip = []
time=[]
wetdays=[]

mydb = mysql.connector.connect(
    host="localhost",
    user="key",
    password="123",
    database="Project"
)
mycursor = mydb.cursor() 

start = datetime.datetime.now()

#get data
for y in range(1981, 2021):

    # Append year from loop to time list
    z = datetime.datetime(y, 1, 1 ,0 ,0 )
    time.append(z)

    # Sql query for annual temp and average it.
    sql = 'SELECT precip FROM Project.AllData WHERE precip > 10 AND YEAR(date_time) = ' + str(y) + ' and hour(date_time) = 23 and location = "E";'  
            # and month(date_time) =' + str(m) + '

    # Subtract the annual average temp from baseline average annual temp and append to anomaly.
    mycursor.execute(sql)
    result = mycursor.fetchall()
    maxprecip.append(result[0][0])
    # totalprecip.append(float(result[0][0]) - baseline['year'])
    
    print(z)

data = pd.DataFrame({'time': time, 
                   'maxprecip': maxprecip})
data = data.set_index('time')
data.to_pickle("Eastmaxprecipyear.pkl")

data = pd.read_pickle("Westwetdaysyear.pkl") 

start_date = '2000-01-01'
end_date = '2020-12-31'
mask = (data.index >= start_date) & (data.index <= end_date)



X = data.index.values
Y = data['wetdays'].values
#convert datetime to number for calculations
X1 = matplotlib.dates.date2num(X)
print(data) # .loc[mask]


mktest = mk.original_test(data['wetdays']) #  .loc[mask] hamed_rao_modification .iloc[23:40,0]
res = stats.theilslopes(Y, X1, 0.95)
lsq_res = stats.linregress(X1, Y)
print(mktest)
print(res)
print(lsq_res)
fig = plt.figure()
ax = fig.add_subplot(111)

data.plot(ax=ax, legend = False)


plt.gcf().autofmt_xdate()
ax.grid()
ax.set_axisbelow(True)

# yabs_max = abs(max(ax.get_ylim(), key=abs))
# ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)

plt.title('Number of Annual Heavy Rainfall Events, West')
plt.xlabel('Year')
plt.ylabel('# of heavy rainfall events')
plt.show()



plt.show()


###Variation