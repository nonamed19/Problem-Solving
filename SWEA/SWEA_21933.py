T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split())) # N
    lst2 = list(map(int, input().split())) # M
    result = []

    if N >= M:
        for i in range(M):
            result.append(lst1.pop(0))
            result.append(lst2.pop(0))
        for j in range(N-M):
            result.append(lst1.pop(0))

    else:
        for i in range(N):
            result.append(lst1.pop(0))
            result.append(lst2.pop(0))
        for j in range(M-N):
            result.append(lst2.pop(0))

    print('#%d' %(tc+1), *result)