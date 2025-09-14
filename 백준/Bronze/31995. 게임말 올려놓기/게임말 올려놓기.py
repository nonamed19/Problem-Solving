import sys; input = sys.stdin.readline


N = int(input())
M = int(input())

if (2 <= N) and (2 <= M):
    print((N - 1)*(M - 1)*2)
else:
    print(0)
