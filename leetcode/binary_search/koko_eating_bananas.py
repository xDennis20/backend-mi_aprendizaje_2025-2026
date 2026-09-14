from math import ceil

def min_eating_speed(piles: list[int], h: int) -> int:
    v_left = 1
    v_right = max(piles)
    total_horas = 0
    recuerdo = 0

    while v_left <= v_right:
        mid = (v_right + v_left) // 2
        for pile in piles:
            total_horas += ceil(pile / mid)
        if total_horas <= h:
            v_right = mid - 1
            recuerdo = mid
        else:
            v_left = mid + 1
        total_horas = 0

    return recuerdo


print(min_eating_speed([25,10,23,4], 4))
print(ceil(3/4))