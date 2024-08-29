def f(A, B, C):
    global cnt_A, cnt_B
    boxA, boxB, boxC = A, B, C

    while boxA >= 1 and boxB >= 1:
        if boxA < boxB and boxB < boxC:
            return cnt_A + cnt_B

        while boxB >= 1:
            boxB -= 1
            cnt_B += 1
            if boxA < boxB and boxB < boxC:
                return cnt_A + cnt_B
        boxA -= 1
        cnt_A += 1
        boxB = B
        cnt_B = 0
    return -1


T = int(input())

for tc in range(T):
    A, B, C = map(int, input().split())
    cnt_A, cnt_B = 0, 0

    print('#%d %d' %(tc+1, (f(A, B, C))))