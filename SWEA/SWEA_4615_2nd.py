from pprint import pprint

def reversi(X, Y, color):
    di = [0, 1, 1, 1, 0, -1, -1, -1] # 3, 5, 6, 7, 9, 11, 12, 1시
    dj = [1, 1, 0, -1, -1, -1, 0, 1] # 3, 5, 6, 7, 9, 11, 12, 1시
    arr[X][Y] = color

    for k in range(8): # direction
        for l in range(1, N): # length
            ni = X + di[k]*l
            nj = Y + dj[k]*l
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] == color: # 색깔을 뒤집을 수 있는 경우
                    for i in range(l):
                        mi = X + di[k]*i
                        mj = Y + dj[k]*i
                        arr[mi][mj] = color
                    break


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    # 정가운데에 배치하고 시작
    arr[N//2-1][N//2] = 1   # black
    arr[N//2-1][N//2-1] = 2 # white
    arr[N//2][N//2-1] = 1   # black
    arr[N//2][N//2] = 2     # white

    for _ in range(M):
        X, Y, color = map(int, input().split())
        reversi(Y-1, X-1, color) # def 내에서는 i, j 취급

    result_black = 0
    result_white = 0
    for i in range(N):
        result_black += arr[i].count(1)
        result_white += arr[i].count(2)

    print(f'#{tc+1} {result_black} {result_white}')