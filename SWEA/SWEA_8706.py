T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    result = 0
    for i in range(N-1):
        while M <= lst[i+1]:
            lst[i] -= M
            result += i
            print(i, lst[i], result)
        lst[i+1] += lst[i]

    print(result)