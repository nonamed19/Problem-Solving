T = int(input()) # 테스트 케이스의 수 T

for tc in range(T):
    N = int(input()) # 테스트 케이스의 번호
    lst = list(map(int, input().split())) # 점수
    lst_temp = [0] * 101

    for num in lst:
        lst_temp[num] += 1

    idx_max = 0
    for num in lst_temp:
        if idx_max <= num:
            idx_max = num

    # score_max = 0
    # score_max = lst_temp.index(idx_max)

    lst_sorted = list(x for x in range(101))
    score_max = 0
    for i in range(len(lst_temp)):
        if lst_temp[i] == idx_max:
            score_max = lst_sorted[i]

    print('#%d %d' %(N, score_max))