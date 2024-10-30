


"""
from itertools import product

N, M = map(int, input().split())

numbers = list(range(1, N+1))
prods = list(product(numbers, repeat = M))

results = []
for prod in prods:
    prod = tuple(sorted(prod))
    results.append(prod)

results = sorted(list(set(results)))

for result in results:
    print(*result)
"""