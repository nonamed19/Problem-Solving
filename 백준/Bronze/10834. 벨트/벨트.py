import sys
input = sys.stdin.readline

M = int(input())

count = 1
direction = 0
for _ in range(M):
    a, b, s = map(int, input().split())

    # 기어비 설정
    count /= a/b
    # 방향 설정
    if s == 1:
        direction = s - direction

print(direction, int(count))