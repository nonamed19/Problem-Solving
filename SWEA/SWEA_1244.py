def f(score, N):
    global result
    perm(0)  # 가능한 모든 자리 변경 조합을 구함

    for _ in range(N):  # N번의 교환을 반복
        max_score = score[:]  # 현재 score를 복사하여 max_score로 설정
        for i, j in lst_idx:  # 가능한 자리 교환 조합을 반복
            i, j = i-1, j-1  # 인덱스를 0 기반으로 조정
            temp = score[:]  # 원본 리스트 복사
            temp[i], temp[j] = temp[j], temp[i]  # 두 자리 교환
            if temp > max_score:  # 교환 후의 숫자가 더 크다면
                max_score = temp  # max_score를 갱신

        score = max_score[:]  # 가장 큰 값을 score에 할당

    result = sum_final(score)  # 최종 결과 값을 계산하여 result에 저장
    return


def perm(x):
    if x == 2:  # 두 자리만 변경하는 경우를 구함
        lst_idx.append(path[:])  # path의 복사본을 lst_idx에 추가
        return

    for i in range(1, len(lst)+1):
        if used[i] == 1:  # 이미 사용된 숫자 건너뜀
            continue

        used[i] = 1  # 현재 숫자를 사용함으로 표시
        path.append(i)  # 현재 숫자를 path에 추가
        perm(x+1)  # 재귀 호출로 다음 자리 숫자 결정
        path.pop()  # 백트래킹을 위해 마지막 추가 숫자 제거
        used[i] = 0  # 사용 표시 해제


def sum_final(score):
    temp_sum = 0
    for i in range(len(score)):
        temp_sum += score[-1-i] * (10**i)  # 최종 점수를 계산하여 반환
    return temp_sum


T = int(input())

for tc in range(T):
    lst, N = input().split()
    lst = list(map(int, lst))  # 입력을 숫자 리스트로 변환
    N = int(N)  # N을 정수로 변환

    path = []
    lst_idx = []
    used = [0]*(len(lst)+1)

    result = 0  # 최종 결과 값을 저장할 변수
    f(lst, N)

    print(result)  # 최종 결과 값 출력