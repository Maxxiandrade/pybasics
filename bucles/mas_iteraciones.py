frutas = ["manzana", "pera","ciruelas","banana","naranja","durazno"]
string = "Hola maxi"
numeros = [1,2,3,4]

#Evitando que se coma una pera con la sentencia continue
for fruta in frutas:
    if fruta == 'pera':
        continue
    print(f'Me voy a comer una {fruta}')
    

#Evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'naranja':
        break
else:
    print('Terminado')


#Recorrer un string
for letra in string:
    print(letra)
    

#for en una sola linea de codigo

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)