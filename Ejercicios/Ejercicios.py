# 1 Alumno es profesor
# 1 Alumno es asistente

# A) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
# El mayor de la clase es el profesor y el menor el asistente


alumno_1 = input('Ingresa la edad del primer alumno: ')
alumno_2 = input('Ingresa la edad del segundo alumno: ')



def quien_es_quien(alumno1, alumno2):
    edad_alumno_1 = int(alumno1)
    edad_alumno_2 = int(alumno2)
    lista_de_alumnos = list([edad_alumno_1,edad_alumno_2])
    lista_de_alumnos.sort(reverse=True)
    
    print(f"""La edad de el primer alumno es {edad_alumno_1}, y la del segundo es {edad_alumno_2}.
          Por lo tanto, el maestro es el que tiene {lista_de_alumnos[0]} años, y el asistente es el que tiene {lista_de_alumnos[1]} años""")
    

quien_es_quien(alumno_1, alumno_2)


def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input('Nombre del compañero? ')
        edad = int(input(f'Edad de {nombre}'))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente,profesor = obtener_compañeros(3)

print(f'El asistente es {asistente} y el profesor es {profesor}')

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b
    return fibonacci_lista

resultado = fibonacci(20)