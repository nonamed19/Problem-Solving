from pprint import pprint

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    arr_d = [[0]*N for _ in range(N)]
    arr_x = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
            xi, xj = [-1, 1, 1, -1], [1, 1, -1, -1]
            for l in range(4):
                for k in range(1, M):
                    ni = i + di[l]*k
                    nj = j + dj[l]*k
                    if 0 <= ni < N and 0 <= nj < N:
                        arr_d[i][j] += arr[ni][nj]
                    mi = i + xi[l]*k
                    mj = j + xj[l]*k
                    if 0 <= mi < N and 0 <= mj < N:
                        arr_x[i][j] += arr[mi][mj]
            arr_d[i][j] += arr[i][j]
            arr_x[i][j] += arr[i][j]

    for i in range(N):
        for j in range(N):
            result = max(result, arr_d[i][j], arr_x[i][j])

    print('#%d %d' %(tc+1, result))