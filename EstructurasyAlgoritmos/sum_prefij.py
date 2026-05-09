# Suma de prefijos

def prefix_sum(lista_numeros: list[int], r: int, l: int) -> int:
    prefijo: list[int] = []
    for i in range(len(lista_numeros)):
        if not prefijo:
            prefijo.append(lista_numeros[i])
        else:
            prefijo.append(prefijo[i - 1] + lista_numeros[i])
    if l == 0:
        res = prefijo[r] - prefijo[l]
        return res
    res = prefijo[r] - prefijo[l-1]
    return res
print(prefix_sum([3,4,5,6,13,24],4,0))

