def binary_search(lista: list, elemento_buscar: int) -> int | None:
    bajo = 0
    alto = len(lista) - 1 #Punteros para hayar el medio de la lista
    while bajo <= alto: # Esto es para que mientras no nos pasemos del indice alto no termine ya que es el final de la lista
        medio = (bajo + alto) // 2 #obtenemos el medio de la lista
        if lista[medio] == elemento_buscar: #Si medio coincide con el elemento que buscamos retornamos el indice medio
            return medio
        elif lista[medio] < elemento_buscar: # Si el elemento es mayor que medio
            bajo = medio + 1 #Pasamos el valor de medio a bajo aumentando uno (achicando mas la lista) para no buscar numero ya pasado
        elif lista[medio] > elemento_buscar: # Si el elemento es menor que medio
            alto = medio - 1 #Pasamos el valor de medio a alto menorando 1 achicando la lista
    return None
print(binary_search([1, 2, 3, 4, 5, 6], 6))
