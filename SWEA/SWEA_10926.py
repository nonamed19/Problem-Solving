T = int(input())

for tc in range(T):
    lst = list(map(int, input()))
    bit = 7

    print('#%d' %(tc+1), end = ' ')
    for i in range(10):
        temp_lst = lst[bit*i:bit*(i+1)]

        temp = 0
        for j in range(bit):
            temp += temp_lst[-1-j]*(2**j)
        print(temp, end = ' ')
    print()