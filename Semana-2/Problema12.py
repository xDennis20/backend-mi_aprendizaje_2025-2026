"""Problema 2: Rotar n posicion a la derecha
Fecha: 07-10-2025"""
def rotar_numeros(lista_numeros: list[int],k: int) -> list[int]:
    ultimos = []
    resto = []

    if not lista_numeros:
        return ultimos

    elif k == 0:
        return lista_numeros

    elif k > len(lista_numeros):
        k = k % len(lista_numeros)

    valor_recorrer = (len(lista_numeros) - k) - 1

    for i in range(0,len(lista_numeros)):
        numero = lista_numeros[i]
        if i <= valor_recorrer:
            resto.append(numero)
        else:
            ultimos.append(numero)
    return ultimos + resto

# print(rotar_numeros([1,2,3,4,5],2))
# print(rotar_numeros([1,2,3],4))
# print(rotar_numeros([1,2,3,4],0))
# print(rotar_numeros([],1))

def rotar_numeros_slicing(lista_numeros: list[int], k: int) -> list[int]:
    if not lista_numeros or k == 0:
        return lista_numeros
    k = k % len(lista_numeros) if k > len(lista_numeros) else k
    return lista_numeros[-k:] + lista_numeros[:-k]

print(rotar_numeros_slicing([1,2,3,4,5],2))
print()