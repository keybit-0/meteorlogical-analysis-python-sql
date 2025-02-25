
import mysql.connector
import numpy as np
#from matplotlib.ticker import FuncFormatter
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pygrib
from datetime import datetime


temp=[]
datetime=[]
dates=[]
precip=[]
precip2 = []

mydb = mysql.connector.connect(
    host="localhost",
    user="key",
    password="123",
    database="Project"
)
mycursor = mydb.cursor()

#gettemp
# sql = "SELECT temp FROM Project.meteorological_data where id <= 500000 order by id2;"
# mycursor.execute(sql)
# temp = mycursor.fetchall()

#getdate
sql = "SELECT date_time FROM Project.AllData where hour(date_time)=23 and location= 'W' order by id;"
mycursor.execute(sql)
datetime = mycursor.fetchall()
# for i in datetime:
#     i = datetime.strptime(i)


# dates = matplotlib.dates.date2num(datetime)

# plt.plot(datetime,temp)

# # ax.plot(x,y, c='b')

# plt.gcf().autofmt_xdate()

# plt.title('Average 2m Temperature in Galway')
# plt.xlabel('Year')
# plt.ylabel('2m Temperature (K)')


# # plt.xticks(datetime,Label, rotation = 'vertical')
# # ax.set_xticks(ax.get_xticks()[::12])
# plt.show()
print('done')


#Precip Plot
sql = "SELECT precip FROM Project.AllData where hour(date_time)=23 and month(datetime) = and location= 'W' order by id;"
mycursor.execute(sql)
precip = mycursor.fetchall()
#print(precip)

plt.plot(datetime, precip)
plt.gcf().autofmt_xdate()


plt.title('Average precipitation in Galway')
plt.xlabel('Year')
plt.ylabel('Rainfall(mm)')

plt.show()