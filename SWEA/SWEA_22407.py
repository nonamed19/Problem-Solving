T = int(input())

for tc in range(T):
    N = 10
    lst_A = list(map(int, input().split()))
    lst_B = list(map(int, input().split()))
    arr = [[0]*N for _ in range(N)]

    A, B, C, D = lst_A
    for i in range(A, C+1):
        for j in range(B, D+1):
            arr[i][j] += 1

    A, B, C, D = lst_B
    for i in range(A, C+1):
        for j in range(B, D+1):
            arr[i][j] += 1

    width, height = 0, 0
    for i in range(N):
        if 2 in arr[i]:
            height += 1
        temp = 0
        for j in range(N):
            if arr[i][j] == 2:
                temp += 1
            width = max(width, temp)

    print(f'#{tc+1} {width} {height}')