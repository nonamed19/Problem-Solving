from collections import deque


def bfs(N, M):
    q = deque()
    q.append(N)
    visited = [-1] * 1000001

    visited[N] = 0
    while q:
        t = q.popleft()
        if t == M:
            return visited[M]

        for x in [t - 1, t + 1, t * 2, t - 10]:
            if 0 < x <= 1000000 and visited[x] == -1:
                q.append(x)
                visited[x] = visited[t] + 1
    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ans = bfs(N, M)
    print(f'#{tc} {ans}')