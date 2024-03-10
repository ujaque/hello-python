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
    return sorted(palabra_uno.lower()) == sorted(palabra_dos.lower())

print(is_anagram("amor", "roma"))
