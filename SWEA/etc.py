T = int(input())


def perm(i, depth, s):
    global min_val
    if depth == n:  # 모든 순열을 돌았다면
        min_val = min(min_val, s + arr[i][0])
        return

    for j in range(n):
        if not p[j]:
            p[j] = 1
            perm(j, depth + 1, s + arr[i][j])
            p[j] = 0


for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_val = 100 * n
    p = [1] + [0] * (n - 1)  # 무조건 첫번째부터 시작
    perm(0, 1, 0)
    print(f'#{tc} {min_val}')