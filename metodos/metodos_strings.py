string1 = "Hola soy maxi"
string2 = "Bienvenido!"

resultado = dir(string1) # -> Nos dice todos los metodos que se pueden utilizar 
mayus = string1.upper() # -> Convierte todo a MAYUSCULA
minus = string1.lower() #-> Convierte todo a minusculas

primer_letra_mayuscula = string1.capitalize() #-> convierte todo en minuscula y Capitaliza

#Buscamos un string en otro string, da un numero que es la posicion en la que se encuentra (devuelve -1 si no encuentra lo que pedimos)
busqueda_find = string1.find("la")

#Buscamos un string en otro string, la diferencia con find nos tira un error si no encuentra coincidencias
busqueda_index = string1.index("i")

#Si es numerico devuelve true, sino false
es_numerico = string1.isnumeric()

#Si es alfanumerico devuelve true, sino false. Los espacios son caracteres especiales
es_alfanumerico = string1.isalpha()

#Buscamos un string en otro string, devuelve la cantidad de veces que coincide
contar_coincidencias = string1.count('a')

#Contamos la longitud del string
string_length = len(string1)

#Verificamos si un string empieza con otro string, si es así devuelve True, sino False
empieza_con = string1.startswith("Hol")

#Verificamos si un string termina con otro string, si es así devuelve True, sino False
termina_con = string1.endswith("maxi")

#Reemplaza un pedazo del string por otro dado, si el valor 1 se encuentra en el string original, reemplaza el valor 1 por el valor 2
new_string = string1.replace('Hola', 'Buenas,')

#Separar strings con el string que le pasemos, lo devuelve como una LISTA
string_separada = string1.split(" ")

print(string_separada)