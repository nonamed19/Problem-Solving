import sys

M = int(sys.stdin.readline())
S = []  # 비어있는 공집합

for i in range(M):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        x = int(command[1])
    command = command[0]

    if command == 'add':
        if not x in S:
            S.append(x)

    if command == 'remove':
        if x in S:
            S.remove(x)

    if command == 'check':
        if x in S:
            print(1)
        else:
            print(0)

    if command == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.append(x)

    if command == 'all':
        S = list(range(1, 21))

    if command == 'empty':
        S = []