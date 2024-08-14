def f(i, j):
    if i == j:
        return i                    # 최종 승자
    else:
        left = f(i, (i+j)//2)       # 왼쪽 그룹
        right = f((i+j)//2+1, j)    # 오른쪽 그룹
        return card(left, right)

def card(left, right):
    if [lst[left], lst[right]] in [[1, 2], [2, 3], [3, 1]]:
        return right
    else:
        return left

T = int(input())

for tc in range(T):
    N = int(input()) # 인원수 N (4 <= N <= 100)
    lst = list(map(int, input().split()))

    print('#%d %d' %(tc+1, f(0, N-1)+1))