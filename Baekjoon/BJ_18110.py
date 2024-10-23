from collections import deque

N = int(input())

if N > 0:
    queue = [int(input()) for _ in range(N)]
    queue.sort()
    queue = deque(queue)

    num_cut = int(N * 0.15)
    if N * 0.15 - num_cut >= 0.5:
        num_cut += 1

    for _ in range(num_cut):
        queue.popleft()
        queue.pop()

    result = int(sum(queue) / len(queue))
    if (sum(queue) / len(queue)) - result >= 0.5:
        result += 1
    print(result)

else:
    print(0)
