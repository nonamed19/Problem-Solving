T = int(input())

for tc in range(T):
    N = int(input())
    status = list(map(int, input().split())) # 전등의 현재 상태
    target = list(map(int, input().split())) # 스위치 조작 후 상태
    cnt = 0

    for i in range(N):
        if status[i] != target[i]:
            cnt += 1
            for j in range(i, N):
                status[j] = 1 - status[j]
    print(f'#{tc+1} {cnt}')