# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)  # initialization

for i in range(1, n+1):
    # 규칙 찾기
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 3
    elif i == 3:
        dp[3] = 5
    else:
        dp[i] = dp[i-1] + dp[i-2]*2

result = dp[n] % 10007
print(result)
