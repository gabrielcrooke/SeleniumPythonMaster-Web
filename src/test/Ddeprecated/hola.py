
#imprimir&formatear_string
Nombre = 'Gabriel'
#print(f'Hola {str(Nombre)}')

#Trabajando con arreglos
array = ['Venezuela', 'Argentina', 'Chile', 'Peru']
array.append('Bolivia')
#print(array[3])

for pais in array:
    print(pais)
    if pais == "Argentina":
        print(f'{Nombre}, vive en {pais}')
        break


#Trabajando con diccionarios
diccionario = {'nombre' : 'Gabriel', 'edad' : 22, 'cursos' : ['python', 'django', 'javascript']}

Nombre= diccionario['nombre']
print(f'Hola {Nombre}')


#acces_token = dicc['acces_token']

#validar = isinstance(dicc, dict)