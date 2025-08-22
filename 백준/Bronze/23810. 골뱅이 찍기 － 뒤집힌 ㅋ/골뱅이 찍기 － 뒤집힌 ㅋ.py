import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    print('@@@@@'*N)

for i in range(N):
    print('@'*N)

for i in range(1, N+1):
    print('@@@@@'*N)

for i in range(N):
    print('@'*N)

for i in range(N):
    print('@'*N)
