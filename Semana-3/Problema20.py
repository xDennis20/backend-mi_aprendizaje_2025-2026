"""Problema 20: Longest Substring Without Repeating Characters
Dado un string s, encuentra la longitud de la subcadena contigua más larga que no contiene caracteres repetidos."""
def subcadena_larga(s: str) -> int:
    set_char = set()
    left = 0
    right = 0
    max_long = 0
    if not s:
        return max_long
    while left < len(s) and right < len(s):
        if  s[right] not in set_char:
            set_char.add(s[right])
            if len(set_char) > max_long:
                max_long = len(set_char)
            right += 1
        else:
            set_char.remove(s[left])
            left += 1
    return max_long

print(subcadena_larga("abcabcbb"))
print(subcadena_larga("pwwkew"))