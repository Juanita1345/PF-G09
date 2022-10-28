create database prueba;
use prueba;

create table columna (
FL_DATE varchar(60),
OP_CARRIER_AIRLINE_ID varchar(60),
ORIGIN_AIRPORT_ID varchar(60),
ORIGIN varchar(60),
ORIGIN_WAC varchar(60),
DEST_AIRPORT_ID varchar(60),
DEST varchar(60),
DEST_WAC varchar(60),
CRS_DEP_TIME varchar(60),
DEP_TIME varchar(60),
DEP_DELAY varchar(60),
CRS_ARR_TIME varchar(60),
ARR_TIME varchar(60),
ARR_DELAY varchar(60),
CANCELLED varchar(60),
CANCELLATION_CODE varchar(60),
DIVERTED varchar(60),
CRS_ELAPSED_TIME varchar(60),
DISTANCE  varchar(60),
CARRIER_DELAY varchar(60),
WEATHER_DELAY varchar(60),
NAS_DELAY varchar(60),
SEGURITY_DELAY varchar(60),
LATE_AIRCRAFT_DELAY varchar(60)
);

LOAD DATA LOCAL INFILE '/home/harold/Escritorio/PGS/PF-G09/Data/2018_2022_24.csv' 
INTO TABLE columna 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

ALTER TABLE columna
ADD Id_flying int auto_increment PRIMARY KEY
first;

select * from columna;