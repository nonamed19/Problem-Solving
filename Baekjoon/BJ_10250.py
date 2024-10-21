T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        XX = str(N // H)
        YY = str(H)
    else:
        XX = str(N // H + 1)
        YY = str(N % H)

    if len(XX) != 2:  # YXX, YYXX 형식 맞춰주기
        XX = '0' + XX

    print(YY + XX)