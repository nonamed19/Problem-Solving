import sys
input = sys.stdin.readline

def Hailstone(n):
    numbers.append(n)
    if n == 1:
        return
    # n이 짝수라면, 2로 나눈다
    elif n % 2 == 0:
        np = n // 2
        numbers.append(np)
        Hailstone(np)
    # n이 홀수라면, 3을 곱한 뒤 1을 더한다
    elif n % 2 == 1:
        np = n*3 + 1
        numbers.append(np)
        Hailstone(np)


T = int(input())

for _ in range(T):
    n = int(input())

    numbers = []
    Hailstone(n)
    print(max(numbers))
