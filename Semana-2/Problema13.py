"""PROBLEMA 13: Comprimir String
Enunciado:
Escribe una función que reciba un string y lo "comprima" contando caracteres consecutivos repetidos.Formato comprimido: caracter + cantidad
Si la compresión NO es más corta que el original, devuelve el string original.
Fecha: 08-10-2025"""

def comprimir_string(palabra: str) -> str:
    contador = 1
    resultado = ""

    if not palabra:
        return palabra

    caracter_actual = palabra[0]

    for caracter in palabra[1:]:
        if caracter != caracter_actual:
            resultado += caracter_actual + str(contador)
            caracter_actual = caracter
            contador = 1
        elif caracter == caracter_actual:
            contador +=1

    resultado += caracter_actual + str(contador)
    if len(resultado) >= len(palabra):
        return palabra
    return resultado

print(comprimir_string("aaabbbccc"))
print(comprimir_string("aabcccccaaa"))
print(comprimir_string("abcdef"))
print(comprimir_string("fffff"))
print(comprimir_string(""))

