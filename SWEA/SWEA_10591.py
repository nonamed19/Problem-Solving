T = int(input()) # 테스트 케이스 개수 T (1<=T<=50)

for tc in range(T):
    P, Pa, Pb = map(int, input().split()) # 1 <= Pa, Pb < P <=1000

    # for A
    start = 1
    end = P
    iter_A = 0
    while start <= end:
        iter_A += 1
        middle = (start + end)//2
        if middle == Pa:
            break
        elif middle > Pa:
            end = middle
        else:
            start = middle

    # for B
    start = 1
    end = P
    iter_B = 0
    while start <= end:
        iter_B += 1
        middle = (start + end) // 2
        if middle == Pb:
            break
        elif middle > Pb:
            end = middle
        else:
            start = middle

    if iter_A < iter_B:
        print('#%d %s' %(tc+1, 'A'))
    elif iter_A == iter_B:
        print('#%d %s' %(tc+1, '0'))
    else:
        print('#%d %s' %(tc+1, 'B'))