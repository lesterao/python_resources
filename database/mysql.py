#!/usr/bin/python
import MySQLdb

# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("192.168.80.18","Lester","xxxx","wmomessages" )
 
# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()
sql = "SELECT * FROM stationset" 
# Ejecutamos un query SQL usando el método execute() que nos proporciona el cursor
try:
   # Ejecutamos el comando
   cursor.execute(sql)
   # Obtenemos todos los registros en una lista de listas
   resultados = cursor.fetchall()
   for registro in resultados:
      Block=registro[0]
      StationNumber=registro[1]
      Position_Latitud=registro[2]
      Position_Longitud=registro[3]
      # Imprimimos los resultados obtenidos
      print "Block=%s, StationNumber=%s, Position_Latitud=%d, Position_Longitud=%s" % (Block, StationNumber, Position_Latitud, Position_Longitud)
except:
   print "Error: No se pudo obtener la data"
 

# Nos desconectamos de la base de datos
bd.close()
