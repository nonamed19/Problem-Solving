def DFS(num, visited):
    global result

    visited[num] = True
    result += 1

    for i in adjL[num]:
        if visited[i] == False:
            DFS(i, visited)


N = int(input())  # 노드의 수 N
M = int(input())  # 간선의 수 M

adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    temp = list(map(int, input().split()))
    adjL[temp[0]].append(temp[1])
    adjL[temp[1]].append(temp[0])

result = 0
visited = [False] * (N + 1)
DFS(1, visited)

print(result - 1)