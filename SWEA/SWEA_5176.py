def inorder(idx):
    if idx > N:
        return

    inorder(idx*2)           # 인덱스가 *2가 되면 왼쪽임
    result.append(idx)
    inorder(idx*2+1)           # 인덱스가 *2+1가 되면 오른쪽임


T = int(input())

for tc in range(T):
    N = int(input())    # node의 수
    lst = list(range(1, N+1))

    idx = 1             # 시작 위치
    result = []
    inorder(idx)

    for i in range(N):
        if result[i] == 1:
            root = lst[i]
        elif result[i] == N//2:
            node = lst[i]

    print('#%d %d %d' %(tc+1, root, node))