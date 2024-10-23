N = int(input())

numbers = [0] * 10001
for i in range(N):
    numbers[int(input())] += 1

for i in range(len(numbers)):
    if numbers[i]:
        for _ in range(numbers[i]):
            print(i)