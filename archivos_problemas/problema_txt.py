#2 listas, una con nombres y otra con apellidos

nombres = ["maxi","jose","marlen","victor","roberto","pedro"]
apellidos=["andrade","urtiaga","camalache","robledo","sanchez"]

#Registrar esta informacion en un TXT de forma optima

with open("archivos_problemas\\nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son\n\n")
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n------------\n') for n,a in zip(nombres,apellidos)]