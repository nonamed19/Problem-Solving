def inorder(arr, index, result):
    if index >= len(arr):
        return result

    inorder(arr, 2 * index + 1, result)
    result.append(arr[index])
    inorder(arr, 2 * index + 2, result)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(range(1, n + 1))
    result = []
    inorder(arr, 0, result)

    dic = {}
    num = 1
    while True:
        for i in result:
            dic[i] = num
            num += 1
        break
    print(dic)
    print(result)
    print(f'#{tc} {dic[1]} {dic[n // 2]}')