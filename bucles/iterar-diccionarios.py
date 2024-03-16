diccionario = {
    "nombre":"Maxi",
    "apellido":"Andrade",
    "edad":23
}

#Recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f'La clave es {key} y el valor es {valor}')
    
#Recorriendo diccionario para obtener las claves
for key in diccionario.items():
    print(key)