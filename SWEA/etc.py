T = int(input())

for tc in range(T):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]

    result = 0
    for _ in range(N):
        A, B, C, D, color = list(map(int, input().split()))
        for i in range(A, C+1):
            for j in range(B, D+1):
                if color == 1:  # 빨강
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 2:
                        arr[i][j] = 0

                elif color == 2: # 파랑
                    if arr[i][j] == 0:
                        arr[i][j] = 2
                    elif arr[i][j] == 1:
                        arr[i][j] = 0

    result = 0

    for i in range(10):
        for j in range(10):
            if arr[i][j] != 0:  # 칸이 색칠된 경우
                if i == 0 or arr[i-1][j] == 0:  # 위쪽 모서리
                    result += 1
                if i == 9 or arr[i+1][j] == 0:  # 아래쪽 모서리
                    result += 1
                if j == 0 or arr[i][j-1] == 0:  # 왼쪽 모서리
                    result += 1
                if j == 9 or arr[i][j+1] == 0:  # 오른쪽 모서리
                    result += 1

    print(f'#{tc+1} {result}')