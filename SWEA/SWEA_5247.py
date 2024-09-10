from collections import deque

def bfs(N, M):
    q = deque() # 큐 생성
    q.append(N) # 시작점 인큐


T = int(input())

for tc in range(T):
    N, M = map(int, input().split()) # N : original, M : target

    bfs(N, M)