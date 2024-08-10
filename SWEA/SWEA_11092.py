T = int(input()) # 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )

for tc in range(T):
    N = int(input()) # 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 100 )
    arr = list(map(int, input().split())) # N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 10 )
    num_max = 1 # N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 10 )
    num_min = 10 # N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 10 )

    #최대값
    for i in range(N):
        if arr[i] >= num_max:
            num_max = arr[i]
            idx_max = i+1

    #최소값
    for i in range(N-1, -1, -1):
        if arr[i] <= num_min:
            num_min = arr[i]
            idx_min = i+1

    print('#%d %d'%(tc+1, abs(idx_max - idx_min)))