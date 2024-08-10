T = int(input())

for tc in range(T):
    N = int(input())
    print('#%d' %(tc+1))

    for i in range(N):
        if i == 0:
            lst = [1]
            lst_pre = lst
            lst_pre = lst
            print(*lst)
        elif i == 1:
            lst = [1, 1]
            print(*lst)
        else:
            temp = []
            temp.append(1)
            for j in range(i-1):
                temp.append(lst[j]+lst[j+1])
            temp.append(1)
            lst = temp
            print(*lst)