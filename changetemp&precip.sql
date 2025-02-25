
-- precip change to mm instead of m
-- UPDATE Project.AllData SET precip = precip*1000;


-- monthly averages
-- Set @y= 1981; 
-- Set @d= 1;
-- Set @total = 0;
-- select temp, date_time from Project.AllData;
select month(date_time) as 'month' from Project.AllData where id<10000;



-- WHILE @x < 2021 DO 
--  if day(@d) = 
-- for x in range1981, 2021)