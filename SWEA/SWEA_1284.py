T = int(input())

for tc in range(T):
    # P : A사 리터당 금액
    # Q : B사 기본 금액(사용량 R리터 이하)
    # R : B사 사용량 기준
    # S : B사 추가 리터당 금액(사용량 R리터 초과)
    # W : 실제 사용량
    P, Q, R, S, W = map(int, input().split())

    # A company
    price_A = P*W

    # B company
    if W <= R:
        price_B = Q
    else:
        price_B = Q + S*(W-R)

    print(f'#{tc+1} {min(price_A, price_B)}')