import sys

def fibonacci(num):
    if num in memo:
        return memo[num]

    memo[num] = fibonacci(num-1) + fibonacci(num-2)
    return memo[num]


n = int(sys.stdin.readline())

memo = {0: 0,
        1: 1}
result = fibonacci(n)
print(result)