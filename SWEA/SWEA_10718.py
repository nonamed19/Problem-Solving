from pprint import pprint

def f(i, j):
    # delta를 통해 행/렬 이동
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while True:
        visited[i][j] += 1
        if arr[i][j] == 3: # 3을 찾은 경우
            return 1

        else: # 3을 찾지 못한 경우
            for w in range(4):
                if arr[i+dx[w]][j+dy[w]] == 0: # 향하는 방향이 통로인 경우
                    stack.append([i, j])
                    i = i + dx[w]
                    j = j + dy[w]
                    f(i, j)

                else: # 향하는 방향이 벽인 경우
                    stack.pop() ######################### 이거 고쳐줘야됨

            stack.append([i, j])


T = int(input())

for tc in range(T):
    N = int(input())
    arr_input = [list(map(int, input())) for _ in range(N)]

    # arr_input의 주위를 1로 채우기. size N x N -> N+2 x N+2
    arr_ones = [list(1 for _ in range(N+2)) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            arr_ones[i+1][j+1] = arr_input[i][j]
    arr = arr_ones
    pprint(arr)

    # 시작 위치 판별
    now_i, now_j = N, 0
    for num in arr[now_i]:
        if num != 2: now_j += 1
        else: break

    # stack에 이동하는 위치를 저장하며 탐색 수행
    visited = list([0 for _ in range(N)] for _ in range(N))
    stack = []

    print(arr[now_i][now_j])