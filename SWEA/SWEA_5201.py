T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst_N = sorted(list(map(int, input().split())), reverse=True) # 화물의 무게
    lst_M = sorted(list(map(int, input().split())), reverse=True) # 트럭의 적재용량
    result = 0

    for truck in lst_M:
        order = 0
        for cntr in lst_N:
            if truck >= cntr:
                result += cntr
                lst_N.pop(order)
                break
            order += 1

    print(f'#{tc+1} {result}')