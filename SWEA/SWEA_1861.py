# 재귀 쓰면 recursion error 발생합니다.. 2200번 돌아야 함

def finds(x, y, num):
    if num in lst_num: # 이미 탐색을 수행한 숫자는 pruning하고 진행하기
        return 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 1

    while True:
        lst_num.append(num)
        validation = 0
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == num + 1:
                x, y = ni, nj
                num += 1
                cnt += 1
                validation = 1
                break
        if validation == 1:
            pass
        else:
            lst_result.append(num)
            lst_cnt.append(cnt)
            return


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst_num = []
    lst_result = []
    lst_cnt = []
    lst_final = []

    for i in range(N):
        for j in range(N):
            finds(i, j, arr[i][j])

    for i in range(len(lst_cnt)):
        if lst_cnt[i] == max(lst_cnt):
            lst_final.append(lst_result[i] - max(lst_cnt) + 1)

    print(f'#{tc+1} {sorted(lst_final)[0]} {max(lst_cnt)}')