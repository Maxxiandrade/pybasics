#listas (Se puede modificar)
list = ['Maxi', "Andrade", 23, True, 1.80,23]
list[3] = 'El kapanga 22'


#tupla (No se puede modificar)
tupla = ('Maxi', "Andrade", 23, True, 1.80,23)

print(tupla[0])
print(list[3])

#creando un conjunto (set) (no se puede llamar a los elementos por su indice) (no almacena datos duplicados)
conjunto = {'Maxi', "Andrade", 23, True, 1.80, 23}

# print(conjunto[3]) -> No puede acceder al elemento

print(tupla)

#creando un diccionario (dict)
diccionario = {
    'nombre': 'Maxi',
    "apellido": "Andrade",
    'edad': 23,
    'dato_duplicado':"Maxi"
}

print(diccionario['edad']+ 1)