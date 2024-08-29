def f(idx):
    global cnt
    if idx == 0:
        return

    if child1[idx]:
        cnt += 1
        f(child1[idx])

    if child2[idx]:
        cnt += 1
        f(child2[idx])


T = int(input())

for tc in range(T):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    child1 = [0]*(E+2)
    child2 = [0]*(E+2)
    cnt = 1

    for i in range(E):                   # E = 0, 1, 2, 3, 4
        if child1[lst[i*2]] == 0:        # child1에 저장
            child1[lst[i*2]] = lst[i*2+1]
        elif child1[lst[i*2]] != 0:      # child2에 저장
            child2[lst[i*2]] = lst[i*2+1]

    idx = N         # 시작 위치 N
    f(idx)

    print('#%d %d' %(tc+1, cnt))