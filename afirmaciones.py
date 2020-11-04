def primera_letra(lista_de_palabras):
    primeras_letras = []
    
    for palabra in lista_de_palabras:
        try: 
            assert type(palabra) == str, f'{palabra} no es str'
            assert len(palabra) > 0, 'No se permiten str vacíos'

            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras

lista_de_palabras = ['Manza','Naranja','Mango', 'Fresa',15,'',2.6,True]
print('Las primeras letras validas son ',primera_letra(lista_de_palabras))
