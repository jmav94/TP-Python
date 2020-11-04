def factorial(n):
    """Calcula el factorial de n

    n int > 0
    return n!
    """

    # Para que la recursividad no sea infinita
    # definimos en que momento terminara.
    if n == 1:
        return 1

    # Llamamos a la función "factorial" a si misma
    # pero el valor de n va disminuyendo en 1
    # a medida que se repite su llamado.
    paso = n * factorial(n-1)
    print (paso)
    return paso

n = int(input('Escribe un entero: '))

print(factorial(n))
