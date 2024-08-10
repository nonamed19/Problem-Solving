def dfs(S, G, V):
    w = S # 현재 위치

    if w == G:
        return 1
    else:
        visited[w] = 1
        for i in lst[w]:
            if visited[i] == 0:
                if dfs(i, G, V):
                    return 1
        return 0

T = int(input())

for tc in range(T):
    V, E = map(int, input().split()) # 정점 개수 V, 간선 개수 E
    lst = list([] for _ in range(V+1))
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        lst[v1].append(v2)

    S, G = map(int, input().split()) # 출발 노드 S, 도착 노드 G

    print('#%d %d' %(tc+1, dfs(S, G, V)))