T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    front = 0
    # rear = 0 # 해당 코드에서 rear는 생략

    print('#%d %d' %(tc+1, lst[front+(M%N)]))