# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(graph, v, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(graph, i, visited)

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
dfs(graph, 1, visited)

for i in range(2, N+1):
    print(visited[i])
