def node_sum(idx):
    global result
    if idx <= N:
        result += lst[idx]
    else:
        return

    node_sum(idx*2)
    node_sum(idx*2+1)


T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    lst = [0]*(N+1)

    for _ in range(M):
        temp_idx, temp_num = map(int, input().split())
        lst[temp_idx] = temp_num

    result = 0
    node_sum(L)

    print('#%d %d' %(tc+1, result))