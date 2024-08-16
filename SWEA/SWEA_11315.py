from pprint import pprint

def f(N):
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(8): # 8 방향 탐색
                    temp = 1       # temp를 0에서 +1 시키는 게 아니라 1로 시작하기.
                    for l in range(1, N):
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            temp += 1
                            if temp == 5:
                                return 'YES'
                        else:
                            break
    return 'NO'


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print('#%d %s' %(tc+1, f(N)))