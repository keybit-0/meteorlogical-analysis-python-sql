import mysql.connector
import numpy as np
import matplotlib
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
import pygrib
import datetime
import pandas as pd
import pickle

# 40 year monthly and year mean temp to be used as baseline for calculating anomalies
with open('baselinetempN.pickle', 'rb') as handle:
    baseline = pickle.load(handle)

# set empty lists
time=[]
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
   
    for m in range(1,13):
            ##old, not needed, save time# sql = 'SELECT year(date_time), month(date_time) FROM Project.AllData where month(date_time) =' + str(m) + ' and year(date_time) =' + str(y) + ' order by id;'
                ## mycursortime.execute(sql)
                ## print(mycursortime.fetchone())
        
        # Append month and year from loop to time list
        z = datetime.datetime(y, m, 1 ,0 ,0 )
        time.append(z)

        # Sql query for montly temp and average it.
        sql = 'SELECT AVG(temp) as avgtemp FROM Project.AllData where month(date_time) =' + str(m) + ' and year(date_time) =' + str(y) + ' and location = "N" order by id;'

            ## quicker to average inside the sql query, time saved.
                ##result = np.average(mycursortemp.fetchall())
                ##anomaly.append(float(result - baseline[m])

        # Subtract the monthly average temp from baseline average for that month and append to anomaly.
        mycursortemp.execute(sql)
        result = mycursortemp.fetchall()
        anomaly.append(float(result[0][0]) - baseline[m])
        
        print(z)
        
#Print time taken for loop.
end = datetime.datetime.now()  
print(end - start)


    ##Try to apply different colours to bars using masked arrays. Not working, decided to learn pandas dataframes.
        ## negative = np.ma.masked_where(anomaly < 0, anomaly, )
        ## positive = np.ma.masked_where(anomaly > 0, anomaly, )
        ## color = (anomaly > 0).apply(lambda x: 'g' if x else 'r')
        ## plt.plot(time, positive, time, negative)
        ## plt.gcf().autofmt_xdate()

#Combine lists into a pandas dataframe for easy graphing.
data = pd.DataFrame({'time': time, 
                   'anomaly': anomaly})
data = data.set_index('time')

##store data to pickle file for future use
data.to_pickle("NorthTempanomMonth.pkl")



###Plotting Anomaly - bar w/ colour###

# #function to determine bar colour
# def bar_color(anomaly,color1,color2):
#     return np.where(np.array(anomaly)>0,color1,color2).T

# #plot the dataframe in bar chart
# ax = data.plot(kind = 'bar', width=0.95, color=bar_color(data,'b','r'), edgecolor = 'k', linewidth=0.4, legend=False)

# #X axis label manipulation to only show year, problem only with bar graph
# x_labels = data.index.strftime('%Y')
# ax.set_xticklabels(x_labels, rotation = 'horizontal')
# ax.set_xticks(ax.get_xticks()[::12])
# plt.gcf().autofmt_xdate()
# ax.grid()


# #Label graph
# plt.title('Monthly Temperature Anomaly in West Ireland')
# plt.xlabel('Year')
# plt.ylabel('Anomaly in deg Celcius')
# plt.show()

###Plotting Anomaly - line w/ trendline###


#line plot w/pandas
fig, ax = plt.subplots()
data.plot(kind = 'line', legend=False, ax=ax, color='k', alpha = 0.7) #

#plt.show()
###linear regression

#Get X and y values
X = data.index.values
Y = data['anomaly'].values
#convert datetime object to number for calculations
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
#convert back to datetime
# x = matplotlib.dates.num2date(x)

# Put data in pandas dataframe
bestfit = pd.DataFrame({'time': time, 
                   'anomaly': list(y)})
bestfit = bestfit.set_index('time')

#store line of bestfit data in a pickle file for future access
bestfit.to_pickle("BestfitWestTempanomMonth.pkl")


    ##Not needed
        #ax.hlines(y=0, xmin=min_x, xmax=max_x, linewidth=0.5, color='k', alpha = 1, legend = False)

#plot line of best fit
bestfit.plot(kind ='line',color='r', alpha = 1,  ax=ax, legend = False)
plt.gcf().autofmt_xdate()


#textbox
textbox = '\n'.join(('slope = '+str("%.5g" % m),
                    'Intercept = '+str("%.5g" % c)))
boxstyle = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.8, 0.1, textbox, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=boxstyle)

#graph labels
plt.title('Monthly Temperature Anomaly in West Ireland')
plt.xlabel('Year')
plt.ylabel('Anomaly in deg Celcius')

plt.show()



