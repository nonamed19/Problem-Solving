T = int(input())

for tc in range(T):
    lst = list(input())
    cnt = 0 # 열린 steel pipe의 수 : '('
    result = 0

    for i in range(len(lst)):
        if lst[i] == '(': # 예상되는 pipe의 위치, including lasor
            cnt += 1
        elif lst[i] == ')' and lst[i-1] == '(': # lasor의 위치, cutting 수행
            cnt -= 1
            result += cnt
        else: # pipe가 close되는 위치
            cnt -= 1
            result += 1

    print('#%d %d' %(tc+1, result))