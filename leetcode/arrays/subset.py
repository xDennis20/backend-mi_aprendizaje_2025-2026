def subsets(nums: list[int]) -> list[list[int]]:
    subconjunto = []

    def backtracking(inicio: int, subconjunto_actual: list[int]):
        subconjunto.append(subconjunto_actual.copy())
        for i in range(inicio, len(nums)):
            subconjunto_actual.append(nums[i])
            backtracking(i + 1, subconjunto_actual)
            subconjunto_actual.pop()
    backtracking(0, [])

    return subconjunto

print(subsets([1,2,3]))
print(subsets([0]))