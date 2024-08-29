def enq(num):
    global last
    last += 1
    heap[last] = num
    p = last
    c = last//2
    if last >= 2:
        while c >= 1:
            if heap[p] < heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
            p //= 2
            c //= 2


T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0]*(N+1)

    last = 0        # index
    for num in lst:
        enq(num)

    step = N
    result = 0
    while step >= 1:
        step //= 2
        result += heap[step]

    print('#%d %d' %(tc+1, result))