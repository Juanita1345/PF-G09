<div align="center">
<h1 style="text-align: center;">Vuelos del Estado de Georgia</h1>
</div>
<div align="center">
<h2 style="text-align: center;">Diseñado Por:</h2>
</div>

<div align="center">
<h3 style="text-align: center;">Cristian Alvarez</h3>
</div>

<div align="center">
<h3 style="text-align: center;">Cristhian Sánchez</h3>
</div>

<div align="center">
<h3 style="text-align: center;">Harold Laserna</h3>
</div>

<div align="center">
<h3 style="text-align: center;">Juanita Ortiz</h3>
</div>


<div align="center">
<h3 style="text-align: center;">Santiago Gallastegui</h3>
</div>


# Introducción

<div align="justify"> La aviación tiene una gran participación en el mercado, y es uno de los ejes centrales dentro de la economía. Durante el siglo XX esta industria se vio afectada por la guerra mundial y la gran depresión, sin embargo a partir de esta época hubo un incremento en la calidad de vida, lo cual aumentó la conectividad y con ello una mayor demanda de la aviación comercial. </div>
<p>&nbsp;</p>
<div align="justify"> Desde ese entonces la industria venía creciendo en un 3% anualmente hasta la crisis del 2008. Actualmente el mundo se enfrenta a dos crisis simultáneamente; el cambio climático y la pandemia del Covid-19, lo cual afectó de forma directa a la aviación comercial, adicional a otros factores como la guerra de Ucrania y el incremento de los precios del petróleo.
</div> 
<p>&nbsp;</p>
<div align="justify">
Afortunadamente en la industria aeronáutica se cuenta con gran información de históricos, lo que permite un análisis amplio de cómo ha ido evolucionando la industria, identificar qué factores son determinantes para obtener un buen rendimiento, generar métricas que realmente evalúan la competitividad dentro del mercado y generar una proyección sobre cuál es el mejor plan de operación.
</div>
<p>&nbsp;</p>
<div align="justify">
Se debe tener en cuenta que la aviación comercial es un mundo muy amplio y con múltiples enfoques, por lo tanto a la hora de hacer un estudio sobre este, se debe segmentar la información. A continuación se listan algunas de las categorías que se presentan en el gremio, sin embargo para este proyecto se trabajará desde un enfoque de vuelos comerciales de pasajeros, con datos gubernamentales , evaluando principalmente las rutas:</div>
<p>&nbsp;</p>
- <div align="justify">Cargo o pasajeros.</div>
- <div align="justify">Aerolíneas, gobierno y aeropuerto.</div>
- <div align="justify">Pasajeros, aeronaves, tripulación, rutas y empleados.</div>

# Objetivos

- <div align="justify">Definir tabla de hechos y dimensiones los cuales contengan la información suficiente de vuelos entre 2018 a 2022 del Estado de Georgia mediante la obtención de datos en la web. Dichas tablas de hechos y dimensiones son obtenidas mediante el análisis de columnas relevantes de los datos obtenidos, con la necesidad de poder generar estadística que nos muestre hechos relevantes sobre los vuelos, principalmente en relación a atrasos y cancelaciones. </div>
<p>&nbsp;</p>
 
 - <div align="justify">Construir KPI’s, las cuales nos ayuden a tomar decisiones relevantes a futuro de la posibilidad de ganancia de un vuelo dado, en este caso teniendo en cuenta ya la construcción de la tabla de hechos.
 </div>
<p>&nbsp;</p>

 - <div align="justify">Generar mapas relacionados a los vuelos categorizados por mes, dia y año, teniendo en cuenta únicamente el rango de datos de 2018 a 2022, en este caso dicho mapa es interactivo, es decir, el usuario final facilite la interpretación de un vuelo dado o un conjunto de vuelos teniendo en cuenta la tabla de hechos y dimensiones.
  </div>
<p>&nbsp;</p>

