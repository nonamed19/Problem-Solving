T = int(input())
for tc in range(1, T+1):
    test = list(input().split())
    B = 0
    O = 1
    robot = [[1, 0], [1, 0]]    # robot[[위치, 마지막 작업 완료시간],..]
    for i in range(1, int(test[0])*2+1, 2):  # i = 1, 3, 5, ....
        if test[i]=='B':
            dist = abs(robot[B][0] - int(test[i+1])) # 거리
            robot[B][1] = max(robot[B][1]+dist+1, robot[O][1]+1) #
            robot[B][0] = int(test[i+1])
        else:   # O
            dist = abs(robot[O][0] - int(test[i + 1]))  # 거리
            robot[O][1] = max(robot[O][1] + dist + 1, robot[B][1] + 1)  #
            robot[O][0] = int(test[i + 1])
    print(f'#{tc} {max(robot[B][1], robot[O][1])}')