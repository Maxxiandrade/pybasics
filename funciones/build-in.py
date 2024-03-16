numeros = [4,6,2,13]

#Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero mas bajo de una lista
numero_mas_chico = min(numeros)
print(numero_mas_chico)

#Redondeando a 6 decimales
numero = round(12.345678,2)
print(numero)

#Retorna False -> 0, vacio, False, ninguno  /  True -> distinto a 0, True, string, dato no vacio
resultado = bool(1)
print(resultado)

#Retorna True si todos los valores son verdaderos
resultado_all = all(["aksda",0.213, 0])
print(resultado_all)

#Suma todos los valores de un iterable
numeros = sum(numeros)
print(numeros)