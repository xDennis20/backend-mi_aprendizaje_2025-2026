"""Problema 18: Contains Duplicate (LeetCode #217)
Descripción: Dado un array de enteros nums,devuelve true si hay al menos un valor que aparece más de una vez.
Devuelve false si todos los elementos son únicos."""

def contar_duplicados(lista_numero: list[int]) -> bool:
    dict_numeros = {}
    for numero in lista_numero:
        if numero in dict_numeros:
            return True
        dict_numeros[numero] = None
    return False

def contar_duplicados_set(lista_numero: list[int]) -> bool:
    duplicados = set(lista_numero)
    return len(lista_numero) != len(duplicados)
print(contar_duplicados([1,3,4,4]))