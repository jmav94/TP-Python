import mysql.connector

# Conexion a la base de datos
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "python")

# Validar que la conexion ha sido correcta
#print(database)

cursor = database.cursor(buffered= True)
# Crear base datos
cursor.execute("CREATE DATABASE IF NOT EXISTS python")
# si marca error de tipo unread_result hay que agregar el parametro buffered = true

# Consultar bases de datos
#cursor.execute("SHOW DATABASES")
#for bd in cursor:
#    print(bd)

# Crear tablas 
cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculo(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null, 
    CONSTRAINT pk_vehiculo PRIMARY KEY(id))""")

# Mostrar tablas 
cursor.execute("SHOW TABLES")
#for table in cursor:
#    print(table)

# Insertar datos en una tabla
#cursor.execute("INSERT INTO vehiculo VALUES(null,'Audi','A7', 1159000)")
#database.commit()

# Insertar datos desde tuplas
coches = [
    ('Ford','F150',600000),
    ('BMW','Serie 3',7200000),
    ('Tesla','Model S',2049000),
    ('Audi','A7',1159000)
]
#cursor.executemany("INSERT INTO vehiculo VALUES(null,%s,%s,%s)",coches)
#database.commit()

#Consulta a tablas de la base de datos
#cursor.execute("SELECT * FROM vehiculo")
#cursor.execute("SELECT * FROM vehiculo WHERE (precio > 100000  AND marca = 'Audi') OR modelo = 'F150'")


#result = cursor.fetchall()

#print("----- TODOS LOS CARROS -----")
#for coche in result:
#    print(coche)
#    print(coche[0],coche[2],coche[3])


# Solo devolver el primer resultado 
#cursor.execute("SELECT * FROM vehiculo")
#coche = cursor.fetchone()
#print(coche)
#print(coche[0],coche[3])

# Eliminar registros
#cursor.execute("DELETE FROM vehiculo WHERE modelo = 'A7'")
# Ejecutar los cambios en la bd
#database.commit()

# Contar los ros resultados de la ejecucion 
#print(cursor.rowcount, "Borrados..")

# Actualizar 
cursor.execute("UPDATE vehiculo SET precio = 100000 WHERE marca = 'Ford'")
database.commit()

# Contar los ros resultados de la ejecucion 
print(cursor.rowcount, "actualizados..")