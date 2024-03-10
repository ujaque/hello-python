## Clases ##


class Person:
    def __init__(self, name, surname) -> None:
        # al poner las barra bajas delante de name se transforma en privada y no se puede acceder
        # de forma normal, el acceso hay que realizarlo a traves de una funcion
        self.__name = name # propiedad privada
        self.surname = surname # propiedad publica
        self.full_name = f"{name} {surname}"
    
    def get_name(self):
        return self.__name 

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("David","Lopez")


my_person.walk()
my_person.get_name()