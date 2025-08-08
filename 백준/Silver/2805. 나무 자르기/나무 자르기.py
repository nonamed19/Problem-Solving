import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for tree in trees:
        if mid <= tree:
            cnt += (tree - mid)

    if M <= cnt:
        start = mid + 1
    else:
        end = mid - 1

print(end)