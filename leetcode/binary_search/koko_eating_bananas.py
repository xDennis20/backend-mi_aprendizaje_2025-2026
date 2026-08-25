from math import ceil

def min_eating_speed(piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)
    total_horas = 0
    res = 0

    while left <= right:
        mid = (right + left) // 2
        for p in piles:
            total_horas += ceil(p/mid)
        if total_horas <= h:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
        total_horas = 0

    return res

print(min_eating_speed([25,10,23,4], 4))



