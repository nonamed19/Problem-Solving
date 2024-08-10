# 제출 1: run-time error
# 제출 2: run-time error.. 왜지
# 제출 3: arr 받을 때 N <-> M 바꿔서 받았음 ..ㅜㅜ
# 제출 4: test case 10/11 .. 허.. result > 0에서 result > 1로 수정

T = int(input())

for tc in range(T):
    N, M = map(int, input().split()) # N x M 행렬(3<=N, M<=100)
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 행 탐색
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if result <= cnt:
                result = cnt

    # 열 탐색
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if result <= cnt:
                result = cnt

    if result > 1:
        print('#%d %d' %(tc+1, result))
    else:
        print('#%d %d' %(tc+1, 0))