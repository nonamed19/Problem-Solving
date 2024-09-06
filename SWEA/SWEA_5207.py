def binary_search(target, l, r):
    global cnt
    m = (l+r)//2

    if lst1[m] == target:
        cnt = []  # global로 관리 중인 cnt 초기화
        return True

    elif l >= r:
        cnt = []  # global로 관리 중인 cnt 초기화
        return False

    elif target < lst1[m]:
        if cnt:
            temp = cnt.pop()
            cnt.append(1)
            if temp == 2:
                return binary_search(target, l, m-1)
            else:
                cnt = []  # global로 관리 중인 cnt 초기화
                return False
        else:
            cnt.append(1)
            return binary_search(target, l, m - 1)

    elif target > lst1[m]:
        if cnt:
            temp = cnt.pop()
            cnt.append(2)
            if temp == 1:
                return binary_search(target, m+1, r)
            else:
                cnt = []  # global로 관리 중인 cnt 초기화
                return False
        else:
            cnt.append(2)
            return binary_search(target, m + 1, r)


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst1 = sorted(list(map(int, input().split())))
    lst2 = list(map(int, input().split()))

    l = 0
    r = N-1
    cnt = [] # stack

    result = 0
    for num in lst2:
        if binary_search(num, l, r):
            result += 1

    print(f'#{tc+1} {result}')