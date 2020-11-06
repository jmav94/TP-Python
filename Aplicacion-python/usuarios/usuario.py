# modulo para fecha
import datetime
# modulo para cifrar conrtraseña
import hashlib
#importar conexion
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]
class Usuario:
    
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
        usuario = (self.nombre,self.apellido,self.email,cifrado.hexdigest(),fecha)
        try:
            cursor.execute(sql,usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0,self]
        
        return result

    def identificar(self):
        return self.nombre