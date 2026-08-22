def search_matrix( matrix: list[list[int]], target: int) -> bool:
    top = 0
    bottom = len(matrix) - 1

    while top <= bottom:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            fila = matrix[row]
            left = 0
            right = len(fila) - 1
            while left <= right:
                mid = (left + right) // 2
                if fila[mid] == target:
                    return True
                elif fila[mid] > target:
                    right = mid - 1
                elif fila[mid] < target:
                    left = mid + 1
            return False
    return False
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15))
print(search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
print(search_matrix([[1], [3]], 1))