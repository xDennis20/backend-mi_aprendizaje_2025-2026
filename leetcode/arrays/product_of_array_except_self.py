def product_except_self(nums: list[int]) -> list[int]:
    prefijo = [1]
    subfijo = [1]
    resultado = []

    for i in range(0,len(nums) - 1):
        producto_pre = prefijo[i] * nums[i]
        prefijo.append(producto_pre)
    i_nums = 0

    for i in range(len(nums) - 1,0,-1):
        producto_sub = subfijo[i_nums] * nums[i]
        subfijo.append(producto_sub)
        i_nums+=1

    subfijo = subfijo[::-1]

    for i in range(len(prefijo)):
        resultado.append(prefijo[i] * subfijo[i])

    return resultado
print(product_except_self([1,2,3,4]))