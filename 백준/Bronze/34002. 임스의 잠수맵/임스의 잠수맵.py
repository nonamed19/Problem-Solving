A, B, C = map(int, input().split())
S, V = map(int, input().split())
L = int(input())

EXP = (250 - L)*100
time = 0
while True:
    while V:
        for i in range(30):
            EXP -= C
            time += 1
            if EXP <= 0:
                print(time)
                exit()
        V -= 1

    while S:
        for i in range(30):
            EXP -= B
            time += 1
            if EXP <= 0:
                print(time)
                exit()
        S -= 1

    while True:
        EXP -= A
        time += 1
        if EXP <= 0:
            print(time)
            exit()
