from usuarios import acciones
# import usuarios.acciones

print("""
Acciones disponibles: 
- Registro 
- Login
""")
hazEl = acciones.Acciones()
accion = input("Que desea hacer? ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()