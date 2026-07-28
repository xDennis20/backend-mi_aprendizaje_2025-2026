def top_k_frequent(nums: list[int], k: int) -> list[int]:
    #inicializo un diccionario donde se almacenara el numero con su numero de veces repetido.
    frecuencia = {}
    #Creo una lista para los buckets, segun la longitud de nums + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    resultado = []
    #Con un for recorro la lista de nums, si es un nuevo numero lo agrego a la lista con el numero de key y de valor 1 por que es la primera vez que aparece y si no le aumento + 1 al valor
    for num in nums:
        if num not in frecuencia:
            frecuencia[num] = 0
        frecuencia[num] += 1
    #Ahora recorro el dict por sus items, ahora el valor va ser el indice de la lista de buckets y el key es el valor que se va agregar cada casilla de los buckets
    for key,value in frecuencia.items():
        buckets[value].append(key)
    #Recorro de derecha a izquierda la lista de buckets hasta encontrar los 2 primeros o segun k de numeros que quiere.
    for i in range(len(buckets) - 1, -1, -1):
        if len(resultado) == k:
            break
        for num in buckets[i]:
            resultado.append(num)
            if len(resultado) == k:
                return resultado
    return resultado
print(top_k_frequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 4], 2))