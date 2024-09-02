def f(i, j, temp_sum):
    global result
    visited[i][j] = 1

    if i == N-1 and j == N-1:
        result = min(result, temp_sum)
        visited[i][j] = 0 # 백트래킹을 위해 방문 상태 초기화
        return

    for di, dj in [(0, 1), (1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == 0:
                f(ni, nj, temp_sum + arr[ni][nj])

    visited[i][j] = 0 # 백트래킹을 위해 방문 상태 초기화


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 10*N*N

    f(0, 0, arr[0][0])

    print(f'#{tc+1} {result}')