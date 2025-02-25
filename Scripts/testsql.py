import mysql.connector
import datetime
import matplotlib
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="key",
    password="123",
    database="Project"
)
###mysql query
    # mycursor = mydb.cursor()
    # temp=0
    # m=1
    # y=1981

    # sql = 'SELECT year(date_time), month(date_time) FROM Project.AllData where id <=8760 and month(date_time) =' + str(m) + ' and year(date_time) =' + str(y) + ' order by id;'
    #         mycursor.execute(sql)
    #         time.append(datetime.datetime(mycursor.fetchone()[0], mycursor.fetchone()[1] ,1 ,0 ,0 ))




###testdata
z = [datetime.datetime(2018, 1, 1),datetime.datetime(2018, 1, 2),datetime.datetime(2018, 1, 3), datetime.datetime(2018, 1, 4)]
anomaly = [10,-5, -20,-50]

##attempt at masked arrays
    #anomaly = np.array(anomaly)
    # positive = np.ma.masked_where(anomaly < 0, anomaly)
    # negative = np.ma.masked_where(anomaly > 0, anomaly)
    # middle = np.ma.masked_where(anomaly == 0, anomaly)
    # print(positive)
    # plt.plot( x, negative, x, positive)
    #plt.show()
    # ax = plt.subplot(111)
    # ax.bar(x, positive, width=0.2, color='b', align='center')
    # ax.bar(x, negative, width=0.2, color='g', align='center')
    # #ax.bar(x, middle, width=0.2, color='r', align='center')
    # ax.xaxis_date()

###bar color attempt
    # #color = (anomaly[i] > 0).apply(lambda x: 'g' if x else 'r')
    # color = (anomaly[]> 0).apply(lambda x: 'g' if x else 'r')
    # plt.bar(x, anomaly)#, color=bar_color(anomaly.items(), 'r','g'))

##decided dataframes pandas better
data = pd.DataFrame({'date': z, 
                   'temp': anomaly})
data = data.set_index('date')


fig, ax = plt.subplots()
##bar plot with color using pandas dataframe
    # def bar_color(anomaly,color1,color2):
    #     return np.where(np.array(anomaly)>0,color1,color2).T
    # data.plot(kind = 'bar', width=1.0, color=bar_color(data,'g','r'),  ax=ax)


##line plot w/pandas
data.plot(kind = 'line', ax=ax)

plt.gcf().autofmt_xdate()



####linear regression



X = data.index.values
Y = data['temp'].values
X = matplotlib.dates.date2num(X)

# Mean X and Y
mean_x = np.average(X)
mean_y = np.mean(Y)

# Total number of values
n = len(X)

# Using the formula to calculate 'm' and 'c' y = mx+c
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
m = numer / denom
c = mean_y - (m * mean_x)

# Printing coefficients
print("Slope", "Intercept")
print(m, c)

##Plotting
max_x = np.max(X) 
min_x = np.min(X) 

# Calculating line values x and y
x = np.linspace(min_x, max_x, n)
y = c + (m * x)
x = matplotlib.dates.num2date(x)

##make dataframe
bestfit = pd.DataFrame({'date': list(x), 
                   'temp': list(y)})
bestfit = bestfit.set_index('date')

bestfit.plot(kind ='line',  ax=ax)
ax.hlines(y=0, xmin=min_x, xmax=max_x, linewidth=5, color='r', alpha = 0.5)

#textbox
textbox = '\n'.join(('slope = '+str(m),
                    'Intercept = '+str(c)))
boxstyle = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.8, 0.1, textbox, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=boxstyle)
#pandas.DataFrame
plt.show()