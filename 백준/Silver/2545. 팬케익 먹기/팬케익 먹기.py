T = int(input())

for _ in range(T):
    _ = input()
    A, B, C, D = map(int, input().split())

    for _ in range(D):
        if A >= max(B, C):
            A -= 1
            continue
        elif B >= max(A, C):
            B -= 1
            continue
        else:
            C -= 1
            continue

    print(A*B*C)
