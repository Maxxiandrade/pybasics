numeros = [1,2,3,4,5,6,7,8,9]

#Funcion lambda. Son funciones anónimas
multiplicar_por_dos = lambda x : x * 2

#Creando una funcion comun
def es_par(num):
    if(num%2==0):
        return True
    
    
#Usando filter con una funcion comun
numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))


#Creando lo mismo que antes pero con lambda
numeros_impares = filter(lambda numero:numero%2==1,numeros)
print(list(numeros_impares))