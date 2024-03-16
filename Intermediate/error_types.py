## Error types ##

# SyntaxError

#print "Hola Comunidad" # Error
print ("Hola Comunidad")

# NameError
language = 'Spanish' # comentar para error
print(language)


# IndexError

my_list = ['Python', 'Swift', 'Kotlin', 'Dart', 'JavaScript']
print(my_list[0])
print(my_list[1])
print(my_list[4])
#print(my_list[5]) # descomentar para error


#ModuleNotFoundError

#import maths # Descomentar para error
import math

# AttibuteError

#print(math.PI)
print(math.pi)


# KeyError

my_dict = {"Nombre":"David",
           "Apellido": "Lopez",
           "Edad":39,
           1: "Python" }

#print(my_dict["Apelido"]) # Descomentar para error
print(my_dict["Apellido"])

# TypeError

#print(my_list["Nombre"]) # Descomentar para error
print(my_list[0])

# ImportError

#from math import PI # Descomentar para error
from math import pi

print(pi)

# ValueError

my_int = int("10")
#my_int = int("10 años") # Descomentar para error
print(type(my_int))

# ZeroDivisionError

print(4/2)
print(4/0)
