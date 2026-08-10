def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    left = 0
    right = 0
    long_vent = set()
    while right < len(nums):
        if len(long_vent) > k:
            long_vent.remove(nums[left])
            left+=1
        if nums[right] in long_vent:
            return True
        long_vent.add(nums[right])
        right+=1
    return False

print(contains_nearby_duplicate([1,2,3,1], 3))
print(contains_nearby_duplicate([1,4,2,3,1,2], 3))
print(contains_nearby_duplicate([1,2], 2))