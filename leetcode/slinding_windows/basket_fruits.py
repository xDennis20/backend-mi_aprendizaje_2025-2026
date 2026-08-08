#Dada un array donde cada numero representa un tipo de fruta, tenemos 2 canastas donde por cada canasta podemos tener un tipo de fruta
#Hallar la longitud de mas frutas conseguidas entre ambas canastas.

def basket_fruits(fruits: list[int]) -> int:
    left = 0
    long_max = 0
    fruits_inside = {}

    for right in range(len(fruits)):
        fruta_actual = fruits[right]
        if fruta_actual not in fruits_inside:
            fruits_inside[fruta_actual] = 1
        else:
            fruits_inside[fruta_actual] += 1

        while len(fruits_inside) > 2:
            fruta_left = fruits[left]
            fruits_inside[fruta_left] -= 1
            if fruits_inside[fruta_left] == 0:
                del fruits_inside[fruta_left]
            left +=1

        long_max = max(right - left + 1, long_max)

    return long_max

print(basket_fruits([1,2,3,2,2]))
print(basket_fruits([0,1,2,2]))