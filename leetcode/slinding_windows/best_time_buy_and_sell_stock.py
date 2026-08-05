def max_profit(prices: list[int]) -> int:
    left = 0
    right = 1
    max_ganancia = 0

    #Mientras right sea menor a la longitud de prices va seguir iterando
    while right < len(prices):
        #Si el numero de prices[left] es menor al numero de prices[right] significa que hay ganancia
        if prices[left] < prices[right]:
            #Hacemos la formula de la ganancia, (dia_venta + dia compra)
            ganancia = prices[right] - prices[left]
            #si ganancia es mayor al maximo de maximo encontrado anteriormente le cambiamos al nuevo maximo
            if ganancia > max_ganancia:
                max_ganancia = ganancia
            #aumentamos right + 1 para pasar al nuevo numero
            right+=1
        else:
            #Si left es mayor a right entonces significa que right es el mejor numero para comprar por ende left ahora pasa a tener el numero de right y a right le aumentamos 1
            left = right
            right+=1

    return max_ganancia

print(max_profit([3,10,1,2]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([7,1,5,3,6,4]))