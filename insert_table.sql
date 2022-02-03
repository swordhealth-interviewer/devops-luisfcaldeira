#!/bin/bash

DB_USER='user'
DB_PASS='password'

DB_NAME='db'

TABLE='nps'

mysql --user=$DB_USER --password=$DB_PASS $DB_NAME --host=0.0.0.0 << EOF

CREATE TABLE $TABLE (
  id int not null AUTO_INCREMENT,
  patient_id int not null,
  scores json not null,
  dateOfAdmission date not null,
  primary key(id)
);

  
INSERT INTO $TABLE (patient_id,scores,dateOfAdmission)
  VALUES 
    (1323,'{"satisfaction": 9, "pain": 2, "fatigue": 2}','2020-06-25'),
    (9032,'{"satisfaction": 2, "pain": 7, "fatigue": 5}','2020-06-30'),
    (2331,'{"satisfaction": 7, "pain": 1, "fatigue": 1}','2020-07-05'),
    (2303,'{"satisfaction": 8, "pain": 9, "fatigue": 0}','2020-07-12'),
    (1323,'{"satisfaction": 10, "pain": 0, "fatigue": 0}','2020-07-09'),
    (2331,'{"satisfaction": 8, "pain": 9, "fatigue": 5}','2020-07-20');
#SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
EOF
