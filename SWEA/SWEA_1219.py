def f(S, G):
    w = S
    visited[w] = 1

    if w == G:
        return 1
    else:
        for i in arr[w]:
            if visited[i] == 0:
                if f(i, G): # 탐색 재수행
                    return 1
        return 0

T = 10

for tc in range(T):
    NT, N = map(int, input().split())
    lst = list(map(int, input().split()))
    lst1, lst2 = [], []
    arr = list([] for _ in range(100))
    visited = [0]*101

    for i in range(N*2):
        if i%2 == 0: lst1.append(lst[i])
        else: lst2.append(lst[i])

    for i in range(len(lst1)):
        arr[lst1[i]].append(lst2[i])

    print('#%d %d' %(tc+1, f(0, 99)))