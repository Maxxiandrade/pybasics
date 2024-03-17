with open("archivos\\texto_de_maxi.txt", 'w', encoding='UTF-8') as archivo:
    #Sobreescribir el archivo
    #archivo.write('Jajaja')
    
    #Agregando 2 lineas con writelines
    archivo.writelines(['Hola\n',"Como andas?\n"])