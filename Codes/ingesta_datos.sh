#!/bin/sh

echo "Por favor ingresa la base de datos que deseas subir: \n"

read variable
echo "Ingrese la contraseña del servidor: \n"
read contrasena

# Ingresar al aws
mysql -h database-1.c03capomxemg.us-east-2.rds.amazonaws.com -P 3306 -u admin -p
echo $contrasena

# ingestar datos desde el local
dirglobal = '/home/harold/Escritorio/PGS/PF-G09/Data/' + $variable  
echo "Subiendo datos, por favor espere..."
LOAD DATA LOCAL INFILE  $dirglobal
INTO TABLE columna 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

echo "Datos subidos."
