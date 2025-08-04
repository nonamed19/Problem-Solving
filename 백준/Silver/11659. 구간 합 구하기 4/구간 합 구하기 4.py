import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

sum_lst = [0]
temp = 0
for i in range(N):
    temp += numbers[i]
    sum_lst.append(temp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    result = sum_lst[j] - sum_lst[i-1]
    print(result)
