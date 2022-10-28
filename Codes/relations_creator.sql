create database nuevo;
use nuevo;

create table codigo_wac(
Code varchar(10),
Description varchar(100),
primary key(Code)
);

create table calendario(
fecha varchar(60),
anio int,
Mes_nombre varchar(60),
Mes int,
Dia int,
semana_del_anio int,
dia_de_la_semana int,
primary key (fecha)
);

create table aeropuerto_origen(
Code int,
Description varchar(100),
primary key(Code)
);

create table codigo_cancelaciones(
Code varchar(8),
Description varchar(100),
primary key(Code)
);

create table codigo_aerolinea(
Code varchar(60),
Description varchar(100),
primary key(Code)
);

drop table general;

create table general(
ID_FLYING int,
FL_DATE varchar(60),
OP_CARRIER_AIRLINE_ID varchar(60),
ORIGIN_AIRPORT_ID int,
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
LATE_AIRCRAFT_DELAY varchar(60),
primary key (ID_FLYING),
foreign key (ORIGIN_AIRPORT_ID) references aeropuerto_origen(Code),
foreign key (CANCELLATION_CODE) references codigo_cancelaciones(Code),
foreign key (OP_CARRIER_AIRLINE_ID) references codigo_aerolinea(Code),
foreign key (FL_DATE) references calendario(fecha),
foreign key (ORIGIN_WAC) references codigo_wac(Code)
);