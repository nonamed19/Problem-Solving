# runtime error : 40 / 50

def f(num, lst_A, lst_B, visited):

    if num == N and len(lst_B) == 3:
        result_A.append(lst_A)
        result_B.append(lst_B)
        return

    for _ in range(N):
        if visited[num]:
            continue

        if num not in lst_A:
            lst_A += [num]
        else:
            lst_B += [num]

        visited[num] = 1
        f(num + 1, lst_A, lst_B, visited)
        visited[num] = 0


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    temp_A, temp_B = [], []
    result_A, result_B = [], []
    visited = [0]*N
    f(0, temp_A, temp_B, visited) # 순열

    print(result_A)
    print(result_B)

    # result = 20000
    # for i in range(len(lst)//2):
    #     sum_A, sum_B = 0, 0
    #     for j in range(N//2):
    #         for k in range(N//2):
    #             sum_A += arr[lst_A[j]][lst_A[k]]
    #             sum_B += arr[lst_B[j]][lst_B[k]]
    #     result = min(result, abs(sum_A - sum_B))
    #
    # print(f'#{tc+1} {result}')