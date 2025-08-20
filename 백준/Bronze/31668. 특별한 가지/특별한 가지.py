import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
K = int(input())

count = M // N
result = K * count

print(result)