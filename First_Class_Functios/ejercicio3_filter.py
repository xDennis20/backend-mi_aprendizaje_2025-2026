def mi_filter(funcion_condicion, lista: list) -> list:
    lista_filtrada = []
    for n in lista:
        if funcion_condicion(n):
            lista_filtrada.append(n)
    return lista_filtrada

def es_par(n):
    return n % 2 == 0


def es_mayor_que_5(n):
    return n > 5


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mi_filter(es_par, numeros))
print(mi_filter(es_mayor_que_5, numeros))