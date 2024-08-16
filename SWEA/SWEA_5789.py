T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    lst = []
    result = [0]*N

    lst.append([0, 0])
    for i in range(Q):
        lst.append(list(map(int, input().split())))

    for i in range(1, Q+1):
        for j in range(lst[i][0]-1, lst[i][1]):
            result[j] = i

    print('#%d' %(tc+1), *result)