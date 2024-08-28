T = int(input())

for tc in range(T):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    child1 = [0]*(E+2)
    child2 = [0]*(E+2)

    for i in range(E):          # E = 0, 1, 2, 3, 4
        if child1[lst[i*2]] == 0:    # child1에 저장
            child1[lst[i*2]] = lst[i*2+1]
        elif child2[lst[i*2]] != 0:     # child2에 저장
            child2[lst[i*2]] = lst[i*2+1]

    print(child1)
    print(child2)