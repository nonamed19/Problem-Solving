import sys; input = sys.stdin.readline

N = int(input())
result = 0
for _ in range(N):
    result += 1 if int(input()[2:]) <= 90 else 0

print(result)