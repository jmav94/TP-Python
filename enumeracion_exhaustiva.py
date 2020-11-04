objetivo = int(input('Escoge un entero: '))

"""Inicializamos respuesta como 0"""
respuesta = 0

"""Mientras respuesta^2 sea menor que nuestro numero objetivo."""
while respuesta**2 < objetivo:
    print(respuesta, respuesta**2)
    respuesta += 1  # Respuesta aumentara en 1.

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')

else:
    print(f'{objetivo} no tiene una raíz cuadrada exacta')
