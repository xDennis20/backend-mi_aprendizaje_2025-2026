"""PROBLEMA 4: Número Mayor en Lista
Enunciado:
Escribe una función que reciba una lista de números y devuelva el número más grande.
Fecha: 29-09-2025
"""
def numero_mayor_lista(lista_numero: list[int]) -> int:
    numero_mayor = lista_numero[0]
    for numero in lista_numero:
        if numero_mayor <= numero:
            numero_mayor = numero
    return numero_mayor