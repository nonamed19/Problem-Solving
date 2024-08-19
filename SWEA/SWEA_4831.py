def f():
    now, cnt = 0, 0
    while True:
        for i in range(K, -1, -1):
            next = now + i
            if next == now: return 0
            if next in lst:
                now = next
                break
            if next >= N: return cnt
        cnt += 1

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    print('#%d %d' %(tc+1, f()))