T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    idx = 0
    num_max = 0

    for i in range(N):
        if num_max <= lst[i]:
            num_max = lst[i]
            idx = i+1

    print('#%d %d %d' %(tc+1, idx, num_max))