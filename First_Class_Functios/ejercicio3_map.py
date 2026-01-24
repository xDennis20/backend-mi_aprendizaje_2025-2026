def mi_map(funcion_transformacion, lista: list) -> list:
    lista_mapeada = []
    for n in lista:
        lista_mapeada.append(funcion_transformacion(n))
    return lista_mapeada

def doble(n):
    return n * 2


def cuadrado(n):
    return n ** 2

numeros = [1, 2, 3, 4, 5]
print(mi_map(doble, numeros))
print(mi_map(cuadrado, numeros))