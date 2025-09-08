import sys
input = sys.stdin.readline


N = int(input())

if N == 1:
    print('*')

elif N % 2 == 0:  # N이 짝수인 경우
    print('*' * N)

    for i in range(0, N//2-1, 1):
        print('*' + ' '*i + '*' + ' '*(N//2-2-i) + ' '*(N//2-2-i) + '*' + ' '*i + '*')

    for i in range(N//2-2, -1, -1):
        print('*' + ' '*i + '*' + ' '*(N//2-2-i) + ' '*(N//2-2-i) + '*' + ' '*i + '*')

    print('*' * N)

else:  # N이 홀수인 경우
    print('*' * N)

    for i in range(0, N//2-1, 1):
        print('*' + ' '*i + '*' + ' '*(N//2-2-i) + ' '*(N//2-1-i) + '*' + ' '*i + '*')

    print('*' + ' '*(N//2-1) + '*' + ' '*(N//2-1) + '*')

    for i in range(N//2-2, -1, -1):
        print('*' + ' ' * i + '*' + ' ' * (N // 2 - 2 - i) + ' ' * (N // 2 - 1 - i) + '*' + ' ' * i + '*')

    print('*' * N)
