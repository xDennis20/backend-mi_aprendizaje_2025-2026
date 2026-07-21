def maxArea(height: list[int]) -> int:
    izquierda = 0
    derecha = len(height) - 1
    area_maxima = 0

    while izquierda < derecha:
        altura_minima = min(height[izquierda], height[derecha])
        ancho = derecha - izquierda
        area_actual = ancho * altura_minima

        if area_actual > area_maxima:
                area_maxima = area_actual

        if height[izquierda] < height[derecha]:
            izquierda += 1
        else:
            derecha -= 1
    return area_maxima

print(maxArea([3,8,2,5,4]))
print(maxArea([1,8,6,2,5,4,8,3,7]))