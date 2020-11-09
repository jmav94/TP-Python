import usuarios.usuario as modelo
import notas.acciones

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

        try:
            # Solicitar email y contraseña
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type (e))
            print(type (e).__name__)
            print("Login incorrecto, verifica los datos ingresados")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles: 
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()
        if accion == "crear":
            print("\nCrear nota")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            print("\nMostrar nota")
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("\nEliminar nota")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"\nOk {usuario[1]}, gracias por usar la aplicacion!")
            exit()
        
        