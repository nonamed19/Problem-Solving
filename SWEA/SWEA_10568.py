T = int(input()) # 테스트 케이스 개수 T ( 1 ≤ T ≤ 50 )

for tc in range(T):
    N = int(input()) # 카드 장수 ( 5 ≤ N ≤ 100 )
    lst = list(map(int, input())) # N개의 숫자 ai (0으로 시작할 수도 있다.)( 0 ≤ ai ≤ 9 )
    temp = [0]*10

    for num in lst:
        temp[num] += 1

    for i in range(0, 10):
        if