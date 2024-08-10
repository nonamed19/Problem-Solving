T = int(input()) # 테스트케이스 수 T
temp = list(x for x in range(1, 10))

for tc in range(T):
    arr = list(map(int, input())) # 테스트케이스 별 6자리 수
    idx = [0]*9
    count_Tri = 0
    count_Run = 0

    # 1부터 9로 구성된 6개의 숫자 개수 list 생성
    for num in arr:
        idx[num-1] += 1

    # Triplet 개수 계산
    for i in range(9):
        while idx[i] >= 3:
            idx[i] -= 3
            count_Tri += 1

    # Run 개수 계산
    for i in range(7):
        while idx[i] and idx[i+1] and idx[i+2] >= 1:
            idx[i] -= 1
            idx[i+1] -= 1
            idx[i+2] -= 1
            count_Run += 1

    if count_Tri + count_Run == 2:
        print('#%d Baby Gin' %(tc+1))
    else:
        print('#%d Lose' %(tc+1))