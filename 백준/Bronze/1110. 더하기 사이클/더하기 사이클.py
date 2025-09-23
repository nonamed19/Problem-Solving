N = input()

result, cycle = '0' + N if len(N) == 1 else N, 0
while True:
    N = '0' + N if len(N) == 1 else N
    cycle += 1
    sumnum = str(int(N[0]) + int(N[1]))
    N = N[1] + sumnum if len(sumnum) == 1 else N[1] + sumnum[1]

    if N == result:
        print(cycle)
        break
