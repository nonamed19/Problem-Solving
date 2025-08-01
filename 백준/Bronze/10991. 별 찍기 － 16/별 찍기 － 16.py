N = int(input())

star = ['*']
space = ['']

for i in range(N):
    # first row
    if i == 0:
        temp = space*(N - 1) + star
        print(*temp)
    # last row
    elif i == (N - 1):
        temp = star*(i + 1)
        print(*temp)
    # rows in-between
    else:
        temp = space * (N - 1 - i)
        for _ in range(i + 1):
            temp += star
        print(*temp)