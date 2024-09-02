def KFC(x):
    if x == N:
        result.append(f(path))
        return

    for i in range(N):
        if used[i] == 1:
            continue

        used[i] = 1
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = 0

def f(lst):
    temp = []
    # 사무실에서 출발하여 사무실로 돌아오는 경로만을 고려
    if lst[0] == 0:
        for i in range(len(lst)-1):
            temp.append(arr[lst[i]][lst[i+1]])
        temp.append(arr[lst[N-1]][0]) # 마지막 항 추가
    else:
        return 100*N*N
    return sum(temp)


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    path = []
    used = [0]*N # 중복 제거

    result = []
    KFC(0)
    print(f'#{tc+1} {min(result)}')