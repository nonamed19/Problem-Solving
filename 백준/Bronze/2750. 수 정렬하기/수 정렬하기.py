N = int(input())

numbers = sorted([x for x in [int(input()) for _ in range(N)]])

for number in numbers:
    print(number)
