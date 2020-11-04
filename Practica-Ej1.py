class Persona():
    def __init__(self, nombre="",edad=0,dni=""):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni = dni
        if self.__dni != "":
            self.validarDNI()
    
    @property
    def nombre(self):
        """
        retornar el valor del atributo nombre
        """
        return self.__nombre

    @property
    def edad(self):
        """
        retorna el valor del atributo edad
        """
        return self.__edad

    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    def validarDNI(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni)!=9:
            print("DNI incorrecto")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""

    @dni.setter
    def dni(self,dni):
        self.__dni = dni
        self.validarDNI()

    @edad.setter
    def edad(self,edad):
        if edad<0:
            print("Edad incorrecta")
            self.__edad = 0
        else: 
            self.__edad = edad

    def mostrar(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad} \nDNI: {self.dni}'

    def esMayorDeEdad(self):
        return self.edad>=18

if __name__ == '__main__':
    unaPersona = Persona()
    unaPersona.nombre = input("Captura el nombre: ")
    unaPersona.edad = int(input("Captura la edad: "))
    unaPersona.dni = input("Captura el dni: ")

    print(unaPersona.mostrar())
    print(unaPersona.esMayorDeEdad())