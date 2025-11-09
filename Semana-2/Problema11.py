from typing import Optional

"""Problema 1: Segundo mayor de la lista
Fecha: 06-10-2025
"""
def segundo_numero_mayor(lista_numero: list[int]) -> Optional[int]:
    if len(lista_numero) < 2:
        return None

    mayor = lista_numero[0]
    segundo_mayor = None

    for i in range(1,len(lista_numero)):
        numero = lista_numero[i]

        if numero > mayor:
            segundo_mayor = mayor
            mayor = numero
            
        elif numero < mayor and (segundo_mayor is None or segundo_mayor < numero):
            segundo_mayor = numero
        
        elif numero == mayor or numero <= segundo_mayor:
            continue
    return segundo_mayor

print(segundo_numero_mayor([5,2,8,1,9]))
print(segundo_numero_mayor([5,2,8,1,9,10]))
print(segundo_numero_mayor([10,10,10]))
print(segundo_numero_mayor([5]))