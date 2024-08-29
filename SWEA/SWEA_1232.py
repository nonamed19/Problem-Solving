T = 10

for tc in range(T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    result = [0]*N

    for i in range(N-1, -1, -1):
        if len(arr[i]) == 2:
            result[i] = int(arr[i][1])
        elif len(arr[i]) == 4:
            left, right = int(arr[i][2])-1, int(arr[i][3])-1
            if arr[i][1] == '+':
                result[i] = result[left] + result[right]
            elif arr[i][1] == '-':
                result[i] = result[left] - result[right]
            elif arr[i][1] == '*':
                result[i] = result[left] * result[right]
            elif arr[i][1] == '/':
                result[i] = result[left] / result[right]

    print('#%d %d' %(tc+1, result[0]))