from pprint import pprint

T = int(input()) # 테스트 케이스의 개수 T

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    temp = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            num_sum = 0
            for k in range(M):
                for l in range(M):
                    num_sum += arr[k][l]
            temp[i][j] = num_sum
    print(temp)

    # num_max = 0
    # for i in range(N):
    #     for j in range(N):
    #         if num_max <= temp[i][j] :
    #             num_max = temp[i][j]
    # print(temp)
    #
    # print('#%d %d' %(tc+1, num_max))