def is_anagram(s: str, t: str) -> bool:
    if s == t:
        return False

    s_order = set(s)
    t_order = set(t)

    if s_order == t_order:
        return True
    return False

print(is_anagram("rat", "cat"))
