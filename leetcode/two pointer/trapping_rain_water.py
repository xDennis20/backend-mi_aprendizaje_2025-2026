def trap(height: list[int]) -> int:
    #inicializar las variables: (max_left, max_right, trap_water)
    left = 0
    right = len(height) - 1
    max_l = height[left]
    max_r = height[right]
    trap_water = 0
    #recorrer la lista dada mediante 2 punteros izquierda y derecha, y inicializando los max_num con el valor del indice.
    while left < right:
        #Si el max_num_right es mayor que el de la izquierda, aumentamos a left + 1, y agarramos el maximo entre el anterior max_num y el nuevo numero de la lista con el indice de left,
        # y calculamos el max con el numero del indice actual,
        if max_l <= max_r:
            left+=1
            altura_actual = height[left]
            max_l = max(max_l, altura_actual)
            trap_water += max(0, max_l - altura_actual)
            # Si el max_num_left es mayor que el de la derecha, restamos right - 1, y agarramos el maximo entre el anterior max_num y el nuevo numero de la lista con el indice de right,
            # y calculamos el max con el numero del indice actual,
        else:
            right-=1
            altura_actual = height[right]
            max_r = max(max_r, altura_actual)
            trap_water += max(0, max_r - altura_actual)

    return trap_water

def trap_1(height: list[int]) -> int:
    n = len(height)
    maxs_left = [0] * n
    maxs_right = [0] * n
    trap_water = 0

    maxs_left[0] = height[0]
    for i in range(1,n):
        maxs_left[i] = max(maxs_left[i-1], height[i])

    maxs_right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        maxs_right[i] = max(maxs_right[i + 1], height[i])

    for actual,left,right in zip(height,maxs_left,maxs_right):
        trap_water += min(left,right) - actual

    return trap_water

print(trap([4,2,0,3,2,5]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))