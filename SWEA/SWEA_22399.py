T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    lst_cnt = [0]*max(lst)
    lst_num = []
    for num in lst:
        lst_cnt[num-1] += 1
        if num not in lst_num:
            lst_num.append(num)

    if len(lst_num) < 3:
        result = -1
    elif len(lst_num) == 3:
        result = max(lst_cnt) - min(lst_cnt)
    else:
        result = 30
        for i in range(1, N-2):
            for j in range(i+1, N-1):
                num_max = max(sum(lst_cnt[:i]), sum(lst_cnt[i:j]), sum(lst_cnt[j:N]))
                num_min = min(sum(lst_cnt[:i]), sum(lst_cnt[i:j]), sum(lst_cnt[j:N]))
                result = min(result, (num_max - num_min))

    print(f'#{tc+1} {result}')