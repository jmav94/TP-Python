objetivo = int(input('Escoge un numero: '))

epsilon = 0.01      # Definimos un margen de error.
paso = (epsilon+.1)**2   # Los pasos para buscar la raíz sera igual a epsilon^2
respuesta = 0       # Inicializamos una respuesta 0


while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
