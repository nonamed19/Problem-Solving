T = int(input())

for tc in range(T):
    temp = list(input().split())
    N = int(temp[0])
    num_16 = list(temp[1])

    dict_16 = {'A': [1, 0, 1, 0],
               'B': [1, 0, 1, 1],
               'C': [1, 1, 0, 0],
               'D': [1, 1, 0, 1],
               'E': [1, 1, 1, 0],
               'F': [1, 1, 1, 1]}

    result = []
    for i in range(len(num_16)):
        temp = [0, 0, 0, 0]
        if num_16[i].isdigit():
            num = int(num_16[i])
            for j in range(4):
                temp[4-1-j] = num % 2
                num //= 2
            result += temp
        else:
            result += dict_16[num_16[i]]

    print('#%d' %(tc+1), end = ' ')
    for i in range(len(result)):
        print(result[i], end = '')
    print()