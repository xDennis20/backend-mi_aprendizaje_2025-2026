"""Antes de empezar Problema 13:
Practica Paso 2 con este micro-problema:
Problema: Contar cuántas veces aparece el número mayor en una lista
Ejemplo: [5,2,8,1,8,8] → 8 aparece 3 veces
Fecha: 09-10-2026"""
def contador_numero_mayor(lista_numeros: list[int]) -> int:
    contador = 1
    mayor = lista_numeros[0]
    for numero in lista_numeros[1:]:
        if numero > mayor:
            mayor = numero
            contador = 1
        elif numero == mayor:
            contador +=1
    return contador
print(contador_numero_mayor([5,2,8,1,8,8]))
    