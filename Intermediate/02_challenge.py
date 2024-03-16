## Challenges ##

"""
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""

def fizzbuzz(value):
    
    if (value % 3 == 0 and value % 5 == 0):
        return "fizz"
    elif value % 5 == 0:
        return "buzz"
    if value % 3 == 0:
        return "fizzbuzz"
    else:
        return value


lista = [fizzbuzz(i) for i in list(range(1,101,1))]

print(lista)



"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """

def is_anagrama(palabra_uno, palabra_dos):
    
    reversed_palabra_dos = palabra_dos[::-1]

    if palabra_uno == reversed_palabra_dos:
        return True
    else:
        return False

print(is_anagrama("amor", "roma"))


def is_anagram(palabra_uno, palabra_dos):
    if palabra_uno == palabra_dos:
        return False
    return sorted(palabra_uno.lower()) == sorted(palabra_dos.lower())

print(is_anagram("Amor", "Roma"))

"""
/* Sucesion de fibonacci
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

def fibonacci():

    fibonacci_list = [0,1] 
    for i in list(range(2,50)):
        fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
        
    print(fibonacci_list)

fibonacci()


def fibonacci_2():

    prev = 0
    next = 1

    for i in range(0,50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci_2()

"""  es un numero primo?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

def numero_primo():
    for number in range(2, 101):
        is_prime = True
        for index in range(2, number):
            if number % index == 0:
                is_prime = False
                break
        if is_prime:
            print(number)

numero_primo()

# Invirtiendo Cadenas

"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""

def reverse(text):

    reversed_text = ""
    text_len = len(text)
    
    for index in range(0, text_len):
        reversed_text += text[text_len - index -1]

    return reversed_text

print(reverse("Hola Mundo"))