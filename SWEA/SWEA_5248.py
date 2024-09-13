def find_set(i):        # i의 대표원소 찾기
    while lst[i] != i:  # 최상단 부모 원소를 찾아서 인덱스를 변경하며 올라가기
        i = lst[i]      # i가 가리키는 원소가 자기자신(대표)인지 확인
    return i


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    lst = list(range(N+1))  # 대표원소 make_set(1) ~ make_set(N)
    for i in range(M):
        n1, n2 = arr[i*2], arr[i*2 + 1]
        lst[find_set(n2)] = find_set(n1)

    result = 0
    for i in range(1, N+1):
        if lst[i] == i:
            result += 1

    print(f'#{tc+1} {result}')