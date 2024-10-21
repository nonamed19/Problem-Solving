while True:
    lst = list(map(int, input().split()))
    lst.sort()
    # 종료 조건
    if sum(lst) == 0:
        break

    for i in range(len(lst)):
        lst[i] **= 2

    if lst[0] + lst[1] == lst[2]:
        print('right')
    else:
        print('wrong')