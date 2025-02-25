
-- decided to add column for humidity and assign data type FLOAT.
ALTER TABLE Project.meteorological_data_N ADD humid FLOAT after absolutehumidity ;

-- populate humid column with appoximation for humidity
update Project.meteorological_data_N set humid = (5 * ( dewtemp - temp)) + 100 where id <= 500000;



