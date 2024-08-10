def f1(i, V):       # V개의 집합에서 i원소의 포함여부 결정
    if i == V:      # 모든 원소에 대해 결정하면
        print(b)
    else:
        b[i] = 1    # a[i]가 부분집합에 포함되는 경우
        f1(i+1, V)
        b[i] = 0
        f1(i+1, V)

def f2(i, V, K):
    global cnt
    if i == V:      # 모든 원소에 대해 결정하면
        s = 0       # 부분집합의 합 저장
        for j in range(V):
            if b[j]:    # a[j]가 포함되면
                s += a[j]
        # print(s)
        if s == K:      # 부분집합의 합이 K인 경우
            cnt += 1
    else:
        b[i] = 1    # a[i]가 부분집합에 포함되는 경우
        f2(i+1, V, K)
        b[i] = 0
        f2(i+1, V, K)

def f3(i, V, N, K): # i: 고려할 원소, V: 원소 수, N: 부분집합 원소 수, K: 찾는 합
    global cnt
    if i == V:      # 모든 원소에 대해 결정하면
        s = 0       # 부분집합의 합 저장
        c = 0       # 부분집합 원소 수
        for j in range(V):
            if b[j]:    # a[j]가 포함되면
                s += a[j]
                c += 1
        # print(s)
        if c == N and s == K:      # 부분집합의 합이 K인 경우
            cnt += 1
    else:
        b[i] = 1    # a[i]가 부분집합에 포함되는 경우
        f3(i+1, V, N, K)
        b[i] = 0
        f3(i+1, V, N, K)

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    a = list(x for x in range(1, 13))
    b = [0]*12      # b[i]: a[i] 원소의 포함여부 표시
    # -------------------------------------------------------
    # 재귀로 모든 부분집합 만들기
    # f1(0, 12)       # 총 12개의 원소, a[0]부터 포함여부 결정하기
    # -------------------------------------------------------
    # 부분집합의 합이 K인 경우의 수 cnt 찾기
    # cnt = 0
    # f2(0, 12, K)
    # print(cnt)
    # -------------------------------------------------------
    # 원소의 개수가 N개이면서, 합이 K인 부분집합의 수 cnt 찾기
    cnt = 0
    f3(0, 12, N, K)
    print(cnt)