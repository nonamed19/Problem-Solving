import sys

n = int(sys.stdin.readline())

calcs = [0] * (n + 1)
calcs[0] = 1  # initialization
calcs[1] = 1  # initialization

for i in range(2, n + 1):
    calcs[i] = calcs[i - 1] + calcs[i - 2]

result = calcs[n - 1]
print(result)
