def total_paginas_libros(libros: list) -> int:
    if len(libros) == 0:
        return 0
    return libros[0] + total_paginas_libros(libros[1:])

def n_factoria(n: int):
    if n < 0:
        raise ValueError("Error: El numero no debe ser negativo")
    if n == 0:
        return 1
    return n * n_factoria(n - 1)

def invertir_string(palabra: str) -> str:
    if len(palabra) == 0:
        return ""
    return invertir_string(palabra[1:]) + palabra[0]

def maximo_recursivo(numeros: list) -> int:
    if not numeros:
        raise IndexError("Error: Lista vacia")
    if len(numeros) == 1:
        return numeros[0]

    numero_mayor = maximo_recursivo(numeros[1:])
    if numeros[0] > numero_mayor:
        return numeros[0]
    else:
        return numero_mayor

print(maximo_recursivo([1,2,9,2,15,3]))