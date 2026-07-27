from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    #creo el dict para agregar de key el anagrama ordenado y de valor los anagramas ordenados que coincidan con el key los agrego sin modificacion de forma original
    grupos = {}
    #Recorro la lista de strs
    for anagrama in strs:
        #Agarro el str y lo ordeno y digo este string ya esta en el dict? y si no esta lo agrego el str ordenado como clave y de valor agrego una lista con el str normal,
        # y si esta simplemente le agrego el anagrama en donde coincidio de forma ordenada
        ana_order = "".join(sorted(anagrama))
        if ana_order not in grupos:
            grupos[ana_order] = []
        grupos[ana_order].append(anagrama)
    #retorno los valores del dict
    return list(grupos.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))