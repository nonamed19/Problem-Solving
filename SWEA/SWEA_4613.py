from pprint import pprint

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = N*M
    for i in range(1, N):
        for j in range(1, N):
            for k in range(1, N):
                if i + j + k == N:
                    # 비교할 arr 생성
                    temp_arr = []
                    for m in range(i):
                        temp_arr.append(['W']*M)
                    for n in range(j):
                        temp_arr.append(['B']*M)
                    for o in range(k):
                        temp_arr.append(['R']*M)

                    cnt = 0
                    # input 받은 arr와 비교
                    for x in range(N):
                        for y in range(M):
                            if arr[x][y] != temp_arr[x][y]:
                                cnt += 1

                    result = min(result, cnt)
    print(f'#{tc+1} {result}')