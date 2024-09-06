def find_min(money, lev):
    global result

    if money >= result:
        return

    if lev >= 12:
        result = min(result, money)
        return

    find_min(money + day*lst[lev], lev + 1)
    if lst[lev]:
        find_min(money + month, lev + 1)
        find_min(money + month_3, lev + 3)


T = int(input())

for tc in range(T):
    day, month, month_3, year = map(int, input().split())
    lst = list(map(int, input().split())) + [0]*2
    result = year
    find_min(0, 0)
    print(f'#{tc+1} {result}')