- <div align="justify">Crear modelo predictivo que permita determinar si un vuelo llegará a su destino con retraso desde una perspectiva categórica y temporal, dicha categoría está referida a la decisión de que dicho vuelo esté retrasado o no. </div>
<p>&nbsp;</p>

- <div align="justify">Crear Dashboard donde se encuentran los mapas interactivos, KPI’s (gráficas de interés) para una facilidad de interpretación fenomenológica, en este caso con los datos estructurados de la tabla de hechos y dimensiones. </div>
<p>&nbsp;</p>

# Alcance

<div align="justify">
Nuestro alcance primordial es obtener una estadística lo suficientemente específica para calcular los retrasos y cancelaciones futuras a los datos brutos, únicamente teniendo en cuenta los datos de vuelos desde el 2018 hasta el 2022 del Estado de Georgia. </div>
<p>&nbsp;</p>
<div align="justify">
 El estado de Georgia cuenta con 5 aeropuertos y uno de los aeropuertos con más demanda en el mundo, que es Atlanta International Airport, con aproximadamente 1000 vuelos diarios. De este modo obtenemos una base de datos aproximadamente de 4 millones de vuelos. 
 </div>
<p>&nbsp;</p>

 Los datos fueron obtenidos desde [OST_R | BTS | Transtats](https://www.transtats.bts.gov/), página donde informan todos los vuelos existentes en Estados Unidos. 

<p>&nbsp;</p>
<div align="justify">
Decimos reducir la cantidad de Aeropuertos, ya que consideramos que analizar una parte del todo es más de lo mismo. Los datasheet obtenidos contienen aproximadamente 110 columnas, con lo que podemos observar que hay mucha información irrelevante para nuestro análisis. 
 </div>
<p>&nbsp;</p>
<div align="justify">
La información que vamos a obtener de dichas tablas son:
  </div>
<p>&nbsp;</p>

| **Variable**              | **Nombre de columna**                            | **Justificación**                                                                                                                         | **Diccionario Datos**                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FL_DATE**               | Fecha de Vuelo                                   | Necesario para todo tipo de análisis temporales.                                                                                          | Fecha completa de la realización del vuelo (dd/mm/aaaa).                                                                                                                                                                                                                                                                                                                                      |
| **OP_CARRIER_AIRLINE_ID** | IdAerolineas                                     | Necesario para determinar a qué aerolínea hace referencia la información del registro.                                                    | Código asignado por la IATA y  usado para identificar a las compañías aéreas.                                                                                                                                                                                                                                                                                                                 |
| **ORIGIN_AIRPORT_ID**     | IdAeropuertoOrigen                               | Necesario para determinar a qué aeropuerto de origen hace referencia la información del registro.                                         | Código numérico del aeropuerto de origen. Se utilizará este campo para analizar el aeropuerto a través de varios años ya que un aeropuerto puede cambiar su código y además puede ser reutilizado.                                                                                                                                                                                            |
| **ORIGIN**                | Ubicación del aeropuerto de origen               | Necesario para determinar posible influencia de cada zona en la problemática y para elaborar mapas de tráfico aéreo.                      | Código del aeropuerto de origen del vuelo, expresado como una cadena de caracteres de tres letras. Código único para cada aeropuerto estandarizado por la Asociación Internacional de Transporte Aéreo (IATA).                                                                                                                                                                                |
| **ORIGIN_WAC**            | Código del área mundial del aeropuerto de origen | Necesario para determinar área de aeropuerto de origen.                                                                                   | Código numérico de la zona de origen del vuelo.                                                                                                                                                                                                                                                                                                                                               |
| **DEST_AIRPORT_ID**       | IdAeropuertoDestino                              | Necesario para determinar a qué aeropuerto de destino hace referencia la información del registro.                                        | Código numérico que identifica el destino de un único aeropuerto.                                                                                                                                                                                                                                                                                                                             |
| **DEST**                  | Ubicación del aeropuerto de destino              | Necesario para determinar posible influencia de cada zona en la problemática y para elaborar mapas de tráfico aéreo.                      | Código del aeropuerto de destino del vuelo, expresado como una cadena de caracteres de tres letras. Código único para cada aeropuerto estandarizado por la Asociación Internacional de Transporte Aéreo (IATA).                                                                                                                                                                               |
| **DEST_WAC**              | Código de área mundial del aeropuerto de destino | Necesario para determinar área de aeropuerto de destino.                                                                                  | Código numérico de zona de destino del vuelo.                                                                                                                                                                                                                                                                                                                                                 |
| **CRS_DEP_TIME**          | Hora de salida ideal                             | Necesario para analizar posible influencia de horario.                                                                                    | Sistema computarizado de reservaciones- Computerized Reservations Systems (CRS)   Hora de salida - Departure time. Tiempo que cada aerolínea tiene computado como tiempo de salida. Puede definirse como la hora de salida que la compañía estima a la que va a salir cada vuelo. Dato muy útil para comprobar la diferencia entre la hora real de salida y la hora estimada por la compañía. |
| **DEP_TIME**              | Hora de salida real                              | Necesario para analizar posible influencia de horario en la problemática en estudio.                                                      | Departure time. Hora de salida del vuelo en hora local real (LMT) expresado como un conjunto de cuatro dígitos, siendo los dos primeros la hora y los dos últimos los minutos. Tiempo computado en el momento en el que la aeronave abandona la puerta o gate. Dato esencial para calcular y prever los colapsos en función de la hora del día y horas punta..                                |
| **Dep_Delay**             | Diferencia entre Salida Ideal y Salida real      | Necesario para diversos análisis a realizar.                                                                                              | iferencia entre la hora de salida  o estimada por la compañía y la hora real de salida en origen, expresada en minutos como un número entero. Información útil para identificar el origen de un problema o retraso.                                                                                                                                                                           |
| **CRS_ARR_TIME**          | Hora de llegada ideal                            | Necesario para analizar posible influencia de horario en la problemática en estudio.                                                      | TIME Computerized Reservations Systems (CRS) arrival time. Tiempo que cada aerolínea tiene computado como tiempo de llegada. Puede definirse como la hora que la compañía estima a la que va a llegar cada vuelo. Dato muy útil para comprobar la diferencia entre la hora real de llegada y la hora estimada por la compañía.                                                                |
| **ARR_TIME**              | Hora de llegada real                             | Necesario para analizar posible influencia de horario en la problemática en estudio                                                       | Arrival time. Hora de llegada del vuelo en hora local real (LMT) expresado como un conjunto de cuatro dígitos, siendo los dos primeros la hora y los dos últimos los minutos.                                                                                                                                                                                                                 |
| **ARR_DELAY**             | Diferencia entre llegada ideal y llegada real    | Necesario para diversos análisis a realizar.                                                                                              | Diferencia entre la hora estimada por la compañía y la hora real de llegada en destino, expresada en minutos como un número entero. Información útil para identificar el origen de un problema o retraso.                                                                                                                                                                                     |
| **CANCELLED**             | Si tiende a valor 1 ( Vuelo cancelado)           | Necesario para diversos análisis a realizar.                                                                                              | Identificador de vuelo cancelado. Expresado como un valor binario, siendo cero si el vuelo se ha efectuado o uno si ha sido cancelado.                                                                                                                                                                                                                                                        |
| **CANCELLATION_CODE**     | Código de cancelación de vuelo                   | Necesario para determinar la causa de cancelación de algún vuelo.                                                                         | Código de cancelación. Expresado con un carácter alfabético en función de la causa de cancelación siguiendo la siguiente leyenda: A-"Carrier", B-"Weather", C-"National Air System", D-"Security".                                                                                                                                                                                            |
| **DIVERTED**              | Desviación del vuelo                             | Necesario para analizar influencia de desvìo de vuelo en problemática en estudio. Si el vuelo es desviado tiende a 1.                     | Indicador de vuelo desviado. Expresado como un valor binario, siendo cero si el vuelo se ha efectuado con normalidad o uno si ha sido desviado.                                                                                                                                                                                                                                               |
| **CRS_ELAPSED_TIME**      | Tiempo de vuelo                                  | Este tiempo de vuelo es necesario para calcular los retrasos de los vuelos y puede ser una cantidad que dependa dentro de nuestros KPI’s. | Computerized Reservations Systems (CRS) elapsed time. Tiempo que cada aerolínea tiene computado en su sistema como tiempo de vuelo, desde la salida en origen hasta la llegada en destino, expresado en minutos como un conjunto de enteros. Dato útil para la estimación e identificación de comportamientos o retrasos en ruta y la diferencia con el tiempo real de vuelo.                 |
| **CARRIER_DELAY**         | Retraso del transportista en minutos             | Cálculo importante para calcular el retraso del vuelo.                                                                                    | Retraso causado por la portadora. Expresado como un conjunto de enteros en minutos. Dato útil para identificar retrasos causados por este factor.                                                                                                                                                                                                                                             |
| **WEATHER_DELAY**         | Retraso por clima en minutos                     | Cálculo importante para calcular el retraso del vuelo.                                                                                    | Retraso causado por inclemencias meteorológicas. Expresado como un conjunto de enteros en minutos. Dato útil para identificar retrasos causados por este factor.                                                                                                                                                                                                                              |
| **NAS_DELAY**             | Retraso por tránsito Aéreo en minutos.           | Cálculo importante para calcular el retraso del vuelo.                                                                                    | Retraso causado por la National Air System. Expresado como un conjunto de enteros en minutos. Dato útil para identificar retrasos causados por este factor.                                                                                                                                                                                                                                   |
| **SEGURITY_DELAY**        | Retraso por seguridad en minutos                 | Cálculo importante para calcular el retraso del vuelo.                                                                                    | Retraso causado por los controles de seguridad o sus inspecciones. Expresado como un conjunto de enteros en minutos. Dato útil para identificar retrasos causados por este factor.                                                                                                                                                                                                            |
| **LATE_AIRCRAFT_DELAY**   | Retraso por avión en minutos                     | Cálculo importante para calcular el retraso del vuelo.                                                                                    | Retraso por llegada tarde de la aeronave. Expresado como un conjunto de enteros en minutos. Dato útil para identificar retrasos causados por este factor.   |
|**DISTANCE**|Distancia entre aeropuertos|Medida importante para el cálculo de la velocidad media de vuelo|Distancia en millas entre aeropuertos de origen y destino.|5|



# KPI's
- Volumen de pasajeros Aéreos (**Tentativo**)
- venta de tiquetes al mes (**Tentativo**)
- Porcentaje de cancelación de vuelos.
- Porcentaje de sitios poco frecuentes.
- Porcentaje de sitios muy frecuentes.
- Velocidad del vuelo y retrasos o cancelaciones.
- Cociente de retraso con cancelación.
- Indicador de retraso de aeropierto con respecto al mes anterior.
- Kilómetros recorridos por pasajero.

| **Valor del KPI**: RETRASOS AEROPUERTOS | Este KPI es un indicador que determina la sumatoria de los retrasos existentes de un aeropuerto respecto del mes anterior.          |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Requerimiento de Datos**              | Tiempo de llegada Ideal, Tiempo de llegada Real, Retraso                                                                            |
| **Fórmula**                             | Diferencia entre tiempo de llegada ideal menos tiempo de llegada real $RAP=TiempoLlegadaProgramada-TiempoLlegadaReal$ |

| **Valor del KPI**: RETRASOS AEROLÍNEAS | Este KPI es un indicador que determina la sumatoria de los retrasos existentes de una aerolínea respecto del mes anterior.                     |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Requerimiento de Datos**             | Tiempo de llegada Ideal, Tiempo de llegada Real, Retraso                                                                                       |
| **Fórmula**                            | Diferencia entre tiempo de llegada ideal menos tiempo de llegada real de retraso $RAP=TiempoLlegadaProgramada-TiempoLlegadarRealRetraso$ |

| **Valor del KPI**: VELOCIDAD DEL VUELO ENTRE AEROPUERTOS |Este KPI es un indicador sobre la velocidad media de las aeronaves trimestralmente entre aeropuertos.                                                              |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Requerimiento de Datos**                | Distancia entre aeropuertos, tiempo de vuelo entre aeropuertos.                                                                                                  |
| **Fórmula**                               | Diferencia entre tiempo de llegada ideal menos tiempo de llegada real de retraso $V_{vuelo}=\frac{DistanciaEntreEeropuertos}{TiempoDeVueloEntreAeropuertos}$ |

| **Valor del KPI**: CANCELACIONES ESTADO GEORGIA ESTÁNDAR | Este KPI es un indicador sobre la cantidad de cancelaciones del estado de Georgia respecto a la media mundial.                                                      |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Requerimiento de Datos**                               | Cancelaciones, Cantidad de vuelos, Cancelaciones de media mundial.                                                                                                  |
| **Fórmula**                                              | Cancelaciones en el estado de Georgia dividido en cancelaciones de media mundial. $C_{GeorgiaEstandar}=\frac{CancelacionesEstadoGeorgia}{CancelacionesMediaMundial}$ |

| **Valor del KPI**: TRÁFICO AÉREO | Este KPI es un indicador que representa el tráfico aéreo, o también visto como la demanda de transporte aéreo.                        |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| **Requerimiento de Datos**       | Número de pasajeros ingresados, distancia recorrida.                                                                                  |
| **Fórmula**                      | Número de pasajeros por los kilómetros recorridos $E(distanciaRecorrida)=\frac{1}{Total_Pasajeros}\sum (pasajeros*DistanciaRecorrida)$ |

# Tecnologías

<div align="justify">
 En primera instancia para este proyecto se plantea trabajar con herramientas en la nube como lo es AWS o Google Cloud, gracias a que con estas herramientas se ofrece una solución donde se puede consultar de forma remota y utilizando recursos de servidores externos. Adicionalmente se obtiene: optimización del procesamiento de limpieza, análisis estadístico y diseño agradable del dashboard. Entre estos dos se presenta una preferencia por el servicio de AWS, debido a que tiene mayor participación en el mercado.
 </div>
  <p>&nbsp;</p>
  <div align="justify">
 Finalmente como alternativa que los dos anteriores servicios no generen una optimización esperable, se usarán herramientas locales para el tratamiento de datos, como lo es Python y las librerías complementarias. 
 </div>
 
 | **AWS**                                                                                                                                | **Google Cloud**                                                                                                      | **Locales (Python y otros)**                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| - AWS Glue DataBrew -> Limpieza / - Dynamo AWS -> DB / - Amazon QuickSight -> Para visualizar / - Amazon SageMaker  -> Para Machine Learning | - Cloud DataFusion -> Limpieza / - Cloud SQL ->  DB / - DataStudio -> Para visualizar / - Google AI -> Para Machine Learning | - Pandas y Numpy -> Limpieza / - SQLite -> DB / - Streamlit -> Para visualizar / - Sklearn -> Para Machine Learning |

<div align="justify">
Teniendo en cuenta que las herramientas no son excluyentes entre sí,  usaremos librerías de python para generar limpiezas de prueba y análisis de prueba antes de la construcción del data warehouse.
 </div>
 
 # Roles
 
 - Project Manager (Cristhian Ipanaqué y Santiago Gallastegui): Organizar, gestionar, documentar
 - Data engineer (Juanita Ortiz, Harold Laserna y Cristian Alvarez):  Generar el ETL y DB 
 - Data Scientist (Harold Laserna y Cristian Alvarez): Generación del modelo predictivo
 - Data Analyst (Cristhian Ipanaqué, Santiago Gallastegui y Juanita Ortiz): Dashboard y análisis de resultados
# Cronograma de desarrollo

![Descripción de la imagen](/images/cronograma.png)
