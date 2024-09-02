def f(score, N, cnt):
    global result

    if cnt == N:
        num = sum_final(score)
        if num > result:
            result = num
        return

    for i in range(len(score)):
        for j in range(i+1, len(score)):
            score[i], score[j] = score[j], score[i] # 두 자리 교환
            f(score, N, cnt+1)  # 다음 교환으로 재귀 호출
            score[i], score[j] = score[j], score[i] # 교환을 원상 복구


def sum_final(score):
    temp_sum = 0
    for i in range(len(score)):
        temp_sum += score[-1-i] * (10**i)
    return temp_sum


T = int(input())

for tc in range(T):
    lst, N = input().split()
    lst = list(map(int, lst))  # 입력을 숫자 리스트로 변환
    N = int(N)  # N을 정수로 변환

    result = 0
    f(lst, N, 0)

    print(f'#{tc+1} {result}')