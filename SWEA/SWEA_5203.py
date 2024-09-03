def baby_jin(lst):
    cnt = 0
    # triplet
    for i in range(10):
        if lst.count(i) >= 3:
            cnt += 1

    # run 판별을 위해 중복이 없는 임시 list 생성
    lst_temp = []
    for num in lst:
        if num not in lst_temp:
            lst_temp.append(num)

    # run
    consecutive = 1
    for i in range(len(lst_temp)-1):
        if lst_temp[i+1] - lst_temp[i] == 1:
            consecutive += 1
            if consecutive >= 3:
                cnt += 1
        else:
            consecutive = 1

    return cnt


T = int(input())

for tc in range(T):
    deck = list(map(int, input().split()))
    player1, player2 = [], []
    result = 0

    for i in range(0, 12, 2): # 12장의 카드 중 6장씩 나눠가지기 위해
        player1.append(deck[i])
        player1.sort() # run 확인을 위해 list sort
        if baby_jin(player1) > 0: # player1 : run, triplet 확인
            result = 1
            break

        player2.append(deck[i+1])
        player2.sort() # run 확인을 위해 list sort
        if baby_jin(player2) > 0: # player2 : run, triplet 확인
            result = 2
            break

    print(f'#{tc+1} {result}')
