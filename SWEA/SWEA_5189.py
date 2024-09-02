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
    for i in range(len(lst)):
        if arr[i][lst[i]] != 0:
            temp.append(arr[i][lst[i]])
        else:
            return 100*N
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