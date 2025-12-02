"""Problema 24: Prefijo comun mas largo
Escribe una función para encontrar la cadena de prefijos común más larga entre un array de cadenas.

Si no hay un prefijo común, se devuelve una cadena vacía .""


Ejemplo 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Ejemplo 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

def prefijo_comun(strings: list[str]) -> str:
    prefijo = ""
    strings.sort()
    primer_str = strings[0]
    ultimo_str = strings[-1]
    i = 0
    j = 0
    while i < len(primer_str) and j < len(ultimo_str):
        if primer_str[i] == ultimo_str[j]:
            prefijo += primer_str[i]
            i+=1
            j+=1
        else:
            break
    return prefijo


print(prefijo_comun(["flower","flow","flight"]))
print(prefijo_comun(["dog","racecar","car"]))

