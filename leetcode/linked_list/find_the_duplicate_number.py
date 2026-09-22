def find_duplicate(nums: list[int]) -> int:
    slow = 0
    fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        if slow == fast:
            break

    return slow

print(find_duplicate([1,3,4,2,2]))