import sys
input = sys.stdin.readline

from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 방문을 위해 인접 리스트 정렬
for i in range(1, N+1):
    graph[i].sort()

visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
