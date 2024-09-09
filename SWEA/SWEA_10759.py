from pprint import pprint

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    result = 0
    for _ in range(N):
        A, B, C, D, color = list(map(int, input().split()))
        for i in range(A, C+1):
            for j in range(B, D+1):
                if color == 1:  # 빨강
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 2:
                        arr[i][j] = 0

                if color == 2: # 파랑
                    if arr[i][j] == 0:
                        arr[i][j] = 2
                    elif arr[i][j] == 1:
                        arr[i][j] = 0

    result = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(10):
        for j in range(10):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < 10 and 0 <= nj < 10:
                    if arr[i][j] != 0:


    print(f'#{tc+1} {result}')