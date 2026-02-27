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

def total_numeros_pares(numeros: list) -> int:
    if len(numeros) == 0:
        return 0

    contador = 0
    if numeros[0] % 2 == 0:
        contador = 1
    return contador + total_numeros_pares(numeros[1:])

def es_palindromo(palabra: str) -> bool:
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    palabra_minuscula = palabra.lower()
    if palabra_minuscula[0] != palabra_minuscula[-1]:
        return False
    return es_palindromo(palabra_minuscula[1:-1])
