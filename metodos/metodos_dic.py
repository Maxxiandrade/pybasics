diccionario={
    "nombre": "Maximiliano",
    "apellido":"Andrade",
    "edad": 23
}

#Devuelve las claves. (Tambien nos sirve para iterar)
claves = diccionario.keys()

#Devuelve el elemento de la key
claves = diccionario.get("apellido")

#Elimina todos los elementos del diccionario
# claves = diccionario.clear()

#Eliminando un elemento del diccionario
diccionario.pop("nombre")

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)