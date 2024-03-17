

def sumar_dos():
    while True:
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        try:
            resultado = int(a) + int(b)
        #Si lanzó una exepcion pedirle que reingrese los datos
        except Exception as e :
            print('Te pedí numeros')
            # print(f'Error: {type(e).__name__}')
        #si todo salio bien termina el bucle
        else:
            break
        finally:
            print('Esto se ejecuta se cumpla la condicion o no')
    return resultado

print(sumar_dos())