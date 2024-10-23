N = int(input())

bag_5kg = N // 5
bag_3kg = N // 3

combinations = []
for i in range(bag_5kg, -1, -1):
    for j in range(bag_3kg, -1, -1):
        combinations.append([i, j])

for combination in combinations:
    if combination[0] * 5 + combination[1] * 3 == N:
        print(combination[0] + combination[1])
        break
else:
    print(-1)