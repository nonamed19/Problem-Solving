import sys
input = sys.stdin.readline


N = int(input())
hands = ['1', '2'] * (N // 2) + ['3' if N % 2 else '']

print(*hands)
