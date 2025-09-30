N, K = map(int, input().split())

checks_pos, checks_neg = [], []
for _ in range(N):
    check = int(input())
    checks_neg.append(abs(check)) if check < 0 else checks_pos.append(check)

checks_pos, checks_neg = sorted(checks_pos, reverse=True), sorted(checks_neg, reverse=True)

distance = 0
for i in range(0, len(checks_pos), K):
    distance += 2 * checks_pos[i]

for i in range(0, len(checks_neg), K):
    distance += 2 * checks_neg[i]

print(distance)
