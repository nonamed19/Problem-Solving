def stacking(num, targets):
    global stacks, results

    stacks.append(num)
    results.append('+')  # push

    if not targets:
        return False

    while stacks:
        if stacks[-1] >= targets[0]:
            if stacks[-1] == targets[0]:
                stacks.pop()
                results.append('-')  # pop
                targets.pop(0)
            else:
                stacks.pop()
                results.append('-')  # pop
        else:  # num < targets[0]:
            return True


N = int(input())

targets = [0]*N
for i in range(N):
    targets[i] = int(input())

stacks = []
results = []
for num in range(1, N+1):
    validation = stacking(num, targets)

if (len(results) == N * 2) and (len(targets) == 0):
    for result in results:
        print(result)
else:
    print('NO')