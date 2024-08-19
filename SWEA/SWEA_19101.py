T = int(input())

for tc in range(T):
    x1, y1, p1, q1 = list(map(int, input().split())) # 첫 번째 사각형
    x2, y2, p2, q2 = list(map(int, input().split())) # 두 번째 사각형

    # 아무것도 아닌 경우
    if q2 < y1 or p1 < x2 or q1 < y2 or p2 < x1:
        print('#%d %d' %(tc+1, 4))

    elif ((x1 == p2 and y1 == q2)
        or (p1 == x2 and y1 == q2)
        or (p1 == x2 and q1 == y2)
        or (x1 == p2 and q1 == y2)):
        print('#%d %d' %(tc+1, 3))

    elif y1 == q2 or p1 == x2 or q1 == y2 or x1 == p2:
        print('#%d %d' %(tc+1, 2))

    else:
        print('#%d %d' %(tc+1, 1))