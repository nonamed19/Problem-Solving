def countsum(total_sum, lev):
    global result

    if lev == N:
        if total_sum == K:
            result += 1
        return

    if total_sum > K:
        return

    if total_sum == K:
        result += 1
        return

    countsum(total_sum + lst[lev], lev + 1)
    countsum(total_sum, lev + 1)


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0
    countsum(0, 0)
    print(f'#{tc+1} {result}')