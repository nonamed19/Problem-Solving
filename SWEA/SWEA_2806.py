def N_queen(order, col, visited):
    global cnt
    if order == N: # 마지막 queen까지 배치를 완료한 경우
        cnt += 1
        return

    for i in range(N):
        if col[i] != 0: # 동일 열 위치에 대해 pruning 수행
            continue

        validation = 1
        for j in range(order): # 대각선 위치에 대해 pruning 수행
            if abs(i - visited[j]) == abs(order - j):
                validation = 0
                break

        if validation == 0:
            continue

        visited[order] = i
        col[i] = 1
        N_queen(order + 1, col, visited) # recursive
        col[i] = 0

    return # 해당 order에서 놓을 수 있는 queen의 자리가 없는 경우


T = int(input())

for tc in range(T):
    N = int(input()) # N queen
    visited = [-1] * N
    col = [0] * N
    cnt = 0

    N_queen(0, col, visited)

    print(f'#{tc+1} {cnt}')