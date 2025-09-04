import sys
input = sys.stdin.readline


N, M, A, B = map(int, input().split())

result = [(N*3 - M)*A + B if (N*3 - M) > 0 else 0]
print(*result)
