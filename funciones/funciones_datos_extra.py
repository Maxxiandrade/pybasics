#Creando una funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos un {adjetivo}'

frase_resultante = frase("Maxi", "Andrade", "Capo")
print(frase_resultante)


#Utilizando keywords arguments
def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos un {adjetivo}'

frase_resultante = frase(adjetivo="capo",nombre="Maxi",apellido="Andrade")
print(frase_resultante)


#Creando la misma funcion con parametro opcional y valor por defecto
def frase(nombre,apellido,adjetivo="capo"):
    return f'Hola {nombre} {apellido}, sos un {adjetivo}'

frase_resultante = frase(nombre="Maxi",apellido="Andrade")
print(frase_resultante)