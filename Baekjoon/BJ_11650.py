N = int(input())

points = []
for _ in range(N):
    points.append(list(map(int, input().split())))

points.sort()
for point in points:
    print(*point)