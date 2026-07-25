def merge_alternately(word1: str, word2: str) -> str:
    i = 0
    resultado = ""
    while i < len(word1) and i < len(word2):
        resultado += word1[i] + word2[i]
        i+=1
    resultado += word2[i:] + word1[i:]

    return resultado

print(merge_alternately("ab","pqrs"))