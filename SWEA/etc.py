from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = 0
    cnt = 0
    min_v = 99999
    for i in range(1, N - 1):
        for j in range(i, N):
            w = b = r = 0
            for k in range(0, i):
                w += M - arr[k].count('W')
            for l in range(i, j):
                b += M - arr[l].count('B')
            for p in range(j, N):
                r += M - arr[p].count('R')

            min_v = min(min_v, w + b + r)
    print(f'#{tc} {min_v}')