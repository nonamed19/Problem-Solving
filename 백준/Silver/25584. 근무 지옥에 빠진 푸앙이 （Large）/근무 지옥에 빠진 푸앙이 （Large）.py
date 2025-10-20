import sys
input = sys.stdin.readline

N = int(input())

schedules = {}
time = [4, 6, 4, 10]
for _ in range(N):
    for i in range(4):
        for name in input().split():
            if name == '-':
                continue
            schedules[name] = schedules.get(name, 0) + time[i]

if not schedules:
    print('Yes')
else:
    print('Yes' if max(schedules.values()) - min(schedules.values()) <= 12 else 'No')
