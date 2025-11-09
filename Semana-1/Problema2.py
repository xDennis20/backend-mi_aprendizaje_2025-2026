"""PROBLEMA 2: Suma de Lista
Enunciado:
Escribe una función que reciba una lista de números y devuelva la suma de todos ellos.
Fecha: 29-09-2025"""

def suma_de_numeros_lista(lista_numeros: list[int]) -> int :
    total = 0
    if not lista_numeros:
        return total
    for numero in lista_numeros:
        total+=numero
    return total
print(suma_de_numeros_lista([1,2,3]))
print(suma_de_numeros_lista([10,-5,3]))
print(suma_de_numeros_lista([]))