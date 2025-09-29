from itertools import *

def is_prime_number(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False
    end = int(n ** 0.5)
    for i in range(2, end+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def find_sum(arr, target):
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == target:
                    return [i, j, k]
    return [0]


T = int(input())

for _ in range(T):
    K = int(input())
    prime_numbers = is_prime_number(K)
    result = find_sum(prime_numbers, K)
    print(*result)
