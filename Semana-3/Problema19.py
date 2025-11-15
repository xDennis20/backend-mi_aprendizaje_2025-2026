from typing import Optional
"""“Primer carácter no repetido”

Descripción:
Dada una cadena, encuentra el primer carácter que NO se repite.
Si no existe, devolver `None`.

Ejemplos:

- `s = "aabbcdd"` → `'c'`

- `s = "xxyz"` → `'y'`

- `s = "aabbcc"` → `None"""

def primer_caracter(s: str) -> Optional[str]:
    dict_char = {}
    if not s:
        return None
    for char in s:
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
    for c in dict_char:
        if dict_char.get(c) == 1:
            return c
    return None

print(primer_caracter("aabbcdd"))
print(primer_caracter("xxyz"))