from math import ceil, floor

N = int(input()) # 참가자의 수
lst_shirt = list(map(int, input().split()))
T, P = map(int, input().split()) # T : 티셔츠 묶음 / P : 펜 묶음

# 1. 티셔츠 주문 따로
result_shirt = []
for shirt in lst_shirt:
    result_shirt.append(ceil(shirt / T))

print(sum(result_shirt))

# 2. 펜 주문 따로
result_pen = []
result_pen.append(floor(N / P))
result_pen.append(N % P)

print(*result_pen)