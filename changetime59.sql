update Project.meteorological_data set date_time = ADDTIME(date_time, "23:59:59") 
where hour(date_time) = 0 and id <=500000 ;

update Project.meteorological_data set date_time = SUBTIME(date_time, "00:00:01") where not minute(date_time)=59 and id <= 500000;