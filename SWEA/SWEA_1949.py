def find_max(x, y, height, length, visited):
    global result
    if result < length:
        result = length

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(4):
        ni = x + di[i]
        nj = y + dj[i]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] < height:
                find_max(ni, nj, arr[ni][nj], length + 1, visited)
        # elif visited == 0:
        #     if arr[ni][nj] - K < height:
        #         height = arr[ni][nj] - 1
        #         visited = 1
        #         continue
        # else:
        #     visited = 0


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            find_max(i, j, arr[i][j], 0, 0) # 초기 height = 0 & length = 0
    print(f'#{tc+1} {result}')