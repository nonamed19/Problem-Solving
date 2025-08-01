import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]

dp = [0]*N
if len(stairs) == 1:
    dp[0] = stairs[0]

elif len(stairs) == 2:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

else:  # elif len(stairs) > 2:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for i in range(2, N):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[N - 1])