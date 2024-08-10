T = int(input()) # 테스트 케이스 개수 T 1≤T≤50

for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    str1_new = []
    result = 0

    # str1에서 중복 삭제
    for letter in str1:
        if letter not in str1_new:
            str1_new.append(letter)

    # str1_new 내 word 중 str2에 몇 번 등장하는지 확인
    str1_cnt = [0] * len(str1_new)

    for i in range(len(str1_new)):
        for j in range(len(str2)):
            if str1_new[i] == str2[j]:
                str1_cnt[i] += 1

    for i in range(len(str1_cnt)):
        if result <= str1_cnt[i]:
            result = str1_cnt[i]

    print('#%d %d' %(tc+1, result))