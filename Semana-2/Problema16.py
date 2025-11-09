"""PROBLEMA 16: Merge Two Sorted Lists

Enunciado:
Tienes dos listas ordenadas de números. Combínalas en UNA lista que también esté ordenada.
No uses .sort() - debes hacerlo manualmente."""

def ordenar_2listas(lista1: list[int],lista2: list[int]) -> list[int]:
    resultado = []
    i = 0
    j = 0
    if not lista1 and lista2:
        return resultado
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i+=1
        elif lista1[i] >= lista2[j]:
            resultado.append(lista2[j])
            j+=1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

print(ordenar_2listas([],[]))
print(ordenar_2listas([1,3,5],[2,4,6]))
print(ordenar_2listas([1,3,5],[2,9]))
print(ordenar_2listas([1,2,4], [1,3,4]))