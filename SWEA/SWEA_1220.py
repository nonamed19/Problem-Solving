from pprint import pprint

T = 10

for tc in range(T):
    N = int(input()) # N = 100으로 고정
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for j in range(N):
        key = 0
        for i in range(N):
            if arr[i][j] == 1:
                key = 1
            elif arr[i][j] == 2 and key == 1:
                result += 1
                key = 0

    print('#%d %d' %(tc+1, result))
