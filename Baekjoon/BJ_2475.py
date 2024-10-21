N = 5

lst_input = list(map(int, input().split()))

lst_sqrd = []
for i in range(N):
    lst_sqrd.append(lst_input[i] ** 2)

result = sum(lst_sqrd) % 10

print(result)