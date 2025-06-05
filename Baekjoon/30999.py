import sys

N, M = map(int, sys.stdin.readline().split())

result = 0
for _ in range(N):
    votes = list(sys.stdin.readline().strip())
    if votes.count('O') > votes.count('X'):
        result += 1

print(result)