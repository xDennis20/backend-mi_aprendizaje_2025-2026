def threeSum(nums: list[int]) -> list[list[int]]:
    list_ordenada = sorted(nums)
    list_resultados = []

    for i in range(len(list_ordenada) - 2):
        izquierda = i + 1
        derecha = len(list_ordenada) - 1
        if i > 0 and list_ordenada[i] == list_ordenada[i - 1]:
            continue
        while izquierda < derecha:
            suma = list_ordenada[i] + list_ordenada[izquierda] + list_ordenada[derecha]
            if suma == 0:
                numeros_resultados = [list_ordenada[i], list_ordenada[izquierda], list_ordenada[derecha]]
                list_resultados.append(numeros_resultados)
                izquierda += 1
                derecha -= 1
                while izquierda < derecha and list_ordenada[izquierda] == list_ordenada[izquierda - 1] :
                    izquierda +=1
                while izquierda < derecha and list_ordenada[derecha] == list_ordenada[derecha + 1]:
                    derecha -=1
            elif suma < 0:
                izquierda +=1
            else:
                derecha -=1
    return list_resultados
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))