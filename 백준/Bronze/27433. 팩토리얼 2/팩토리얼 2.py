import sys
input = sys.stdin.readline

def factorial(N):
    global result
    if N == 0:
        return result
    else:
        result *= N
        factorial(N - 1)


N = int(input())
result = 1
factorial(N)

print(result)
