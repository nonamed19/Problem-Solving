T = int(input())

for tc in range(T):
    N = int(input()) # 당근의 개수 (3<=N<=1000)
    lst = list(map(int, input().split())) # N개의 당근 크기 Ci (1<=Ci<=30)

    idx = [0]*(max(lst))
    for num in lst:
        idx[num-1] += 1

    # 소, 중, 대를 담는 리스트 생성
    lst_size = []
    for i in range(1, len(idx)-1):
        for j in range(i+1, len(idx)):
            small = sum(idx[:i])
            medium = sum(idx[i:j])
            large = sum(idx[j:])
            lst_size.append([small, medium, large])

    result = 30 # Ci_max - Ci_min + 1(조건 4 판별을 위함)
    for i in range(len(lst_size)):
        if max(lst_size[i]) <= N//2:
            temp = max(lst_size[i]) - min(lst_size[i])
            if temp < result:
                result = temp
    if result == 30: # 조건 4 위배
        result = -1

    print('#%d %d' %(tc+1, result))