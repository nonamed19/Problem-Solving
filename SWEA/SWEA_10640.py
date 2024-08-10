T = int(input()) # 테스트 케이스 개수 T (1≤T≤50)

for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    validation = 0

    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:i+len(str1)]:
            validation += 1

    print('#%d %d' %(tc+1, validation))