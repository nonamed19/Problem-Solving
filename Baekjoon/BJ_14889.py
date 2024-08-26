N = int(input())
arr_input = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        arr[i+1][j+1] = arr_input[i][j]

people = list(range(1, N+1))

# 부분집합
subsets = [[]]

for num in people:
    size = len(subsets)
    for i in range(size):
        subsets.append(subsets[i]+[num])

for i in range(len(subsets)-1, -1, -1):
    if len(subsets[i]) != N//2:
        subsets.pop(i)

result = 100
for i in range(len(subsets)):
    temp = list(range(1, N+1))
    temp1 = sorted(subsets[i], reverse=True)
    for num in temp1:
        temp.pop(num-1)
    team1 = arr[temp[0]][temp[1]] + arr[temp[1]][temp[0]]
    team2 = arr[temp1[0]][temp1[1]] + arr[temp1[1]][temp1[0]]
    # result = min(result, abs(team1 - team2))

# print(result)