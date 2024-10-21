N, K = map(int, input().split())

# initialization of Binominal Coefficient
tree = [[1], [1, 1]]
for _ in range(9):
    tree.append([1])

for i in range(2, N + 1):
    for j in range(i - 1):
        tree[i].append(tree[i-1][j] + tree[i-1][j+1])
    tree[i].append(1)

print(tree[N][K])