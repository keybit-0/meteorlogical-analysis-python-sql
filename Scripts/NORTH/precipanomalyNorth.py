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

with open('baselineprecipN.pickle', 'rb') as handle:
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
        # Append year from loop to time list
        z = datetime.datetime(y, 1, 1 ,0 ,0 )
        time.append(z)

        # Sql query for annual temp and average it.
        sql = 'SELECT sum(precip) AS totalprecip FROM Project.AllData WHERE YEAR(date_time) =' + str(y) + ' and hour(date_time) = 23 and location = "N" ORDER BY id;'

        # Subtract the annual average temp from baseline average annual temp and append to anomaly.
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        totalprecip.append(float(result[0][0]) - baseline['year'])
       
        print(z)
   
#Print time taken for loop.
end = datetime.datetime.now()  
print(end - start)
print(np.average(totalprecip))
#Combine lists into a pandas dataframe for easy graphing.
data = pd.DataFrame({'time': time, 
                   'precipanomaly': totalprecip})
data = data.set_index('time')

# ax = data.plot( kind = 'bar', width=0.95, alpha = 1, edgecolor = 'k', legend=False)

# x_labels = data.index.strftime('%Y')
# ax.set_xticklabels(x_labels, rotation = 'horizontal')
# ax.set_xticks(ax.get_xticks()[::3])


# plt.title('Annual Precipitation anomaly in West Ireland')
# plt.xlabel('Year')
# plt.ylabel('Precipitation anomaly (mm)')

# plt.show()

#Get X and y values
X = data.index.values
Y = data['precipanomaly'].values
#convert datetime to number for calculations
X = matplotlib.dates.date2num(X)

# Averages
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
n = len(X)

# Calculate 'm' and 'c', use y = mx+c to find y values. 
numerator = 0
denomenator = 0

# Forumla for slope given n, x and y values
for i in range(n):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denomenator += (X[i] - mean_x) ** 2
m = numerator / denomenator
c = mean_y - (m * mean_x)

# Printing coefficients
print("Slope", "Intercept")
print(m, c)

# Calculate line values
max_x = np.max(X) 
min_x = np.min(X) 
x = np.linspace(min_x, max_x, n)
y = c + (m * x)


# Put bestfit values in pandas dataframe
data['bestfit'] = list(y)
# bestfit = pd.DataFrame({'time': time, 
#                    'anomaly': list(y)})
# bestfit = bestfit.set_index('time')


##store line of bestfit data in a pickle file for future access
#bestfit.to_pickle("BestfitWestTempanomYear.pkl")
#data.to_pickle("NorthprecipanomYear+bestfit.pkl")
print(data)
#plot line of best fit
fig, ax = plt.subplots()
# fig, ax = plt.subplots()
data.plot(y = 'precipanomaly', use_index=True, kind = 'line', legend=False, ax=ax, color='k', alpha = 0.7) 
data.plot(y = 'bestfit', use_index=True, kind = 'line', color='r', linewidth = 2, alpha = 1, legend = False, ax=ax)

#textbox
textbox = '\n'.join(('slope = '+str("%.5g" % m),
                    'Intercept = '+str("%.5g" % c)))
boxstyle = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.8, 0.1, textbox, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=boxstyle)


plt.gcf().autofmt_xdate()
ax.grid()
ax.set_axisbelow(True)

yabs_max = abs(max(ax.get_ylim(), key=abs))
ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)

plt.title('Annual Precipitation Anomaly in North Ireland')
plt.xlabel('Year')
plt.ylabel('Anomaly in mm')
plt.show()
