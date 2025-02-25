-- Create a new table to combine all locations into, make it the same as previous tables.

create table Project.AllData like Project.meteorological_data_N;

-- Insert from each location specific table the values required (temperature, precipitation, dewtemperature, humidity, location, datetime)
-- Data ordered by id2, the index used to sort by datetime
-- id column will auto-increment for each addition, giving us correct indexing.

insert into Project.AllData (temp, precip, dewtemp, humid, location, date_time)
select temp, precip, dewtemp, humid, location, date_time from Project.meteorological_data_N order by id2;

insert into Project.AllData (temp, precip, dewtemp, humid, location, date_time) 
select temp, precip, dewtemp, humid, location, date_time from Project.meteorological_data_S order by id2;

insert into Project.AllData (temp, precip, dewtemp, humid, location, date_time) 
select temp, precip, dewtemp, humid, location, date_time from Project.meteorological_data_E order by id2;

insert into Project.AllData (temp, precip, dewtemp, humid, location, date_time) 
select temp, precip, dewtemp, humid, location, date_time from Project.meteorological_data_W order by id2;

-- drop id2, which was used for previous indexing as it is not needed
ALTER TABLE Project.AllData drop column id2 ;