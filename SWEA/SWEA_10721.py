def perm(idx, N):
    global num_min
    if idx == N:
        # lst.append(arr[:])
        temp = 0
        for i in range(N):
            temp += arr_input[i][arr[i]]
        if num_min > temp:
            num_min = temp

    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1, N)
            arr[idx], arr[i] = arr[i], arr[idx]

T = int(input())

for tc in range(T):
    N = int(input()) # N x N 행렬, (3<=N<=10)
    arr_input = [list(map(int, input().split())) for _ in range(N)]
    arr = [x for x in range(N)]

    num_min = 100 * N

    perm(0, N)

    print('#%d %d' %(tc+1, num_min))