from pprint import pprint

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list([0]*(10+1)) for _ in range(10+1)] # 11 x 11 matrix

    for _ in range(N):
        lst = list(map(int, input().split())) # temporary

        for i in range(lst[0], lst[2]+1):
            for j in range(lst[1], lst[3]+1):
                arr[i][j] = 1

    result = 0
    for i in range(len(arr)):
        result += arr[i].count(1)

    print(f'#{tc+1} {result}')
