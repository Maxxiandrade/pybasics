animales = ["perro", "gato", "cocodrilo", "loro", "pez"]
numeros = [1,2,3,4,5]

for animal in animales:
    print(f'Ahora la variable animal es igual a {animal}')
    
for numero in numeros:
    resultado = numero * 2
    print(resultado)
    
#Iterando 2 listas/conjuntos/tuplas con la misma cantidad de elementos 
for animal, numero in zip(animales,numeros):
    #print(f'Recorriendo lista 1: {numero}')
    #print(f'Recorriendo lista 2: {animal}')
    print(f'{numero} animal: {animal}')
 
#Forma no optima de recorrer una lista con su indice (No funciona en conjuntos)
for num in range(5,10):
    print(num)
    
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorrer una lista/conjunto/tupla con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#Usando el for else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print('El bucle terminó')
    
