def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    set_nums = set(nums)
    racha_actual = 1
    for i in set_nums:
        if i - 1 in set_nums:
            continue
        suma_con = i + 1
        long_con = 1
        while suma_con in set_nums:
            long_con += 1
            suma_con = suma_con + 1
        if long_con > racha_actual:
            racha_actual = long_con
    return racha_actual
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))