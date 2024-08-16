def convert(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 0
            elif arr[i][j] == 'H':
                arr[i][j] = 1
            elif arr[i][j] == 'A':
                arr[i][j] = -100
            elif arr[i][j] == 'B':
                arr[i][j] = -200
            elif arr[i][j] == 'C':
                arr[i][j] = -300
            else:
                return 0
    return arr

T = int(input())

for tc in range(T):
    n = int(input()) # n x n 행렬
    arr = [list(input()) for _ in range(n)]
    arr = convert(arr)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(n):
        for j in range(n):

            if arr[i][j] == -100:
                for k in range(4): # delta
                    for l in range(1, 2): # repeat
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        if 0 <= ni < n and 0 <= nj < n:
                            arr[ni][nj] -= 1

            if arr[i][j] == -200:
                for k in range(4): # delta
                    for l in range(1, 3): # repeat
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        if 0 <= ni < n and 0 <= nj < n:
                            arr[ni][nj] -= 1

            if arr[i][j] == -300:
                for k in range(4): # delta
                    for l in range(1, 4): # repeat
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        if 0 <= ni < n and 0 <= nj < n:
                            arr[ni][nj] -= 1

    result = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                result += 1

    print('#%d %d' %(tc+1, result))