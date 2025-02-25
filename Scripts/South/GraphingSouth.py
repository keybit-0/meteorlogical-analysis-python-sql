
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
sql = "SELECT date_time FROM Project.meteorological_data where hour(date_time)=23 and id <= 500000 order by id2;"
mycursor.execute(sql)
datetime = mycursor.fetchall()
print(datetime)
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



#Precip Plot
sql = "SELECT precip FROM Project.meteorological_data where hour(date_time)=23 and id <= 500000 order by id2;"
mycursor.execute(sql)
precip = mycursor.fetchall()
#print(precip)

#precip = [x*1000 for x in precip ]
for i in precip:
    precip2.append(i*1000)
    #print(i)
print(precip2)
# for i in datetime:
#     dates.append(matplotlib.dates.date2num(i))
#dates = matplotlib.dates.date2num(datetime)

plt.plot(datetime, precip)
plt.gcf().autofmt_xdate()


plt.title('Average precipitation in Galway')
plt.xlabel('Year')
plt.ylabel('Rainfall(mm)')

plt.show()