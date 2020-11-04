print("""
Acciones disponibles: 
- Registro 
- Login
""")

accion = input("Que desea hacer?")

if accion == "registro":
    print("Ok!, vamos a registrarle en el sistema...")
    # capturar campos de la bd

elif accion == "login":
    print("ok!, Identificate en el sistema...")
    # solicitar email y contraseña