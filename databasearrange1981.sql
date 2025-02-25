update Project.meteorological_data set date_time = ADDTIME(date_time, "1:00:0") where id <= 8759;
update Project.meteorological_data set date_time = SUBTIME(date_time, "24:00:0")
where id <= 8759
and hour(date_time) = 0 ;