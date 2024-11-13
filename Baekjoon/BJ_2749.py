## Pisano Period

import sys

k = 1000000
p = 15 * k // 10
n = int(sys.stdin.readline())
n %= p

calcs = [0] * (n + 2)
calcs[0] = 0  # initialization
calcs[1] = 1  # initialization

for i in range(2, n + 2):
    calcs[i] = (calcs[i - 1] + calcs[i - 2]) % k

result = calcs[n]
print(result)