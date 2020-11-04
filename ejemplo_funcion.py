"""Aquí definimos una función suma"""
def suma(a, b):
    total = a + b
    return total

"""Y para ejecutarlo simplemente llamamos a la
función por su nombre e ingresamos los parámetros que necesita"""

print(suma(2, 3))

def nombre_completo(nombre, apellido, inverso=False);
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

print(nombre_completo('Juan', 'Ahumada', True))

def func1(un_arg, una_func):
    def func2(otro_arg):
        return otro_arg * 2

    valor = func2(un_arg)
    return una_func(valor)

un_arg = 1

def cualquier_func(cualquier_arg):
    return cualquier_arg + 5

func1(un_arg, cualquier_func)

