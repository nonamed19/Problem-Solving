T = int(input()) # 테스트케이스 개수 1<=T<=10

for tc in range(T):
    N = int(input()) # 수열의 길이 10<=N<=1000
    lst = list(map(int, input()))
    count = 0
    num_max = 0

    for num in lst:
        if num == 1:
            count += 1
            if num_max <= count:
                num_max = count
        else:
            count = 0

    print('#%d %d' %(tc+1, num_max))