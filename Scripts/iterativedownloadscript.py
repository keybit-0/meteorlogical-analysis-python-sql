# imports
import mysql.connector
import pygrib
import numpy as np
import cdsapi
from datetime import datetime, timedelta

#Function to take values extracted from grib and store in MySQL database
def foobar(_temp, _dew, _precip, _Date):
  sql = "INSERT INTO meteorological_data (temp, dewtemp, precip, location, date_time) VALUES (%s, %s, %s, %s, %s)"
  val = (_temp, _dew, _precip, 'W', _Date)
  mycursor.execute(sql, val)
  mydb.commit()
  temp = 0
  dew = 0
  precip = 0
    

for x in range (1981,2020,1):                       #For loop that causes iteration

  # Api request
  c = cdsapi.Client()
  time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
  c.retrieve('reanalysis-era5-land',
  {
    'format': 'grib',
    'variable': [
        '2m_dewpoint_temperature', '2m_temperature', 'total_precipitation',
    ],
    'year': str(x),
    'month': [
        '01', '02', '03',
        '04', '05', '06',
        '07', '08', '09',
        '10', '11', '12',
    ],
    'day': [
        '01', '02', '03',
        '04', '05', '06',
        '07', '08', '09',
        '10', '11', '12',
        '13', '14', '15',
        '16', '17', '18',
        '19', '20', '21',
        '22', '23', '24',
        '25', '26', '27',
        '28', '29', '30',
        '31',
    ],
    'time': [
        '00:00', '01:00', '02:00',
        '03:00', '04:00', '05:00',
        '06:00', '07:00', '08:00',
        '09:00', '10:00', '11:00',
        '12:00', '13:00', '14:00',
        '15:00', '16:00', '17:00',
        '18:00', '19:00', '20:00',
        '21:00', '22:00', '23:00',
    ],
    'area': [
        53.76, -9.85, 53.26,
        -9.35,
    ],
  }, "download" + time + ".grib")

  # MYSQL connection
  mydb = mysql.connector.connect(        #connect to database
    host="localhost", 
    user="key",
    password="123",
    database="Project"
  )
  #MySQl cursor for selecting data
  mycursor = mydb.cursor()

  # # open grib using Pygrib
  grbs = pygrib.open('download' + time + '.grib')
  #variables
  temp = 0
  dew = 0
  precip = 0

  j = 0 # variable counter
  h = 0 # hour counter

  
  # print(temp)
  for i in grbs:                           #for each message in GRIB file
    j = j + 1                              #Add one to j variable
    if(i.paramId == 167):                  #if id of message is temp, let temp = average of array
        temp = np.average(i.values) 
    elif(i.paramId == 168): 
        dew = np.average(i.values)         #if id of message is dewtemp, let dewtemp = average of array
    elif(i.paramId == 228):
        precip = np.average(i.values)      #if id of message is precip, let precip = average of array
      
    if(j == 3):                            #when j = 3, extract datetime from GRIB, and append values to database(foobar function)
        j=0
        temp_string = str(i.dataDate)
        y = temp_string[0] + temp_string[1] + temp_string[2] + temp_string[3]
        m = temp_string[4] + temp_string[5]
        d = temp_string[6] + temp_string[7]

        cTime = datetime(int(y), int(m), int(d) ,hour=h)
        #
        h = h + 1                           #add 1 to h
        foobar(temp, dew, precip, cTime)
    if(h == 24):                            #when h=24, set it back to 0. This is false hour maker I made.
        h=0
        
        
        
  print("years done: " + str(x-1980))    #Print years done, repeat for next year



# 'tempdataMonthlyGalway/tempdata.grib'

# ** this is a read
# mycursor.execute("SELECT * FROM meteorological_data")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# END EXAMPLE **


