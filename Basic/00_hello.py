# Esto es un comentario
# Hola mundo
print("Hola Python")


"""
Este es un comentario
en varias lineas
"""

# Consultar tipo de dato
print(type("hello"))
print(type(5))

language = 'Python'

mi_lista = list()
otra_lista = ['David', 'Lopez']

print(type(otra_lista))

print('David' in otra_lista)


my_dict = dict()
my_other_dict = {'Nombre': 'David',
                 'Apellido': 'Lopez',
                 'Edad': 39,
                 'Lenguajes': {'Python', 'Swift', 'Kotlin'}
                               }
print(my_dict)

print(my_other_dict['Lenguajes'])

print('David' in my_other_dict)
print('Nombre' in my_other_dict)

print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())

# Crea un diccionario con claves y sin valores en blanco
print(dict.fromkeys(('Nombre', 'Apellido', 'Piso')))

# crea una copia del diccionario, pero vacio
print(dict.fromkeys(my_other_dict))

new_dict = dict.fromkeys(my_other_dict, ('David', 'Lopez'))

print(list(new_dict))

print(list(my_other_dict.values()))

