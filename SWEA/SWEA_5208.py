def f(now, cnt): # cnt는 -1으로 시작
    global result
    if cnt >= result: # pruning, 시간 차이 별로 없네요..
        return

    if now >= N - 1:
        result = min(result, cnt)
        return

    else: # now < N:
        for i in range(1, lst[now]+1):
            f(now + i, cnt + 1)


# 목적지에 도달하지 못하는 경우는 없음
T = int(input())

for tc in range(T):
    N, *lst = list(map(int, input().split()))
    result = N

    f(0, -1)
    print(f'#{tc+1} {result}')