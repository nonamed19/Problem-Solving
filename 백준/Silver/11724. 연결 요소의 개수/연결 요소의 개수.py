# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)