def dfs(num, lst):
    global result

    result_temp = 0 # result_temp 계산
    for i in range(num):
        result_temp += arr[i][lst[i]]

    if num == N:    # result 판별
        result = min(result, result_temp)
        return
    elif num > N:   # pruning
        if result_temp > result:
            return

    for i in range(N):
        if visited[i] or i in lst:
            continue

        lst += [i]
        dfs(num + 1, lst)
        lst.pop()


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst_perm = []
    visited = [0] * N

    result = 10*N
    dfs(0, lst_perm)

    print(f'#{tc+1} {result}')
