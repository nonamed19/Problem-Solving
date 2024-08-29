T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    result = [0]
    for i in range(1, N+1):
        result.append(lst[i-1])
        print(i, i//2)
        if i == 2:  # len(result) == 3일 때, i는 2
            if result[i] < result[i-1]:
                result[i-1], result[i] = result[i], result[i-1]
        elif i > 2:  # len(result) > 3일 때, i는 3 이상
            if result[i] < result[i//2]:
                result[i], result[i//2] = result[i//2], result[i]

    print(result)

    cnt = 0
    step = N
    while step > 0:  # step != 0 대신 step > 0 사용
        cnt += result[step]
        step = step//2
    print(cnt)