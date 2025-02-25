-- create a backup table and store current table inside of it

create table Project.bupall like Project.AllData;
insert into Project.bupall select * from Project.AllData ;
