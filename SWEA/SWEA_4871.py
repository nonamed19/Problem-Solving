def DFS(s, G, V):
    visited = [0]*(V+1)         # 방문한 정점을 표시
    stack = []                  # 스택 생성
    visited[s] = 1              # 시작정점 방문표시
    v = s

    while True:
        for w in adjL[v]:       # v에 인접하고, 방문 안 한 w가 있으면
            if visited[w] == 0:
                stack.append(v) # push(v): 현재 정점을 push하고
                v = w           # w에 방문
                if v == G:
                    validation = 1
                    return validation
                visited[w] = 1  # w에 방문 표시
                print(visited)
                break           # for w, v부터 다시 탐색
        else:                   # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack:           # 이전 갈림길을 스택에서 꺼내서 ... if TOP > -1
                v = stack.pop()
            else:               # 되돌아갈 곳이 없으면/남은 갈림길이 없으면 탐색종료
                validation = 0
                return validation

T = int(input())  # 테스트 케이스의 수를 입력받음

for tc in range(1, T+1):  # 각 테스트 케이스에 대해 반복
    V, E = map(int, input().split())  # 정점의 수 V와 간선의 수 E를 입력받음
    adjL = [[] for _ in range(V+1)]  # 인접 리스트를 초기화 (1부터 V까지 사용)
    validation = 0

    for i in range(E):  # 각 간선에 대해 반복
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)  # 첫 번째 정점에 두 번째 정점을 추가

    S, G = map(int, input().split())

    print('#%d %d' %(tc, DFS(S, G, V)))