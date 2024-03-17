#Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("archivos_problemas\\datos.csv")
#Convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#Mostrar el tipo de dato del primer elemento de la columna edad
print(type(df['edad'][0]))

#reemplazando los datos de "andrade" por "maestro"
df['apellido'].replace("andrade","maestro",inplace=True)
print(df['apellido'])

#Eliminando las filas con datos vacíos
df= df.dropna(axis=1)

#Eliminando las filas con datos repetidos
df = df.drop_duplicates()

#Creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")