def find_set(i):
    while lst[i] != i:
        i = lst[i]
    return i


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(range(N+1))

    for _ in range(M):
        n1, n2 = map(int, input().split())
        lst[find_set(n2)] = find_set(n1)

    result = 0
    for i in range(1, N+1):
        if lst[i] == i:
            result += 1

    print(f'#{tc+1} {result}')