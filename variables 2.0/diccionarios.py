#Creando diccionarios con dict()
diccionario = dict(
    nombre= "Maxi",
    apellido="Andrade"
)

#Las listas no pueden ser claves
diccionario={
    ("maxi",23):"hoola" #Las tuplas, sí
    #["maxi",23]:"hoola" #Las listas, no
    #{"maxi",23}:"hoola" #Los conjuntos no, a no ser que sea un frozenset
}

#Creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido"])

#Creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys("nombre","apellido")

#Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "No se")

print(diccionario)