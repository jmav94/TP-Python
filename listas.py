"""Vamos a generar nuestra primera lista"""
my_list = [1, 2, 3]

"""Para acceder al primer índice lo haremos de la siguiente forma"""
print(my_list[0])

#1

########################################################

"""Si queremos utilizar la notación de slices (dividir) definimos los
índices en los que dividiremos nuestra lista."""

"""Aquí llamaremos desde el 2do índice hasta el final."""
print(my_list[1:])
#[2, 3]

########################################################

"""Para agregar un ítem a nuestra lista lo haremos con la función append"""
my_list.append(4)

"""Ahora la lista tendrá 4 objetos."""
print(my_list)
#[1, 2, 3, 4]

########################################################

"""Para modificar un elemento podemos hacerlo
referenciando su índice"""
my_list[0] = 'a'
print(my_list)
#['a', 2, 3, 4]

########################################################

"""El método pop eliminara el último elemento de nuestra lista"""
my_list.pop()
#4

print(my_list)
########################################################

"""Cuando una variable hace referencia a una lista
significa que apunta al mismo espacio en memoria,
esto significa que si cambia la lista se vera reflejado
en todas sus referencias, esto es un side effect"""

"""Creamos la lista a"""
a = [1, 2, 3]

"""Creamos la lista b que hará referencia a la lista a"""
b = a

print(id(a))
print(id(b))
