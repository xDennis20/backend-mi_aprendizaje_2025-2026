from math import ceil

def min_eating_speed(piles: list[int], h: int) -> int:
    v_left = 1
    v_right = max(piles)
    total_horas = 0
    res = 0

    while v_left <= v_right:
        v_mid = (v_right + v_left) // 2
        for pila in piles:
            total_horas += ceil(pila / v_mid)
        if total_horas <= h:
            res = v_mid
            v_right = v_mid - 1
            total_horas = 0
        else:
            v_left = v_mid + 1
            total_horas = 0

    return res


print(min_eating_speed([25,10,23,4], 4))
