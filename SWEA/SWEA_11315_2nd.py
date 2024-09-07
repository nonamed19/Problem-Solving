def omok():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4): # 4방향 탐색
                    cnt = 1
                    for l in range(1, 5): # 5개 연속 여부 판별
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 'o':
                                cnt += 1
                    if cnt == 5:
                        return True
    return False


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = [0, 1, 1, 1] # 3시, 5시, 6시, 7시
    dj = [1, 1, 0, -1] # 3시, 5시, 6시, 7시

    if omok():
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')