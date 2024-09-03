T = int(input())

for tc in range(T):
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    lst.sort(key = lambda x:x[1])

    time_now = lst[0][1] # 제일 처음 끝나는 시간부터 탐색 시작
    result = 1 # 처음 1회는 lst[0]이 수행된 후를 기준으로 하고 있음
    for i in range(1, N):
        if time_now <= lst[i][0]:
            time_now = lst[i][1]
            result += 1

    print(f'#{tc+1} {result}')