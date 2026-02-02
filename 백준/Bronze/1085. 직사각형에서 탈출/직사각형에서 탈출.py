import sys; input = sys.stdin.readline

x, y, w, h = map(int, input().split())

dist_x = min(x, w-x)
dist_y = min(y, h-y)
print(min(dist_x, dist_y))
