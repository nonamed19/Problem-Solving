def is_prime_number(n):
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False
    end = int(n ** 0.5)
    for i in range(2, end+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def count_num(arr, target):
    if target == 1:
        return 1
    counts = [count for count in arr if target < count < target*2]
    return len(counts)


while True:
    K = int(input())
    if not K:
        exit()

    prime_numbers = is_prime_number(K*2)
    result = count_num(prime_numbers, K)
    print(result)
