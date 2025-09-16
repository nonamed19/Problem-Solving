T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    wins, losses, scores = [0]*(n+1), [0]*(n+1), [0]*n

    for _ in range(m):
        a, b, p, q = map(int, input().split())
        wins[a] += p
        wins[b] += q
        losses[a] += q
        losses[b] += p

    for i in range(1, n+1):
        if wins[i] == 0 and losses[i] == 0:
            scores[i - 1] = 0
        else:
            scores[i - 1] = (wins[i] ** 2 / (wins[i] ** 2 + losses[i] ** 2)) * 1000

    print(int(max(scores)))
    print(int(min(scores)))
