T = int(input())

for tc in range(T):
    N, K = map(int, input().split()) # 원소의 수 N, 부분 집합의 합 K
    arr = [x for x in range(1, 13)]
    cnt = 0

    for i in range(1 << 12): # 12개의 원소들 중에서 집합을 찾아야 하기 때문에
        temp = []
        for j in range(12): # 12개의 원소들 중에서 집합을 찾아야 하기 때문에
            if i & (1 << j):
                temp.append(arr[j])

        if (len(temp) == N) and (sum(temp) == K):
            cnt += 1

    print('#%d %d' %(tc+1, cnt))