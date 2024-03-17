import re

texto = """Hola maestro, como va? Este es el string 111.
Esta es la segunda linea de texto
Esta es la 3ra! Nos vemos maestro"""

#Haciendo una busqueda simple
resultado = re.findall('Esta',texto, flags=re.IGNORECASE) #Ignorar mayusculas

#\d -> Busca digitos numericos del 0 - 9
resultado = re.findall(r'\d',texto)

#\d -> Busca TODO MENOS digitos numericos del 0 - 9
resultado = re.findall(r'\D',texto)

#\w -> Busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r'\w',texto)

#\W -> Busca TODO MENOS caracteres alfanumericos
resultado = re.findall(r'\W',texto)

#\s -> Busca espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r'\s',texto)

#\S -> Busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
resultado = re.findall(r'\S',texto)

#. -> Busca TODO menos saltos de linea
resultado = re.findall(r'.',texto)

#\n -> Busca saltos de linea
resultado = re.findall(r'\n',texto)

#\ -> Cancelamos caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r'\.',texto)

#Armando un string que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s', texto)

#^ -> Busca el comienzo de una linea (buscando hola al principio de la linea)
resultado = re.findall(r'^Esta',texto, flags=re.M) #Quiero que cada linea la interpretes como la primera linea 

#$ -> Busca el final de una linea
resultado = re.findall(r'texto$', texto, flags=re.M)

#{n} -> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}',texto)

#{n,m} -> Almenos n, como máximo m
resultado = re.findall(r'\d{1,3}', texto) 

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{1,3}|Hola',texto)

print(resultado)