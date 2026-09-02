from collections import deque

def max_sliding_window( nums: list[int], k: int) -> list[int]:
    left = 0
    cola = deque()
    resultado = []

    for right, num in enumerate(nums):
        while cola and num >= nums[cola[-1]] :
            cola.pop()

        cola.append(right)

        if cola[0] < left:
            cola.popleft()

        if (right - left) + 1 == k:
            resultado.append(nums[cola[0]])
            left+=1

    return resultado

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
print(max_sliding_window([1,2,1,0,4,2,6], 3))
print(max_sliding_window([7,2,4], 2))
print(max_sliding_window([-7,-8,7,5,7,1,6,0], 4))