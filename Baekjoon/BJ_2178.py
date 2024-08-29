from pprint import pprint

def f(now_i, now_j):
    global cnt
    visited = [[0]*(M+2) for _ in range(N+2)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    before_i, before_j = 0, 0

    while True:
        visited[now_i][now_j] = 1
        if now_i == N and now_j == M:
            return cnt
        for i in range(4):
            ni = now_i + di[i]
            nj = now_j + dj[i]
            if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                before_i, before_j = now_i, now_j
                now_i, now_j = ni, nj
                cnt += 1
                break
        else:
            now_i, now_j = before_i, before_j
            cnt -= 1


N, M = map(int, input().split())
arr_input = [list(map(int, input())) for _ in range(N)]

arr = [[0]*(M+2) for _ in range(N+2)]
for i in range(N):
    for j in range(M):
        arr[i+1][j+1] = arr_input[i][j]

now_i, now_j = 1, 1
cnt = 1
print(f(now_i, now_j))