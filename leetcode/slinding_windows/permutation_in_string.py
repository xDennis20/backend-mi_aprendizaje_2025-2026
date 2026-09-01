def check_inclusion(s1: str, s2: str) -> bool:
    ch_freq: dict[str,int] = {}
    for ch in s1:
        if ch not in ch_freq:
            ch_freq[ch] = 1
        else:
            ch_freq[ch] += 1

    left = 0

    for i, ch in enumerate(s2):
        if ch in ch_freq:
            ch_freq[ch] -= 1
            while ch_freq[ch] < 0:
                if s2[left] in ch_freq:
                    ch_freq[s2[left]] += 1
                left+=1
            if (i - left) + 1 == len(s1):
                return True
        else:
            while left < i:
                if s2[left] in ch_freq:
                    ch_freq[s2[left]] += 1
                left += 1
            left = i + 1

    return False

print(check_inclusion("abc", "lecabee"))
print(check_inclusion("abc","lecaabee"))
print(check_inclusion("ky","ainwkckifykxlribaypk"))