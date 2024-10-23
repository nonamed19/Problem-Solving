N = int(input())

persons = list([] for _ in range(N))

for i in range(N):
    persons[i] = list(map(int, input().split())) + [i]

persons = sorted(persons, reverse = True)

order = 0
orders = []
for i in range(N):
    if i == 0:
        order += 1
    else:  # if i >= 2:
        for j in range(1, i + 1):
            if persons[i][0] < persons[i-j][0] and persons[i][1] < persons[i-j][1]:
                order += 1

    orders.append(order)
    order = 1

results = [0] * N
for i in range(N):
    results[persons[i][2]] = orders[i]

print(*results)