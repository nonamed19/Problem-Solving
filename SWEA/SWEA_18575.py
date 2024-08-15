from pprint import pprint

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_zero = [list(0 for _ in range(N)) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    num_max = 0
    num_min = 10000

    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(1, N):
                for l in range(4):
                    ni = i + di[l]*k
                    nj = j + dj[l]*k
                    if (0 <= ni < N) and (0 <= nj < N):
                        temp += arr[ni][nj]
            arr_zero[i][j] = arr[i][j] + temp
            if num_max < arr_zero[i][j]:
                num_max = arr_zero[i][j]
            if num_min > arr_zero[i][j]:
                num_min = arr_zero[i][j]

    print('#%d %d' %(tc+1, num_max - num_min))