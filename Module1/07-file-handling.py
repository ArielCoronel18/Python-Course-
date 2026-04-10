### File Handling ###

import os

# .txt file
txt_file = open("Module1/my_file.txt", "w+") # para leer y escribir se utiliza "r+" y para crearlo por si se borra o no existe se utiliza "w+"
txt_file.write("Mi nombre es Ariel\nMi apellido es Coronel\n37 años\nY mi lenguaje\nfavorito es Python")

#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta JavaScript")
print(txt_file.readline())

txt_file.close()

# Eliminar fichero

#os.remove("Module1/my_file.txt")