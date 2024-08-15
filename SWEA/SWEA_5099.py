T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    queue = []

    for i in range(N):
        queue.append(i)
    front = N

    while sum(lst) != 1:
        temp = queue.pop(0)
        lst[temp] //= 2
        if lst[temp] > 0:
            queue.append(temp)
        elif lst[temp] == 0 and front < M:
            queue.append(front)
            front += 1

    print('#%d %d' %(tc+1, queue[0]+1))