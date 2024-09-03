T = int(input())

for tc in range(T):
    lst = list(input())
    N = len(lst)

    cnt = 0
    for i in range(N-1):
        if lst[i] == '(' and lst[i+1] == '|':
            cnt += 1
        if lst[i] == '|' and lst[i+1] == ')':
            cnt += 1
        if lst[i] == '(' and lst[i+1] == ')':
            cnt += 1

    print(f'#{tc+1} {cnt}')