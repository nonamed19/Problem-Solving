T = int(input())

for tc in range(T):
    N, M = map(int, input().split()) # N x M 행렬(3<=N, M<=100)
    arr = [list(map(int, input().split())) for _ in range(M)]
    result = 0

    for i in range(N):
        for j in range(M):
            print(arr[i])
            print(arr[i][j])