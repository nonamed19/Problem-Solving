def find_max(X, Y, height, length, arr, path, validation):
    global result
    if result < length:
        result = length

    path[X][Y] = 1      # 현재 위치 저장
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for k in range(4):
        ni = X + di[k]
        nj = Y + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] < height and path[ni][nj] == 0:
                find_max(ni, nj, arr[ni][nj], length + 1, arr, path, validation)

            elif arr[ni][nj] - K < height and path[ni][nj] == 0 and validation == 0:
                height_original = arr[ni][nj]
                arr[ni][nj] = height - 1
                find_max(ni, nj, arr[ni][nj], length + 1, arr, path, validation = 1)
                arr[ni][nj] = height_original
    path[X][Y] = 0      # 탐색 후 되돌아오기


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    arr_input = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    result = 0 # global result

    top_height = 0
    for i in range(N): # 가장 높은 봉우리 탐색
        top_height = max(top_height, max(arr_input[i]))

    for i in range(N):
        for j in range(N):
            if arr_input[i][j] == top_height:
                find_max(i, j, arr_input[i][j], 1, arr_input, visited, 0)

    print(f'#{tc+1} {result}')