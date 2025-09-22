import sys; input = sys.stdin.readline

N, M = map(int, input().split())

S = [input().strip() for _ in range(N)]

result = 0
for _ in range(M):
    if input().strip() in S:
        result += 1

print(result)
