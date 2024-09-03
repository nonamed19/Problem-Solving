T = int(input())

for tc in range(T):
    N, *lst = input().split()
    N = int(N)

    blue, orange = [1, 0], [1, 0] # [현재 위치, required time]
    for i in range(0, N*2, 2):
        if lst[i] == 'B': # 처리해야 할 로봇이 BLUE인 경우
            blue[1] = max(blue[1] + abs(int(lst[i+1]) - blue[0])+1, orange[1]+1) # blue[1] + dist(blue) + 1 vs. orange + 1
            blue[0] = int(lst[i+1])
        else: # lst[i] == 'O'
            orange[1] = max(blue[1]+1, orange[1] + abs(int(lst[i+1]) - orange[0])+1) # blue + 1 vs. orange[1] + dist(orange) + 1
            orange[0] = int(lst[i+1])

    print(f'#{tc+1} {max(blue[1], orange[1])}')00