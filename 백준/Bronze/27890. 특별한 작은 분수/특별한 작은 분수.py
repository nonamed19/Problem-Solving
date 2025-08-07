import sys

x0, N = map(int, sys.stdin.readline().split())

dp = [x0]*(N+1)  # initialization

for i in range(1, N+1):
    # x_t가 짝수인 경우
    if dp[i-1] % 2 == 0:
        dp[i] = int(dp[i-1]/2) ^ 6

    # x_t가 홀수인 경우
    else:
        dp[i] = (2*dp[i-1]) ^ 6

print(dp[N])
