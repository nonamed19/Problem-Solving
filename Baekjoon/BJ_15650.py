N, M = map(int, input().split())



"""
from itertools import permutations

N, M = map(int, input().split())

numbers = list(range(1, N+1))
perms = list(permutations(numbers, M))

results = []
for perm in perms:
    perm = tuple(sorted(perm))
    results.append(perm)

results = sorted(list(set(results)))

for result in results:
    print(*result)
"""