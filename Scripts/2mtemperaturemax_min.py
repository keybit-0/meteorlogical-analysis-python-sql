
import numpy as np
#from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as tick
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pygrib
from datetime import datetime


grbs = pygrib.open('tempdataMonthlyGalway/tempdata.grib')
temp = grbs.select(name='2 metre temperature')
dtemp = grbs.select(name='2 metre dewpoint temperature')
test = grbs.select(name='2 metre temperature' '2 metre dewpoint temperature')[0]
print(test)


def str2year(value):
    string = str(value)
    if len(string) > 4:

        new_value = string[0:4]
        return new_value
    else:
        return value


avg_temp = []
avg_dtemp = []
time = []
Label = []

for i in temp:

    temp_val = i.values
    print(temp_val)
    avg_temp.append(np.average(temp_val))
    
    date = str(i.dataDate)
    time.append(date)
    
    

# for i in dtemp:

#     dtemp_val = i.values
#     avg_dtemp.append(np.average(dtemp_val))

for i in time:
    Label.append(str2year(i))



#plot 
x = time
#y1 = avg_dtemp 
y = avg_temp

fig, ax = plt.subplots()

ax.plot(x,y, c='b')
#ax.plot(x,y1, c='r')

plt.title('Average 2m Temperature in Galway')
plt.xlabel('Year')
plt.ylabel('2m Temperature (K)')


plt.xticks(x,Label, rotation = 'vertical')
ax.set_xticks(ax.get_xticks()[::12])

#ax.set_xticks(ax.get_xticks()[::60], rotation = 'vertical')
#ax.xaxis.set_major_formatter(DateFormatter("%Y%m%d"))
#plt.xticks(x1,Label, rotation = 'vertical')


plt.show()







# msg = grbs[2]
# print(msg)
# temp_vals = msg.values
# lat, lons = msg.latlons()
# print(lat, lons)
# print(temp_vals)
# print(temp_vals.shape)
# print(np.amax(temp_vals), np.amin(temp_vals), np.average(temp_vals))
# # DATA=np.array(tempObj)


# np.average
# # tempObj = gribs.select(name='2 metre temperature')

