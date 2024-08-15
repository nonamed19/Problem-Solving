def bfs(i, j, N):
    # 준비
    visited = [[0]*N for _ in range(N)] # visited 생성
    q = []                              # queue 생성
    q.append([i, j])                    # 시작점 enqueue
    visited[i][j] = 1                   # 시작점 enqueue 표시
    # 탐색
    while q:
        ti, tj = q.pop(0)               # dequeue
        if maze[ti][tj] == 3:           # visit(t)
            return visited[ti][tj] - 1 - 1  # 경로의 빈칸 수
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 미로 내부에서 인접이고, 벽이 아니면,
            wi, wj = ti+di, tj+dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])        # enqueue
                visited[wi][wj] = visited[ti][tj] + 1   # enqueue 표시
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())

for tc in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    print('#%d %d' %(tc+1, bfs(sti, stj, N)))