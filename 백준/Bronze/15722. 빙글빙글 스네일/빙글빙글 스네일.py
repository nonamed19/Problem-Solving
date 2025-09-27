n = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

point = [0, 0]
count = 0
now = 0

while True:
    for _ in range(count//2 + 1):
        if now == n:
            print(*point)
            exit()

        point[0] += dx[count%4]
        point[1] += dy[count%4]
        now += 1
    count += 1
