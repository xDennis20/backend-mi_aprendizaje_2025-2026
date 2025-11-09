""""Problema 14: Two Sum
Fecha: 19-10-2025 a 20-10-2025"""
def two_sum(lista_numeros: list[int],target: int) -> list[int]:
    indices = []
    for i in range(0,len(lista_numeros)):
        for j in range(i+1,len(lista_numeros)):
            if lista_numeros[i] + lista_numeros[j] == target:
                indices = [i,j]
    return indices
print(two_sum([3,2,5,7,2],4))

def two_sum_dict(lista_numeros: list[int],target: int):
    dict_indices = dict()
    indices = []
    for i in range(0,len(lista_numeros)):
        numero = lista_numeros[i]
        complemento = target - numero
        if complemento in dict_indices:
            indices = [dict_indices.get(complemento), i]
        dict_indices[lista_numeros[i]] = i
    return indices
print(two_sum_dict([3,2,5,7,2],4))