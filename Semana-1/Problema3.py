"""Enunciado:
Escribe una función que reciba un string y devuelva cuántas vocales (a, e, i, o, u) contiene.
 No distingue mayúsculas/minúsculas.
 Fecha: 29-09-2025"""

def contador_vocales(palabra: str) -> int:
    vocales = ["a","e","i","o","u"]
    contador = 0
    for letra in palabra.lower():
        if letra in vocales:
            contador+=1
    return contador

print(contador_vocales("hola"))
print(contador_vocales("Python"))
print(contador_vocales("xyz"))
print(contador_vocales("AEIOU"))