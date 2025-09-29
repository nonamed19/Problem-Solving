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
    left, right = 0, len(arr) - 1
    pair, min_diff = None, float('inf')

    while left <= right:
        s = arr[left] + arr[right]
        if s == target:
            diff = abs(arr[right] - arr[left])
            if diff < min_diff:
                min_diff = diff
                pair = [arr[left], arr[right]]
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

    return pair


T = int(input())

for _ in range(T):
    K = int(input())
    prime_numbers = is_prime_number(K)
    result = find_sum(prime_numbers, K)
    print(*result)
