"""Enunciado:
Escribe una función que reciba una lista de números y un número objetivo,
y devuelva cuántas veces aparece ese número en la lista.
Fecha: 01-10-2025"""
def contar_ocurrencia(lista_numero: list[int],numero_objetivo: int) -> int:
    contador = 0
    for numero in lista_numero:
        if numero == numero_objetivo:
            contador+=1
    return contador

print(contar_ocurrencia([1, 2, 3, 2, 4, 2], 2))
print(contar_ocurrencia([5, 5, 5], 5))
print(contar_ocurrencia([1, 2, 3], 9))