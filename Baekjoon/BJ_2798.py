from itertools import combinations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers_comb = list(combinations(numbers, 3))
result = []
result_idx = []
for comb in numbers_comb:
    temp = sum(comb)
    result.append(temp)
    result_idx.append(M / temp)

print(result)
print(result_idx)