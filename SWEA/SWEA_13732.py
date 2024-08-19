from pprint import pprint

T = int(input())

for tc in range(T):
    N = int(input())
    arr_input = [list(input()) for _ in range(N)]
    arr = [['.']*(N+2) for _ in range(N+2)]

    for i in range(N):
        for j in range(N):
            arr[i+1][j+1] = arr_input[i][j]

    lst = [] # 꼭지점 : 좌상, 우상, 좌하, 우하
    lst_cnt = []

    for i in range(1, N+1):
        lst_cnt.append(arr[i].count('#'))
        for j in range(1, N+1):
            if arr[i][j] == '#':
                if arr[i-1][j] == '.' and arr[i][j-1] == '.':
                    lst.append([i, j])
                if arr[i-1][j] == '.' and arr[i][j+1] == '.':
                    lst.append([i, j])
                if arr[i+1][j] == '.' and arr[i][j-1] == '.':
                    lst.append([i, j])
                if arr[i+1][j] == '.' and arr[i][j+1] == '.':
                    lst.append([i, j])

    # 열 별로 '#'의 개수 확인
    validation = 1
    while validation != 0:
        validation = 0
        if 0 in lst_cnt:
            lst_cnt.remove(0)
            validation += 1

    for i in range(len(lst_cnt)):
        if lst_cnt[i] != lst_cnt[0]:
            lst.append([0, 0]) # dummy

    # 정사각형 모양 확인
    if len(lst_cnt) != lst_cnt[0]:
        lst.append([0, 0]) # dummy

    # 사각형 모양 확인
    if len(lst) != 4:
        print('#%d no' %(tc+1))
    else:
        if ((lst[0][0] == lst[1][0])
            and (lst[1][1] == lst[3][1])
            and (lst[0][1] == lst[2][1])
            and (lst[2][0] == lst[3][0])):
            print('#%d yes' %(tc+1))
        else:
            print('#%d no' % (tc+1))