T = int(input())

for _ in range(T):
    input()
    A, B, C, D = map(int, input().split())
    A, B, C = sorted((A, B, C))

    S1 = A + B + C - D
    A = min(A, S1//3)
    S2 = S1 - A
    B = min(B, S2//2)
    C = S2 - B

    print(A*B*C)
