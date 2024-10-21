N = int(input())
numbers = list(map(int, input().split()))

result = 0
for number in numbers:
    temp = []

    for num in range(2, number + 1):
        if number % num == 0:
            temp.append(num)

    if len(temp) == 1:
        result += 1

print(result)