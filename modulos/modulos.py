#Importar un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#Desde ese modulo importamos 2 funciones y les cambiamos el nombre
from modulo_saludar import Saludar, saludar_raro as saludar_como_coscu, saludar
import modulo_saludar as m_saludar

#Importamos todo
#from modulo_saludar import *

#Creamos las variables con los resultados
saludo = Saludar('Maxi')
saludo_raro = saludar_como_coscu('Roco')

#Mostramos los resultados
print(saludo)
print(saludo_raro)

#Para ver las propiedades y metodos del namespace
#print(dir(m_saludar))

#Accedemos al nombre de este modulo
print(__name__)

#Accedemos al nombre del modulo llamado
print(m_saludar.__name__)