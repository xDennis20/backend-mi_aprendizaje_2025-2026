"""Problema 8: Fibonacci
Fecha: 02-10-2025"""
def fibonacci(numero_objetivo: int) -> int:
    anterior = 1
    ante_anterior = 0
    i = 2
    if numero_objetivo < i:
        return numero_objetivo
    while i <= numero_objetivo:
        actual = anterior + ante_anterior
        ante_anterior = anterior
        anterior = actual
        i+=1
    return anterior
print(fibonacci(5))