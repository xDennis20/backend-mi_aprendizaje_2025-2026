def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        sum_t = numbers[left] + numbers[right]
        if sum_t == target:
            return [left + 1, right + 1]
        elif sum_t > target:
            right -= 1
        else:
            left += 1

    return []

print(two_sum_ii([2,3,4], 6))
print(two_sum_ii([2,7,11,15], 9))
print(two_sum_ii([-1,0], -1))