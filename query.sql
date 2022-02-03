#!/bin/bash

DB_USER='user'
DB_PASS='password'

DB_NAME='db'

TABLE='nps'

mysql --user=$DB_USER --password=$DB_PASS $DB_NAME --host=0.0.0.0 << EOF
drop table if exists nps_month_last_visit, new_table, promdem, results;

create table nps_month_last_visit as 
  select distinct patient_id, 
                  monthname(dateofAdmission) as month, 
                  year(dateofAdmission) as year, 
                  max(day(dateofAdmission)) as maxday 
    from nps
    group by patient_id, month,year;

create table new_table as 
  select t1.*,t2.month 
  from nps as t1
  inner join nps_month_last_visit as t2 
  on  t1.patient_id = t2.patient_id 
    and monthname(t1.dateofAdmission) = t2.month 
    and day(dateofAdmission) = maxday 
    and year(t1.dateofAdmission) = year;
                                            

create table promdem as 
select 
      patient_id,
      month,
      scores,
      case 
      when scores -> '$.satisfaction' > 7 then 1 
      else 0 
      end prom,
      case when scores -> '$.satisfaction' <= 7 then 1
      else 0
      end det
  from new_table;


create table results as 
  select 
    month,
    ((sum(prom) - sum(det))/count(*))*100 as nps
    from promdem
    group by month



EOF
