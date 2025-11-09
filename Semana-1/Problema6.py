"""Enunciado:
Escribe una función que reciba un string y devuelva el mismo string pero al revés.
Ejemplos:

Input: "hola" → Output: "aloh"
Input: "Python" → Output: "nohtyP"
Input: "a" → Output: "a"
Input: "" → Output: ""
Fecha: 30-09-2025
"""

def palabras_invertida(palabra: str) -> str:
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    return palabra_invertida

print(palabras_invertida("hola"))
print(palabras_invertida("Python"))
print(palabras_invertida("a"))
print(palabras_invertida(""))

"""Problema 6: Escribe una función que reciba un string y devuelva True si es un palíndromo 
(se lee igual al derecho y al revés), y False si no lo es. Ignora mayúsculas."""
def es_palindromo(frase: str) -> bool:
    frase_invertida = palabras_invertida(frase).replace(" ", "")
    if frase.lower().replace(" ","") == frase_invertida.lower():
        return True
    else:
        return False
print(es_palindromo("anita lava la tina"))
print(es_palindromo("oso"))
print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Python"))