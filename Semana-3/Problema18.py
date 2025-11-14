"""Problema 18: Valid Anagram
Descripción: Dadas dos strings s y t, devuelve true si t es un anagrama de s (mismas letras, mismas cantidades, orden diferente). False sino.
Ejemplos:

s = "anagram", t = "nagaram" → true
s = "rat", t = "car" → false"""
def valid_anagram(s: str, t: str) -> bool:
    dict_s = {}
    dict_t = {}
    if len(s) != len(t):
        return False
    for char1 in s:
        if char1 in dict_s:
            dict_s[char1] +=1
        else:
            dict_s[char1] = 1
    for char2 in t:
        if char2 in dict_t:
            dict_t[char2] +=1
        else:
            dict_t[char2] = 1
    return dict_s == dict_t
print(valid_anagram("anagram","nagaram"))
print(valid_anagram("","nagaram"))