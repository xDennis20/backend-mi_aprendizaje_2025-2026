"""Enunciado:
Escribe una función que reciba un número entero y devuelva True si es par, y False si es impar.
Fecha: 29-09-2025
"""
def par_impar(numero: int) -> bool:
    return numero % 2 == 0

print(par_impar(10))