T = int(input())

for tc in range(T):
    N = float(input())

    result = []
    for i in range(12):
        if N >= 2**(-(i+1)):
            N -= 2**(-(i+1))
            result.append(1)
            if N == False:
                break
        else:
            result.append(0)

    if N:
        print('#%d' %(tc+1), 'overflow')
    else:
        print('#%d' %(tc+1), end = ' ')
        for i in range(len(result)):
            print(result[i], end = '')
        print()