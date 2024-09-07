from copy import deepcopy


def find_max(X, Y, height, length, arr, path, validation):
    global result
    if result < length:
        result = length

    path[X][Y] = 1  # 현재 위치 저장
    di = [0, 1, 0, -1]  # 상하좌우 이동
    dj = [1, 0, -1, 0]

    for k in range(4):
        ni = X + di[k]
        nj = Y + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            # 방문하지 않았고, 현재 높이보다 낮은 곳만 이동
            if arr[ni][nj] < height and path[ni][nj] == 0:
                find_max(ni, nj, arr[ni][nj], length + 1, arr, path, validation)

    # 모든 방향으로 이동 후 공사 기회 사용 여부 체크
    if validation == 0:  # 공사 기회가 아직 남아 있을 때
        for k in range(4):
            ni = X + di[k]
            nj = Y + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 현재 높이보다 최대 K만큼 깎을 수 있는지 확인
                if arr[ni][nj] - K < height and path[ni][nj] == 0:
                    original_value = arr[ni][nj]  # 원래 값을 저장
                    arr[ni][nj] = height - 1  # 공사로 높이를 낮춤
                    find_max(ni, nj, arr[ni][nj], length + 1, arr, path, 1)  # 공사 후 탐색
                    arr[ni][nj] = original_value  # 공사 전 원래 값으로 복구

    path[X][Y] = 0  # 탐색 후 경로 복구


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())  # N: 배열 크기, K: 최대 공사 가능 깊이
    arr_input = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    result = 0

    top_height = 0
    for i in range(N):  # 가장 높은 봉우리 탐색
        top_height = max(top_height, max(arr_input[i]))

    start_point = []
    for i in range(N):
        for j in range(N):
            if arr_input[i][j] == top_height:
                start_point.append([i, j])  # 가장 높은 위치의 좌표 저장

    for X, Y in start_point:
        find_max(X, Y, arr_input[X][Y], 1, deepcopy(arr_input), deepcopy(visited), 0)  # 탐색 시작 (length를 1로 설정)

    print(f'#{tc + 1} {result}')