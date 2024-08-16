T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(input().split())

    if N % 2 == 0: # 짝수일 때
        temp1 = []
        temp2 = []
        result = []
        temp1.append(lst[:N//2])
        temp2.append(lst[N//2:])

        for i in range(N//2):
            result.append(temp1[0][i])
            result.append(temp2[0][i])

    else:
        temp1 = []
        temp2 = []
        result = []
        temp1.append(lst[:N//2+1])
        temp2.append(lst[N//2+1:])

        for i in range(N//2):
            result.append(temp1[0][i])
            result.append(temp2[0][i])
        result.append(temp1[0][N//2])

    print('#%d' %(tc+1), *result)