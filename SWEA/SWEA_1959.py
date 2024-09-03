T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split())) # len(lst1) == N
    lst2 = list(map(int, input().split())) # len(lst2) == M


    result = []
    if N < M: # lst1보다 lst2의 길이가 더 긴 경우
        for i in range(M-N+1):
            temp = 0
            for j in range(N):
                temp += lst1[j] * lst2[i+j]
            result.append(temp)

    else: # lst2보다 lst1의 길이가 더 긴 경우
        for i in range(N-M+1):
            temp = 0
            for j in range(M):
                temp += lst1[i+j] * lst2[j]
            result.append(temp)

    print(f'#{tc+1} {max(result)}')