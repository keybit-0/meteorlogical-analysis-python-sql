-- Due to splitting script to download year not in order, the auto-increment id index is scrambled.
-- Create a new id index, id2 and increment it in order of datetime.
ALTER TABLE Project.meteorological_data_N ADD column id2 int;

SELECT @i:=0;
UPDATE meteorological_data_N SET id2 = @i:=@i+1 ORDER BY date_time;
SELECT @i:=0;
UPDATE Project.meteorological_data SET id2 = @i:=@i+1 ORDER BY date_time; 

-- Later found to be unnecessary, could have just ordered by datetime.