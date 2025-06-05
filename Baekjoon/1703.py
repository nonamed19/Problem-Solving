import sys

while True:
    branch = list(map(int, sys.stdin.readline().split()))
    if len(branch) == 1:  # 종료 조건
        break

    a, *b = branch
    result = 1
    for i in range(a):
        s_factor = b[2*i]
        pruning = b[2*i + 1]
        result = result * s_factor - pruning
    print(result)