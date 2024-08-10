from pprint import pprint

T = int(input()) # 테스트 케이스 개수 T ( 1 ≤ T ≤ 50 )
arr = [x for x in range(1, 13)]

for tc in range(T):
    # 부분집합 원소의 수 N과 부분 집합의 합 K ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )
    N, K = map(int, input().split())
    temp = [[]]
    lst_sum = []
    result = 0

    # array가 가지는 모든 부분집합을 구하는 함수
    for num in arr:
        size = len(temp)
        for y in range(size):
            temp.append(temp[y] + [num])

    for lst in temp:
        if len(lst) == N:
            num_sum = 0
            for i in range(N):
                num_sum += lst[i]
            lst_sum.append(num_sum)

    for num in lst_sum:
        if num == K:
            result += 1

    if result >= 1:
        print('#%d %d' %(tc+1, result))
    else:
        print('#%d %d' %(tc+1, 0))

