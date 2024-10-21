T = int(input())

for tc in range(T):
    lst = list(input())

    score = 1
    result = 0
    for OX in lst:
        if OX == 'O':
            result += score
            score += 1
        else:  # if OX == 'X':
            score = 1  # 연속된 점수 초기화

    print(result)