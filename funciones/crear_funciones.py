#Creando una funcion simple
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == 'h'):
        adjetivo='loco'
    elif(sexo == 'f'):
        adjetivo='loca'
    else:
        adjetivo='crack'
    print(f'Hola {nombre}, que haces {adjetivo}')
    
nombre = input('Introduzca su nombre: ')
sexo = input('Introduzca su sexo (H/F): ')
saludar(nombre, sexo)


#Crear una funcion que nos devuelve valores

def crear_contraseña_random(numero):
    chars = "abcdefghij"
    num_entero = str(numero)
    numero = int(num_entero[0])
    c1 = numero - 2
    c2 = numero 
    c3 = numero - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num_entero*2}'
    return contraseña, numero

contraseña, primer_numero = crear_contraseña_random(231)
print(f'Tu contraseña es {contraseña}, y el numero utilizado fue {primer_numero}')


