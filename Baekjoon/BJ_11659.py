import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    low, high = map(int, sys.stdin.readline().split())

    print(sum(numbers[low-1:high]))