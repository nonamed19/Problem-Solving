def bfs(s, V):  # s : 시작점, V : 마지막 정점
    # 준비
    visited = [0]*(V+1)    # visited 생성
    q = []                 # queue 생성
    q.append(s)            # 시작점 enqueue
    visited[s] = 1         # 시작점 방문(enqueue 표시)
    # 탐색
    while q:               # 탐색할 정점이 남아 있으면
        t = q.pop(0)       # t <- dequeue
        # print(t)           # 처리
        for w in adj_l[t]:    # t에 인접이고, enqueue된 적이 없으면,
            if visited[w] == 0:
                q.append(w)      # enqueue하고
                # visited[w] = 1   # enqueue 표시
                visited[w] = visited[t] + 1     # 이렇게 표현하면 탐색 중 거리정보를 알 수 있음
    return visited

T = int(input())

for tc in range(T):
    V, E = map(int, input().split()) # V : 정점의 수, E : 간선의 수

    adj_l = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)    # 무방향인 경우
        adj_l[v2].append(v1)    # 무방향인 경우

    S, G = map(int, input().split()) # V : 정점의 수, E : 간선의 수

    visited = bfs(S, V)   # 출발점, 정점수
    if visited[G] != 0:
        print('#%d %d' %(tc+1, visited[G]-1))
    else:
        print('#%d %d' %(tc+1, 0))