"""Problema 10: Fizzbuzz
Escribe una función que reciba un número n y devuelva una lista con los números del 1 al n, pero:

Si el número es divisible por 3, en vez del número pon "Fizz"
Si es divisible por 5, pon "Buzz"
Si es divisible por ambos (3 y 5), pon "FizzBuzz"
Si no, pon el número
Fecha: 03-10-2025"""

def fizzbuzz(numero_objetivo: int) -> list:
    lista_final = []
    for numero in range(1,numero_objetivo + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            lista_final.append("FizzBuzz")
        elif numero % 3 == 0:
            lista_final.append("Fizz")
        elif numero % 5 == 0:
            lista_final.append("Buzz")
        else:
            lista_final.append(numero)
    return lista_final

print(fizzbuzz(5))
print(fizzbuzz(15))