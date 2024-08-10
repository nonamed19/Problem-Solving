from pprint import pprint

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    # N x M 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 빈 N x M 행렬
    arr_zero = [list(0 for _ in range(M)) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    num_max = 0

    for i in range(N): # 3
        for j in range(M): # 5
            temp = 0
            for k in range(1, arr[i][j]+1):
                for l in range(4):
                    ni = i + di[l]*k
                    nj = j + dj[l]*k
                    if (0 <= ni < N) and (0 <= nj < M):
                        temp += arr[ni][nj]
            arr_zero[i][j] = arr[i][j] + temp
            if num_max <= arr_zero[i][j]:
                num_max = arr_zero[i][j]

    print('#%d %d' %(tc+1, num_max))