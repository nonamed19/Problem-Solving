def countsum(x, y, temp, lev):
    if lev == 7:
        lst.append(temp)
        return

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(4):
        ni = x + di[i]
        nj = y + dj[i]
        if 0 <= ni < N and 0 <= nj < N:
            countsum(ni, nj, temp + arr[ni][nj], lev + 1)


T = int(input())

for tc in range(T):
    N = 4 # 4 x 4 matrix
    arr = [list(input().split()) for _ in range(N)] # 편의를 위해 str type으로 저장
    lst = [] # 서로 다른 일곱 자리 수들의 개수 저장을 위한 리스트

    for i in range(N):
        for j in range(N):
            countsum(i, j, '', 0)
    lst = set(lst)
    print(f'#{tc+1} {len(lst)}')