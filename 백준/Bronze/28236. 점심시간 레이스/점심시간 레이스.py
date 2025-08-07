import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

classroom = k + 1       # initialization
distance = n + m + 1    # initialization

for i in range(1, k+1):
    f, d = map(int, input().split())
    temp = (f - 1) + (m - d)

    if temp < distance:
        distance = temp
        classroom = i
    elif temp == distance:
        if i < classroom:
            classroom = i

print(classroom)
