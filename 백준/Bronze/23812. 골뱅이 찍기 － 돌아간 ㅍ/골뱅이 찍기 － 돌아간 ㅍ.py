import sys
input = sys.stdin.readline


N = int(input())

for _ in range(N):
    temp = ''
    temp += '@'*N
    temp += '   '*N
    temp += '@'*N
    print(temp)

for _ in range(N):
    temp = '@@@@@'*N
    print(temp)

for _ in range(N):
    temp = ''
    temp += '@'*N
    temp += '   '*N
    temp += '@'*N
    print(temp)

for _ in range(N):
    temp = '@@@@@'*N
    print(temp)

for _ in range(N):
    temp = ''
    temp += '@'*N
    temp += '   '*N
    temp += '@'*N
    print(temp)
