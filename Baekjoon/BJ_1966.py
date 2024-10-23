from collections import deque

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    # N : 문서의 개수
    # M : 몇 번째로 인쇄되었는지가 궁금한 문서 index
    importance = list(map(int, input().split()))
    # importance : 문서 별 중요도 list
    importance = deque(importance)
    orders = deque(list(range(N)))
    target = orders[M]
    cnt = 0

    while len(importance) >= 1:
        number = importance.popleft()
        order = orders.popleft()
        cnt += 1
        for i in range(len(importance)):
            if number < importance[i]:
                importance.append(number)
                orders.append(order)
                cnt -= 1
                break

        if target not in orders:
            print(cnt)
            break