def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    speeds = dict(zip(position,speed))
    position.sort(reverse=True)
    stack = []
    for i in position:
        tiempo = (target - i) / speeds[i]
        if not stack:
            stack.append(tiempo)
            continue
        if tiempo > stack[-1]:
            stack.append(tiempo)
    return len(stack)

print(car_fleet(12,[10,8,0,5,3],[2,4,1,1,3]))