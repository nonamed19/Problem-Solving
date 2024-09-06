def perm(idx, temp):
    global result
    if temp > result: # pruning 수행
        return

    if idx == N:
        result = temp
        return

    for i in range(N):
        if used[i]:
            continue

        used[i] = True
        perm(idx + 1, temp + arr[idx][i])
        used[i] = False


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * (N+1) # 굳이 list comprehension으로 만들지 말자 ..
    result = 99*N

    perm(0, 0)
    print(f'#{tc+1} {result}')