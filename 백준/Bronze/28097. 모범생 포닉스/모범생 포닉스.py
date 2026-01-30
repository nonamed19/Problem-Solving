import sys; input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))

time_total = 0
for time in T:
    time_total += time + 8
time_total -= 8  # 중복 처리

day = time_total // 24
hour = time_total - 24*day
print(day, hour)
