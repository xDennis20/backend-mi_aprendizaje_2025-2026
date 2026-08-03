def find_min(nums: list[int]) -> int:
    right = len(nums) - 1
    left = 0

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] <= nums[right]:
            right = mid

    return nums[left]

print(find_min([4,5,6,7,0,1,2]))
print(find_min([5,1,2,3,4]))
print(find_min([11,13,15,17]))
