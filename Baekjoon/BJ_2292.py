N = int(input())

result = 0 # 변수 초기화
if N == 1:
    result = 1
else:
    mul, order, iter = 0, 1, 2
    while True:
        div = (mul + order)

        # 종료 조건
        if N / (1 + 6*div) <= 1:
            result = iter
            break

        # 다음 계산 수행
        mul = div
        order += 1
        iter += 1

print(result)