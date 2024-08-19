N = int(input())
lst = list(map(int, input().split()))
lst_stu = list(range(1, N+1))
result = []

for i in range(N):
    temp = lst_stu.pop(0)
    result.insert(i-lst[i], temp)

print(*result)