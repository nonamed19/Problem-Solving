'''
1989. 초심자의 회문검사

"level"과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(palindrome)이라 한다.
단어를 입력 받아 회문이면 1을 출력하고 아니라면 0을 출력하는 프로그램을 작성하라.

3
level
samsung
eye
#1 1
#2 0
#3 1
'''

T = int(input()) # number of test cases

for tc in range(T):
    lst = list(map(str, input()))
    N = len(lst)
    valid = 1

    for i in range(N//2):
        if lst[i] != lst[-1-i]:
            valid = 0
            break

    print('#%d %d' %(tc+1, valid))