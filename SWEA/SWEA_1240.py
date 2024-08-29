T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    X, Y = 0, 0
    for i in range(N):
        if 1 in arr[i]:
            X = i
            for j in range(M-1, -1, -1):
                if arr[i][j] == 1:
                    Y = j
                    break
            if X:
                break

    lst = arr[X][Y-55:Y+1]
    result = [0]*8
    for i in range(8):
        temp_lst = lst[7*i:7*(i+1)]
        if temp_lst == [0, 0, 0, 1, 1, 0, 1]:
            result[i] = 0
        elif temp_lst == [0, 0, 1, 1, 0, 0, 1]:
            result[i] = 1
        elif temp_lst == [0, 0, 1, 0, 0, 1, 1]:
            result[i] = 2
        elif temp_lst == [0, 1, 1, 1, 1, 0, 1]:
            result[i] = 3
        elif temp_lst == [0, 1, 0, 0, 0, 1, 1]:
            result[i] = 4
        elif temp_lst == [0, 1, 1, 0, 0, 0, 1]:
            result[i] = 5
        elif temp_lst == [0, 1, 0, 1, 1, 1, 1]:
            result[i] = 6
        elif temp_lst == [0, 1, 1, 1, 0, 1, 1]:
            result[i] = 7
        elif temp_lst == [0, 1, 1, 0, 1, 1, 1]:
            result[i] = 8
        elif temp_lst == [0, 0, 0, 1, 0, 1, 1]:
            result[i] = 9

    odd, even = 0, 0
    for i in range(4):
        odd += result[2*i]
        even += result[(2*i)+1]

    if (odd*3 + even) % 10 == 0:
        print('#%d %d' %(tc+1, odd+even))
    else:
        print('#%d %d' %(tc+1, 0))