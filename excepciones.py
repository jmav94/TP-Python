"""Creamos una función en donde cada elemento de 
una lista es dividida por un divisor definido"""
def divide_elementos_de_lista(lista, divisor):
    """El programa intentara realizar la división"""
    try:
        return [i / divisor for i in lista]
    
    
    except ZeroDivisionError as e:
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))

# Python

def busca_pais(paises, pais):
    """
    Países es un diccionario. País es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None

paises = {1:'Mexico',2: 'Inglaterra' }

#for pais in paises:
 #   print(busca_pais(paises,pais))

[ print(busca_pais(paises,pais)) for  pais in paises]