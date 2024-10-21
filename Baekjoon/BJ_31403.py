N = 3

lst = list(input() for _ in range(N))

# result1
result1 = int(lst[0]) + int(lst[1]) - int(lst[2])

# result2
result2 = int(lst[0] + lst[1]) - int(lst[2])

print(result1)
print(result2)