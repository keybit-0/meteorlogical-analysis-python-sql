

update Project.meteorological_data_E set humid = (5 * ( dewtemp - temp )) + 100;
