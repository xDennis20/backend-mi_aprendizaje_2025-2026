def length_of_longest_substring(s: str) -> int:
    left = 0
    right = 0
    max_lenght = 0
    vistos = {}
    #Mientras right sea menor a la longitud del string dado seguira iterando
    while right < len(s):
        #Si el caracter de right se encuentra en el dict de vistos
        if s[right] in vistos:
            #Se cambia el valor de left por el indice del caracter de right que se encuentra guardado en el dict + 1 y a right tambien se le sube + 1
            left = max(vistos.get(s[right]) + 1, left)
        vistos[s[right]] = right
        long = right - left + 1
        if long > max_lenght:
            max_lenght = long
        right += 1
    return max_lenght

print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("baaabca"))