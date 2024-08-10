def perm(idx, N):

    if idx == N:
        lst.append(arr[:])

    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1, N)
            arr[idx], arr[i] = arr[i], arr[idx]

T = int(input())

for tc in range(T):
    N = int(input()) # N x N 행렬, (3<=N<=10)
    arr_input = [list(map(int, input().split())) for _ in range(N)]
    arr = [x for x in range(N)]
    lst = []
    result = 10*N

    perm(0, N)

    for i in range(len(lst)):
        temp = 0
        for j in range(N):
            temp += arr_input[j][lst[i][j]]
        if temp < result: # 같거나 같으면?
            result = temp

    print('#%d %d' %(tc+1, result))