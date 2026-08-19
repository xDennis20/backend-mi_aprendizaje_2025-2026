def largest_rectangle_area(heights: list[int]) -> int:
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            altura = stack.pop()
            if not stack:
                anchura = i
            else:
                anchura = i - stack[-1] - 1
            max_area = max(max_area, heights[altura] * anchura)
        stack.append(i)
    n = len(heights)
    while stack:
        ultimo = stack.pop()
        if not stack:
            anchura = n
        else:
            anchura = n - stack[-1] - 1
        max_area = max(max_area, heights[ultimo] * anchura)

    return max_area

print(largest_rectangle_area([7,1,7,2,2,4]))
print(largest_rectangle_area([2,1,5,6,2,3]))