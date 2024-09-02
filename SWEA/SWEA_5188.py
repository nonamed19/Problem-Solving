def f(now_i, now_j):
    global cnt
    if now_i == N-1 and now_j == N-1:
        print(cnt)
        return

    if 0 <= now_i < N and 0 <= now_j < N:
        cnt += arr[now_i][now_j]
        f(now_i+1, now_j)
        f(now_i, now_j+1)


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    start = [0, 0]
    f(start[0], start[1])