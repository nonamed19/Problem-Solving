def cycle(lst, queue):
    while True:
        for i in range(1, 6):
            temp = queue.pop(0)
            if lst[temp] - i > 0:
                lst[temp] -= i
                queue.append(temp)
            else:
                lst[temp] = 0
                queue.append(temp)
                return lst, queue

T = 10

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    queue = [x for x in range(8)]
    result = []

    lst, queue = cycle(lst, queue)

    for num in queue:
        result.append(lst[num])

    print('#%d' %(tc+1), *result)