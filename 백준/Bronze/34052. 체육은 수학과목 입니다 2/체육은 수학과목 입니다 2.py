import sys

time = 0
for _ in range(4):
    time += int(sys.stdin.readline())

if time + 300 <= 1800:
    print('Yes')
else:  # elif time + 300 > 1800:
    print('No')
