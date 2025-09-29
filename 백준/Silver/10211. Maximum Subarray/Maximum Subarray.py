T = int(input())

for _ in range(T):
    N = int(input())
    Xs = list(map(int, input().split()))
    dp = [0]*N
    for i in range(N):
        dp[i] = max(dp[i-1] + Xs[i], Xs[i])
    print(max(dp))