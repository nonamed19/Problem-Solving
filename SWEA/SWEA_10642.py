T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    result = []

    # 행 탐색
    for i in range(N):
        for j in range(N-M+1):
            lst = list(arr[i][x] for x in range(j, j+M))

            for k in range(M//2):
                if lst[k] != lst[-1-k]:
                    break
            else:
                result = lst
                break

    # 열 탐색
    for j in range(N):
        for i in range(N-M+1):
            lst = list(arr[x][j] for x in range(i, i+M))

            for k in range(M//2):
                if lst[k] != lst[-1-k]:
                    break
            else:
                result = lst
                break

    print('#%d %s' %(tc+1, ''.join(result)))