def longest_ones(nums: list[int], k: int) -> int:
    left = 0
    count_0 = 0
    max_long = 0

    #Recorrer por indices hasta el ultimo elemento del array nums:
    for right in range(len(nums)):
        #Si el valor de right es 0, aumentar + 1 a count_0
        if nums[right] == 0:
            count_0 +=1
        # mientras count_0 sea mayor a k achicar la ventana desde left+=1 y restar count_0 si el valor de left es 0
        while count_0 > k:
            if nums[left] == 0:
                count_0 -= 1
            left += 1
        long = right - left + 1
        max_long = max(max_long,long)

    return max_long

print(longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(longest_ones([1,1,1,0,0,0,1,1,1,1,0],2))