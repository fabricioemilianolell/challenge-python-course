# el famoso fizz buzz
"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""


def multiplo():
    # value = ""
    for el in range(1,101):
        if el % 3 == 0 and el % 5 == 0:
            print("fizzbuzz")
        elif el % 3 == 0:
            print("fizz")
        elif el % 5 == 0:
            print("buzz")
        else:
            print(el)

multiplo()




# Anagrama
"""
Escribe una funcion que reciba dos palabras(String) y retorne verdadero o falso(bool) segun sean anagramas o no.
- Un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial
- No hace falta comprobar que ambas palabras existan
- Dos palabras exactamente iguales no son anagrama
"""

def anagrama(str_one,str_two):
    str_value_one = str_one.lower()
    str_value_two = str_two.lower()
    #si son iguales. es falso. no hay anagrama
    if str_value_one == str_value_two:
        return False
    #anagrama - compara arrays
    return sorted(str_value_one) == sorted(str_value_two)

print(anagrama("Amor","Roma"))
print(anagrama("CARO","ROCA"))
print(anagrama("frase","fresa"))




#Sucesión de Fibonacci
"""
Escribe un programa que imprima los 50 primeros numeros de la 
sucesion de fibonacci empezando en 0-
- la serie fibonacci se compone por una sucesión de números en la que el 
siguiente es la suma de los dos anteriores
- 0, 1, 1, 2, 3, 4, 5, 8, 13,21,34 - wuma los dos anteriores y te da el siguiente
(1 + 1)(2 + 1)(3 + 2)(3 + 4)(4 + 5)
"""

def fibonacci(num_prev = 0,num_next = 1):
     
    for el in range(0,50):
        print(num_prev)
        fibo = num_prev + num_next # 0 + 1 = 1 / 1 + 1 = 2 / 1 + 2 = 3 
        num_prev = num_next # 0 = 1 / 1 = 1 / 1 = 2
        num_next = fibo  # 1 = 1 / 1 = 2 / 2 = 3

print(fibonacci())


#Es un número primo
"""
Escribe un programa que se encargue de comprobar si es un numero primo o no.
Imprime los números primos entre 1 y 100
numero natural mayor que uno que tiene dos divisores positivos. el mismo y el numero
"""


def num_primo(number):
    # no es primo
    if number < 2:
        return False
    #no es primo. si se cumple es divisible por otro numero 
    for el in range(2,number):
        if number % el == 0:
            return False
    #todos los demas son primos. divisibles por uno y el mismo numero
    return True
num_primo(5)



def num_primo1():

    for number in range(1,101):
    
        if number >= 2:
            divisible = False
            
            for el in range(2,number):
                if number % el == 0:
                    divisible = True
                    break
            
            if not divisible:
                print(number)

num_primo1()


# invertir una cadena
"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo nos retornaría "odnum aloH"
"""

def invertirCadena(texto):
    str_text = ""
    for el in range(0, len(texto)):
        str_text += texto[len(texto) - el - 1]
    return str_text

print(invertirCadena("Hola mundo"))