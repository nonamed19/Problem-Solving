def f(height, lev):
    global result
    if lev == N:
        if height >= B:
            result = min(result, height) # 결과값 재할당
        return

    if height >= B:
        result = min(result, height) # 결과값 재할당
        return

    f(height + lst[lev], lev + 1) # 현재 층수 선택
    f(height, lev + 1) # 현재 층수 미선택


T = int(input())

for tc in range(T):
    N, B = map(int, input().split()) # 1 <= N <= 20, 1 <= B <= S
    lst = list(map(int, input().split())) # N명
    lst.sort(reverse=True)
    result = sum(lst) # 초기 result는 가능한 가장 큰 값
    f(0, 0)
    print(f'#{tc+1} {result - B}')