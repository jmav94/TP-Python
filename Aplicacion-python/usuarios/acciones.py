import usuarios.usuario as modelo


class Acciones:
    def registro(self):
        print("\nOk!, vamos a registrarle en el sistema...")
        # capturar campos de la bd
        nombre = input("Cual es tu nombre?: ")
        apellido =input("Cual es tu apellido?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
        
        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!!")
    
    def login(self):
        print("\nok!, Identificate en el sistema...")
        # solicitar email y contraseña
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")