N, K = map(int, input().split())

queue = list(range(1, N+1))

results = []
while len(queue) >= 2:
    temp = queue * K
    eliminated = temp.pop(K-1)
    idx = queue.index(eliminated)

    queue.remove(eliminated)
    results.append(eliminated)

    for _ in range(idx):
        queue.append(queue.pop(0))

results += queue
print('<', end = '')
for i in range(N):
    if i < N - 1:
        print(results[i], end = ', ')
    else:
        print(results[i], end = '')
print('>')