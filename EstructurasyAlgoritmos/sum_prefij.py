# Suma de prefijos

def prefix_sum(lista_numeros: list[int], r: int, l: int) -> int:
    prefijo: list[int] = []
    for i in range(len(lista_numeros)):
        if not prefijo:
            prefijo.append(lista_numeros[i])
        else:
            prefijo.append(prefijo[i - 1] + lista_numeros[i])
    if l == 0:
        res = prefijo[r] - prefijo[l]
        return res
    res = prefijo[r] - prefijo[l-1]
    return res

def product_except_self(nums: list[int]) -> list[int]:
    prefijo = [1]
    for i in range(1,len(nums)):
        prefijo.append(prefijo[i - 1] * nums[i - 1])
    subfijo = [1]
    for derecha in range(1,len(nums)):
        subfijo.append(subfijo[derecha - 1]  * nums[-derecha])
    resultado = []
    for p,s in zip(prefijo,subfijo[::-1]):
        resultado.append(p*s)
    return resultado
print(product_except_self([1,2,3,4,5]))

def find_missing_letter(chars: list[str]):
    alfabeto = {
        "a" : "b",
        "b" : "c",
        "c" : "d",
        "d" : "e",
        "e" : "f",
        "f" : "g",
        "g" : "h",
        "h" : "i",
        "i" : "j",
        "j" : "k",
        "k" : "l",
        "l" : "m",
        "m" : "n",
        "n" : "o",
        "o" : "p",
        "p" : "q",
        "q" : "r",
        "r" : "s",
        "s" : "t",
        "t" : "u",
        "u" : "v",
        "v" : "w",
        "w" : "x",
        "x" : "y",
        "y" : "z"
      }
    for char in chars:
        if char.isupper():
            obtener_char_s = alfabeto.get(char.lower())
            obtener_char_s = obtener_char_s.upper()
        else:
            obtener_char_s = alfabeto.get(char)
        if obtener_char_s not in chars:
            if char.isupper():
                char_faltante = alfabeto.get(char.lower())
                return char_faltante.upper()
            char_faltante = alfabeto.get(char.lower())
            return char_faltante
    return None
print(find_missing_letter(['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r']))