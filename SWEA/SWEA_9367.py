T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 1
    cnt = 1

    for i in range(N-1):
        if lst[i] < lst[i+1]:
            cnt += 1
            result = max(result, cnt)
        else:
            cnt = 1

    print(f'#{tc+1} {result}')