-- This query fixes problems with the datetime values in the database.
-- A problem specific to 1981 where the data was off by 1 hour.
-- From the download script I wrote in Python, the maximum value for each day was being stored on hour 00:00:00

-- Add 1 hour to all datetimes in 1981, subtract a day for any datetimes that rolled over because of this. 
update meteorological_data_N set date_time = ADDTIME(date_time, "1:00:0") where id <= 8759;
update meteorological_data_N set date_time = SUBTIME(date_time, "24:00:0")
where id <= 8759
and hour(date_time) = 0 ;

-- Add 23:59:59 to 00:00:00 hours so 
update meteorological_data_N set date_time = ADDTIME(date_time, "23:59:59")
where hour(date_time) = 0;
-- subtract 1 second from every datetime except the ones altered above to create a uniform database. 
update meteorological_data_N set date_time = SUBTIME(date_time, "00:00:01")
where not minute(date_time) = 59;

