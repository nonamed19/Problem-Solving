import sys

n = int(sys.stdin.readline())

calcs = [0] * (n + 2)
calcs[0] = 0  # initialization
calcs[1] = 1  # initialization

for i in range(2, n + 2):
    calcs[i] = (calcs[i - 1] + calcs[i - 2]) % 1000000007

result = calcs[n]
print(result)