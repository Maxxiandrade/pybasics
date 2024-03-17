import pandas as pd
#Usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#Obteniendo los datos de la columna nombre
nombres = df["nombre"]

string = '0123456789'

#Slicing
#print(string[0:5])

#Ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#Ordenandolo de forma descendente
df_orden_descendente = df.sort_values("edad", ascending=False)

#Concatenando los 2 dataframes
df_concatenado = pd.concat([df, df2])

#Accediendo a la primeras 3 filas con head() 
primer_fila = df.head(3)

#Accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#Accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

#Obteniendo data estadística del dataframe
df_info = df.describe()

#Accediendo a un elemento especifico del dataframe con loc
elemento_especifico_loc = df.loc[2,"edad"] #con el nombre

#Accediendo a un elemento especifico del dataframe con iloc
elemento_especifico_iloc = df.iloc[2,2] #con el indice

#Accediendo a todas las filas de una columna
apellidos_loc = df.loc[:,"apellido"]

#Accediendo a todas las filas de una columna
apellidos_iloc = df.iloc[:,1]

#Accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#Accediendo a la fila 3 con iloc
fila_3iloc = df.iloc[2,:]

#Accediendo a filas con edad mayor a 20
mayor_que_20 = df.loc[df["edad"]>20,:]

print(mayor_que_20)