# imports
import mysql.connector
import pygrib
import numpy as np

import cdsapi
import datetime

# Api
c = cdsapi.Client()
time = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
c.retrieve('reanalysis-era5-land',
{
  'format': 'grib',
  'variable': [
      '2m_dewpoint_temperature', '2m_temperature', 'total_precipitation',
  ],
  'year': '1981',
  'month': [
      '01'
  ],
  'day': [
      '01'
  ],
  'time': [
      '00:00'
  ],
  'area': [
      53.76, -9.85, 53.26,
      -9.35,
  ],
}, ''+time+'_test2Galway.grib')

# MYSQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="key",
  password="123",
  database="Project"
)

mycursor = mydb.cursor()


# open grib
grbs = pygrib.open(''+time+'_test2Galway.grib')

#temp = grbs.select(name='2 metre temperature''total precipitation')

# print(temp)
for i in grbs:
  if(i.paramId == 167): 
    print("FUCKING EHHHY")
  elif(i.paramId == 168): 
    print("FUCKING EHHHY B")
  else:
    print("end")

    # temp_val = np.average(i.values)
    # sql = "INSERT INTO meteorological_data (temp, date_time) VALUES (%s, %s)"
    # val = (np.average(i.values), i.dataDate)
    # mycursor.execute(sql, val)
    # mydb.commit()

# 'tempdataMonthlyGalway/tempdata.grib'

# ** this is a read
# mycursor.execute("SELECT * FROM meteorological_data")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# END EXAMPLE **


