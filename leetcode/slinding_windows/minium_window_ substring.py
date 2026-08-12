def min_window(s: str, t: str) -> str:
    left = 0
    falta = len(t)
    ch_frequencia = {}
    ventana_actual = ""
    long_min = float('inf')
    min_left = 0
    for i in t:
        if i not in ch_frequencia:
            ch_frequencia[i] = 1
        else:
            ch_frequencia[i] +=1

    for right in range(len(s)):
        ventana_actual += s[right]
        if s[right] in ch_frequencia:
            if ch_frequencia[s[right]] > 0:
                falta-=1
            ch_frequencia[s[right]] -= 1
        while falta == 0:
            long = right - left + 1
            if long < long_min:
                long_min = long
                min_left = left
            if s[left] in ch_frequencia:
                ch_frequencia[s[left]] += 1
                if ch_frequencia[s[left]] > 0:
                    falta+=1
            left+=1
    return s[min_left:min_left + long_min]

print(min_window("AAB", "AB"))
print(min_window("ADOBECODEBANC","ABC"))
print(min_window("OUZODYXAZV","XYZ"))
