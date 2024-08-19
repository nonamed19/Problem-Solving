from pprint import pprint

T = int(input())

for tc in range(T):
    N = int(input())
    arr_input = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0]*(N+2) for _ in range(N+2)]
    result = []

    for i in range(N):
        for j in range(N):
            arr[i+1][j+1] = arr_input[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i+1][j+1] == 1 and arr[i][j+1] == 0 and arr[i+1][j] == 0:
                start_i, start_j, now_i, now_j = i+1, j+1, i+1, j+1
                while arr[now_i+1][now_j] == 1:
                    now_i += 1
                while arr[now_i][now_j+1] == 1:
                    now_j += 1
                result.append((now_i-start_i+1)*(now_j-start_j+1))

    print('#%d %d' %(tc+1, max(result)))