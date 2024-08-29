T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(str, range(10)))
    cnt = 0

    while lst:
        cnt += 1
        mul = N*cnt
        temp = list(str(mul))
        for num in temp:
            if num in lst:
                lst.remove(num)

    print('#%d %d' %(tc+1, mul))