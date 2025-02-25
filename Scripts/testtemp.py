import pygrib
import numpy as np


grbs = pygrib.open('17-11-2020 11:29:05_testtempGalway.grib')
temp = grbs.select(name='2 metre temperature')

#dtemp = grbs.select(name='2 metre dewpoint temperature')
msg = grbs[4]
print(msg)
temp_vals = msg.values
print(temp_vals)
# templist = []
# for i in temp:

#     temp_val = i.values
#     print(temp_val)
   
