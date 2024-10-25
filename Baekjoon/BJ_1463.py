X = int(input())

result = 0
while X != 1:
    if X % 3 == 0:
        X /= 3
        result += 1
    elif (X - 1) % 3 == 0:
        X -= 1
        result += 1
    else:
        X /= 2
        result += 1

print(result)