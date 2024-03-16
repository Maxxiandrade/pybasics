#Creando un conjunto con set
conjunto = set(["Dato1", "Dato2"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato2"}

print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)  #Conjunto 2, es un subconjunto de conjunto 1? Sí, porque en el conjunto 2 podemos encontrar elementos que ya estan en conjunto 1 - o superconjunto
resultado = conjunto2 <= conjunto1

#Verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#Verificar si hay algun numero en comun
resulado = conjunto2.isdisjoint(conjunto1) #Cuando un solo elemento no coincide, ya da False

print(resultado)