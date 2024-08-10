T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # M개 만큼 i, j의 값 받기
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1 # index 맞추기

        #i를 기준으로 j개 만큼 좌우 탐색을 수행
        for k in range(1, j+1):
            i_left = i-k
            i_right = i+k
            if (0 <= i_left < N) and (0 <= i_right < N):
                if lst[i_left] == 0 and lst[i_right] == 0:
                    lst[i_left] = 1
                    lst[i_right] = 1
                elif lst[i_left] == 1 and lst[i_right] == 1:
                    lst[i_left] = 0
                    lst[i_right] = 0

    print('#%d' %(tc+1), *lst)