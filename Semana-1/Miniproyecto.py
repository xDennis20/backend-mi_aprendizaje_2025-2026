from Problema4 import numero_mayor_lista
"""Crea un programa que reciba una lista de números y calcule:

Promedio
Número mayor
Número menor
Cantidad de números pares
Cantidad de números impares
Requisitos:

Crea una función para CADA estadística
Usa las funciones que ya creaste antes si puedes
El programa debe ser interactivo (pide números al usuario)
Muestra resultados bonitos (formateados)
Fecha: 04-10-2025"""

def promedio_lista(lista_numero: list[int]) -> float:
    total_suma = 0
    for numero in lista_numero:
        total_suma += numero
    return total_suma / len(lista_numero)

def numero_mayor(lista_numero: list[int]) -> int:
    return numero_mayor_lista(lista_numero)

def numero_menor(lista_numero: list[int]) -> int:
    numero_menor_guardado = lista_numero[0]
    for numero in lista_numero:
        if numero <= numero_menor_guardado:
            numero_menor_guardado = numero
    return numero_menor_guardado

def numeros_pares(lista_numeros: list[int]) -> int:
    contador = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador+=1
    return contador

def numeros_impares(lista_numeros: list[int]) -> int:
    contador = 0
    for numero in lista_numeros:
        if not numero % 2 == 0:
            contador +=1
    return contador

def main():
    lista_numeros = []
    salir = True
    while salir:
        print("1. Ingresar numero")
        print("2. Salir")
        opcion = int(input("Seleccione una opcion: "))
        numero = 0
        if opcion == 1:
            try:
                numero = int(input("Ingrese un numero: "))
            except ValueError:
                print("Ingrese el tipo de dato entero")
            lista_numeros.append(numero)
        elif opcion == 2:
            salir = False
        else:
            print("Ingrese una opcion valida")

    print(f"""Resultados:
    Promedio: {promedio_lista(lista_numeros)}
    Numero mayor de la lista: {numero_mayor(lista_numeros)}
    Numero menor de la lista: {numero_menor(lista_numeros)}
    Numeros pares de la lista: {numeros_pares(lista_numeros)}
    Numeros impares de la lista: {numeros_impares(lista_numeros)}  
    """)

main()