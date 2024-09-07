T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                width, height = 1, 1
                while arr[i + width][j] == 1:
                    width += 1
                while arr[i][j + height] == 1:
                    height += 1
                result = max(result, width * height)

    print(f'#{tc+1} {result}')