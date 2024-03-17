#Creando mi propia exepcion
class MiExepcion(Exception):
    def __init__(self, err):
        print(f'Impresionante, cometiste el siguiente error: {err}')
        
#Manejandola
try:
    raise MiExepcion('Jajajaja')
except:
    print('Como vas a cometer ese error?')
    
#Lanzando mi propia exepcion
raise MiExepcion('JAjaj')