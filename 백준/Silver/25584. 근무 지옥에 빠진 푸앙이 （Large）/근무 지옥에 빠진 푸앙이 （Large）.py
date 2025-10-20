N = int(input())

schedules = {}
time = [4, 6, 4, 10]
for _ in range(N):
    for i in range(4):
        names = input().split()
        for name in names:
            if name not in schedules:
                schedules[name] = time[i]

            else:
                schedules[name] += time[i]

if '-' in schedules:
    schedules.pop('-')

if schedules and (max(schedules.values()) - min(schedules.values())) <= 12:
    print('Yes')
elif not schedules:
    print('Yes')
else:
    print('No')
