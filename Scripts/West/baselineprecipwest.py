import mysql.connector
import numpy as np
import pygrib
import datetime
import pandas as pd
import pickle

## This script will create baseline averages so precipitation anomalies can be calculated.
yearavgtotal = 0
yearavg = 0
monthavg = 0
result = 0

#empty dictionary for storing baseline precipitation values
baselineprecipW = {} 


# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="key",
    password="123",
    database="Project"
)
mycursormonth = mydb.cursor() 
mycursoryear = mydb.cursor() 

for m in range(1,13):
    # Sql query for total monthly temp.
    sql = 'SELECT SUM(precip) as totalprecip FROM Project.AllData where month(date_time) =' + str(m) + ' and hour(date_time) = 23 and location = "W";'

    # Average all monthly temps over 40 years to get a baseline precipitation value for that month.
    mycursormonth.execute(sql)
    monthavg = mycursormonth.fetchall()
    #append to dictionary
    baselineprecipW[m]=(monthavg[0][0])/(len(range(1981, 2021)))
    
#get the total precipitation over the whole dataset and average over 40 years
sql = 'SELECT SUM(precip) as totalprecip FROM Project.AllData where hour(date_time) = 23 and location = "W" order by id;'
mycursoryear.execute(sql)
result = mycursoryear.fetchall()

# add average annual temp to baseline West dictionary
yearavg = (result[0][0])/(len(range(1981, 2021)))
baselineprecipW['year']= yearavg

# Dictionary baselineWest looks like:
# {1: 278.8710404765221, 2: 278.82679092272195, 3: 279.8465638806743, 4: 281.50411990483605, 5: 284.0620424352666, 
# 6: 286.2424135218726, 7: 287.78887214558097, 8: 287.68210292939216, 9: 286.1726274649302, 10: 283.5712959474133, 
# 11: 280.94217085096574, 12: 279.3689460340353, 'year': 282.92848373848176}

# Store this dictionary in pickle file so I can use it in other scripts.
with open('baselineprecipW.pickle', 'wb') as handle:
    pickle.dump(baselineprecipW, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('baselineprecipW.pickle', 'rb') as handle:
    output = pickle.load(handle)
print(output)