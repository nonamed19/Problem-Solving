import sys

N, K = map(int, sys.stdin.readline().split())

prices = [0] * N
for i in range(N):
    prices[i] = int(sys.stdin.readline())

result = 0
for i in range(N-1, -1, -1):
    if prices[i] <= K:
        count = K // prices[i]
        K -= prices[i] * count
        result += count

print(result)