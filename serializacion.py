f = open('D:/notas.txt', 'wt')
# También podía haber hecho: with open('notas.txt', 'wt') as f:

# Pedir el número de alumnos
num = 0
while n < 1:
    n = int( input('¿Cuántos alumnos tenemos? ') )
    while n > 0:
        # Pedir los datos de los alumnos
        dni = input('\nIntroduce el DNI (ocho números y letra) del alumno: ')
        nota1 = float( input('Dame la nota del primer examen: ') )
        nota2 = float( input('Dame la nota del segundo examen: ') )
        # Imprimir la media
        media = (nota1 + nota2) / 2
        print(dni, media, file=f)
        # También podía haber hecho: f.write(dni + ' ' + str(media) + '\n')
        n = n -1
        num = num +1

        f.close()