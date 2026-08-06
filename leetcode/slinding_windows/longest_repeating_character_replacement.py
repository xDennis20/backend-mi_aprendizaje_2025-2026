def character_replacement(s: str, k: int) -> int:
    left = 0
    freq = {}
    max_freq = 0
    max_long = 0
    #Mientras right sea menor a la longitud de s
    for right in range(len(s)):
        #si el caracter nuevo ya esta en el dict  le sumamos 1 y si no le agregamos de valor 1
        if s[right] not in freq:
            freq[s[right]] = 1
        else:
            freq[s[right]] += 1
        #Buscamos la max_freq dentro del dict y comparando con el anterior max_freq
        max_freq = max(max_freq, freq[s[right]])
        #Formula para hayar la longitud de la ventana actual
        long_vent = right - left + 1
        # Si (right - left + 1) - max_freq <= k
        if long_vent - max_freq <= k:
            #Si long_vent es mayor que max_long se actualiza max_long por el nuevo valor de long_vent
            if long_vent > max_long:
                max_long = long_vent
        else:
            #Si no restamos -1 en el dict de frecuencia el caracter que tiene left
            freq[s[left]] -= 1
            #Y aumentamos left hacia el siguiente caracter
            left += 1
    return max_long

print(character_replacement("AABABBA", 1))
print(character_replacement("XYYX", 2))