T = int(input())

for tc in range(T):
    N = int(input())
    lst_x, lst_y = [], []

    for i in range(N):
        temp = list(map(int, input().split()))
        lst_x.append(temp[0])
        lst_y.append(temp[1])

    cnt = 0
    for i in range(N-1):
        for j in range(i, N):
            if lst_x[i] < lst_x[j] and lst_y[i] > lst_y[j]:
                cnt += 1
            elif lst_x[i] > lst_x[j] and lst_y[i] < lst_y[j]:
                cnt += 1

    print(f'#{tc+1} {cnt}')