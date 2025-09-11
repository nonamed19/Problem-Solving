import sys; input = sys.stdin.readline


N = int(input())
words = list(input().split())

print(*list(word + 'DORO' for word in words))
