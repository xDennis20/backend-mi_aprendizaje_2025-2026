def check_inclusion(s1: str, s2: str) -> bool:
    letras_s1: dict[str,int] = {}
    for s in s1:
        if s not in letras_s1:
            letras_s1[s] = 1
        else:
            letras_s1[s] += 1

    left = 0

    for right, ch in enumerate(s2):
        if ch in letras_s1:
            letras_s1[ch] -= 1
            while letras_s1[ch] < 0:
                if s2[left] in letras_s1:
                    letras_s1[s2[left]] += 1
                left += 1
            if (right - left) + 1 == len(s1):
                return True
        else:
            while left < right:
                if s2[left] in letras_s1:
                    letras_s1[s2[left]] += 1
                left += 1
            left = right + 1

    return False

print(check_inclusion("abc", "lecabee"))
print(check_inclusion("abc","lecaabee"))
print(check_inclusion("ky","ainwkckifykxlribaypk"))