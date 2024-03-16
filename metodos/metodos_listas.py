#Creando una lista con list
lista = list(["Hola", "Maxi", 23])
num_list = list([123,44,2,663412,9])

#Cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregar elementos a la lista con append
agregando_con_append = lista.append("Agregado con Append")

#Agregando elementos en un indice específico
lista.insert(2, "Agregado con extend")

#Agregando varios elementos a la lista
lista.extend(["Agregado con Extend", 16.03])

#Eliminando un elemento por su indice (con -1 se elimina el ultimo de la lista)
lista.pop(-1)

#Removiendo un elemento de la lista por su valor
lista.remove(23)

#Ordena la lista por orden ascendente
num_list.sort()
num_list.sort(reverse=True) #Los ordena por orden descendiente

#Invierte los elementos
num_list.reverse()

#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index('Maxi')

print(elemento_encontrado)
print(num_list)
print(lista)


#Elimina todos los elementos de la lista
lista.clear()