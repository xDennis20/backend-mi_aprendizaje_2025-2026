def decrypt(code: list[int], k: int) -> list[int]:
    long = len(code)
    result = []
    if k == 0:
        return [0] * long
    elif k > 0:
        right = k
        left = 1
        sum_anterior = sum(code[left:right+1])
        result.append(sum_anterior)
        for i in range(1,long):
            sum_anterior = sum_anterior - code[left] + code[(right + 1) % long]
            result.append(sum_anterior)
            left = (left + 1) % long
            right = (right + 1) % long
        return result
    else:
        right = -1 % long
        left = k % long
        sum_anterior = sum(code[left:right+1])
        result.append(sum_anterior)
        for i in range(1, long):
            sum_anterior = sum_anterior - code[left] + code[(right + 1) % long]
            result.append(sum_anterior)
            left = (left + 1) % long
            right = (right + 1) % long
        return result
print(decrypt([5,7,1,4], 3))
print(decrypt([2,4,9,3], -2))
