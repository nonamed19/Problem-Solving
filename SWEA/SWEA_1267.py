T = 1

for tc in range(T):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    lst_adj = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = i*2, i*2 + 1
        lst_adj[arr[n2]] = [arr[n1]]

    print(lst_adj)