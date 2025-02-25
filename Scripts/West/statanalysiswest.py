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
#import seaborn library
# variance, mean std dev
#distplot()
#compare to norm dist.
#skewness kurtosis.

#mannkendaltest
data_west = pd.read_pickle("EastPrecipanomYear+bestfit.pkl") #. WestPrecipanomYear+bestfit
print(data_west)
#H0 = no trend in data

result = mk.hamed_rao_modification_test(data_west['precipanomaly']) # original
print(result)



#Gaussian fit
#data_west = pd.read_pickle("WestPrecipanomYear+bestfit.pkl")

#Open pickle files 
data_east = pd.read_pickle("Eastmonthlyprecipanom.pkl") 
data_west = pd.read_pickle("Westmonthlyprecipanom.pkl") 
data_south = pd.read_pickle("Southmonthlyprecipanom.pkl") 
data_north = pd.read_pickle("Northmonthlyprecipanom.pkl") 
#join files together
frames = [data_east,data_north,data_south,data_west]
alldata = pd.concat(frames)
#calculate mean, stddev, min max values
mean = np.mean(alldata["precip"].values)
stdev = np.std(alldata["precip"].values)
max_x = alldata["precip"].max()
min_x = alldata["precip"].min()

#plot distribution using Seaborn library
ax = sns.distplot(alldata["precip"],
                    kde_kws={"color": "r", "lw": 2.5, "label": "Experimental", "alpha":0.6},
                    hist_kws={"density":True,"alpha": 0.6})


#Create Gaussian Distribution
x = np.linspace(min_x, max_x, 1000)
y = norm.pdf(x, mean, stdev)
#plot Gaussian
ax.plot(x, y, label = 'Gaussian', color = 'b', lw = 2.5, alpha = 0.6)
#plt mean line
ax.plot([mean,mean], [0.,0.00975], linewidth = 3, color = 'k', alpha = 0.6, label = 'mean = '+str("%.5g" % mean) )

#turn on grid
ax.grid()
ax.set_axisbelow(True)
#set legend position
ax.legend(loc = "upper left", facecolor = "wheat", fontsize = "large")
#set x-axis limits
ax.set_xlim(-150, 150)

#skewness kurtosis calculations using SciPy stats
stddev = alldata['precip'].std()
skew = stats.skew(data_west["precip"].values)
kurtosis = stats.kurtosis(data_west["precip"].values)

#Store, skewness and kurtosis in textbox and display on graph
textbox = '\n'.join(('Skewness = '+str("%.5g" % skew),
                    'Kurtosis = '+str("%.5g" % kurtosis)))
boxstyle = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.8, 0.2, textbox, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=boxstyle)   

#Graph labels
plt.title('Precipitation Anomaly Distribution')
plt.xlabel('Anomaly')
plt.ylabel('Density')       
plt.show()

