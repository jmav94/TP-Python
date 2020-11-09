import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"ok {usuario[1]}, puedes crear una nueva nota")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Captura el contenido de la nota: ")

        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Listo, has guardado la nota {nota.titulo}")

        else:
            print(f"\n No se ha guardado la nota, intenta de nuevo {usuario[1]}")

    def mostrar(self, usuario):
        print (f"\n{usuario[1]} aqui estan tus notas: ")    
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        #print(notas)
        for nota in notas:
            print("*********************************")
            print(f"Titulo: {nota[2]}")
            print(f"Contenido: {nota[3]}")
            print("*********************************")

    def borrar(self,usuario):
        print(f"\nHola {usuario[1]} vas a borrar notas")
        titulo = input("\nIntroduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0],titulo)
        eliminar = nota.eliminar()

        if eliminar[0]>=1:
            print(f"La nota {nota.titulo} se ha borrrado")
        else:
            print("No se ha borrado la nota.")