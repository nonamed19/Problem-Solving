import sys
input = sys.stdin.readline

M = int(input())

direction = 0
count = 1
for _ in range(M):
    a, b, s = map(int, input().split())
    count = int(count * b/a)
    direction = (direction + s) % 2

print(direction, count)
