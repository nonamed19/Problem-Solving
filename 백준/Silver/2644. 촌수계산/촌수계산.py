# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

def dfs(graph, v, b, visited, count):
    count += 1
    visited[v] = True

    if v == b:
        result.append(count)
        return

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, b, visited, count)

import sys
input = sys.stdin.readline

n = int(input())  # 전체 사람의 수
a, b = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())  # 부모 자식들 간의 관계의 개수

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())  # 부모 자식간의 관계를 나타내는 두 번호
    graph[x].append(y)
    graph[y].append(x)

result = []
visited = [False] * (n+1)

dfs(graph, a, b, visited, -1)

if len(result) == 1:
    print(*result)
else:
    print(-1)