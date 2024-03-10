## FUNCTIONS ##

def my_function ():
    print("Esto es una función")

my_function()

def sum_two_values(firts_number: int, second_number: int):

    print(firts_number + second_number)


sum_two_values(5, 7)


def sum_two_values_with_return(firts_number: int, second_number: int):
    
    return firts_number + second_number

my_result = sum_two_values_with_return(10, 5)

print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Lopez", name="David")


def print_name_with_default(name, surname, alias = "sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("David", "Lopez")


# el asterico indica que le puedo pasar varios parametros del mismo tipo
def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Adios", "Bla")

