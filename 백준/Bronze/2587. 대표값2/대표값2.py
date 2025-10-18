numbers = []
for _ in range(5):
    numbers.append(int(input()))

numbers.sort()
print(int(sum(numbers)/len(numbers)))
print(numbers[len(numbers)//2])
