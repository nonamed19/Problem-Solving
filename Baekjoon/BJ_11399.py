import sys

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()

temp = 0
result = 0
for time in times:
    temp += time
    result += temp

print(result)