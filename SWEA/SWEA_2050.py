lst = list(map(ord, input()))

for i in range(len(lst)):
    lst[i] -= 64

print(*lst)