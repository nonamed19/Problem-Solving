def inorder(idx):
    if idx > N:
        return

    inorder(idx*2)
    result.append(idx) # 중위순회
    inorder(idx*2+1)


T = 10

for tc in range(T):
    N = int(input())
    lst_num = [0]*(N+1)
    lst_alp = ['0']*(N+1)
    result = []

    for i in range(N):
        temp = list(input().split())
        lst_num[i+1] = int(temp[0])
        lst_alp[i+1] = temp[1]

    idx = 1
    inorder(idx)

    print('#%d' %(tc+1), end = ' ')
    for i in range(N):
        print(lst_alp[result[i]], end = '')
    print()