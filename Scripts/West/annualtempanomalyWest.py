import mysql.connector
import numpy as np
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle
# # 30 year average monthly mean temp (1961-1990) - from met Erieann - Claremorris, month:avgtemp(deg_C)
# baseline1961 = {1: 4.3, 2:5.9, 3:5.9, 4:7.6, 5:10.0, 6:12.6, 7:14.3, 8:14.0, 9:12.10, 10:9.8, 11:6.2, 12:5.1, 'year':8.9}#{1: 5.7, 2:5.6, 3:6.8, 4:8.2, 5:10.3, 6:12.6, 7:14.0, 8:14.1, 9:12.8, 10:10.8, 11:7.7, 12:6.6, 'year':9.6}
# # 30 year average monthly mean temp (1981-2010) - from met Erieann - Belmullet, month:avgtemp(deg_C)
# baseline1981 = {1:6.3 , 2:6.4, 3:7.6, 4:9.0, 5:11.2, 6:13.3, 7:14.9, 8:15.0, 9:13.6, 10:11.1, 11:8.5, 12:6.7, 'year':10.3}
# # convert baseline averages to K
# for key, value in baseline1961.items():
#     baseline1961[key] = round(value+273.15, 2)
# for key, value in baseline1981.items():
#     baseline1981[key] = round(value+273.15, 2)

# 40 year mean temp to be used as baseline for calculating anomalies
with open('baselinetempW.pickle', 'rb') as handle:
    baseline = pickle.load(handle)


# set empty lists
monthavgtemp=[]
time=[]
dates=[]
anomaly=[]

# Mysql connection + cursor
mydb = mysql.connector.connect(
    host="localhost",
    user="key",
    password="123",
    database="Project"
)
mycursortemp = mydb.cursor() 

start = datetime.datetime.now()

# get data
for y in range(1981, 2021):
        # Append year from loop to time list
        z = datetime.datetime(y, 1, 1 ,0 ,0 )
        time.append(z)

        # Sql query for annual temp and average it.
        sql = 'SELECT AVG(temp) AS avgtemp FROM Project.AllData WHERE YEAR(date_time) =' + str(y) + '\
             and location = "W" ORDER BY id;'

        # Subtract the annual average temp from baseline average annual temp and append to anomaly.
        mycursortemp.execute(sql)
        result = mycursortemp.fetchall()
        anomaly.append(float(result[0][0]) - baseline['year'])
        
        print(z)
   
#Print time taken for loop.
end = datetime.datetime.now()  
print(end - start)

#Combine lists into a pandas dataframe for easy graphing.
data = pd.DataFrame({'time': time, 
                   'anomaly': anomaly})
data = data.set_index('time')
##store data in pickle file for future use
data.to_pickle("WestTempanomYear.pkl")


##Plotting Anomaly - bar w/ colour###

#function to determine bar colour
def bar_color(anomaly,color1,color2):
    return np.where(np.array(anomaly)>0,color1,color2).T


#plot the dataframe in bar chart
# fig, ax = plt.subplots()
ax = data.plot(y='anomaly', use_index=True, kind = 'bar', width=0.95, color=bar_color(data['anomaly'],'r','b'), alpha = 1, edgecolor = 'k', legend=False)

#X axis label manipulation to only show year, problem only with bar graph
x_labels = data.index.strftime('%Y')
ax.set_xticklabels(x_labels, rotation = 'horizontal')
ax.set_xticks(ax.get_xticks()[::3])


#Label graph
plt.title('Annual Temperature Anomaly in West Ireland')
plt.xlabel('Year')
plt.ylabel('Anomaly in deg Celcius')

plt.show()


###Plotting Anomaly - line w/ trendline###


#line plot w/pandas
fig, ax = plt.subplots()
data.plot(y = 'anomaly', use_index=True, kind = 'line', legend=False, ax=ax, color='k', alpha = 0.7) #


##linear regression

#Get X and y values
X = data.index.values
Y = data['anomaly'].values
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
data.to_pickle("WestTempanomYear+bestfit.pkl")
print(data)
#plot line of best fit
data.plot(y = 'bestfit', use_index=True, kind = 'line', color='r', linewidth = 2, alpha = 1, legend = False, ax=ax)

#textbox
textbox = '\n'.join(('slope = '+str("%.5g" % m),
                    'Intercept = '+str("%.5g" % c)))
boxstyle = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.8, 0.1, textbox, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=boxstyle)

#format x axis to datetime.
plt.gcf().autofmt_xdate()
#turn on grid
ax.grid()
ax.set_axisbelow(True)
#centre graph on y-axis
yabs_max = abs(max(ax.get_ylim(), key=abs))
ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)

plt.title('Annual Temperature Anomaly in West Ireland')
plt.xlabel('Year')
plt.ylabel('Anomaly in deg Celcius')
plt.show()






