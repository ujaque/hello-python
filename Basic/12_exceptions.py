## Manejo de errores ##

numberOne = 5
numberTwo = 1

numberTwo = "1"
try:
    print(numberOne + numberTwo)
except ValueError as error:
    print("se ha producido un Value error: ", error)    
except TypeError as error:
    print("se ha producido un Type error: ", error)
except Exception as error: #error generico
    print("se ha producido un Type error: ", error)
