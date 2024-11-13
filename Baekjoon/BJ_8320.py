import sys

n = int(sys.stdin.readline())

result = n

for i in range(1, n+1):
    if int(n // i) == 2:
        result += n // i - 1
    else:
        break

# print(result)