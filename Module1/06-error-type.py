# Error Type

# xxxxxxxxxxxxxxxxx    SyntaxError     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
#print "¡Hola Mundo!" # Error en la Sintaxis
print("¡Hola Mundo!")

# xxxxxxxxxxxxxxxxx      NameError    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
#print(language)         # No esta definida
language = "Spanish"
print(language)

# xxxxxxxxxxxxxxxxx     IndexError    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) #IndexError porque el elemento encuentra fuera del Rango de la Lista

# xxxxxxxxxxxxxxxx     ModuleNotfoundError     xxxxxxxxxxxxxxxxxxx #
#import maths # Genera Error porque el Modulo no es Correcto
import math

# xxxxxxxxxxxxxxxxx     AttributeError      xxxxxxxxxxxxxxxxxxxxxxxxx #
#print(math.PI)  # Genera Error porque el atributo PI en mayuscula no existe
print(math.pi)

# xxxxxxxxxxxxxxxxxxx     KeyError    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
my_dict = {"Nombre":"Ariel", "Apellido": "Coronel", "Edad":35, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Genera Error porque la (clave-Key) no es correcta
print(my_dict["Apellido"])

# xxxxxxxxxxxxxxxxxxxx     TypeRror    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
#print(my_list["Nombre"])  # Genera Error porque no puedes pasar un String(cadenaTexto)
print(my_list[0])

# xxxxxxxxxxxxxxxxxx       ImportError     xxxxxxxxxxxxxxxxxxxxxxxxxx #
#from math import PI # Genera Error porque no esta dentro de la libreria
from math import pi
print(pi)

# xxxxxxxxxxxxxxxxxx        ValueError      xxxxxxxxxxxxxxxxxxxxxxxxx #
#my_int = int("10 Años") # Genera un Error porque la cade texto no se puede transformar
my_int = int("10")
print(type(my_int))

# xxxxxxxxxxxxxxxxxx        ZeroDivisionError       xxxxxxxxxxxxxxxxx #
print(4/2)
#print(4/0)  # Genera Error porque no se puede dividir entre 0