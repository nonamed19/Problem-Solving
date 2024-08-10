T = int(input()) # 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

for tc in range(T):
    n, m = map(int, input().split())    # 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
    lst = list(map(int, input().split()))
    num_max = 1 * m
    num_min = 10000 * m

    for i in range(n-m+1):
        num_sum = 0
        for j in range(m):
            num_sum += lst[i+j]
        # print(num_sum)

        if num_sum > num_max:
            num_max = num_sum
        if num_sum < num_min:
            num_min = num_sum

    print('#%d %d' %(tc+1, num_max - num_min))