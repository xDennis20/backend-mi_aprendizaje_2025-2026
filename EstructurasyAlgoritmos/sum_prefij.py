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

def product_except_self(nums: list[int]) -> list[int]:
    prefijo = [1]
    for i in range(1,len(nums)):
        prefijo.append(prefijo[i - 1] * nums[i - 1])
    subfijo = [1]
    for derecha in range(1,len(nums)):
        subfijo.append(subfijo[derecha - 1]  * nums[-derecha])
    resultado = []
    for p,s in zip(prefijo,subfijo[::-1]):
        resultado.append(p*s)
    return resultado
print(product_except_self([1,2,3,4,5]))