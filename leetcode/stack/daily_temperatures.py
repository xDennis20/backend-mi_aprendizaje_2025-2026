def daily_temperatures(temperatures: list[int]) -> list[int]:
    long_temp = len(temperatures)
    day_cal = [0] * long_temp
    stack = []
    for i in range(long_temp):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            indice_anterior = stack.pop()
            day_cal[indice_anterior] = (i - indice_anterior)
        stack.append(i)

    return day_cal

print(daily_temperatures([73,74,75,71,69,72,76,73]))
print(daily_temperatures([30,40,50,60]))
