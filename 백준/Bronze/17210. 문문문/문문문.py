import sys; input = sys.stdin.readline


N = int(input())
door = int(input())

if N >= 6:
    print('Love is open door')
else:
    for i in range(N - 1):
        door = 1 - door
        print(door)
