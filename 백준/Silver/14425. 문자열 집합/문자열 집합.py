N, M = map(int, input().split())

S = [input() for _ in range(N)]

result = 0
for _ in range(M):
    result += 1 if str(input()) in S else 0

print(result)
