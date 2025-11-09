"""Problema 9:Duplicados en Lista (Viernes)
Enunciado:
Escribe una función que reciba una lista de números y devuelva True si hay algún número duplicado, False si todos son únicos.
Fecha: 02-10-2025"""

def numeros_duplicados(lista_numeros: list[int]) -> bool:
    numeros_guardados = []
    duplicado_encontrado = False
    for numero in lista_numeros:
        if numero in numeros_guardados:
            duplicado_encontrado = True
        else:
            numeros_guardados.append(numero)
    if duplicado_encontrado:
        return True
    return False

print(numeros_duplicados([1, 2, 3, 4]))
print(numeros_duplicados([1, 2, 3, 1]))
print(numeros_duplicados([5, 5, 5]))
print(numeros_duplicados([]))