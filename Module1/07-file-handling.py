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

# .json file

import json # json es una especie de mapa - un diccionario, crea calve valor

json_file = open("Module1/my_file.json", "w+")


json_test = {
    "Name": "Ariel", 
    "Surname": "Coronel", 
    "Age": 35, 
    "Languages": ["Python", "Swift", "Kotlin"],
    "WebSite": "https://arielcoro.dev"}

json.dump(json_test, json_file, indent = 2)

json_file.close()

with open("Module1/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Module1/my_file.json"))
print(json_dict)
print(type(json_dict))  # Ejecuta que es una clase de tipo Diccionario
print(json_dict["Name"])

# .csv file 

import csv

csv_file = open("Module1/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "SurName", "Age", "Language", "WebSite"])
csv_writer.writerow(["Ariel", "Coronel", "37", "Pytho", "https://arielcor.dev"])
csv_writer.writerow(["Ross", "", "2", "COBOL", ""])

csv_file.close()

with open("Module1/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file

#import xlrd  # Debe instalarse el modulo xlrd

# .xml

#import xml