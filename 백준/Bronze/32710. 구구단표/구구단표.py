N = int(input())

flag = 1 if N == 1 else 0
for i in range(2, 10):
    if (N % i == 0) and (N // i <= 9):
        flag = 1
        break

print(flag)
