N = int(input())

lst = []
for _ in range(51):
    lst.append([])

for _ in range(N):
    temp = input()
    lst[len(temp)].append(temp)

result = []
for i in range(51):
    lst[i] = list(set(lst[i]))
    lst[i].sort()
    result += lst[i]

for i in range(len(result)):
    print(result[i])