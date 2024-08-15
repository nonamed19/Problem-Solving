from pprint import pprint

def reversi(lst):
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    arr[lst[0]][lst[1]] = lst[2] # 지정한 위치에 돌 두기

    player = lst[2]
    if player == 1:
        opponent = 2
    else:
        opponent = 1

    for i in range(8):
        ni = lst[0]+di[i]
        nj = lst[1]+dj[i]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == opponent:
            for k in range(2, N):
                ki = lst[0] + di[i]*k
                kj = lst[1] + dj[i]*k

                if 0 <= ki < N and 0 <= kj < N:
                    if arr[ki][kj] == player:
                        for l in range(k):
                            li = lst[0] + di[i] * l
                            lj = lst[1] + dj[i] * l
                            arr[li][lj] = player
                        break
                    elif arr[ki][kj] == 0:
                        break


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    arr[N//2-1][N//2] = 1 # 백의 초기 위치
    arr[N//2][N//2-1] = 1 # 백의 초기 위치
    arr[N//2-1][N//2-1] = 2 # 흑의 초기 위치
    arr[N//2][N//2] = 2 # 흑의 초기 위치

    lst = [[0, 0, 0]]*M
    for i in range(M):
        n1, n2, n3 = map(int, input().split())
        lst[i] = [n1-1, n2-1, n3]

    for play in lst:
        reversi(play)

    result1 = 0
    result2 = 0
    for i in range(N):
        result1 += arr[i].count(1)
        result2 += arr[i].count(2)

    print('#%d %d %d' %(tc+1, result1, result2))