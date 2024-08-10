from pprint import pprint

T = int(input()) # 테스트 케이스의 개수 T

for tc in range(T):
    N = int(input()) # 크기 N은 1 이상 10 이하의 정수 (1 ≤ N ≤ 10)
    temp = [[0 for _ in range(N+2)] for _ in range(N+2)]
    now = [1, 0]
    num, iter = 0, 0

    for i in range(N+2):
        temp[0][i] = 1
        temp[i][0] = 1
        temp[N+1][i] = 1
        temp[i][N+1] = 1

    while iter < N**2:
        while temp[now[0]][now[1]+1] == 0:
            num += 1
            now[1] += 1
            temp[now[0]][now[1]] = num
            iter += 1

        while temp[now[0]+1][now[1]] == 0:
            num += 1
            now[0] += 1
            temp[now[0]][now[1]] = num
            iter += 1

        while temp[now[0]][now[1]-1] == 0:
            num += 1
            now[1] -= 1
            temp[now[0]][now[1]] = num
            iter += 1

        while temp[now[0]-1][now[1]] == 0:
            num += 1
            now[0] -= 1
            temp[now[0]][now[1]] = num
            iter += 1

    print('#%d' %(tc+1))
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(temp[i][j], end = ' ')
        print()